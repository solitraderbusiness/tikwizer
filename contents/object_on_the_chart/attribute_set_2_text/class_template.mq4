
class ObjectOnTheChart_string_id
  {
public:
    field_body
public:
   void              init()
     {
    init_body
     }
   string               calc()
     {
      string name = Name;

      if(ObjSource == "objloop")
        {
         name = loaded_object_name();
        }

      if(ObjectFind(0,name) < 0)
        {
         return EMPTY_VALUE;
        }

      string retval = "";

      if(Property == OBJPROP_NAME)
        {
         retval = ObjectGetString(0,name,OBJPROP_NAME,0);
        }
      if(Property == OBJPROP_TEXT)
        {
         retval = ObjectGetString(0,name,OBJPROP_TEXT,0);
        }
      if(Property == OBJPROP_TOOLTIP)
        {
         retval = ObjectGetString(0,name,OBJPROP_TOOLTIP,0);
        }
      if(Property == OBJPROP_FONT)
        {
         retval = ObjectGetString(0,name,OBJPROP_FONT,0);
        }
      if(Property == OBJPROP_SYMBOL)
        {
         retval = ObjectGetString(0,name,OBJPROP_SYMBOL,0);
        }

      return retval;

     }
  };
