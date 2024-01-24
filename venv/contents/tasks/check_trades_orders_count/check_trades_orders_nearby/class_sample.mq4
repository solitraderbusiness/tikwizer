//+------------------------------------------------------------------+
//|                                                      ProjectName |
//|                                      Copyright 2018, CompanyName |
//|                                       http://www.companyname.net |
//+------------------------------------------------------------------+

#define ROUTE_1_PASSED 1
#define ROUTE_2_PASSED 0

string overriding_symbol = "";
string overriding_timeframe = -1;












//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class BlockParent
  {
public:
   int               current_source_id;
   int               nexts_true[];//static, filled by generator
   int               nexts_false[];//static, filled by generator
   int               prevs_true[];//static, filled by generator
   int               prevs_false[];//static, filled by generator

public:
   virtual void      onResult(int result) = NULL;
  };

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task
  {
public:
   string            name;
public:
                     Task(string name)
     {
      this.name = name;
     }

   virtual void               run(int block_id, BlockParent &block)
     {

     }

   virtual void      reset(int level) = NULL;

  };

#define ORDER_GROUP_MODE_ALL 0
#define ORDER_GROUP_MODE_NUMBER 1
#define ORDER_GROUP_MODE_AUTOMATED 2

#define PRICE_AUTO 1 //auto means ask for buy and bid for sell
#define PRICE_ASK 2
#define PRICE_BID 3
#define PRICE_MID 4

#define RANGE_MODE_PIPS 1
#define RANGE_MODE_PRICE_FRACTION 2

#define RANGE_POSITION_AROUND 1
#define RANGE_POSITION_WINNING_SIDE 2
#define RANGE_POSITION_LOSING_SIDE 3



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
   int               price_mode;
   int               range_mode;
   int               range_position;
   double            range_value;




public:
                     Task17(string name):Task(name)
     {
      //specified by user
      symbol = NULL;
      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 25;
      int mtype[] = {1,2}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      count_limit = 0;
      price_mode = PRICE_AUTO;
      range_mode = RANGE_MODE_PIPS;
      range_position = RANGE_POSITION_AROUND;
      range_value = 10;
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
              {
               int orderType = OrderType();
               double price;
               double ask = SymbolInfoDouble(msymbol, SYMBOL_ASK);
               double bid = SymbolInfoDouble(msymbol, SYMBOL_BID);
               double point = SymbolInfoDouble(msymbol, SYMBOL_POINT);
               if(price_mode==PRICE_AUTO)
                 {
                  if(MathMod(orderType,2)==0)
                     price = ask;
                  else
                     price = bid;
                 }
               else
                  if(price_mode==PRICE_MID)
                     price = (ask+bid)/2;
                  else
                     if(price_mode==PRICE_ASK)
                        price = ask;
                     else
                        if(price_mode==PRICE_BID)
                           price = bid;

               double rangeFraction;
               if(range_mode==RANGE_MODE_PIPS)
                  rangeFraction = range_value*point*10;
               else
                  if(range_mode==RANGE_MODE_PRICE_FRACTION)
                     rangeFraction = range_value;

               //Now we have range value and price, start comparison process.
               double openPrice = OrderOpenPrice();
               if(range_position==RANGE_POSITION_AROUND)  //Order type doesn't matter
                 {
                  if((price>=openPrice && price<openPrice+rangeFraction) || (price<=openPrice && price>openPrice-rangeFraction))
                     count++;
                 }
               else
                  if(range_position==RANGE_POSITION_LOSING_SIDE)
                    {
                     if(MathMod(orderType, 2)==0)   //buy
                       {
                        if(openPrice-rangeFraction<=price)
                           count++;
                       }
                     else    //sell
                       {
                        if(openPrice+rangeFraction>=price)
                           count++;
                       }

                    }
                  else
                     if(range_position==RANGE_POSITION_WINNING_SIDE)
                       {
                        if(MathMod(orderType, 2)==0)   //buy
                          {
                           if(openPrice+rangeFraction<=price)
                              count++;
                          }
                        else    //sell
                          {
                           if(openPrice-rangeFraction>=price)
                              count++;
                          }

                       }
              }

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







//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void OnTick()
  {

  }
//+------------------------------------------------------------------+
