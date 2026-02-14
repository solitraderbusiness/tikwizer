
class Task_id : public Task
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
                     Task_id(string name):Task(name)
     {
      server_or_local_time = server_or_local_time_val;
      time_start_mode = time_start_mode_val;
      time_start = time_start_val;
      time_start_year = time_start_year_val;
      time_start_month = time_start_month_val;
      time_start_day = time_start_day_val;
      time_start_hour = time_start_hour_val;
      time_start_minute = time_start_minute_val;
      time_start_second = time_start_second_val;
      time_end_mode = time_end_mode_val;
      time_end = time_end_val;
      time_end_year = time_end_year_val;
      time_end_month = time_end_month_val;
      time_end_day = time_end_day_val;
      time_end_hour = time_end_hour_val;
      time_end_minute = time_end_minute_val;
      time_end_second = time_end_second_val;
      time_end_rel_years = time_end_rel_years_val;
      time_end_rel_months = time_end_rel_months_val;
      time_end_rel_days = time_end_rel_days_val;
      time_end_rel_hours = time_end_rel_hours_val;
      time_end_rel_minutes = time_end_rel_minutes_val;
      time_end_rel_seconds = time_end_rel_seconds_val;
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
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level)
     {

     }

  };

