
class ForceIndex

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               ma_method;
   int               applied_price;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 13;
      ma_method = MODE_SMA;
      applied_price = PRICE_CLOSE;
      shift = 0;
     }

   double            calc()

     {
      double result = iForce(symbol, timeframe, period, ma_method, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
