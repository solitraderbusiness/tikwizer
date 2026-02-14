
class ACCUMULATION_DISTRIBUTION

  {
   string            symbol;
   int               timeframe;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      shift = 1;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);

      double result = iAD(symbol,timeframe,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
