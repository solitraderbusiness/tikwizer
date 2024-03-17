//+------------------------------------------------------------------+
//|                                                      ProjectName |
//|                                      Copyright 2018, CompanyName |
//|                                       http://www.companyname.net |
//+------------------------------------------------------------------+

#define TIME_SERVER 1
#define TIME_LOCAL 2
#define TIME_GMT 3

#define VALUE_TYPE_NUMERIC 1
#define VALUE_TYPE_BOOLEAN 2
#define VALUE_TYPE_COLOR 3
#define VALUE_TYPE_PIPS 4
#define VALUE_TYPE_TEXT 5
#define VALUE_TYPE_TEXT_CODE_INPUT 6
#define VALUE_TYPE_TIME 7

#define VALUE_PIPS_AS_IS 1
#define VALUE_PIPS_AS_PRICE_FRACTION 2

#define MODE_TIME_NOW 1
#define MODE_TIME_TIMESTAMP 2
#define MODE_TIME_COMPONENTS 3
#define MODE_TIME_CANDLE_TIME 4
#define MODE_TIME_TIME_VALUE 5


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Value20
  {
public:
   int               type;
   string               value;
   string               adjust;
   //for pips
   int               pips_mode;
   string            symbol;
   //for time (phase 2)
   //defined by user
   int               mode_time;
   int               time_source;
   string            time_stamp;
   int               time_candle_id;
   string            time_market;
   ENUM_TIMEFRAMES   time_candle_timeframe;
   int               time_component_year;
   int               time_component_month;
   double            time_component_day;
   double            time_component_hour;
   double            time_component_minute;
   int               time_component_second;
   datetime          time_value;
   int               mode_time_shift;
   int               time_shift_years;
   int               time_shift_months;
   int               time_shift_weeks;
   double            time_shift_days;
   double            time_shift_hours;
   double            time_shift_minutes;
   int               time_shift_seconds;
   bool              time_skip_weekdays;
   //defined by system
   datetime          retval;
   datetime          retval0;
   datetime          Time[];







   string            msymbol;

public:

   void              init()

     {
      type = VALUE_TYPE_TIME;
      value = 10;
      //for pips
      pips_mode = VALUE_PIPS_AS_IS;
      symbol = NULL;
      //for time (phase 2)
      //defined by user
      mode_time = MODE_TIME_NOW;
      time_source = TIME_SERVER;
      time_stamp = "00:00";
      time_candle_id = 1;
      time_market = "";
      time_candle_timeframe = 0;
      time_component_year = 0;
      time_component_month = 0;
      time_component_day = 0.0;
      time_component_hour = 12.0;
      time_component_minute = 0.0;
      time_component_second = 0;
      time_value = 0;
      mode_time_shift = 0;
      time_shift_years = 0;
      time_shift_months = 0;
      time_shift_weeks = 0;
      time_shift_days = 0.0;
      time_shift_hours = 0.0;
      time_shift_minutes = 0.0;
      time_shift_seconds = 0;
      time_skip_weekdays = false;
      //defined by system
      retval =  0;
      retval0 =  0;
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



string overriding_symbol = "";

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
string getSymbol(string symbol)
  {
   return (symbol==NULL || symbol=="") && overriding_symbol != "" ? overriding_symbol : symbol;
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int SecondsFromComponents(double days, double hours, double minutes, int seconds)
  {
   int retval =
      86400 * (int)MathFloor(days)
      + 3600 * (int)(MathFloor(hours) + (24 * (days - MathFloor(days))))
      + 60 * (int)(MathFloor(minutes) + (60 * (hours - MathFloor(hours))))
      + (int)((double)seconds + (60 * (minutes - MathFloor(minutes))));

   return retval;
  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
datetime TimeFromComponents(
   int time_src = 0,
   int    y = 0,
   int    m = 0,
   double d = 0,
   double h = 0,
   double i = 0,
   int    s = 0
)
  {
   MqlDateTime tm;
   int offset = 0;

   if(time_src == 0)
     {
      TimeCurrent(tm);
     }
   else
      if(time_src == 1)
        {
         TimeLocal(tm);
         offset = (int)(TimeLocal() - TimeCurrent());
        }
      else
         if(time_src == 2)
           {
            TimeGMT(tm);
            offset = (int)(TimeGMT() - TimeCurrent());
           }

   if(y > 0)
     {
      if(y < 100)
        {
         y = 2000 + y;
        }
      tm.year = y;
     }
   if(m > 0)
     {
      tm.mon = m;
     }
   if(d > 0)
     {
      tm.day = (int)MathFloor(d);
     }

   tm.hour = (int)(MathFloor(h) + (24 * (d - MathFloor(d))));
   tm.min  = (int)(MathFloor(i) + (60 * (h - MathFloor(h))));
   tm.sec  = (int)((double)s + (60 * (i - MathFloor(i))));

   datetime time = StructToTime(tm) - offset;

   return time;
  }




//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void OnTick()
  {

  }


//+------------------------------------------------------------------+
