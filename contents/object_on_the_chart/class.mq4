
#define TLOBJPROP_TIME1 801
#define OBJPROP_TL_PRICE_BY_SHIFT 802
#define OBJPROP_TL_SHIFT_BY_PRICE 803
#define OBJPROP_FIBOVALUE 804
#define OBJPROP_FIBOPRICEVALUE 805
#define OBJPROP_BARSHIFT1 807
#define OBJPROP_BARSHIFT2 808
#define OBJPROP_BARSHIFT3 809

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class ObjectOnTheChart
  {
public:
   string            ObjSource;
   string            Name;
   int               Property;
   int               FiboLevelID;
   double            TLpriceLevel;
   int               Shift;
public:
   void              init()
     {
      ObjSource = "name";
      Name = "my_object_name";
      Property = OBJPROP_PRICE1;
      FiboLevelID = 0;
      TLpriceLevel = 1.2;
      Shift = 0;
     }
   double               calc()
     {
      string name = Name;

      if(ObjSource == "objloop")
        {
         name = loaded_object_name();
        }
      if(ObjectFind(0,name)<0)
        {
         return EMPTY_VALUE;
        }

      double retval = 0;
      int modifier  = 0;

      double Fibo100  = 0;
      double Fibo0    = 0;
      double FiboDiff = 0;

      if(Property == OBJPROP_TIME1)
        {
         retval = (int)ObjectGetInteger(0,name,OBJPROP_TIME,0);
        }
      else
         if(Property == OBJPROP_TIME2)
           {
            retval = (int)ObjectGetInteger(0,name,OBJPROP_TIME,1);
           }
         else
            if(Property == OBJPROP_TIME3)
              {
               retval = (int)ObjectGetInteger(0,name,OBJPROP_TIME,2);
              }

            else
               if(Property == OBJPROP_PRICE1)
                 {
                  retval = ObjectGetDouble(0,name,OBJPROP_PRICE,0);
                 }
               else
                  if(Property == OBJPROP_PRICE2)
                    {
                     retval = ObjectGetDouble(0,name,OBJPROP_PRICE,1);
                    }
                  else
                     if(Property == OBJPROP_PRICE3)
                       {
                        retval = ObjectGetDouble(0,name,OBJPROP_PRICE,2);
                       }

                     else
                        if(Property == OBJPROP_BARSHIFT1)
                          {
                           retval = iBarShift(Symbol(), Period(), (int)ObjectGetInteger(0,name,OBJPROP_TIME,0), true);
                           if(retval==-1)
                             {

                             }
                          }
                        else
                           if(Property == OBJPROP_BARSHIFT2)
                             {
                              retval = iBarShift(Symbol(), Period(), (int)ObjectGetInteger(0,name,OBJPROP_TIME,1), true);
                              if(retval==-1)
                                {

                                }
                             }
                           else
                              if(Property == OBJPROP_BARSHIFT3)
                                {
                                 retval = iBarShift(Symbol(), Period(), (int)ObjectGetInteger(0,name,OBJPROP_TIME,2), true);
                                 if(retval==-1)
                                   {

                                   }
                                }

                              else
                                 if(Property == OBJPROP_COLOR)
                                   {
                                    retval = (int)ObjectGetInteger(0,name,OBJPROP_COLOR);
                                   }
                                 else
                                    if(Property == OBJPROP_STYLE)
                                      {
                                       retval = (int)ObjectGetInteger(0,name,OBJPROP_STYLE);
                                      }
                                    else
                                       if(Property == OBJPROP_WIDTH)
                                         {
                                          retval = (int)ObjectGetInteger(0,name,OBJPROP_WIDTH);
                                         }
                                       else
                                          if(Property == OBJPROP_BACK)
                                            {
                                             retval = (int)ObjectGetInteger(0,name,OBJPROP_BACK);
                                            }
                                          else
                                             if(Property == OBJPROP_RAY_LEFT)
                                               {
                                                retval = (int)ObjectGetInteger(0,name,OBJPROP_RAY_LEFT);
                                               }
                                             else
                                                if(Property == OBJPROP_RAY_RIGHT)
                                                  {
                                                   retval = (int)ObjectGetInteger(0,name,OBJPROP_RAY_RIGHT);
                                                  }
                                                else
                                                   if(Property == OBJPROP_RAY)
                                                     {
                                                      retval = (int)ObjectGetInteger(0,name,OBJPROP_RAY);
                                                     }
                                                   else
                                                      if(Property == OBJPROP_ELLIPSE)
                                                        {
                                                         retval = (int)ObjectGetInteger(0,name,OBJPROP_ELLIPSE);
                                                        }
                                                      else
                                                         if(Property == OBJPROP_ARROWCODE)
                                                           {
                                                            retval = (int)ObjectGetInteger(0,name,OBJPROP_ARROWCODE);
                                                           }
                                                         else
                                                            if(Property == OBJPROP_FONTSIZE)
                                                              {
                                                               retval = (int)ObjectGetInteger(0,name,OBJPROP_FONTSIZE);
                                                              }
                                                            else
                                                               if(Property == OBJPROP_CORNER)
                                                                 {
                                                                  retval = (int)ObjectGetInteger(0,name,OBJPROP_CORNER);
                                                                 }
                                                               else
                                                                  if(Property == OBJPROP_XDISTANCE)
                                                                    {
                                                                     retval = (int)ObjectGetInteger(0,name,OBJPROP_XDISTANCE);
                                                                    }
                                                                  else
                                                                     if(Property == OBJPROP_YDISTANCE)
                                                                       {
                                                                        retval = (int)ObjectGetInteger(0,name,OBJPROP_YDISTANCE);
                                                                       }
                                                                     else
                                                                        if(Property == OBJPROP_LEVELCOLOR)
                                                                          {
                                                                           retval = (int)ObjectGetInteger(0,name,OBJPROP_LEVELCOLOR);
                                                                          }
                                                                        else
                                                                           if(Property == OBJPROP_LEVELSTYLE)
                                                                             {
                                                                              retval = (int)ObjectGetInteger(0,name,OBJPROP_LEVELSTYLE);
                                                                             }
                                                                           else
                                                                              if(Property == OBJPROP_LEVELWIDTH)
                                                                                {
                                                                                 retval = (int)ObjectGetInteger(0,name,OBJPROP_LEVELWIDTH);
                                                                                }
                                                                              else
                                                                                 if(Property == OBJPROP_ANCHOR)
                                                                                   {
                                                                                    retval = (int)ObjectGetInteger(0,name,OBJPROP_ANCHOR);
                                                                                   }
                                                                                 else
                                                                                    if(Property == OBJPROP_DIRECTION)
                                                                                      {
                                                                                       retval = (int)ObjectGetInteger(0,name,OBJPROP_DIRECTION);
                                                                                      }
                                                                                    //else if (Property == OBJPROP_DEGREE)     {retval = (int)ObjectGetInteger(0,name,OBJPROP_DEGREE);}
                                                                                    //else if (Property == OBJPROP_DRAWLINES)  {retval = (int)ObjectGetInteger(0,name,OBJPROP_DRAWLINES);}
                                                                                    else
                                                                                       if(Property == OBJPROP_STATE)
                                                                                         {
                                                                                          retval = (int)ObjectGetInteger(0,name,OBJPROP_STATE);
                                                                                         }
                                                                                       else
                                                                                          if(Property == OBJPROP_XSIZE)
                                                                                            {
                                                                                             retval = (int)ObjectGetInteger(0,name,OBJPROP_XSIZE);
                                                                                            }
                                                                                          else
                                                                                             if(Property == OBJPROP_YSIZE)
                                                                                               {
                                                                                                retval = (int)ObjectGetInteger(0,name,OBJPROP_YSIZE);
                                                                                               }
                                                                                             else
                                                                                                if(Property == OBJPROP_PERIOD)
                                                                                                  {
                                                                                                   retval = (int)ObjectGetInteger(0,name,OBJPROP_PERIOD);
                                                                                                  }
                                                                                                else
                                                                                                   if(Property == OBJPROP_LEVELS)
                                                                                                     {
                                                                                                      retval = (int)ObjectGetInteger(0,name,OBJPROP_LEVELS);
                                                                                                     }

                                                                                                   else
                                                                                                      if(Property == OBJPROP_ANGLE)
                                                                                                        {
                                                                                                         retval = ObjectGetDouble(0,name,OBJPROP_ANGLE);
                                                                                                        }
                                                                                                      else
                                                                                                         if(Property == OBJPROP_SCALE)
                                                                                                           {
                                                                                                            retval = ObjectGetDouble(0,name,OBJPROP_SCALE);
                                                                                                           }
                                                                                                         else
                                                                                                            if(Property == OBJPROP_DEVIATION)
                                                                                                              {
                                                                                                               retval = ObjectGetDouble(0,name,OBJPROP_DEVIATION);
                                                                                                              }

                                                                                                            else
                                                                                                               if(Property == OBJPROP_FIRSTLEVEL)
                                                                                                                 {
                                                                                                                  retval = ObjectGetDouble(0,name,OBJPROP_LEVELVALUE,FiboLevelID);
                                                                                                                 }
                                                                                                               else
                                                                                                                  if(Property == OBJPROP_TL_PRICE_BY_SHIFT)
                                                                                                                    {
                                                                                                                     //retval = ObjectGetValueByShift(name, Shift+FXD_MORE_SHIFT);
                                                                                                                    }
                                                                                                                  else
                                                                                                                     if(Property == OBJPROP_TL_SHIFT_BY_PRICE)
                                                                                                                       {
                                                                                                                        retval = ObjectGetShiftByValue(name,TLpriceLevel);
                                                                                                                       }

                                                                                                                     else
                                                                                                                        if(Property == OBJPROP_FIBOVALUE)
                                                                                                                          {
                                                                                                                           Fibo100  = ObjectGetDouble(0,name,OBJPROP_PRICE,0);
                                                                                                                           Fibo0    = ObjectGetDouble(0,name,OBJPROP_PRICE,1);
                                                                                                                           FiboDiff = Fibo100 - Fibo0;
                                                                                                                           retval=0;
                                                                                                                           if(FiboDiff != 0)
                                                                                                                             {
                                                                                                                              retval = (SymbolInfoDouble(Symbol(),SYMBOL_BID)-Fibo0)/FiboDiff;
                                                                                                                             }
                                                                                                                          }
                                                                                                                        else
                                                                                                                           if(Property == OBJPROP_FIBOPRICEVALUE)
                                                                                                                             {
                                                                                                                              Fibo100  = ObjectGetDouble(0,name,OBJPROP_PRICE,0);
                                                                                                                              Fibo0    = ObjectGetDouble(0,name,OBJPROP_PRICE,1);
                                                                                                                              FiboDiff = Fibo100 - Fibo0;
                                                                                                                              retval=(ObjectGetDouble(0,name,OBJPROP_LEVELVALUE,FiboLevelID)*(FiboDiff))+Fibo0;
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
