
class Task_id : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               count_limit;

public:
                     Task_id(string name):Task(name)
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
      count_limit = count_limit_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int count_total = OrdersTotal();
      int count = 0;
      for(int i = 0 ; i < count_total ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(filterGeneral())
               count++;
           }
        }

      bool result = count operator_val count_limit;
      if(result)
        {
         printf("task" + block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level) {}
   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }
  };
