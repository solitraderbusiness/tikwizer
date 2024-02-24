
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

      msymbol = getSymbol(symbol);
      string result = "";
      switch(type)
        {
         case VALUE_TYPE_NUMERIC:
         case VALUE_TYPE_BOOLEAN:
         case VALUE_TYPE_COLOR:
         case VALUE_TYPE_TEXT:
            result = value;
            break;

         case VALUE_TYPE_TEXT_CODE_INPUT:
            result = "\"" + value + "\"";
            break;

         case VALUE_TYPE_PIPS:
            if(pips_mode == VALUE_PIPS_AS_IS)
              {
               result =  value;
              }
            else
               if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                 {
                  double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                  result = (string)(point*10*(double)value);  //STest, *10 works for all symbols?
                 }
            break;

         case VALUE_TYPE_TIME:
            break;
        }
        return result;
     }
  };
