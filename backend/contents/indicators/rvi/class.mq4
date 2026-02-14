
class RVI

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 10;
      mode = MODE_MAIN;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iRVI(symbol,timeframe,period, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
