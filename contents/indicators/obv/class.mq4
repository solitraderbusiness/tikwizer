
class OBV

  {
   string            symbol;
   int               timeframe;
   int               applied_price;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      applied_price = PRICE_CLOSE;
      shift = 1;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iOBV(symbol,timeframe, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
