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
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               on_profit_mode;
   double            pips_on_profit;
   int               bep_offset_mode;
   double            bep_offset;
   //defined by system
   string            msymbol;
public:
                     Task0(string name):Task(name)
     {
      symbol = NULL;//STest, no lists yet, also all is not suported yet.
      group_mode = ORDER_GROUP_MODE_NONE;
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
      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

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
               distance = toDigits(pips_on_profit, msymbol);
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
            printf("AAAA "+(SymbolInfoDouble(msymbol,SYMBOL_ASK)-SymbolInfoDouble(msymbol,SYMBOL_BID)));
            bool con1 = orderType == OP_BUY && (SymbolInfoDouble(msymbol,SYMBOL_ASK)-OrderOpenPrice() > distance) && (OrderStopLoss() < OrderOpenPrice());
            bool con2 = orderType == OP_SELL && (OrderOpenPrice()-SymbolInfoDouble(msymbol,SYMBOL_BID) > distance) && ((OrderStopLoss() > OrderOpenPrice()) || OrderStopLoss() == 0);
            if(con1 || con2)
              {
               double be_offset = 0;

               if(bep_offset_mode == BEP_OFFSET_MODE_PIPS_OFFSET)
                 {
                  be_offset = toDigits(bep_offset,symbol);
                  if(orderType == OP_SELL)
                     be_offset *=-1;
                 }
               double new_slPrice = OrderOpenPrice()+be_offset;
               OrderModify(OrderTicket(), OrderOpenPrice(), new_slPrice, OrderTakeProfit(), 0, clrNONE);
              }
           }
        }
      printf("task"+block_id + " passsed route 1");
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
      bool con1 = (msymbol==NULL && OrderSymbol()==Symbol()) || msymbol==OrderSymbol();
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
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
