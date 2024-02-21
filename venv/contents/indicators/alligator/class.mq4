
class Alligator

  {
   string            symbol;
   int               timeframe;
   int               jaw_period;
   int               jaw_shift;
   int               teeth_period;
   int               teeth_shift;
   int               lips_period;
   int               lips_shift;
   int               ma_method;
   int               applied_price;
   int               mode;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      jaw_period = 13;
      jaw_shift = 8;
      teeth_period = 8;
      teeth_shift = 5;
      lips_period = 5;
      lips_shift = 3;
      ma_method = MODE_SMMA;
      applied_price = PRICE_MEDIAN;
      mode = MODE_GATORJAW;
      shift = 1;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);

      double result = iAlligator(symbol,timeframe,jaw_period,jaw_shift,teeth_period, teeth_shift, lips_period, lips_shift, ma_method, applied_price, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
