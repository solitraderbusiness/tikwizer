
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



class Task20 : public Task
  {


public:
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   double            older_than;//in minutes
   color             arrow_color;
   double            slippage;

   int               retryCount;

public:
   void              Task20(string name): Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      int mtype[] = {0}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      older_than = 0.3;//in minutes
      arrow_color = Red;
      slippage = 3;

      retryCount = 0;
     }


   virtual void      run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      //STest, trades not sorted by newest
      for(int i = OrdersTotal()-1 ; i >=0 ; i--)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            if(!filterAge(older_than))
               continue;
            bool result = OrderClose(OrderTicket(),OrderLots(),OrderClosePrice(),slippage,arrow_color);
            if(!result)  //STest, if fatal error, skip retry, otherwise retry.
              {
               int err = GetLastError();
              } else {
                OnTrade();
              }
           }
        }
      retryCount++;
      block.onResult(ROUTE_1_PASSED);
     }

   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

   bool              filterAge(double mins)
     {
      datetime openTime = OrderOpenTime();
      return TimeCurrent() - OrderOpenTime() >= mins*60;
     }
  };






//Considering each magic number is a 7 digit number like 2088100,
//I choose to take first two digits as group number.
int getGroupNumber(int magic)
  {
   return (int)(magic/100000);
  }

//This just checks if order is buy or sell
bool sameOrderType(int &type[], int orderType)
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
