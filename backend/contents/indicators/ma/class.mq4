
class MovingAverage

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
      ma_period = 13;
      ma_shift = 8;
      ma_method = MODE_SMMA;
      applied_price = PRICE_MEDIAN;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);

      double result = iMA(symbol, timeframe, ma_period, ma_shift, ma_method, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
