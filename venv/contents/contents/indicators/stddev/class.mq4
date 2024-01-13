
class StdDev

  {
   string            symbol;
   int               timeframe;
   int               ma_period;
   int               ma_shift;
   int               ma_method;
   int               applied_price;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      ma_period = 10;
      ma_shift = 0;
      ma_method = MODE_EMA;
      applied_price = PRICE_CLOSE;
      shift = 0;
     }

   double            calc()

     {
      double result = iStdDev(symbol, timeframe, ma_period, ma_shift, ma_method, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
