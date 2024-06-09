
#define TRAILING_DISTANCE_MODE_FIXED 1
#define TRAILING_DISTANCE_MODE_DYNAMIC 2
#define TRAILING_DISTANCE_MODE_DYNAMIC_PIPS 3
#define TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS 4


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task3 : public Task
  {
public:
      //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   int               trailing_distance_mode;
   double            t_distance_pips;
   double            t_step_pips;

public:
                     Task3(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      int mtype[] = {2, 3, 4, 5}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.

      trailing_distance_mode = TRAILING_DISTANCE_MODE_FIXED;
      t_distance_pips = 10.0;
      t_step_pips = 1.0;
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

            string symbol   = OrderSymbol();
            double price    = (IsOrderTypeBuy()) ? SymbolAsk(symbol) : SymbolBid(symbol);
            double distance = 0;
            int digits      = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);

            if(trailing_distance_mode == TRAILING_DISTANCE_MODE_FIXED)
               distance = toDigits(t_distance_pips, symbol);
            else
               if(trailing_distance_mode == TRAILING_DISTANCE_MODE_DYNAMIC)
                 {
                  Value1_right value1_right;
                  value1_right.init();
                  double valueValue1_right_d = value1_right.calc();
                  distance = price - valueValue1_right_d;
                 }
               else
                  if(trailing_distance_mode == TRAILING_DISTANCE_MODE_DYNAMIC_PIPS)
                    {
                     Value1_right value1_right;
                     value1_right.init();
                     double valueValue1_right_dp = value1_right.calc();
                     distance = toDigits(valueValue1_right_dp, OrderSymbol());
                    }
                  else
                     if(trailing_distance_mode == TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS)
                       {
                        Value1_right value1_right;
                        value1_right.init();
                        double valueValue1_right_dd = value1_right.calc();
                        distance = valueValue1_right_dd;
                       }


            distance = NormalizeDouble(MathAbs(distance), digits);

            double old_op = 0, old_sl = 0, old_tp = 0;
            double new_op = 0, new_sl = 0, new_tp = 0;

            if(MathAbs(price - OrderOpenPrice()) >= MathAbs(distance + toDigits(t_step_pips, symbol)))
              {
               old_sl = OrderStopLoss();
               old_tp = OrderTakeProfit();
               old_op = OrderOpenPrice();

               if(IsOrderTypeBuy() == true)
                 {
                  new_op = IsOrderTypeStop() ? price + distance : price - distance;

                  if(old_sl > 0)
                     new_sl = new_op - (old_op - old_sl);
                  if(old_tp > 0)
                     new_tp = new_op + (old_tp - old_op);
                 }
               else
                 {
                  new_op = IsOrderTypeStop() ? price - distance : price + distance;

                  if(old_sl > 0)
                     new_sl = new_op + (old_sl - old_op);
                  if(old_tp > 0)
                     new_tp = new_op - (old_op - old_tp);
                 }

               bool result = OrderModify(OrderTicket(), new_op, new_sl, new_tp, 0, clrBlack);
               if (result)
                  OnTrade();
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
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

  };

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double SymbolAsk(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return SymbolInfoDouble(symbol, SYMBOL_ASK);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double SymbolBid(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return SymbolInfoDouble(symbol, SYMBOL_BID);
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool IsOrderTypeBuy()
  {
   int type = OrderType();

   return (type == OP_BUY || type == OP_BUYSTOP || type == OP_BUYLIMIT);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool IsOrderTypeStop()
  {
   int type = OrderType();

   return (type == OP_BUYSTOP || type == OP_SELLSTOP);
  }
