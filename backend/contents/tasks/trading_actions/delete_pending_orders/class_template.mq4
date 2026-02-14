
// Delete pending orders
class Task_id : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[];
   color             arrow_color;

public:
                     Task_id(string name):Task(name)
     {
      //specified by user
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;

      group_mode = group_mode_val;
      group_number = group_number_val;
      arrow_color = arrow_color_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
      ArrayResize(type, 0, 0);
      int mtype[] = type_val;
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      for(int i = OrdersTotal()-1 ; i >= 0 ; i--)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            bool success = DeleteOrder(OrderTicket(), arrow_color);
            if (success)
                OnTrade();
           }
        }
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

