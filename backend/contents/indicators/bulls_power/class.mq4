
class BullsPower

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
      period = 13;
      applied_price = PRICE_CLOSE;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);

      double result = iBullsPower(symbol,timeframe,period, applied_price, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
