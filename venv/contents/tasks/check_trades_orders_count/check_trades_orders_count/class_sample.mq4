#define SYMBOL_MODE_SPECIFIED 1
#define SYMBOL_MODE_ANY 2

/*
all items in check trade/orders count section can be covered by this
function, except for items containing nearby in their title. for example
count_limit=0 and operator = "==" means no trade of type ... .
count_limit=10 and operator = ">" and type=[1,2,3,4,5] means all types
of trades be more than 10.
count_limit=10 and operator = ">=" and type=[3,4,5,6] means all pending
orders be at least 10.
*/
class Task0 : public Task
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
                     Task0(string name):Task(name)
     {
      //specified by user
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_NONE;
      group_number = 25;
      int mtype[] = {1,2}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      count_limit = 0;
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

      bool result = count>count_limit;
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
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }
  };
