#define TIME_MODE_TEXT 1
#define TIME_MODE_COMPONENT 2
#define TIME_MODE_RELATIVE 3



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task0 : public Task
  {
public:
   int               server_or_local_time;
   int               time_start_mode;
   string            time_start;
   int               time_start_year;
   int               time_start_month;
   double            time_start_day;
   double            time_start_hour;
   double            time_start_minute;
   int               time_start_second;
   int               time_end_mode;
   string            time_end;
   int               time_end_year;
   int               time_end_month;
   double            time_end_day;
   double            time_end_hour;
   double            time_end_minute;
   int               time_end_second;
   int               time_end_rel_years;
   int               time_end_rel_months;
   double            time_end_rel_days;
   double            time_end_rel_hours;
   double            time_end_rel_minutes;
   int               time_end_rel_seconds;

public:
                     Task0(string name):Task(name)
     {
      server_or_local_time = TIME_SERVER;
      time_start_mode = TIME_MODE_TEXT;
      time_start = "00:00";
      time_start_year = 0;
      time_start_month = 0;
      time_start_day = 0.0;
      time_start_hour = 1.0;
      time_start_minute = 0.0;
      time_start_second = 0;
      time_end_mode = TIME_MODE_TEXT;
      time_end = "00:01";
      time_end_year = 0;
      time_end_month = 0;
      time_end_day = 0.0;
      time_end_hour = 1.0;
      time_end_minute = 1.0;
      time_end_second = 0;
      time_end_rel_year = 0;
      time_end_rel_months = 0;
      time_end_rel_days = 0.0;
      time_end_rel_hours = 0.0;
      time_end_rel_minutes = 1.0;
      time_end_rel_seconds = 0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      datetime t0 = 0, t1 = 0, tx = 0, now = 0;
      int mode_time = 0;

      if(server_or_local_time == TIME_SERVER)
        {
         mode_time = 0;
         now = TimeCurrent();
        }
      else
         if(server_or_local_time == TIME_LOCAL)
           {
            mode_time = 1;
            now = TimeLocal();
           }
         else
            if(server_or_local_time == TIME_GMT)
              {
               mode_time = 2;
               now = TimeGMT();
              }

      //-- start time
      if(time_start_mode == TIME_MODE_TEXT)
        {
         t0 = TimeFromString(mode_time, time_start);
        }
      else
         if(time_start_mode == TIME_MODE_COMPONENT)
           {
            t0 = TimeFromComponents(mode_time, time_start_year, time_start_month, time_start_day, time_start_hour, time_start_minute, time_start_second);
           }

      //-- end time
      if(time_end_mode == TIME_MODE_TEXT)
        {
         t1 = TimeFromString(mode_time, time_end);
        }
      else
         if(time_end_mode == TIME_MODE_COMPONENT)
           {
            t1 = TimeFromComponents(mode_time, time_end_year, time_end_month, time_end_day, time_end_hour, time_end_minute, time_end_second);
           }
         else
            if(time_end_mode == TIME_MODE_RELATIVE)
              {
               MqlDateTime tm;
               TimeToStruct(t0, tm);

               tm.year += time_end_rel_years;
               tm.mon  += time_end_rel_months;
               tm.day  += (int)MathFloor(time_end_rel_days);
               tm.hour += (int)(MathFloor(time_end_rel_hours) + (24 * (time_end_rel_hours - MathFloor(time_end_rel_hours))));
               tm.min  += (int)(MathFloor(time_end_rel_minutes) + (60 * (time_end_rel_minutes - MathFloor(time_end_rel_minutes))));
               tm.sec  += (int)((double)time_end_rel_seconds + (60 * (time_end_rel_seconds - MathFloor(time_end_rel_seconds))));

               t1 = StructToTime(tm);

               if(t1 < t0)
                 {
                  t1 = t1 + 86400;
                 }
              }

      if((now >= t0 && now < t1) || (t0 > t1 && (now >= t0 || now < t1)))
        {
         printf("task" + block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level)
     {

     }

  };





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
datetime TimeFromString(int mode_time, string stamp)
  {
   datetime t = 0;

   if(mode_time == 0)
      t = TimeCurrent();
   else
      if(mode_time == 1)
         t = TimeLocal();
      else
         if(mode_time == 2)
            t = TimeGMT();

   int stamplen = StringLen(stamp);

   if(stamplen < 9)
     {
      int thour    = TimeHour(t);
      int tminute  = TimeMinute(t);
      int tseconds = TimeSeconds(t);

      int hour   = (int)StringSubstr(stamp, 0, 2);
      int minute = (int)StringSubstr(stamp, 3, 2);
      int second = 0;

      if(stamplen > 5)
        {
         second = (int)StringSubstr(stamp, 6, 2);
        }

      datetime t1 = (datetime)(t - (thour-hour)*3600 - (tminute - minute)*60 - (tseconds-second));

      return t1;
     }

   return StringToTime(stamp);
  }


