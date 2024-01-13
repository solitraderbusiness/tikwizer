
class MACD

  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      fast_ema_period = 12;
      slow_ema_period = 26;
      signal_period = 9;
      applied_price = PRICE_CLOSE;
      mode = MODE_MAIN;
      shift = 0;
     }

   double            calc()

     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
