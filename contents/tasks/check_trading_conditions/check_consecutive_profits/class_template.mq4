class Task3 : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   int                ConsecutiveCount;

public:
                     Task3(string name):Task(name)
     {
      //specified by user
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      ConsecutiveCount = (int)ConsecutiveCount_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int count = 0;
      int total          = OrdersHistoryTotal();

      for(int index = total-1; index >= 0; index--)
        {
         if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)
           {
            if(!filterGeneral())
               continue;
            if(OrderProfit() <= 0)
              {
               break;
              }

            count++;
           }
        }

      if(count compare_val ConsecutiveCount)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
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

  };
