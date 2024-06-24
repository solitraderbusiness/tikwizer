
class Task_id : public Task
  {
   int                 server_or_local_time;
   bool                monday;
   bool                tuesday;
   bool                wednesday;
   bool                thursday;
   bool                friday;
   bool                saturday;
   bool                sunday;

public:
                     Task_id(string name):Task(name)
     {
      server_or_local_time = server_or_local_time_val;
      monday = monday_val;
      tuesday = tuesday_val;
      wednesday = wednesday_val;
      thursday = thursday_val;
      friday = friday_val;
      saturday = saturday_val;
      sunday = sunday_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int day = 0;

      if(server_or_local_time == TIME_SERVER)
        {
         day = TimeDayOfWeek(TimeCurrent());
        }
      else
         if(server_or_local_time == TIME_LOCAL)
           {
            day = TimeDayOfWeek(TimeLocal());
           }
         else
            if(server_or_local_time == TIME_GMT)
              {
               day = TimeDayOfWeek(TimeGMT());
              }

      if(
         (monday    && day == 1)
         || (tuesday   && day == 2)
         || (wednesday && day == 3)
         || (thursday  && day == 4)
         || (friday    && day == 5)
         || (saturday  && day == 6)
         || (sunday    && day == 0)
      )
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
