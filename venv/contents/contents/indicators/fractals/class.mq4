
class Fractals

  {
   string            symbol;
   int               timeframe;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      mode = MODE_UPPER;
      shift = 3;
     }

   double            calc()

     {
      double result = iFractals(symbol,timeframe, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
