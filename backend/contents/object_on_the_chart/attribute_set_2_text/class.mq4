
class ObjectOnTheChart_string
  {
public:
   string            ObjSource;
   string            Name;
   ENUM_OBJECT_PROPERTY_STRING Property;
public:
   void              init()
     {
      ObjSource = "name";
      Name = "my_object_name";
      Property = OBJPROP_TEXT;
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


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
string loaded_object_name(string name="")
  {
   static string memory="";
   if(name!="")
     {
      memory=name;
     }
   return(memory);
  }
