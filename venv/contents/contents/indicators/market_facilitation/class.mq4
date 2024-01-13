
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
      double result = iBWMFI(symbol,timeframe,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
