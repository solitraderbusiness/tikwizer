class Task_id : public Task
  {
   double                SetHours;
   double                SetMinutes;
   double                SetSeconds;
public:
                     Task_id(string name):Task(name)
     {
      SetHours = (double)SetHours_val;
      SetMinutes = (double)SetMinutes_val;
      SetSeconds = (double)SetSeconds_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      double time = (3600*SetHours) + (60*SetMinutes) + (SetSeconds);
      bool success = OnTimerSet(time);
      if(success == true)
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

