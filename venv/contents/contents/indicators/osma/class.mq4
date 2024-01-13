
class OsMA

  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      fast_ema_period = 12;
      slow_ema_period = 26;
      signal_period = 9;
      applied_price = PRICE_OPEN;
      shift = 1;
     }

   double            calc()

     {
      double result = iOsMA(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
