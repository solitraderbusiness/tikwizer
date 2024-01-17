
class Value_id
  {
public:
    field_body

public:

   void              init()

     {
      init_body
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
            if(pips_mode == VALUE_PIPS_AS_IS)
              {
               return (string) value;
              }
            else
               if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
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
