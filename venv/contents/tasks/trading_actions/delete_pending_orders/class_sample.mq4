
// Delete pending orders
class Task20 : public Task
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
                     Task20(string name):Task(name)
     {
      symbol = NULL;//STest, no lists yet, also all is not supported yet.
      group_mode = ORDER_GROUP_MODE_NONE;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      arrow_color = clrPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      for(int i = OrdersTotal()-1 ; i >= 0 ; i--)
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

