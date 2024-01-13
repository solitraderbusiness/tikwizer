
class BOLLINGER_BAND

  {

   string            symbol;
   int               timeframe;
   int               period;
   double               deviation;
   int               bands_shift;
   int               applied_price;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 20;
      deviation = 2;
      bands_shift = 0;
      applied_price = PRICE_CLOSE;
      mode = MODE_LOWER;
      shift = 0;
     }

   double            calc()

     {
      double result = iBands(symbol,timeframe,period,deviation,bands_shift,applied_price,mode,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
