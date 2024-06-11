class Task2 : public Task
  {
public:
   int                server_or_local_time;
   string                StartHour;
   string                EndHour;
   bool                SecondHoursBlock;
   string                SecondStartHour;
   string                SecondEndHour;
   bool                ThirdHoursBlock;
   string                ThirdStartHour;
   string                ThirdEndHour;
   bool               FourthHoursBlock;
   string               FourthStartHour;
   string               FourthEndHour;
public:
                     Task2(string name):Task(name)
     {
      server_or_local_time = TIME_SERVER;
      StartHour = "00:00";
      EndHour = "06:00";
      SecondHoursBlock = false;
      SecondStartHour = "06:00";
      SecondEndHour = "12:00";
      ThirdHoursBlock = false;
      ThirdStartHour = "12:00";
      ThirdEndHour = "18:00";
      FourthHoursBlock = false;
      FourthStartHour = "18:00";
      FourthEndHour = "00:00";
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      bool pass     = false;
      int mode_time = 0;
      datetime start = 0, end = 0, now = 0;

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

      start = TimeFromString(mode_time, StartHour);
      end   = TimeFromString(mode_time, EndHour);

      if(end < start)
         end = end + 86400;

      if(now >= start && now < end)
         pass=true;

      if(pass == false && SecondHoursBlock == true)
        {
         start = TimeFromString(mode_time, SecondStartHour);
         end   = TimeFromString(mode_time, SecondEndHour);

         if(end < start)
            end = end + 86400;

         if(now >= start && now < end)
            pass = true;
        }

      if(pass == false && ThirdHoursBlock == true)
        {
         start = TimeFromString(mode_time, ThirdStartHour);
         end   = TimeFromString(mode_time, ThirdEndHour);

         if(end < start)
            end = end + 86400;

         if(now >= start && now < end)
            pass = true;
        }

      if(pass == false && FourthHoursBlock == true)
        {
         start = TimeFromString(mode_time, FourthStartHour);
         end   = TimeFromString(mode_time, FourthEndHour);

         if(end < start)
            end = end + 86400;
         if(now >= start && now < end)
            pass = true;
        }

      if(pass)
        {
         printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };

