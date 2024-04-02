#define ORDER_BUY 1
#define ORDER_SELL 2
#define ORDER_BUY_PENDING 3
#define ORDER_SELL_PENDING 4

#define OPEN_AT_ASK 1
#define OPEN_AT_BID 2
#define OPEN_AT_MID 3
#define OPEN_AT_CUSTOM_PRICE 4

#define LOOK_UP_RUNNING_THEN_HISTORY 0
#define LOOK_UP_RUNNING_ONLY 1
#define LOOK_UP_HISTORY_ONLY 2

//TP SL modes are different only at items 1&2 and 5&6
#define TPSL_MODE_NO_TP 1
#define TPSL_MODE_NO_SL 2
#define TPSL_MODE_FIXED_PIPS 3
#define TPSL_MODE_PERCENT_OF_PRICE 4
#define TPSL_MODE_PERCENT_FROM_SL 5
#define TPSL_MODE_PERCENT_FROM_TP 6
#define TPSL_MODE_CUSTOM_PRICE_LEVEL 7
#define TPSL_MODE_CUSTOM_PIPS 8
#define TPSL_MODE_CUSTOM_PRICE_FRACTION 9

#define MONEY_MANAGEMENT_FIXED_VOLUME 1
#define MONEY_MANAGEMENT_PERCENT_OF_EQUITY 2
#define MONEY_MANAGEMENT_PERCENT_OF_BALANCE 3
#define MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN 4
#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY 5
#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE 6
#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN 7
#define MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY 8
#define MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE 9
#define MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN 10
#define MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY 11
#define MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES 12
#define MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI 13
#define MONEY_MANAGEMENT_CUSTOM_VALUE 14


#define POINT_FORMAT_RULES "0.001=0.01,0.00001=0.0001,0.000001=0.0001" // this is deserialized in a special function later


class Task0 : public Task
  {
   //values set by user
   string            symbol;
   int               group;
   int               order_type;
   int               money_management;
   double            how_much_volume;
   double            volume_upper_limit;
   int               open_at_price;
   double            price_offset;
   bool              price_offset_as_pip;
   int               slippage;
   int               stop_loss_mode;
   int               take_profit_mode;
   double            stoploss;
   double            takeprofit;
   string            comment;
   int               magic;
   datetime          expiration;
   color             arrow_color;
   //values set by system
   int               cmd;
   double            price;
   double            volume;
   int               ticket;
   double            slPrice;
   double            tpPrice;
   double            mstoploss;
   double            mtakeprofit;
   bool              initialized;
   string            msymbol;
   //martingale inputs
   int               look_up_on;
   double            martingale_init_vol;
   double            martingale_multiply_on_loss;
   double            martingale_multiply_on_profit;
   double            martingale_addlots_on_loss;
   double            martingale_addlots_on_profit;
   double            martingale_reset_on_n_losses;
   double            martingale_reset_on_n_profits;
   int               type[];
public:
                     Task0(string name):Task(name)
     {
      symbol = NULL;
      group = 11;
      order_type = ORDER_BUY_PENDING;
      money_management = MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI;
      how_much_volume = 35;
      volume_upper_limit = 0;
      open_at_price = OPEN_AT_ASK;
      price_offset = 25;
      price_offset_as_pip = true;

      slippage = 4;
      stoploss = 20;
      takeprofit = 20;
      take_profit_mode = TPSL_MODE_FIXED_PIPS;
      stop_loss_mode = TPSL_MODE_FIXED_PIPS;
      comment = 0;
      expiration = 0;
      arrow_color = clrYellow;

      //martingale
      look_up_on = LOOK_UP_RUNNING_ONLY;
      int mtype[] = {0,1};//This doesn't seem to be an input. So this remains static forever.
      ArrayCopy(type, mtype, 0, 0, WHOLE_ARRAY);
      martingale_init_vol = 0.1;
      martingale_multiply_on_loss = 0;
      martingale_multiply_on_profit = 0;
      martingale_addlots_on_loss = 0.1;
      martingale_addlots_on_profit = 0.1;
      martingale_reset_on_n_losses = 5;
      martingale_reset_on_n_profits = 5;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = getSymbol(symbol);

      calc();
      if(!initialized)
        {
         printf("Not initialized");
         block.onResult(ROUTE_2_PASSED);
         return;
        }

      int retryCount = 0;

      while(!IsStopped())
        {

         if(retryCount>30)
            break;

         WaitTradeContextIfBusy();

         //-- send ---------------------------------------------------------
         ResetLastError();

         ticket = OrderSend(msymbol,cmd,volume,price,(int)(slippage * PipValue(msymbol)),slPrice,tpPrice,comment,magic,expiration,arrow_color);
         if(ticket>0)  //Must be here
            break;
         //-- error check --------------------------------------------------
         string msg_prefix = (cmd > OP_SELL) ? "New order error" : "New trade error";

         int erraction = CheckForTradingError(GetLastError(), msg_prefix);

         switch(erraction)
           {
            case 0:
               break;    // no error
            case 1:
               retryCount ++;
               continue; // overcomable error
            case 2:
               break;    // fatal error
           }
        }

      if(ticket > 0)
        {
         //onTrade()
         printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }
private:
   //does needed calculations
   void              calc()
     {
      fitGroup();
      buildMagic();
      if(order_type==ORDER_BUY)
        {
         cmd = OP_BUY;
        }
      else
         if(order_type==ORDER_SELL)
           {
            cmd = OP_SELL;
           }
         else
            if(order_type==ORDER_BUY_PENDING)
              {
               if(price_offset>=0)
                  cmd = OP_BUYSTOP;
               else
                  cmd = OP_BUYLIMIT;
              }
            else
               if(order_type==ORDER_SELL_PENDING)
                 {
                  if(price_offset>=0)
                     cmd = OP_SELLSTOP;
                  else
                     cmd = OP_SELLLIMIT;
                 }

      calcVolume();
      calc_entry_price();
      if(cmd==OP_BUY || cmd==OP_BUYLIMIT ||cmd==OP_BUYSTOP)
        {
         calc_tp_buy();
         calc_sl_buy();
        }
      else
         if(cmd==OP_SELL || cmd==OP_SELLLIMIT || cmd==OP_SELLSTOP)
           {
            calc_tp_sell();
            calc_sl_sell();
           }

      if(MathAbs(tpPrice-slPrice)/Point()<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      initialized = true;
     }

   void              calc_entry_price()
     {
      if(cmd==OP_BUY)
        {
         price = Ask;
        }
      else
         if(cmd==OP_SELL)
           {
            price = Bid;
           }
         else
           {
            switch(open_at_price)
              {
               case OPEN_AT_ASK:
                  price = SymbolInfoDouble(msymbol, SYMBOL_ASK);
                  break;
               case OPEN_AT_BID:
                  price = SymbolInfoDouble(msymbol, SYMBOL_BID);
                  break;
               case OPEN_AT_MID:
                  price = (SymbolInfoDouble(msymbol, SYMBOL_ASK)+SymbolInfoDouble(msymbol, SYMBOL_BID))/2;
                  break;
               case OPEN_AT_CUSTOM_PRICE:
                  RSI1_left rsi1_left;
                  rsi1_left.init();
                  double valueRsi1_left = rsi1_left.calc();
                  price = valueRsi1_left;
                  break;
              }
           }


      double offset = price_offset;
      if(price_offset_as_pip)
         offset = price_offset * Point() * 10;

      if(cmd==OP_SELLLIMIT || cmd==OP_SELLSTOP)
         price -= offset;
      else if (cmd==OP_BUYLIMIT || cmd==OP_BUYSTOP)
         price += offset;
     }

   ////////////////////////////////////////////////////////////

   void              calc_tp_buy()
     {
      switch(take_profit_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mtakeprofit = NormalizeDouble(takeprofit*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            tpPrice = price + mtakeprofit;
            break;
         case TPSL_MODE_NO_TP:
            tpPrice = 0;
            break;
        }
     }

   void              calc_sl_buy()
     {
      switch(stop_loss_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mstoploss = NormalizeDouble(stoploss*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            slPrice = price - mstoploss;
            break;
         case TPSL_MODE_NO_SL:
            slPrice = 0;
            break;
        }
     }

   void              calc_tp_sell()
     {
      switch(take_profit_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mtakeprofit = NormalizeDouble(takeprofit*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            tpPrice = price - mtakeprofit;
            break;
         case TPSL_MODE_NO_TP:
            tpPrice = 0;
            break;
        }
     }

   void              calc_sl_sell()
     {
      switch(stop_loss_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mstoploss = NormalizeDouble(stoploss*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            slPrice = price + mstoploss;
            break;
         case TPSL_MODE_NO_SL:
            slPrice = 0;
            break;
        }
     }

   void              calcVolume()
     {
      if(money_management == MONEY_MANAGEMENT_FIXED_VOLUME)
        {
         volume = DynamicLots(msymbol, money_management, how_much_volume);
        }
      else
         if(money_management == MONEY_MANAGEMENT_PERCENT_OF_EQUITY)
           {
            volume = DynamicLots(msymbol, money_management, how_much_volume);
           }
         else
            if(money_management == MONEY_MANAGEMENT_PERCENT_OF_BALANCE)
              {
               //lots = DynamicLots(Symbol, money_management, VolumeBlockPercent);
              }
            else
               if(money_management == MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN)
                 {
                  //lots = DynamicLots(Symbol, money_management, VolumeBlockPercent);
                 }
               else
                  if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY)
                    {
                     //lots = DynamicLots(Symbol, money_management, VolumePercent);
                    }
                  else
                     if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE)
                       {
                        //lots = DynamicLots(Symbol, money_management, VolumePercent);
                       }
                     else
                        if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN)
                          {
                           //lots = DynamicLots(Symbol, money_management, VolumePercent);
                          }
                        else
                           if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY)
                             {
                              //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                             }
                           else
                              if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE)
                                {
                                 //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                                }
                              else
                                 if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN)
                                   {
                                    //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                                   }
                                 else
                                    if(money_management == MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY)
                                      {
                                       //lots = DynamicLots(Symbol, money_management, VolumeSizeRisk, pre_sl_pips);
                                      }
                                    else
                                       if(money_management == MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES)
                                         {
                                          //lots = DynamicLots(Symbol, money_management, FixedRatioUnitSize, FixedRatioDelta);
                                         }
                                       else
                                          if(money_management == MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI)
                                            {
                                             volume = BetMartingale(msymbol, look_up_on, group, type, martingale_init_vol, martingale_multiply_on_loss, martingale_multiply_on_profit, martingale_addlots_on_loss, martingale_addlots_on_profit, martingale_reset_on_n_losses, martingale_reset_on_n_profits);
                                            }
                                          else
                                             if(money_management == MONEY_MANAGEMENT_CUSTOM_VALUE)
                                               {
                                                //lots = _dVolumeSize_();
                                               }


      if(volume_upper_limit>0 && volume>volume_upper_limit)
         volume = volume_upper_limit;
     }

   void              fitGroup()
     {
      //STest, take care of group number rules later
      if(group<11)
         group = 11;
      if(group>99)
         group = 99;
     }

   void              buildMagic()
     {
         magic = StrToInteger(group + "72" + "000"); //72 shows it's automated (opened by the expert).
     }

  };







//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double BetMartingale(
   string symbol,
   int look_up_on,
   int group,
   int &type[],
   double initialLots,
   double multiplyOnLoss,
   double multiplyOnProfit,
   double addOnLoss,
   double addOnProfit,
   int resetOnLoss,
   int resetOnProfit
)
  {
   double info[];
   GetBetTradesInfo(info, symbol, look_up_on, group, type, true);

   double lots         = info[0];
   double profitOrLoss = info[1]; // 0 - unknown, 1 - profit, -1 - loss
   double consecutive  = info[2];

//-- Martingale Logic
   if(lots == 0)
     {
      lots = initialLots;
      printf("11111");
     }
   else
     {
      if(profitOrLoss == 1)
        {
         if(resetOnProfit > 0 && consecutive >= resetOnProfit)
           {
            lots = initialLots;
            printf("22222");
           }
         else
           {
            if(multiplyOnProfit <= 0)
              {
               multiplyOnProfit = 1;
              }

            lots = (lots * multiplyOnProfit) + addOnProfit;
            printf("33333 " + multiplyOnProfit);
           }
        }
      else
        {
         if(resetOnLoss > 0 && consecutive >= resetOnLoss)
           {
            lots = initialLots;
            printf("444444");
           }
         else
           {
            if(multiplyOnLoss <= 0)
              {
               multiplyOnLoss = 1;
              }

            lots = (lots * multiplyOnLoss) + addOnLoss;
            printf("555555");
           }
        }
     }

   return lots;
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void GetBetTradesInfo(
   double &output[],
   string symbol,
   int look_up_on, // 0: try running trades first and then history trades, 1: try running only, 2: try history only
   int group,
   int &type[],
   bool findConsecutive = false
)
  {
   if(ArraySize(output) < 4)
     {
      ArrayResize(output, 4);
      ArrayInitialize(output, 0.0);
     }

   double lots         = output[0]; // will be the lot size of the first loaded trade
   double profitOrLoss = output[1]; // 0 is initial value, 1 is profit, -1 is loss
   double consecutive  = output[2]; // the number of consecutive profitable or losable trades
   double profit       = output[3]; // will be the profit of the first loaded trade
   bool historyTrades  = look_up_on == LOOK_UP_RUNNING_ONLY ? false : true;

   int total = (historyTrades) ? OrdersHistoryTotal() : OrdersTotal();

   for(int pos = total - 1; pos >= 0; pos--)
     {
      printf("AAA");
      bool con1 = !historyTrades && TradeSelectByIndex(pos, ORDER_GROUP_MODE_NUMBER, group, symbol, type);
      bool con2 = historyTrades && HistoryTradeSelectByIndex(pos, ORDER_GROUP_MODE_NUMBER, group, symbol, type);
      if(con1 || con2)
        {
         printf("BBB");
         bool skipCon1 = ((look_up_on == 0 || look_up_on == 1) && TimeCurrent() - OrderOpenTime() < 3); // skip for brand new trades
         bool skipCon2 = !historyTrades && OrderExpiration() > 0 && OrderExpiration() <= OrderCloseTime(); // exclude expired pending orders
         if(skipCon1 || skipCon2)
            continue;
         printf("CCC");
         if(lots == 0.0)
           {
            lots = OrderLots();
           }

         profit = OrderClosePrice() - OrderOpenPrice();
         profit = NormalizeDouble(profit, SymbolDigits(OrderSymbol()));

         if(profit == 0.0)
           {
            // Consider a trade with zero profit as non existent
            continue;
            printf("DDD");
           }

         if(IsOrderTypeSell())
           {
            profit = -1 * profit;
           }

         if(profitOrLoss == 0)
           {
            // We enter here only for the first trade
            profitOrLoss = (profit < 0.0) ? -1 : 1;

            consecutive++;
            printf("EEE");
            if(findConsecutive == false)
               break;
           }
         else
           {
            // For the trades after the first one, if its profit is the opposite of profitOrLoss, we need to break
            if(
               (profitOrLoss > 0.0 && profit < 0.0)
               || (profitOrLoss < 0.0 && profit > 0.0)
            )
              {
               break;
              }

            consecutive++;
           }
        }
     }

   output[0] = lots;
   output[1] = profitOrLoss;
   output[2] = consecutive;
   output[3] = profit;

   if(look_up_on == 0 && (findConsecutive || profitOrLoss == 0))
     {
      // running trades tried, continue with the history trades
      look_up_on = 2;
      GetBetTradesInfo(output, symbol, look_up_on, group, type, findConsecutive);
     }
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool TradeSelectByIndex(
   int index,
   string group_mode,
   string group,
   string msymbol,
   int type[]
)
  {
   if(OrderSelect(index, SELECT_BY_POS, MODE_TRADES))
     {
      bool x = filterGeneral(msymbol, type, group_mode, group);
      printf("XXXX "+x);
      return x;
     }

   return false;



  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool HistoryTradeSelectByIndex(
   int index,
   string group_mode,
   string group,
   string msymbol,
   int type[]
)
  {
   if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)
     {
      bool x = filterGeneral(msymbol, type, group_mode, group);
      return x;
     }

   return false;
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool              filterGeneral(string symbol, int type[], int group_mode, int group_number)
  {
   bool con1 = (symbol==NULL && OrderSymbol()==Symbol()) || symbol==OrderSymbol();
   bool con2 = sameOrderType(type, OrderType());
   bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
   bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
   return con1 && con2 && con3 && con4;
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int SymbolDigits(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool IsOrderTypeSell()
  {
   int type = OrderType();

   return (type == OP_SELL || type == OP_SELLSTOP || type == OP_SELLLIMIT);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double DynamicLots(string symbol, int mode, double value=0, double sl=0, string align="align", double RJFR_initial_lots=0)
  {
   double size=0;
   double LotStep=MarketInfo(symbol,MODE_LOTSTEP);
   double LotSize=MarketInfo(symbol,MODE_LOTSIZE);
   double MinLots=MarketInfo(symbol,MODE_MINLOT);
   double MaxLots=MarketInfo(symbol,MODE_MAXLOT);
   double TickValue=MarketInfo(symbol,MODE_TICKVALUE);
   double point=MarketInfo(symbol,MODE_POINT);
   double ticksize=MarketInfo(symbol,MODE_TICKSIZE);
   double margin_required=MarketInfo(symbol,MODE_MARGINREQUIRED);

   if(mode==MONEY_MANAGEMENT_FIXED_VOLUME)
     {
      size=value;

     }
   else
      if(mode==MONEY_MANAGEMENT_PERCENT_OF_EQUITY)
        {
         size=(value/100)*AccountEquity()/margin_required;
        }
      else
         if(mode==MONEY_MANAGEMENT_PERCENT_OF_BALANCE)
           {
            size=(value/100)*AccountBalance()/margin_required;
           }
         else
            if(mode==MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN)
              {
               size=(value/100)*AccountFreeMargin()/margin_required;
              }
            else
               if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY)
                 {
                  size=(value/100)*AccountEquity()/(LotSize*TickValue);
                 }
               else
                  if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE)
                    {
                     size=(value/100)*AccountBalance()/(LotSize*TickValue);
                    }
                  else
                     if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN)
                       {
                        size=(value/100)*AccountFreeMargin()/(LotSize*TickValue);
                       }
                     else
                        if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY)
                          {
                           size=((value/100)*AccountEquity())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                          }
                        else
                           if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE)
                             {
                              size=((value/100)*AccountBalance())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                             }
                           else
                              if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN)
                                {
                                 size=((value/100)*AccountFreeMargin())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                                }
                              else
                                 if(mode=="fixedRisk")
                                   {
                                    size=(value)/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                                   }
                                 else
                                    if(mode=="fixedRatio" || mode=="RJFR")
                                      {

                                       /////
                                       // Ryan Jones Fixed Ratio MM static data
                                       static double RJFR_start_lots=0;
                                       static double RJFR_delta=0;
                                       static double RJFR_units=1;
                                       static double RJFR_target_lower=0;
                                       static double RJFR_target_upper=0;
                                       /////

                                       if(RJFR_start_lots<=0)
                                         {
                                          RJFR_start_lots=value;
                                         }
                                       if(RJFR_start_lots<MinLots)
                                         {
                                          RJFR_start_lots=MinLots;
                                         }
                                       if(RJFR_delta<=0)
                                         {
                                          RJFR_delta=sl;
                                         }
                                       if(RJFR_target_upper<=0)
                                         {
                                          RJFR_target_upper=AccountEquity()+(RJFR_units*RJFR_delta);
                                          Print("Fixed Ratio MM: Units=>",RJFR_units,"; Delta=",RJFR_delta,"; Upper Target Equity=>",RJFR_target_upper);
                                         }
                                       if(AccountEquity()>=RJFR_target_upper)
                                         {
                                          while(true)
                                            {
                                             Print("Fixed Ratio MM going up to ",(RJFR_start_lots*(RJFR_units+1))," lots: Equity is above Upper Target Equity (",AccountEquity(),">=",RJFR_target_upper,")");
                                             RJFR_units++;
                                             RJFR_target_lower=RJFR_target_upper;
                                             RJFR_target_upper=RJFR_target_upper+(RJFR_units*RJFR_delta);
                                             Print("Fixed Ratio MM: Units=>",RJFR_units,"; Delta=",RJFR_delta,"; Lower Target Equity=>",RJFR_target_lower,"; Upper Target Equity=>",RJFR_target_upper);
                                             if(AccountEquity()<RJFR_target_upper)
                                               {
                                                break;
                                               }
                                            }
                                         }
                                       else
                                          if(AccountEquity()<=RJFR_target_lower)
                                            {
                                             while(true)
                                               {
                                                if(AccountEquity()>RJFR_target_lower)
                                                  {
                                                   break;
                                                  }
                                                if(RJFR_units>1)
                                                  {
                                                   Print("Fixed Ratio MM going down to ",(RJFR_start_lots*(RJFR_units-1))," lots: Equity is below Lower Target Equity | ", AccountEquity()," <= ",RJFR_target_lower,")");
                                                   RJFR_target_upper=RJFR_target_lower;
                                                   RJFR_target_lower=RJFR_target_lower-((RJFR_units-1)*RJFR_delta);
                                                   RJFR_units--;
                                                   Print("Fixed Ratio MM: Units=>",RJFR_units,"; Delta=",RJFR_delta,"; Lower Target Equity=>",RJFR_target_lower,"; Upper Target Equity=>",RJFR_target_upper);
                                                  }
                                                else
                                                  {
                                                   break;
                                                  }
                                               }
                                            }
                                       size=RJFR_start_lots*RJFR_units;
                                      }
   if(size==EMPTY_VALUE)
     {
      size=0;
     }

   size=MathRound(size/LotStep)*LotStep;
   return (size);
  }



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double PipValue(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return CustomPoint(symbol) / SymbolInfoDouble(symbol, SYMBOL_POINT);
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double CustomPoint(string symbol)
  {
   static string symbols[];
   static double points[];
   static string last_symbol = "-";
   static double last_point  = 0;
   static int last_i         = 0;
   static int size           = 0;

//-- variant A) use the cache for the last used symbol
   if(symbol == last_symbol)
     {
      return last_point;
     }

//-- variant B) search in the array cache
   int i       = last_i;
   int start_i = i;
   bool found  = false;

   if(size > 0)
     {
      while(true)
        {
         if(symbols[i] == symbol)
           {
            last_symbol = symbol;
            last_point  = points[i];
            last_i      = i;

            return last_point;
           }

         i++;

         if(i >= size)
           {
            i = 0;
           }
         if(i == start_i)
           {
            break;
           }
        }
     }

//-- variant C) add this symbol to the cache
   i     = size;
   size  = size + 1;

   ArrayResize(symbols, size);
   ArrayResize(points, size);

   symbols[i]  = symbol;
   points[i]   = 0;
   last_symbol = symbol;
   last_i      = i;

//-- unserialize rules from FXD_POINT_FORMAT_RULES
   string rules[];
   StringExplode(",", POINT_FORMAT_RULES, rules);

   int rules_count = ArraySize(rules);

   if(rules_count > 0)
     {
      string rule[];

      for(int r = 0; r < rules_count; r++)
        {
         StringExplode("=", rules[r], rule);

         //-- a single rule must contain 2 parts, [0] from and [1] to
         if(ArraySize(rule) != 2)
           {
            continue;
           }

         double from = StringToDouble(rule[0]);
         double to   = StringToDouble(rule[1]);

         //-- "to" must be a positive number, different than 0
         if(to <= 0)
           {
            continue;
           }

         //-- "from" can be a number or a string
         // a) string
         if(from == 0 && StringLen(rule[0]) > 0)
           {
            string s_from = rule[0];
            int pos       = StringFind(s_from, "?");

            if(pos < 0)  // ? not found
              {
               if(StringFind(symbol, s_from) == 0)
                 {
                  points[i] = to;
                 }
              }
            else
               if(pos == 0)  // ? is the first symbol => match the second symbol
                 {
                  if(StringFind(symbol, StringSubstr(s_from, 1), 3) == 3)
                    {
                     points[i] = to;
                    }
                 }
               else
                  if(pos > 0)  // ? is the second symbol => match the first symbol
                    {
                     if(StringFind(symbol, StringSubstr(s_from, 0, pos)) == 0)
                       {
                        points[i] = to;
                       }
                    }
           }

         // b) number
         if(from == 0)
           {
            continue;
           }

         if(SymbolInfoDouble(symbol, SYMBOL_POINT) == from)
           {
            points[i] = to;
           }
        }
     }

   if(points[i] == 0)
     {
      points[i] = SymbolInfoDouble(symbol, SYMBOL_POINT);
     }

   last_point = points[i];

   return last_point;
  }



template<typename T>
void StringExplode(string delimiter, string inputString, T &output[])
  {
   int begin   = 0;
   int end     = 0;
   int element = 0;
   int length  = StringLen(inputString);
   int length_delimiter = StringLen(delimiter);
   T empty_val  = (typename(T) == "string") ? (T)"" : (T)0;

   if(length > 0)
     {
      while(true)
        {
         end = StringFind(inputString, delimiter, begin);

         ArrayResize(output, element + 1);
         output[element] = empty_val;

         if(end != -1)
           {
            if(end > begin)
              {
               output[element] = (T)StringSubstr(inputString, begin, end - begin);
              }
           }
         else
           {
            output[element] = (T)StringSubstr(inputString, begin, length - begin);
            break;
           }

         begin = end + 1 + (length_delimiter - 1);
         element++;
        }
     }
   else
     {
      ArrayResize(output, 1);
      output[element] = empty_val;
     }
  }
