#define LOOP_DIRECTION_NEWEST_TO_OLDEST 1
#define LOOP_DIRECTION_OLDEST_TO_NEWEST 2
#define LOOP_DIRECTION_PROFITABLE_FIRST 3
#define LOOP_DIRECTION_PROFITABLE_LAST 4

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task12 : public Task
  {
   //defined by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               loop_direction;
   int               skip_n;
   int               not_more_than_n;
   int               every_n;
   //defined by system
   string            msymbol;

public:
                     Task12(string name):Task(name)
     {
      symbol = NULL;//STest, no lists yet, also all is not supported yet.
      group_mode = ORDER_GROUP_MODE_NONE;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      loop_direction = LOOP_DIRECTION_OLDEST_TO_NEWEST;
      skip_n = 1;//STest, default must be 0
      not_more_than_n = 5;
      every_n = 2;//STest default must be 1
     }

   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      int trades[];
      getTrades(trades);
      int size = ArraySize(trades);
      if(size==0)
        {
         block.onResult(ROUTE_2_PASSED);
         return;
        }
      if(size>=2)
         sortTrades(trades, loop_direction);
      int starti, endi;
      starti = skip_n;
      endi = not_more_than_n*every_n+starti;
      if(starti<=size-1)
         for(int i = starti ; i < MathMin(endi, size) ; i+every_n)
           {
            if(OrderSelect(trades[i], SELECT_BY_POS, MODE_TRADES))
              {
               if(!filterGeneral())
                  continue;
               block.onResult(ROUTE_1_PASSED);
              }
           }
      block.onResult(ROUTE_2_PASSED);
     }
   virtual void      reset(int level)
     {

     }
   bool              filterGeneral()
     {
      bool con1 = (msymbol==NULL && OrderSymbol()==Symbol()) || msymbol==OrderSymbol();
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }


   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              getTrades(int &trades[])
     {
      for(int i=0; i<OrdersTotal(); i++)
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(OrderType()==OP_BUY || OrderType()==OP_SELL)
              {
               AddToArray(trades, i);
              }
           }
      return trades;
     }



   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              sortTrades(int &trades[], int loop_direction)
     {
      if(loop_direction == LOOP_DIRECTION_OLDEST_TO_NEWEST)
         return trades;
      else
         if(loop_direction == LOOP_DIRECTION_NEWEST_TO_OLDEST)
           {
            ReverseList(trades);
            return trades;
           }
         else
            if(loop_direction == LOOP_DIRECTION_PROFITABLE_FIRST || loop_direction == LOOP_DIRECTION_PROFITABLE_LAST)
              {
               sortTradesByProfit(trades, loop_direction);
               return trades;
              }
      return trades;
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              sortTradesByProfit(int &trades[], int loop_direction)
     {
      if(ArraySize(trades)<2)
         return;
      for(int i=0; i<ArraySize(trades)-1; i++)
        {
         for(int j=i+1; j<ArraySize(trades); j++)
           {
            double profit1 = 0, profit2 = 0;
            if(OrderSelect(trades[i], SELECT_BY_POS, MODE_TRADES))
               profit1 = OrderProfit();
            if(OrderSelect(trades[j], SELECT_BY_POS, MODE_TRADES))
               profit2 = OrderProfit();
            if(loop_direction == LOOP_DIRECTION_PROFITABLE_FIRST && profit1<profit2)
              {
               int swap1 = trades[i];
               trades[i] = trades[j];
               trades[j] = swap1;
              }
            else
              {
               if(loop_direction == LOOP_DIRECTION_PROFITABLE_LAST && profit1>profit2)
                 {
                  int swap2 = trades[i];
                  trades[i] = trades[j];
                  trades[j] = swap2;
                 }
              }
           }
        }
     }


  };



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void ReverseList(int &arr[])
  {
   int size = ArraySize(arr);
   ArraySetAsSeries(arr, true);

   for(int i = 0; i < size / 2; i++)
     {
      int temp = arr[i];
      arr[i] = arr[size - 1 - i];
      arr[size - 1 - i] = temp;
     }
  }
