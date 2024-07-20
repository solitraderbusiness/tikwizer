

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task0 : public Task
  {
public:
   //value set by user
   string            title;
   string            obj_chart_subwindow;
   int               obj_corner;
   int               obj_x;
   int               obj_y;
   string            obj_title_font;
   color             obj_title_font_color;
   int               obj_title_font_size;
   string            obj_label_font;
   color             obj_label_font_color;
   int               obj_label_font_size;
   string            obj_font;
   int               obj_font_color;
   int               obj_font_size;
   string            label_1;
   int               format_number_1;
   int               format_time_1;
   string            label_2;
   int               format_number_2;
   int               format_time_2;
   string            label_3;
   int               format_number_3;
   int               format_time_3;
   string            label_4;
   int               format_number_4;
   int               format_time_4;
   string            label_5;
   int               format_number_5;
   int               format_time_5;
   string            label_6;
   int               format_number_6;
   int               format_time_6;
   string            label_7;
   int               format_number_7;
   int               format_time_7;
   string            label_8;
   int               format_number_8;
   int               format_time_8;
   //value set by system
   bool              initialized;
public:
                     Task0(string name):Task(name)
     {
      title = "Comment Message";
      obj_chart_subwindow = "";
      obj_corner = CORNER_LEFT_UPPER;
      obj_x = 800;
      obj_y = 200;
      obj_title_font = "Georgia";
      obj_title_font_color = clrBlue;
      obj_title_font_size = 13;
      obj_label_font = "Verdana";
      obj_label_font_color = clrDarkGray;
      obj_label_font_size = 10;
      obj_font = "Verdana";
      obj_font_color = clrWhite;
      obj_font_size = 10;
      label_1 = "Hello1";
      format_number_1 = 50;
      format_time_1 = EMPTY_VALUE;
      label_2 = "Hello2";
      format_number_2 = EMPTY_VALUE;
      format_time_2 = EMPTY_VALUE;
      label_3 = "Hello3";
      format_number_3 = EMPTY_VALUE;
      format_time_3 = EMPTY_VALUE;
      label_4 = "Hello4";
      format_number_4 = EMPTY_VALUE;
      format_time_4 = EMPTY_VALUE;
      label_5 = "Hello5";
      format_number_5 = EMPTY_VALUE;
      format_time_5 = EMPTY_VALUE;
      label_6 = "Hello6";
      format_number_6 = EMPTY_VALUE;
      format_time_6 = EMPTY_VALUE;
      label_7 = "Hello7";
      format_number_7 = EMPTY_VALUE;
      format_time_7 = EMPTY_VALUE;
      label_8 = "Hello8";
      format_number_8 = EMPTY_VALUE;
      format_time_8 = EMPTY_VALUE;
      /* Static Parameters (initial value) */
      initialized =  false;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      double valueX = 0;


      if(!MQLInfoInteger(MQL_TESTER) || MQLInfoInteger(MQL_VISUAL_MODE))
        {


         long ObjChartID = 0;
         int ObjAnchor   = ANCHOR_LEFT;

         if(obj_corner == CORNER_RIGHT_UPPER || obj_corner == CORNER_RIGHT_LOWER)
           {
            ObjAnchor = ANCHOR_RIGHT;
           }

         string namebase = "mexpert_cmnt_" + block_id;

         int subwindow = WindowFindVisible(ObjChartID, obj_chart_subwindow);

         if(subwindow >= 0)
           {
            //-- draw comment title
//            if((string)title != "")
//              {
               string nametitle = namebase;

               if(ObjectFind(ObjChartID, nametitle) < 0)
                 {
                  if(!ObjectCreate(ObjChartID, nametitle, OBJ_LABEL, subwindow, 0, 0, 0, 0))
                    {
                     Print(__FUNCTION__, ": failed to create text object! Error code = ", GetLastError());
                    }
                  else
                    {
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_FONTSIZE, (int)(obj_title_font_size));
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_COLOR, obj_title_font_color);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_BACK, 0);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_SELECTABLE, 1);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_SELECTED, 0);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_HIDDEN, 1);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_CORNER, obj_corner);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_ANCHOR, ObjAnchor);

                     ObjectSetString(ObjChartID, nametitle, OBJPROP_FONT, obj_title_font);

                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_XDISTANCE, obj_x);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_YDISTANCE, obj_y);
                    }
                 }
               else
                 {
                  obj_x = (int)ObjectGetInteger(ObjChartID, nametitle, OBJPROP_XDISTANCE);
                  obj_y = (int)ObjectGetInteger(ObjChartID, nametitle, OBJPROP_YDISTANCE);
                 }

               ObjectSetString(ObjChartID, nametitle, OBJPROP_TEXT, (string)title);

               obj_y = (int)(obj_y + obj_title_font_size / 3);
//              }

            //-- draw comment rows
            for(int i = 1; i <= 8; i++)
              {
               string text    = "";
               string textlbl = "";

               switch(i)
                 {
                  case 1:
                    {
                     if(label_1 != "")
                       {
                        textlbl = label_1;
                        text    = FormatValueForPrinting(valueX, format_number_1, format_time_1);
                       }

                     break;
                    }
                  case 2:
                    {
                     if(label_2 != "")
                       {
                        textlbl = label_2;
                        text    = FormatValueForPrinting(valueX, format_number_2, format_time_2);
                       }

                     break;
                    }
                  case 3:
                    {
                     if(label_3 != "")
                       {
                        textlbl = label_3;
                        text    = FormatValueForPrinting(valueX, format_number_3, format_time_3);
                       }

                     break;
                    }
                  case 4:
                    {
                     if(label_4 != "")
                       {
                        textlbl = label_4;
                        text    = FormatValueForPrinting(valueX, format_number_4, format_time_4);
                       }

                     break;
                    }
                  case 5:
                    {
                     if(label_5 != "")
                       {
                        textlbl = label_5;
                        text    = FormatValueForPrinting(valueX, format_number_5, format_time_5);
                       }

                     break;
                    }
                  case 6:
                    {
                     if(label_6 != "")
                       {
                        textlbl = label_6;
                        text    = FormatValueForPrinting(valueX, format_number_6, format_time_6);
                       }

                     break;
                    }
                  case 7:
                    {
                     if(label_7 != "")
                       {
                        textlbl = label_7;
                        text    = FormatValueForPrinting(valueX, format_number_7, format_time_7);
                       }

                     break;
                    }
                  case 8:
                    {
                     if(label_8 != "")
                       {
                        textlbl = label_8;
                        text    = FormatValueForPrinting(valueX, format_number_8, format_time_8);
                       }

                     break;
                    }
                 }

               string name    = namebase + "_" + (string)i;
               string namelbl = name + "_l";

               if(textlbl == "")
                 {
                  if(!initialized)
                    {
                     //-- pre-delete
                     ObjectDelete(ObjChartID, namelbl);
                     ObjectDelete(ObjChartID, name);
                    }

                  continue;
                 }

               //-- draw initial objects
               if(ObjectFind(ObjChartID, name) < 0)
                 {
                  if(textlbl == "")
                    {
                     continue;
                    }

                  if(ObjectCreate(ObjChartID, namelbl, OBJ_LABEL, subwindow, 0, 0, 0, 0))
                    {
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_CORNER, obj_corner);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_ANCHOR, ObjAnchor);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_BACK, 0);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_SELECTABLE, 0);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_SELECTED, 0);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_HIDDEN, 1);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_FONTSIZE, obj_label_font_size);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_COLOR, obj_label_font_color);
                     ObjectSetString(ObjChartID, namelbl, OBJPROP_FONT, obj_label_font);
                    }
                  else
                    {
                     Print(__FUNCTION__, ": failed to create text object! Error code = ", GetLastError());
                    }

                  if(ObjectCreate(ObjChartID, name, OBJ_LABEL, subwindow, 0, 0, 0, 0))
                    {
                     ObjectSetInteger(ObjChartID, name, OBJPROP_CORNER, obj_corner);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_ANCHOR, ObjAnchor);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_BACK, 0);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_SELECTABLE, 0);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_SELECTED, 0);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_HIDDEN, 1);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_FONTSIZE, obj_font_size);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_COLOR, obj_font_color);
                     ObjectSetString(ObjChartID, name, OBJPROP_FONT, obj_font);
                    }
                  else
                    {
                     Print(__FUNCTION__, ": failed to create text object! Error code = ", GetLastError());
                    }
                 }
               else
                 {
                  if(textlbl == "")
                    {
                     ObjectDelete(ObjChartID, namelbl);
                     ObjectDelete(ObjChartID, name);
                     continue;
                    }
                 }

               obj_y  = (int)(obj_y + obj_font_size + obj_font_size/2);

               //-- update label objects
               ObjectSetInteger(ObjChartID, namelbl, OBJPROP_XDISTANCE, obj_x);
               ObjectSetInteger(ObjChartID, namelbl, OBJPROP_YDISTANCE, obj_y);
               ObjectSetString(ObjChartID, namelbl, OBJPROP_TEXT, (string)textlbl);

               //-- update value objects
               int x        = 0;
               int xsizelbl = (int)ObjectGetInteger(ObjChartID, namelbl, OBJPROP_XSIZE);

               if(xsizelbl == 0)
                 {
                  //-- when the object is newly created, it returns 0 for XSIZE and YSIZE, so here we will trick it somehow
                  xsizelbl = (int)(StringLen((string)textlbl) * obj_font_size / 1.5 + obj_font_size / 2);
                 }

               x = obj_x + (xsizelbl + obj_font_size/2);

               ObjectSetInteger(ObjChartID, name, OBJPROP_XDISTANCE, x);
               ObjectSetInteger(ObjChartID, name, OBJPROP_YDISTANCE, obj_y);
               ObjectSetString(ObjChartID, name, OBJPROP_TEXT, (string)text);
              }

            ChartRedraw();
           }

         initialized = true;
        }

      block.onResult(ROUTE_1_PASSED);

     }
   virtual void      reset(int level)
     {

     }

  };










template<typename T>
string FormatValueForPrinting(T value, int digits, int timeFormat)
  {
   string outputValue = "";
   string typeName    = typename(value);

   if(typeName == "double" || typeName == "float")
     {
      if(digits >= -16 && digits <= 8)
        {
         if(value > -1.0 && value < 1.0)
           {
            /**
            * Find how many zeroes are after the point, but before the first non-zero digit.
            * For example 0.000195 has 3 zeroes
            * The function would return negative value for values bigger than 0
            *
            * @see https://stackoverflow.com/questions/31001901/how-can-i-count-the-number-of-zero-decimals-in-javascript/31002148#31002148
            */
            int zeroesAfterPoint = (int)-MathFloor(MathLog10(MathAbs(value)) + 1);

            digits = zeroesAfterPoint + digits;
           }

         T normalizedValue  = NormalizeDouble(value, digits);
         outputValue = DoubleToString(normalizedValue, digits);
        }
      else
        {
         outputValue = (string)NormalizeDouble(value, 8);
        }
     }
   else
     {
      outputValue = IntegerToString((long)value);
     }

   return outputValue;
  }




/**
* Bool overload
*/
string FormatValueForPrinting(
   bool value,
   int digits,
   int timeFormat
)
  {
   return (value) ? "true" : "false";
  }

/**
* Datetime overload
*/
string FormatValueForPrinting(
   datetime value,
   int digits,
   int timeFormat
)
  {
   if(timeFormat == (int)EMPTY_VALUE || timeFormat == EMPTY_VALUE)
      timeFormat = TIME_DATE|TIME_MINUTES;
   return TimeToString(value, timeFormat);
  }

/**
* String overload
*/
string FormatValueForPrinting(
   string value,
   int digits,
   int timeFormat
)
  {
   return value;
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int WindowFindVisible(long chart_id, string term)
  {
//-- the search term can be chart name, such as Force(13), or subwindow index
   if(term == "" || term == "0")
     {
      return 0;
     }

   int subwindow = (int)StringToInteger(term);

   if(subwindow == 0 && StringLen(term) > 1)
     {
      subwindow = ChartWindowFind(chart_id, term);
     }

   if(subwindow > 0 && !ChartGetInteger(chart_id, CHART_WINDOW_IS_VISIBLE, subwindow))
     {
      return -1;
     }

   return subwindow;
  }
//+------------------------------------------------------------------+
