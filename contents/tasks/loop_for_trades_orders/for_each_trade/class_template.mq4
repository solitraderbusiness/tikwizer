
class Task_id : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               loop_direction;
   int               skip_n;
   int               not_more_than_n;
   int               every_n;


public:
                     Task_id(string name):Task(name)
     {
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      loop_direction = loop_direction_val;
      skip_n = skip_n_val;//STest, default must be 0
      not_more_than_n = not_more_than_n_val;
      every_n = every_n_val;//STest default must be 1
     }

   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

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
         for(int i = starti ; i < MathMin(endi, size) ; i+=every_n)
           {
            if(exit_loop)
                return;//STest, logical?
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
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
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
