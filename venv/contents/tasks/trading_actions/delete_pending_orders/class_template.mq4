
// Delete pending orders
class Task_id : public Task
  {
   //defined by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   color             arrow_color;
   //defined by system
   string            msymbol;
public:
                     Task_id(string name):Task(name)
     {
      //specified by user
      symbol = symbol_val;
      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      arrow_color = arrow_color_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      for(int i = OrdersTotal() ; i >= 0 ; i--)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            DeleteOrder(OrderTicket(), arrow_color);
           }
        }
      block.onResult(ROUTE_1_PASSED);
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

  };

