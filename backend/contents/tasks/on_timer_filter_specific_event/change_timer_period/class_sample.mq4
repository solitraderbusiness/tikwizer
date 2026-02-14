

bool ONTIMER_TAKEN      = false;
bool ONTIMER_TAKEN_IN_MILLISECONDS = false;
double ONTIMER_TAKEN_TIME = 0;


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task6 : public Task
  {
   double                SetHours;
   double                SetMinutes;
   double                SetSeconds;
public:
                     Task6(string name):Task(name)
     {
      SetHours = (double)0.0;
      SetMinutes = (double)1.0;
      SetSeconds = (double)0.0;
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


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool OnTimerSet(double seconds)
  {
   if(ONTIMER_TAKEN)
     {
      if(seconds<=0)
        {
         ONTIMER_TAKEN_IN_MILLISECONDS = false;
         ONTIMER_TAKEN_TIME = 0;
        }
      else
         if(seconds < 1)
           {
            ONTIMER_TAKEN_IN_MILLISECONDS = true;
            ONTIMER_TAKEN_TIME = seconds*1000;
           }
         else
           {
            ONTIMER_TAKEN_IN_MILLISECONDS = false;
            ONTIMER_TAKEN_TIME = seconds;
           }

      return true;
     }

   if(seconds<=0)
     {
      EventKillTimer();
     }
   else
      if(seconds < 1)
        {
         return (EventSetMillisecondTimer((int)(seconds*1000)));
        }
      else
        {
         return (EventSetTimer((int)seconds));
        }

   return true;
  }
