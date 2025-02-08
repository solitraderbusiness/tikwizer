

enum Test {hello, goodbye};


class MovingAverage3_right
  {
public:
   string            Symbol;
   ENUM_TIMEFRAMES   Period;
   string            ModeOutput;
   string            TimeStamp;
   int               VisibleID;
   int               VisibleShift;
   int               VisibleLimit;
   int               RangeCandleStart;
   int               RangeCandleEnd;
   string            RangeTimeSource;
   string            RangeTimeStart;
   string            RangeTimeEnd;
   double            RangeDayOffset;
   string            RangeValue;
   int               Shift;

public:
   void              init()
     {
      Symbol = (string)"";
      Period = (ENUM_TIMEFRAMES)PERIOD_CURRENT;
      ModeOutput = (string)"id";
      TimeStamp = (string)"00:00";
      VisibleID = (int)0;
      VisibleShift = (int)0;
      VisibleLimit = (int)100;
      RangeCandleStart = (int)0;
      RangeCandleEnd = (int)10;
      RangeTimeSource = (string)"server";
      RangeTimeStart = (string)"01:00";
      RangeTimeEnd = (string)"08:00";
      RangeDayOffset = (double)0.0;
      RangeValue = (string)"max";
      Shift = (int)0;
     }

   double            calc()
     {


      string symbol = getSymbol(Symbol);
      ENUM_TIMEFRAMES timeframe = getTimeframe(Period);

      int buffer    = 0;
      int shift     = Shift;//STest, + cross length

      double retval = EMPTY_VALUE;
      int i;
      double ival;

      if(ModeOutput == "id")
        {
         retval = iCustom(symbol, timeframe, "AO Custom", hello, buffer, shift);

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
            retval = iCustom(symbol, timeframe, "AO Custom", (Test)Test::hello, buffer, shift);
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
                  ival = iCustom(symbol, timeframe, "AO Custom", (Test)Test::hello, buffer, shift + i);

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
                        ival = iCustom(symbol, timeframe, "AO Custom", (Test)Test::hello, buffer, shift + i);
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
                           ival = iCustom(symbol, timeframe, "AO Custom", (Test)Test::hello, buffer, shift + i);
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
                           ival = iCustom(symbol, timeframe, "AO Custom", (Test)Test::hello, buffer, shift + i);
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
                              ival = iCustom(symbol, timeframe, "AO Custom", (Test)Test::hello, buffer, shift + i);
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




int iCandleID(string SYMBOL, ENUM_TIMEFRAMES TIMEFRAME, datetime time_stamp)
  {
   bool TimeStampPrevDayShift = true;
   int CandleID               = 0;

// get the time resolution of the desired period, in minutes
   int mins_tf  = TIMEFRAME;
   int mins_tf0 = 0;

   if(TIMEFRAME == PERIOD_CURRENT)
     {
      mins_tf = (int)PeriodSeconds(PERIOD_CURRENT) / 60;
     }

// get the difference between now and the time we want, in minutes
   int days_adjust = 0;

   if(TimeStampPrevDayShift)
     {
      // automatically shift to the previous day
      if(time_stamp > TimeCurrent())
        {
         time_stamp = time_stamp - 86400;
        }

      // also shift weekdays
      while(true)
        {
         int dow = TimeDayOfWeek(time_stamp);

         if(dow > 0 && dow < 6)
           {
            break;
           }

         time_stamp = time_stamp - 86400;
         days_adjust++;
        }
     }

   int mins_diff = (int)(TimeCurrent() - time_stamp);
   mins_diff = mins_diff - days_adjust*86400;
   mins_diff = mins_diff / 60;

// the difference is negative => quit here
   if(mins_diff < 0)
     {
      return (int)EMPTY_VALUE;
     }

// now calculate the candle ID, it is relative to the current time
   if(mins_diff > 0)
     {
      CandleID = (int)MathCeil((double)mins_diff/(double)mins_tf);
     }

// now, after all the shifting and in case of missing candles, the calculated candle id can be few candles early
// so we will search for the right candle
   while(true)
     {
      if(iTime(SYMBOL, TIMEFRAME, CandleID) >= time_stamp)
        {
         break;
        }

      CandleID--;

      if(CandleID <= 0)
        {
         CandleID = 0;
         break;
        }
     }

   return CandleID;
  }


