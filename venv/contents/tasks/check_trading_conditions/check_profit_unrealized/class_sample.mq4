#define ORDER_GROUP_MODE_NONE 0
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

#define PROFIT_MODE_PIPS 1
#define PROFIT_MODE_MONEY 2

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task33 : public Task
  {

public:
   //defined by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               profit_mode;
   double            profit_benchmark_filter;
   double            profit_benchmark_comparison;
   //defined by system
   string            msymbol;

public:
   void              Task33(string name): Task(name)
     {
      symbol = NULL;//STest, no lists yet, also all is not supported yet.
      group_mode = ORDER_GROUP_MODE_NONE;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      profit_mode = PROFIT_MODE_MONEY;
      profit_benchmark_filter = 0;
      profit_benchmark_comparison = 100;
     }


   virtual void      run(int block_id, BlockParent &block)
     {
      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      double profitTotal=0;
      for(int i = 0 ; i < OrdersTotal() ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;

            double profit = getProfit();

            if(!filterSpecific(profit))
               continue;

            profitTotal += profit;
           }
        }

      bool result = profitTotal >= profit_benchmark_comparison;
      if(result)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }

   bool              filterGeneral()
     {
      bool con1 = (msymbol==NULL && OrderSymbol()==Symbol()) || msymbol==OrderSymbol();
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

   bool              filterSpecific(double profit)
     {
      return profit != profit_benchmark_filter;
     }

   double              getProfit()
     {
      double tradeProfit;
      if(profit_mode == PROFIT_MODE_MONEY)
        {
         tradeProfit = NormalizeDouble(OrderProfit() + OrderSwap() + OrderCommission(), 2); //STest, sure about + ?
        }
      else
         if(profit_mode == PROFIT_MODE_PIPS)
           {
            double profitVal = OrderType()==OP_BUY ? OrderClosePrice() - OrderOpenPrice() : OrderOpenPrice() - OrderClosePrice(); //STest, commission and swap
            tradeProfit = toPips(profitVal, OrderSymbol());
           }
      return tradeProfit;
     }

   double            toPips(double price, string symbol)
     {
      if(msymbol == "")
         msymbol = Symbol();
      return price/SymbolInfoDouble(msymbol, SYMBOL_POINT)/10;
     }
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
