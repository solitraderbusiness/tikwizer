

class Task_id : public Task
  {
public:
   //specified by user
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
   //specified by system
   bool              initialized;
public:
                     Task_id(string name):Task(name)
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
                        initializer_1
                        text    = FormatValueForPrinting(variable_name_1, FormatNumber1, FormatTime1);
                       }

                     break;
                    }
                  case 2:
                    {
                     if(Label2 != "")
                       {
                        textlbl = Label2;
                        initializer_2
                        text    = FormatValueForPrinting(variable_name_2, FormatNumber2, FormatTime2);
                       }

                     break;
                    }
                  case 3:
                    {
                     if(Label3 != "")
                       {
                        textlbl = Label3;
                        initializer_3
                        text    = FormatValueForPrinting(variable_name_3, FormatNumber3, FormatTime3);
                       }

                     break;
                    }
                  case 4:
                    {
                     if(Label4 != "")
                       {
                        textlbl = Label4;
                        initializer_4
                        text    = FormatValueForPrinting(variable_name_4, FormatNumber4, FormatTime4);
                       }

                     break;
                    }
                  case 5:
                    {
                     if(Label5 != "")
                       {
                        textlbl = Label5;
                        initializer_5
                        text    = FormatValueForPrinting(variable_name_5, FormatNumber5, FormatTime5);
                       }

                     break;
                    }
                  case 6:
                    {
                     if(Label6 != "")
                       {
                        textlbl = Label6;
                        initializer_6
                        text    = FormatValueForPrinting(variable_name_6, FormatNumber6, FormatTime6);
                       }

                     break;
                    }
                  case 7:
                    {
                     if(Label7 != "")
                       {
                        textlbl = Label7;
                        initializer_7
                        text    = FormatValueForPrinting(variable_name_7, FormatNumber7, FormatTime7);
                       }

                     break;
                    }
                  case 8:
                    {
                     if(Label8 != "")
                       {
                        textlbl = Label8;
                        initializer_8
                        text    = FormatValueForPrinting(variable_name_8, FormatNumber8, FormatTime8);
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
