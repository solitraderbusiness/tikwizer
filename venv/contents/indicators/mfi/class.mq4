
class MFI

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
      period = 14;
      shift = 1;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iMFI(symbol,timeframe,period,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
