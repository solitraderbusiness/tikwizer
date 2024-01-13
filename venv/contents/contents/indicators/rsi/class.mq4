
class RSI

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               applied_price;
   int               shift;

   int              buy_threshold;
   int              sell_threshold;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 14;
      applied_price = PRICE_CLOSE;
      shift = 0;

      buy_threshold = 70;
      sell_threshold = 30;
     }

   double            calc()

     {
      double result = iRSI(symbol,timeframe,period, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
