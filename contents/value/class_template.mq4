
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
               result = value;
              }
            else
               if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                 {
                  double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                  result = (string)(point*10*(double)value);  //STest, *10 works for all symbols?
                 }
            break;

         case VALUE_TYPE_TIME:

            if(time_market == "" || time_market == NULL)
               time_market = Symbol();

            if(mode_time == MODE_TIME_NOW)
              {
               if(time_source == TIME_SERVER)
                 {
                  retval = TimeCurrent();
                 }
               else
                  if(time_source == TIME_LOCAL)
                    {
                     retval = TimeLocal() + (TimeCurrent() - TimeLocal());
                    }
                  else
                     if(time_source == TIME_GMT)
                       {
                        retval = TimeGMT() + (TimeCurrent() - TimeGMT());
                       }
              }
            else
               if(mode_time == MODE_TIME_TIMESTAMP)
                 {
                  retval  = StringToTime(time_stamp);
                  retval0 = retval;
                 }
               else
                  if(mode_time==MODE_TIME_COMPONENTS)
                    {
                     retval = TimeFromComponents(time_source, time_component_year, time_component_month, time_component_day, time_component_hour, time_component_minute, time_component_second);
                    }
                  else
                     if(mode_time == MODE_TIME_CANDLE_TIME)
                       {
                        ArraySetAsSeries(Time,true);
                        CopyTime(time_market,time_candle_timeframe,time_candle_id,1,Time);
                        retval = Time[0];
                       }
                     else
                        if(mode_time == MODE_TIME_TIME_VALUE)
                          {
                           retval = time_value;
                          }

            if(mode_time_shift > 0)
              {
               int sh = 1;

               if(mode_time_shift == 1)
                 {
                  sh = -1;
                 }

               if(time_shift_years > 0 || time_shift_months > 0)
                 {
                  int year = 0, month = 0, week = 0, day = 0, hour = 0, minute = 0, second = 0;

                  if(mode_time == MODE_TIME_CANDLE_TIME) //STest, It sounds component mode is expected. A bug from fxd?
                    {
                     year   = time_component_year;
                     month  = time_component_month;
                     day    = (int)MathFloor(time_component_day);
                     hour   = (int)(MathFloor(time_component_hour) + (24 * (time_component_day - MathFloor(time_component_day))));
                     minute = (int)(MathFloor(time_component_minute) + (60 * (time_component_hour - MathFloor(time_component_hour))));
                     second = (int)(time_component_second + (60 * (time_component_minute - MathFloor(time_component_minute))));
                    }
                  else
                    {
                     year   = TimeYear(retval);
                     month  = TimeMonth(retval);
                     day    = TimeDay(retval);
                     hour   = TimeHour(retval);
                     minute = TimeMinute(retval);
                     second = TimeSeconds(retval);
                    }

                  year  = year + time_component_year * sh;
                  month = month + time_component_month * sh;

                  if(month < 0)
                    {
                     month = 12 - month;
                    }
                  else
                     if(month > 12)
                       {
                        month = month - 12;
                       }

                  retval = StringToTime(IntegerToString(year)+"."+IntegerToString(month)+"."+IntegerToString(day)+" "+IntegerToString(hour)+":"+IntegerToString(minute)+":"+IntegerToString(second));
                 }

               retval = retval + (sh * ((604800 * time_shift_weeks) + SecondsFromComponents(time_shift_days, time_shift_hours, time_shift_minutes, time_shift_seconds)));

               if(time_skip_weekdays == true)
                 {
                  int weekday = TimeDayOfWeek(retval);

                  if(sh > 0)    // forward
                    {
                     if(weekday == 0)
                       {
                        retval = retval + 86400;
                       }
                     else
                        if(weekday == 6)
                          {
                           retval = retval + 172800;
                          }
                    }
                  else
                     if(sh < 0) // back
                       {
                        if(weekday == 0)
                          {
                           retval = retval - 172800;
                          }
                        else
                           if(weekday == 6)
                             {
                              retval = retval - 86400;
                             }
                       }
                 }
              }

            result = retval;
            break;
        }
      return result;
     }
  };
