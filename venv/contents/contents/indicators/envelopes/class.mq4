
class Envelopes

  {
   string            symbol;
   int               timeframe;
   int               ma_period;
   int               ma_method;
   int               ma_shift;
   int               applied_price;
   double            deviation;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      ma_period = 13;
      ma_method = MODE_SMA;
      ma_shift = 10;
      applied_price = PRICE_CLOSE;
      deviation = 0.2;
      mode = MODE_UPPER;
      shift = 0;
     }

   double            calc()

     {
      double result = iEnvelopes(symbol, timeframe, ma_period, ma_method, ma_shift, applied_price, deviation, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
