class Task_id : public Task
  {
   int               weekdays[]; //0 sunday, 1 monday, ...
   string            time_mode;
public:
                     Task_id(string name):Task(name)
     {
      int mweekdays[]  = weekdays_val;
      ArrayCopy(weekdays, mweekdays, 0, 0, WHOLE_ARRAY);
      time_mode = time_mode_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int day;
      if(time_mode==TIME_SERVER)
         day = TimeDayOfWeek(TimeCurrent());
      else
         if(time_mode==TIME_LOCAL)
            day = TimeDayOfWeek(TimeLocal());
         else
            if(time_mode==TIME_GMT)
               day = TimeDayOfWeek(TimeGMT());

      bool result = false;
      if(ArraySize(weekdays)>0)//STest, in case size is zero, should it return true or false?
        {
         for(int i=0; i<ArraySize(weekdays); i++)
            if(day==weekdays[i])
              {
               result = true;
               break;
              }
        }
      if(result)
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
