class Task_id : public Task
  {
public:
   double               sleep_seconds;
   bool              sleep_tester_normal;
   bool              sleep_tester_visual;

public:
                     Task_id(string name):Task(name)
     {
      sleep_seconds = sleep_seconds_val;
      sleep_tester_normal = sleep_tester_normal_val;
      sleep_tester_visual = sleep_tester_visual_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      if(MQLInfoInteger(MQL_TESTER) == false)
        {
         Sleep(sleep_seconds*1000);
        }
      else
        {
         if(
            (sleep_tester_visual == true && MQLInfoInteger(MQL_VISUAL_MODE) == true)
            || (sleep_tester_normal == true && MQLInfoInteger(MQL_VISUAL_MODE) == false)
         )
           {
            SleepEx(sleep_seconds*1000,false);
           }
        }
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
