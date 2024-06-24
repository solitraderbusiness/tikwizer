#define ON_PROFIT_MODE_FIXED_VALUE 1
#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_SL 2
#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_TP 3

#define BEP_OFFSET_MODE_NONE 1
#define BEP_OFFSET_MODE_PIPS_OFFSET 2

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
   int               on_profit_mode;
   double            pips_on_profit;
   int               bep_offset_mode;
   double            bep_offset;

public:
                     Task0(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.

      on_profit_mode = ON_PROFIT_MODE_FIXED_VALUE;
      pips_on_profit = 20;
      bep_offset_mode = BEP_OFFSET_MODE_PIPS_OFFSET;
      bep_offset = 10;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      for(int i = 0 ; i < OrdersTotal() ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            //This check is beyond user defined filter.
            int orderType = OrderType();
            if(orderType!=OP_BUY && orderType!=OP_SELL)
               continue;

            double distance = 0;

            if(on_profit_mode == ON_PROFIT_MODE_FIXED_VALUE)
              {
               distance = toDigits(pips_on_profit, OrderSymbol());
              }
            else
               if(on_profit_mode == ON_PROFIT_MODE_PERCENT_OF_CURRENT_SL)
                 {
                  distance = MathAbs(OrderOpenPrice()-OrderStopLoss())*pips_on_profit/100;
                 }
               else
                  if(on_profit_mode == ON_PROFIT_MODE_PERCENT_OF_CURRENT_TP)
                    {
                     distance = MathAbs(OrderOpenPrice()-OrderTakeProfit())*pips_on_profit/100;
                    }
            bool con1 = orderType == OP_BUY && (SymbolInfoDouble(OrderSymbol(),SYMBOL_ASK)-OrderOpenPrice() > distance) && (OrderStopLoss() < OrderOpenPrice());
            bool con2 = orderType == OP_SELL && (OrderOpenPrice()-SymbolInfoDouble(OrderSymbol(),SYMBOL_BID) > distance) && ((OrderStopLoss() > OrderOpenPrice()) || OrderStopLoss() == 0);
            if(con1 || con2)
              {
               double be_offset = 0;

               if(bep_offset_mode == BEP_OFFSET_MODE_PIPS_OFFSET)
                 {
                  be_offset = toDigits(bep_offset,OrderSymbol());
                  if(orderType == OP_SELL)
                     be_offset *=-1;
                 }
               double new_slPrice = OrderOpenPrice()+be_offset;
               bool result = OrderModify(OrderTicket(), OrderOpenPrice(), new_slPrice, OrderTakeProfit(), 0, clrNONE);
               if (result)
                  OnTrade();
              }
           }
        }
      //printf("task"+block_id + " passed route 1");
      //block.onResult(ROUTE_1_PASSED);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   virtual void      reset(int level)
     {

     }
   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

  };


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double toDigits(double pips, string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   int digits   = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
   double point = SymbolInfoDouble(symbol, SYMBOL_POINT);

   return NormalizeDouble(pips * PipValue(symbol) * point, digits);
  }
