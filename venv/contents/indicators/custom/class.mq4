
class CustomIndicator

  {
   string            symbol;
   int               timeframe;
   string            name;

   custom_field

   int               mode;
   int               shift;

public:

   void              init()

     {
      custom_init
     }

   double            calc()

     {
      double result = iCustom(symbol, timeframe, name,       custom_params       mode, shift);
      return result;
     }



  };
