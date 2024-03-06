#define PRICE_RELATIVE_TO_OPEN_PRICE 1
#define PRICE_RELATIVE_TO_CURRENT_PRICE 2
#define PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL 3

#define NEW_STOPS_FIXED 1
#define NEW_STOPS_PERCENT_OF_CURRENT_TPSL 2
#define NEW_STOPS_CUSTOM_PRICE_LEVEL 3

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task0 : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   string            msymbol;

   int               order_age_mins;
   int               relative_to;
   int               new_tpsl_mode;
   double            new_stoploss;
   double            new_stoploss_percent;
   double            new_takeprofit;
   double            new_takeprofit_percent;
   color             level_color;


public:
                     Task0(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_NONE;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.

      order_age_mins = 0;
      relative_to = PRICE_RELATIVE_TO_CURRENT_PRICE;
      new_tpsl_mode = NEW_STOPS_FIXED;
      new_stoploss = 30.0;
      new_stoploss_percent = 50.0;
      new_takeprofit = 80.0;
      new_takeprofit_percent = 50.0;
      level_color = clrDeepPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      for(int m = OrdersTotal()-1 ; m >= 0 ; m--)
        {
         if(OrderSelect(m, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;

            if(!filterAge())
               continue;
            

            string symbol = OrderSymbol();//STest, conflict with symbol in the field

            int digits   = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
            double oldSL = NormalizeDouble(OrderStopLoss(), digits);
            double oldTP = NormalizeDouble(OrderTakeProfit(), digits);
            double OP    = NormalizeDouble(OrderOpenPrice(), digits);

            //reference price
            double price = 0;

            if(relative_to == PRICE_RELATIVE_TO_OPEN_PRICE)
              {
               price = OP;
              }
            else
               if(relative_to == PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL)
                 {

                  Value1_right value1_right;
                  value1_right.init();
                  double valueValue1_right_d = value1_right.calc();
                  price = valueValue1_right_d;


                 }
               else
                  if(relative_to == PRICE_RELATIVE_TO_CURRENT_PRICE)
                    {
                     price = (OrderType() == 0) ? SymbolInfoDouble(symbol, SYMBOL_ASK) : SymbolInfoDouble(symbol, SYMBOL_BID);
                    }

            //-- Calculate the new SL and TP
            double SL = 0;
            double TP = 0;

            if(new_tpsl_mode == NEW_STOPS_FIXED)
              {
              
               SL = toDigits(new_stoploss, symbol);
               TP = toDigits(new_takeprofit, symbol);

               printf(SL);

               if(OrderType() == 0)
                 {
                  if(SL != 0)
                    {
                     SL = price - SL;
                    }
                  if(TP != 0)
                    {
                     TP = price + TP;
                    }
                 }
               else
                 {
                  if(SL != 0)
                    {
                     SL = price + SL;
                    }
                  if(TP != 0)
                    {
                     TP = price - TP;
                    }
                 }
              }
            else
               if(new_tpsl_mode == NEW_STOPS_PERCENT_OF_CURRENT_TPSL)
                 {
                  if(OrderType() == 0)
                    {
                     SL = price - (((OP - oldSL) * new_stoploss_percent) / 100);
                     TP = price + (((oldTP - OP) * new_takeprofit_percent) / 100);
                    }
                  else
                    {
                     SL = price + (((oldSL - OP) * new_stoploss_percent) / 100);
                     TP = price - (((OP - oldTP) * new_takeprofit_percent) / 100);
                    }
                 }
               else
                  if(new_tpsl_mode == NEW_STOPS_CUSTOM_PRICE_LEVEL)
                    {

                     Value1_right value1_right;
                     value1_right.init();
                     double valueValue1_right_d = value1_right.calc();
                     SL = valueValue1_right_d;

                     Value3_right value3_right;
                     value3_right.init();
                     double valueValue3_right_d = value1_right.calc();
                     TP = valueValue3_right_d;

                    }

            SL = NormalizeDouble(SL, digits);
            TP = NormalizeDouble(TP, digits);

            if(SL != oldSL || TP != oldTP)
              {
                bool result = OrderModify(OrderTicket(), OrderOpenPrice(), SL, TP, OrderExpiration(), level_color);  
              }
           }
        }
        
      printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
      
     }
   virtual void      reset(int level)
     {

     }
   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

   bool              filterAge()
     {
      datetime time_diff = TimeCurrent() - OrderOpenTime();
      if(time_diff < 0)// sometimes happens
        {
         time_diff = 0;
        }
      return time_diff >= 60 * order_age_mins;
     }

  };
