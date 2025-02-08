class MyIndicator_id
  {
public:
    field_body

public:
   void              init()
     {
        init_body
     }

   double            calc()
     {


      string symbol = getSymbol(Symbol);
      ENUM_TIMEFRAMES timeframe = getTimeframe(Period);

      int buffer    = buffer_val;
      int shift     = Shift;//STest, + cross length

      double retval = EMPTY_VALUE;
      int i;
      double ival;

      if(ModeOutput == "id")
        {
         retval = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift);

        }
      else
         if(ModeOutput == "time")
           {
            datetime time;

            if(0 && StringFind(TimeStamp, ":") == -1)
              {
               time = (datetime)StringToInteger(TimeStamp); // hangs in MQL4!!!
              }
            else
              {
               time = StringToTime(TimeStamp);
              }

            shift = iCandleID(symbol, timeframe, time);
            retval = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift);
           }
         else
            if(ModeOutput == "visible" || ModeOutput == "id_by_visible")
              {
               if(VisibleLimit == 0)
                 {
                  VisibleLimit = iBars(symbol, timeframe);
                 }

               int vid = 0;

               for(i = shift; i <= VisibleLimit; i++)
                 {
                  ival = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift + i);

                  if(ival == EMPTY_VALUE || ival == 0)
                    {
                     continue;
                    }
                  if(vid >= VisibleID)
                    {
                     if(ModeOutput == "visible")
                       {
                        retval = ival;
                       }
                     else
                       {
                        retval = i;
                       }
                     break;
                    }

                  vid++;
                 }
              }
            else
               if(ModeOutput == "range")
                 {
                  int cstart = RangeCandleStart;
                  int cend   = RangeCandleEnd;
                  //string RangeValue = RangeValue;

                  // reverse values, if needed
                  if(RangeCandleStart > RangeCandleEnd)
                    {
                     int ctmp = RangeCandleEnd;
                     RangeCandleEnd = RangeCandleStart;
                     RangeCandleStart = ctmp;
                    }

                  if(RangeValue == "max")
                    {
                     retval = -EMPTY_VALUE;

                     for(i = RangeCandleStart; i <= RangeCandleEnd; i++)
                       {
                        ival = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift + i);
                        if(ival == EMPTY_VALUE || ival == 0)
                          {
                           continue;
                          }
                        if(ival > retval)
                          {
                           retval = ival;
                          }
                       }

                     if(retval == -EMPTY_VALUE)
                       {
                        retval = EMPTY_VALUE;
                       }
                    }
                  else
                     if(RangeValue == "min")
                       {
                        retval = EMPTY_VALUE;

                        for(i = RangeCandleStart; i <= RangeCandleEnd; i++)
                          {
                           ival = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift + i);
                           if(ival == EMPTY_VALUE || ival == 0)
                             {
                              continue;
                             }
                           if(ival < retval)
                             {
                              retval = ival;
                             }
                          }
                       }
                 }
               else
                  if(ModeOutput == "range_time")
                    {
                     datetime offset = 0;
                     if(RangeTimeSource == "gmt")
                       {
                        offset = (int)(TimeCurrent() - TimeLocal() + TimeGMTOffset());
                       }
                     else
                        if(RangeTimeSource == "server")
                          {
                           offset = (int)(TimeCurrent() - TimeLocal());
                          }

                     datetime time1 = StringToTime(RangeTimeStart)-(datetime)(86400*RangeDayOffset) + offset;
                     datetime time2 = StringToTime(RangeTimeEnd)-(datetime)(86400*RangeDayOffset) + offset;

                     int x1 = iBarShift(symbol, timeframe, time1, false);
                     int x2 = iBarShift(symbol, timeframe, time2, false);
                     if(x1<x2)
                       {
                        x1=iBarShift(symbol,timeframe,(time1-86400),false);
                       }

                     if(RangeValue == "max")
                       {
                        retval = -EMPTY_VALUE;

                        for(i=x2; i<=x1; i++)
                          {
                           ival = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift + i);
                           if(ival == EMPTY_VALUE || ival == 0)
                             {
                              continue;
                             }
                           if(ival > retval)
                             {
                              retval = ival;
                             }
                          }

                        if(retval == -EMPTY_VALUE)
                          {
                           retval = EMPTY_VALUE;
                          }
                       }
                     else
                        if(RangeValue == "min")
                          {
                           retval = EMPTY_VALUE;

                           for(i=x2; i<=x1; i++)
                             {
                              ival = iCustom(symbol, timeframe, indicator_name_val, indicator_input_val, buffer, shift + i);
                              if(ival == EMPTY_VALUE || ival == 0)
                                {
                                 continue;
                                }
                              if(ival < retval)
                                {
                                 retval = ival;
                                }
                             }
                          }
                    }

      return retval;

     }

  };

