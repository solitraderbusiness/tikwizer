
class MARKET_FACILITATION

  {
   string            symbol;
   int               timeframe;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 10;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iBWMFI(symbol,timeframe,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
