

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task0 : public Task
  {
public:
   //value set by user
   string            Title;
   string            ObjChartSubWindow;
   int               ObjCorner;
   int               ObjX;
   int               ObjY;
   string            ObjTitleFont;
   color             ObjTitleFontColor;
   int               ObjTitleFontSize;
   string            ObjLabelsFont;
   color             ObjLabelsFontColor;
   int               ObjLabelsFontSize;
   string            ObjFont;
   int               ObjFontColor;
   int               ObjFontSize;
   string            Label1;
   int               FormatNumber1;
   int               FormatTime1;
   string            Label2;
   int               FormatNumber2;
   int               FormatTime2;
   string            Label3;
   int               FormatNumber3;
   int               FormatTime3;
   string            Label4;
   int               FormatNumber4;
   int               FormatTime4;
   string            Label5;
   int               FormatNumber5;
   int               FormatTime5;
   string            Label6;
   int               FormatNumber6;
   int               FormatTime6;
   string            Label7;
   int               FormatNumber7;
   int               FormatTime7;
   string            Label8;
   int               FormatNumber8;
   int               FormatTime8;
   //value set by system
   bool              initialized;
public:
                     Task0(string name):Task(name)
     {
      Title = "Comment Message";
      ObjChartSubWindow = "";
      ObjCorner = CORNER_LEFT_UPPER;
      ObjX = 800;
      ObjY = 200;
      ObjTitleFont = "Georgia";
      ObjTitleFontColor = clrBlue;
      ObjTitleFontSize = 13;
      ObjLabelsFont = "Verdana";
      ObjLabelsFontColor = clrDarkGray;
      ObjLabelsFontSize = 10;
      ObjFont = "Verdana";
      ObjFontColor = clrWhite;
      ObjFontSize = 10;
      Label1 = "Hello1";
      FormatNumber1 = 50;
      FormatTime1 = EMPTY_VALUE;
      Label2 = "Hello2";
      FormatNumber2 = EMPTY_VALUE;
      FormatTime2 = EMPTY_VALUE;
      Label3 = "Hello3";
      FormatNumber3 = EMPTY_VALUE;
      FormatTime3 = EMPTY_VALUE;
      Label4 = "Hello4";
      FormatNumber4 = EMPTY_VALUE;
      FormatTime4 = EMPTY_VALUE;
      Label5 = "Hello5";
      FormatNumber5 = EMPTY_VALUE;
      FormatTime5 = EMPTY_VALUE;
      Label6 = "Hello6";
      FormatNumber6 = EMPTY_VALUE;
      FormatTime6 = EMPTY_VALUE;
      Label7 = "Hello7";
      FormatNumber7 = EMPTY_VALUE;
      FormatTime7 = EMPTY_VALUE;
      Label8 = "Hello8";
      FormatNumber8 = EMPTY_VALUE;
      FormatTime8 = EMPTY_VALUE;
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

         if(ObjCorner == CORNER_RIGHT_UPPER || ObjCorner == CORNER_RIGHT_LOWER)
           {
            ObjAnchor = ANCHOR_RIGHT;
           }

         string namebase = "fxd_cmnt_" + block_id;

         int subwindow = WindowFindVisible(ObjChartID, ObjChartSubWindow);

         if(subwindow >= 0)
           {
            //-- draw comment title
            if((string)Title != "")
              {
               string nametitle = namebase;

               if(ObjectFind(ObjChartID, nametitle) < 0)
                 {
                  if(!ObjectCreate(ObjChartID, nametitle, OBJ_LABEL, subwindow, 0, 0, 0, 0))
                    {
                     Print(__FUNCTION__, ": failed to create text object! Error code = ", GetLastError());
                    }
                  else
                    {
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_FONTSIZE, (int)(ObjTitleFontSize));
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_COLOR, ObjTitleFontColor);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_BACK, 0);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_SELECTABLE, 1);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_SELECTED, 0);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_HIDDEN, 1);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_CORNER, ObjCorner);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_ANCHOR, ObjAnchor);

                     ObjectSetString(ObjChartID, nametitle, OBJPROP_FONT, ObjTitleFont);

                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_XDISTANCE, ObjX);
                     ObjectSetInteger(ObjChartID, nametitle, OBJPROP_YDISTANCE, ObjY);
                    }
                 }
               else
                 {
                  ObjX = (int)ObjectGetInteger(ObjChartID, nametitle, OBJPROP_XDISTANCE);
                  ObjY = (int)ObjectGetInteger(ObjChartID, nametitle, OBJPROP_YDISTANCE);
                 }

               ObjectSetString(ObjChartID, nametitle, OBJPROP_TEXT, (string)Title);

               ObjY = (int)(ObjY + ObjTitleFontSize / 3);
              }

            //-- draw comment rows
            for(int i = 1; i <= 8; i++)
              {
               string text    = "";
               string textlbl = "";

               switch(i)
                 {
                  case 1:
                    {
                     if(Label1 != "")
                       {
                        textlbl = Label1;
                        text    = FormatValueForPrinting(valueX, FormatNumber1, FormatTime1);
                       }

                     break;
                    }
                  case 2:
                    {
                     if(Label2 != "")
                       {
                        textlbl = Label2;
                        text    = FormatValueForPrinting(valueX, FormatNumber2, FormatTime2);
                       }

                     break;
                    }
                  case 3:
                    {
                     if(Label3 != "")
                       {
                        textlbl = Label3;
                        text    = FormatValueForPrinting(valueX, FormatNumber3, FormatTime3);
                       }

                     break;
                    }
                  case 4:
                    {
                     if(Label4 != "")
                       {
                        textlbl = Label4;
                        text    = FormatValueForPrinting(valueX, FormatNumber4, FormatTime4);
                       }

                     break;
                    }
                  case 5:
                    {
                     if(Label5 != "")
                       {
                        textlbl = Label5;
                        text    = FormatValueForPrinting(valueX, FormatNumber5, FormatTime5);
                       }

                     break;
                    }
                  case 6:
                    {
                     if(Label6 != "")
                       {
                        textlbl = Label6;
                        text    = FormatValueForPrinting(valueX, FormatNumber6, FormatTime6);
                       }

                     break;
                    }
                  case 7:
                    {
                     if(Label7 != "")
                       {
                        textlbl = Label7;
                        text    = FormatValueForPrinting(valueX, FormatNumber7, FormatTime7);
                       }

                     break;
                    }
                  case 8:
                    {
                     if(Label8 != "")
                       {
                        textlbl = Label8;
                        text    = FormatValueForPrinting(valueX, FormatNumber8, FormatTime8);
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
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_CORNER, ObjCorner);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_ANCHOR, ObjAnchor);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_BACK, 0);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_SELECTABLE, 0);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_SELECTED, 0);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_HIDDEN, 1);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_FONTSIZE, ObjLabelsFontSize);
                     ObjectSetInteger(ObjChartID, namelbl, OBJPROP_COLOR, ObjLabelsFontColor);
                     ObjectSetString(ObjChartID, namelbl, OBJPROP_FONT, ObjLabelsFont);
                    }
                  else
                    {
                     Print(__FUNCTION__, ": failed to create text object! Error code = ", GetLastError());
                    }

                  if(ObjectCreate(ObjChartID, name, OBJ_LABEL, subwindow, 0, 0, 0, 0))
                    {
                     ObjectSetInteger(ObjChartID, name, OBJPROP_CORNER, ObjCorner);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_ANCHOR, ObjAnchor);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_BACK, 0);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_SELECTABLE, 0);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_SELECTED, 0);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_HIDDEN, 1);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_FONTSIZE, ObjFontSize);
                     ObjectSetInteger(ObjChartID, name, OBJPROP_COLOR, ObjFontColor);
                     ObjectSetString(ObjChartID, name, OBJPROP_FONT, ObjFont);
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

               ObjY  = (int)(ObjY + ObjFontSize + ObjFontSize/2);

               //-- update label objects
               ObjectSetInteger(ObjChartID, namelbl, OBJPROP_XDISTANCE, ObjX);
               ObjectSetInteger(ObjChartID, namelbl, OBJPROP_YDISTANCE, ObjY);
               ObjectSetString(ObjChartID, namelbl, OBJPROP_TEXT, (string)textlbl);

               //-- update value objects
               int x        = 0;
               int xsizelbl = (int)ObjectGetInteger(ObjChartID, namelbl, OBJPROP_XSIZE);

               if(xsizelbl == 0)
                 {
                  //-- when the object is newly created, it returns 0 for XSIZE and YSIZE, so here we will trick it somehow
                  xsizelbl = (int)(StringLen((string)textlbl) * ObjFontSize / 1.5 + ObjFontSize / 2);
                 }

               x = ObjX + (xsizelbl + ObjFontSize/2);

               ObjectSetInteger(ObjChartID, name, OBJPROP_XDISTANCE, x);
               ObjectSetInteger(ObjChartID, name, OBJPROP_YDISTANCE, ObjY);
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
