class Task_id : public Task
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
   double            takeprofit_percent;
   double            stoploss_percent;
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
                     Task_id(string name):Task(name)
     {
      symbol = symbol_val;
      group = group_val;
      order_type = order_type_val;
      money_management = money_management_val;
      how_much_volume = how_much_volume_val;
      volume_upper_limit = volume_upper_limit_val;
      open_at_price = open_at_price_val;
      price_offset = price_offset_val;
      price_offset_as_pip = price_offset_as_pip_val;

      slippage = slippage_val;
      stoploss = stoploss_val;
      takeprofit = takeprofit_val;
      takeprofit_percent = takeprofit_percent_val;
      stoploss_percent = stoploss_percent_val;
      take_profit_mode = take_profit_mode_val;
      stop_loss_mode = stop_loss_mode_val;
      comment = comment_val;
      expiration = expiration_val;
      arrow_color = arrow_color_val;

      //martingale
      look_up_on = look_up_on_val;
      int mtype[] = {0, 1};//This doesn't seem to be an input. So this remains static forever.
      ArrayCopy(type, mtype, 0, 0, WHOLE_ARRAY);
      martingale_init_vol = martingale_init_vol_val;
      martingale_multiply_on_loss = martingale_multiply_on_loss_val;
      martingale_multiply_on_profit = martingale_multiply_on_profit_val;
      martingale_addlots_on_loss = martingale_addlots_on_loss_val;
      martingale_addlots_on_profit = martingale_addlots_on_profit_val;
      martingale_reset_on_n_losses = martingale_reset_on_n_losses_val;
      martingale_reset_on_n_profits = martingale_reset_on_n_profits_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = getSymbol(symbol);

      calc();
      if(!initialized)
        {
         printf("Buy/Sell/Pending class calcs failed");
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

         if(erraction==0)
           {
            break;    // no error
           }
         else
            if(erraction==1)
              {
               retryCount ++;
               continue; // overcomable error
              }
            else
               if(erraction==2)
                 {
                  break;    // fatal error
                 }
        }

      if(ticket > 0)
        {
         OnTrade();
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }
private:
   void              calc()
     {
      fitGroup();
      buildMagic();
      calc_entry_price();//Should be called first
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
               if(price > SymbolInfoDouble(msymbol, SYMBOL_ASK))
                  cmd = OP_BUYSTOP;
               else
                  cmd = OP_BUYLIMIT;
              }
            else
               if(order_type==ORDER_SELL_PENDING)
                 {
                  if(price < SymbolInfoDouble(msymbol, SYMBOL_BID))
                     cmd = OP_SELLSTOP;
                  else
                     cmd = OP_SELLLIMIT;
                 }


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

      calcVolume();
      if(take_profit_mode!=TPSL_MODE_NO_TP && stop_loss_mode!=TPSL_MODE_NO_SL && MathAbs(tpPrice-slPrice)/ MarketInfo(msymbol, MODE_POINT)<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      initialized = true;
     }

   void              calc_entry_price()
     {
      if(order_type==ORDER_BUY)
        {
         price = SymbolInfoDouble(msymbol, SYMBOL_ASK);
        }
      else
         if(order_type==ORDER_SELL)
           {
            price = SymbolInfoDouble(msymbol, SYMBOL_BID);
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
                  initializer_oacp
                  price = variable_name_oacp;
                  break;
              }
           }


      double offset = price_offset;
      if(price_offset_as_pip)
         offset = price_offset *  MarketInfo(msymbol, MODE_POINT) * 10;

      if(order_type == ORDER_SELL_PENDING)
         price -= offset;
      else
         if(order_type == ORDER_BUY_PENDING)
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
         case TPSL_MODE_PERCENT_OF_PRICE:
            tpPrice = SymbolInfoDouble(msymbol, SYMBOL_ASK) + (SymbolInfoDouble(msymbol, SYMBOL_ASK) * takeprofit_percent / 100);
            break;
         case TPSL_MODE_PERCENT_OF_SL:
            calc_sl_buy();
            tpPrice = price + ((price-slPrice) * takeprofit_percent / 100);
            break;
         case TPSL_MODE_CUSTOM_PRICE_LEVEL:
            initializer_tmcpl_tb
            tpPrice = variable_name_tmcpl_tb;
            break;
         case TPSL_MODE_CUSTOM_PIPS:
            initializer_tmcp_tb
            double digits = toDigits(variable_name_tmcp_tb, msymbol);
            tpPrice = price + digits;
            break;
         case TPSL_MODE_CUSTOM_PRICE_FRACTION:
            initializer_tmcpf_tb
            tpPrice = price + variable_name_tmcpf_tb;
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
         case TPSL_MODE_PERCENT_OF_PRICE:
            slPrice = SymbolInfoDouble(msymbol, SYMBOL_ASK) - (SymbolInfoDouble(msymbol, SYMBOL_ASK) * stoploss_percent / 100);
            break;
         case TPSL_MODE_PERCENT_OF_TP:
            calc_tp_buy();
            slPrice = price - ((tpPrice-price) * stoploss_percent / 100);
            break;
         case TPSL_MODE_CUSTOM_PRICE_LEVEL:
            initializer_tmcpl_sb
            slPrice = variable_name_tmcpl_sb;
            break;
         case TPSL_MODE_CUSTOM_PIPS:
            initializer_tmcp_sb
            double digits = toDigits(variable_name_tmcp_sb, msymbol);
            slPrice = price - digits;
            break;
         case TPSL_MODE_CUSTOM_PRICE_FRACTION:
            initializer_tmcpf_sb
            slPrice = price - variable_name_tmcpf_sb;
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
         case TPSL_MODE_PERCENT_OF_PRICE:
            tpPrice = SymbolInfoDouble(msymbol, SYMBOL_BID) - (SymbolInfoDouble(msymbol, SYMBOL_BID) * takeprofit_percent / 100);
            break;
         case TPSL_MODE_PERCENT_OF_SL:
            calc_sl_sell();
            tpPrice = price - ((slPrice-price) * takeprofit_percent / 100);
            break;
         case TPSL_MODE_CUSTOM_PRICE_LEVEL:
            initializer_tmcpl_ts
            tpPrice = variable_name_tmcpl_ts;
            break;
         case TPSL_MODE_CUSTOM_PIPS:
            initializer_tmcp_ts
            double digits = toDigits(variable_name_tmcp_ts, msymbol);
            tpPrice = price - digits;
            break;
         case TPSL_MODE_CUSTOM_PRICE_FRACTION:
            initializer_tmcpf_ts
            tpPrice = price - variable_name_tmcpf_ts;
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
         case TPSL_MODE_PERCENT_OF_PRICE:
            slPrice = SymbolInfoDouble(msymbol, SYMBOL_BID) + (SymbolInfoDouble(msymbol, SYMBOL_BID) * stoploss_percent / 100);
            break;
         case TPSL_MODE_PERCENT_OF_TP:
            calc_tp_buy();
            slPrice = price + ((price-tpPrice) * stoploss_percent / 100);
            break;
         case TPSL_MODE_CUSTOM_PRICE_LEVEL:
            initializer_tmcpl_ss
            slPrice = variable_name_tmcpl_ss;
            break;
         case TPSL_MODE_CUSTOM_PIPS:
            initializer_tmcp_ss
            double digits = toDigits(variable_name_tmcp_ss, msymbol);
            slPrice = price + digits;
            break;
         case TPSL_MODE_CUSTOM_PRICE_FRACTION:
            initializer_tmcpf_ss
            slPrice = price + variable_name_tmcpf_ss;
            break;
        }
     }

/////////////////////////////////////////////////////////////

   void              calcVolume()
     {
      if(money_management == MONEY_MANAGEMENT_FIXED_VOLUME)
        {
         volume = DynamicLots(msymbol, money_management, how_much_volume);
        }
      else
         if(money_management == MONEY_MANAGEMENT_PERCENT_OF_EQUITY)
           {
            volume = lotsPercentOfEquity(msymbol, price, slPrice, how_much_volume);
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
                                             int mlook_up_on =  order_type == ORDER_BUY || order_type == ORDER_SELL ? look_up_on : 0;
                                             volume = BetMartingale(msymbol, mlook_up_on, group, type, martingale_init_vol, martingale_multiply_on_loss, martingale_multiply_on_profit, martingale_addlots_on_loss, martingale_addlots_on_profit, martingale_reset_on_n_losses, martingale_reset_on_n_profits);
                                            }
                                          else
                                             if(money_management == MONEY_MANAGEMENT_CUSTOM_VALUE)
                                               {
                                                //lots = _dVolumeSize_();
                                               }


      if(volume_upper_limit>0 && volume>volume_upper_limit)
         volume = volume_upper_limit;
     }

   double            lotsPercentOfEquity(string symbol, double entry, double stopLossLevel, double riskPercent)
     {
      double point = MarketInfo(symbol,MODE_POINT);
      if(point==0)
        {
         printf("Failed to calc lot size: point value is zero");
         return 0;
        }
      double stopLossPips = MathAbs(entry - stopLossLevel) / point;
      double accountEquity = AccountEquity();
      double riskAmount = (riskPercent / 100.0) * accountEquity;
      double pipValue = MarketInfo(symbol, MODE_TICKVALUE);
      double lotSize = riskAmount / (stopLossPips * pipValue);
      return NormalizeDouble(lotSize, 2); // round to 2 decimal places
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
