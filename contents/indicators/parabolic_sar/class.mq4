
class Parabolic_SAR

  {
   string            symbol;
   int               timeframe;
   double            step;
   double            maximum;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      step = 0.02;
      maximum = 0.2;
      shift = 0;
     }

   double            calc()

     {
     string symbol =  getSymbol(this.symbol);
      int timeframe = getTimeframe(this.timeframe);


      double result = iSAR(symbol,timeframe,step, maximum, shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
