

class ICHIMOKU

  {

   

   string            symbol;

   int               timeframe;

   int               tenkan_sen;

   int               kijun_sen;

   int               senkou_span_b;

   int               mode;

   int               shift;



public:

   void              init()

     {

      

      symbol = NULL;

      timeframe = 0;

      tenkan_sen = 9;

      kijun_sen = 26;

      senkou_span_b = 52;

      mode = MODE_TENKANSEN;

      shift = 1;

     }



   double            calc()

     {

      double result = iIchimoku(symbol,timeframe,tenkan_sen,kijun_sen,senkou_span_b,mode,shift);

      return result;

     }



  };