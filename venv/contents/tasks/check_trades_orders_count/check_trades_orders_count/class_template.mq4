/*
all items in check trade/orders count section can be covered by this
function, except for items containing nearby in their title. for example
count_limit=0 and operator = "==" means no trade of type ... .
count_limit=10 and operator = ">" and type=[1,2,3,4,5] means all types
of trades be more than 10.
count_limit=10 and operator = ">=" and type=[3,4,5,6] means all pending
orders be at least 10.
*/
class Task_id : public Task
  {
   //specified by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               count_limit;

public:
                     Task_id(string name):Task(name)
     {
      //specified by user
      symbol = symbol_val;
      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      count_limit = count_limit_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      msymbol = getSymbol(symbol);
      int count_total = OrdersTotal();
      int count = 0;
      for(int i = 0 ; i < count_total ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            bool con1 = msymbol==NULL || msymbol==OrderSymbol();
            bool con2 = sameOrderType(type, OrderType());
            bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
            bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
            if(con1 && con2 && con3 && con4)
               count++;
           }
        }

      bool result = count operator_val count_limit;
      if(result)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level) {}
  };

