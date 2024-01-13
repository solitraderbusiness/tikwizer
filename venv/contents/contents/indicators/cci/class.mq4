
class CCI

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               applied_price;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 12;
      applied_price = PRICE_TYPICAL;
      shift = 0;
     }

   double            calc()

     {
      double result = iCCI(symbol,timeframe,period, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
