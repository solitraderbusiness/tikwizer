
class Momentum

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               applied_price;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 12;
      applied_price = PRICE_CLOSE;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iMomentum(symbol,timeframe,period, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
