
class ADX

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               applied_price;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 14;
      applied_price = PRICE_HIGH;
      mode = MODE_MAIN;
      shift = 0;
     }

   double            calc()

     {
      double result = iADX(symbol,timeframe,period, applied_price, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
