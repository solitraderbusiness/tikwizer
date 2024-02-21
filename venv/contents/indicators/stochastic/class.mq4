
class Stochastic

  {
   string            symbol;
   int               timeframe;
   int               k_period;
   int               d_period;
   int               slowing;
   int               method;
   int               price_field;
   int               mode;
   int               shift;

public:

   void              init()
     {
      symbol = NULL;
      timeframe = 0;
      k_period = 5;
      d_period = 3;
      slowing = 3;
      method = MODE_SMA;
      price_field = 0;
      mode = MODE_MAIN;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iStochastic(symbol,timeframe,k_period,d_period,slowing, method, price_field, mode, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
