
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
   int               pips_mode;
   string            symbol;
   //for time (phase 2)

   string            msymbol;

public:

   void              init()

     {
      type = VALUE_TYPE_PIPS;
      value = 10;
      //for pips
      pips_mode = VALUE_PIPS_AS_IS;
      symbol = "NULL";
      //for time (phase 2)
     }

   string              calc()
     {

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;
      string result = "";
      switch(type)
        {
         case VALUE_TYPE_NUMERIC:
         case VALUE_TYPE_BOOLEAN:
         case VALUE_TYPE_COLOR:
         case VALUE_TYPE_TEXT:
            result = (string)value;
            break;

         case VALUE_TYPE_TEXT_CODE_INPUT:
            result = "\"" + value + "\"";
            break;

         case VALUE_TYPE_PIPS:
            if(pips_mode == VALUE_PIPS_AS_IS)
              {
               result = (string) value;
              }
            else
               if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                 {
                  double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                  result = (string)(point*10*value);  //STest, *10 works for all symbols?
                 }
            break;

         case VALUE_TYPE_TIME:
            break;
        }
        return result;
     }
  };
