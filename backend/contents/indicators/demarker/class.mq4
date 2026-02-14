
class DeMarker

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 13;
      shift = 1;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);

      double result = iDeMarker(symbol,timeframe,period, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
