
int ORDER_GROUP_MODE_NUMBER = 1;
int ORDER_GROUP_MODE_AUTOMATED = 2;



/*
all items in check trade/orders count section can be covered by this
function, except for items containing nearby in their title. for example
count_limit=0 and operator = "==" means no trade of type ... .
count_limit=10 and operator = ">" and type=[1,2,3,4,5] means all types
of trades be more than 10.
count_limit=10 and operator = ">=" and type=[3,4,5,6] means all pending
orders be at least 10.
*/
class Task17 : public Task
  {
   //specified by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               count_limit;

public:
                     Task17(string name):Task(name)
     {
      //specified by user
      symbol = NULL;
      group_mode = ORDER_GROUP_MODE_NUMBER;
      group_number = 25;
      int mtype[] = {1,2}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      count_limit = 0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      string msymbol = overriding_symbol=="" ? symbol : overriding_symbol;
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

      bool result = count>count_limit;
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






//Considering each magic number is a 7 digit number like 2088100,
//I choose to take first two digits as group number.
int getGroupNumber(int magic)
  {
   return (int)(magic/100000);
  }

//This just checks if order is buy or sell
bool sameOrderType(int type[], int orderType)
  {
   for(int i=0; i<ArraySize(type); i++)
      if(orderType==type[i])
         return true;
   return false;
  }

//72 is the number in magic 3rd and 4th
//digits that show it is opened by the expert
bool isAutomated(int magic)
  {
   return MathMod((int)(magic/1000), 100) == 72;
  }


