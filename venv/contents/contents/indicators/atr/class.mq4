
class ATR

  {
   string            symbol;
   int               timeframe;
   int               period;
   int               shift;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      period = 14;
      shift = 0;
     }

   double            calc()

     {
      double result = iATR(symbol,timeframe,period,shift);
      return result;
     }



  };
//+------------------------------------------------------------------+
