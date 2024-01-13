
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
      double result = iAD(symbol,timeframe,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
