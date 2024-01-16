
#define VALUE_TYPE_NUMERIC 1
#define VALUE_TYPE_BOOLEAN 2
#define VALUE_TYPE_COLOR 3
#define VALUE_TYPE_PIPS 4
#define VALUE_TYPE_TEXT 5
#define VALUE_TYPE_TEXT_CODE_INPUT 6
#define VALUE_TYPE_TIME 7

#define VALUE_PIPS_AS_IS 1
#define VALUE_PIPS_AS_PRICE_FRACTION 2

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Value20
  {
public:
   int               type;
   int               value;
   string               adjust;
   //for pips
   int               pips_type;
   string            symbol;
   //for time (phase 2)

   string            msymbol;

public:

   void              init()

     {
      type = VALUE_TYPE_PIPS;
      value = 10;
      adjust = 20;
      //for pips
      pips_type = CANDLE_LOW;
      symbol = "2023.4.26 13:40:30";
      //for time (phase 2)
     }

   string              calc()
     {

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      switch(type)
        {
         case VALUE_TYPE_NUMERIC:
         case VALUE_TYPE_BOOLEAN:
         case VALUE_TYPE_COLOR:
         case VALUE_TYPE_TEXT:
            return (string)value;

         case VALUE_TYPE_TEXT_CODE_INPUT:
            return "\"" + value + "\"";

         case VALUE_TYPE_PIPS:
            if(pips_type == VALUE_PIPS_AS_IS)
              {
               return (string) value;
              }
            else
               if(pips_type == VALUE_PIPS_AS_PRICE_FRACTION)
                 {
                  double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                  return (string)(point*10*value);  //STest, *10 works for all symbols?
                 }
            return "";

         case VALUE_TYPE_TIME:
            return "";
        }
     }
  };
