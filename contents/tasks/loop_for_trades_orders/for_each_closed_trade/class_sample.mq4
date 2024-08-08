//For each closed trade
class Task2 : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[];
   string            loop_direction;
   int               skip_n;
   int               not_more_than_n;
   int               every_n;
   string            second_output;
public:
                     Task2(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "";

      group_mode = ORDER_GROUP_MODE_NUMBER;
      group_number = 11;
      loop_direction = "newest_first";
      skip_n = 0;//STest, default must be 0
      not_more_than_n = 0;
      every_n = 1;//STest default must be 1
      second_output = "always";

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
      ArrayResize(type, 0, 0);
      int mtype[] = {1,0};
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      int trades[];
      getTrades(trades);
      int size = ArraySize(trades);
      if(size==0)
        {
         //printf("task"+block_id + " passed route 2 ");
         block.onResult(ROUTE_2_PASSED);
         return;
        }
      if(size>=2)
         sortTrades(trades);
      int starti, endi;
      starti = skip_n;
      endi = not_more_than_n<=0 ? size : not_more_than_n*every_n+starti;
      if(starti<=size-1)
         for(int i = starti ; i < MathMin(endi, size) ; i+=every_n)
           {
            if(exit_loop)
               return;//STest, logical?
            if(OrderSelect(trades[i], SELECT_BY_POS, MODE_HISTORY))
              {
               if(!filterGeneral())
                  continue;
               //printf("task"+block_id + " passed route 1 ");
               block.onResult(ROUTE_1_PASSED);
              }
           }
      if(
         second_output=="always" ||
         (second_output=="if_empty" && ArraySize(trades)==0) ||
         (second_output=="if_not_empty" && ArraySize(trades)>0)
      )
        {
         //printf("task"+block_id + " passed route 2 ");
         block.onResult(ROUTE_2_PASSED);
        }
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
      for(int i=0; i<OrdersHistoryTotal(); i++)
         if(OrderSelect(i, SELECT_BY_POS, MODE_HISTORY))
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
   void              sortTrades(int &trades[])
     {
      if(loop_direction == "oldest_first")
         return trades;
      else
         if(loop_direction == "newest_first")
           {
            ReverseList(trades);
            return trades;
           }
         else
            if(loop_direction == "profitable_first" || loop_direction == "profitable_last")
              {
               sortTradesByProfit(trades);
               return trades;
              }
      return trades;
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              sortTradesByProfit(int &trades[])
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
            if(loop_direction == "profitable_first" && profit1<profit2)
              {
               int swap1 = trades[i];
               trades[i] = trades[j];
               trades[j] = swap1;
              }
            else
              {
               if(loop_direction == "profitable_last" && profit1>profit2)
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
