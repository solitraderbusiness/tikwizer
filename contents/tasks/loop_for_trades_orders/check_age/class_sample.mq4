class Task3 : public Task
  {
   string                AgeRelativeTo;
   double                AgeDays;
   double                AgeHours;
   double                AgeMinutes;
   double                AgeSeconds;
public:
                     Task3(string name):Task(name)
     {
      AgeRelativeTo = (string)"open-time";
      AgeDays = (double)0.0;
      AgeHours = (double)1.0;
      AgeMinutes = (double)0.0;
      AgeSeconds = (double)0.0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(exit_loop)
        {
         return;
        }

      //LoopedResume();

      bool pass = false;
      int age   = 0;
      datetime current_time      = TimeCurrent(); // the current server time
      datetime trade_time        = 0;             // the time of the trade
      datetime saturday_midnight = 0;             // the time at 00:00 on the next Saturday after the trade creation
      int weeks = 1;                              // the amount of weeks after trade creation, used to subtract the number of weekends

      if(AgeRelativeTo == "open-time")
        {
         trade_time = OrderOpenTime();
        }
      else
         if(AgeRelativeTo == "close-time")
           {
            trade_time = OrderCloseTime();
           }

      age = (int)(current_time - trade_time);

      MqlDateTime t;
      TimeToStruct(trade_time, t);

      if(t.day_of_week > 0 && t.day_of_week < 6)
        {
         saturday_midnight = trade_time + ((6 - t.day_of_week) * 86400) - ((t.hour * 3600) + (t.min * 60) + (t.sec));

         // do the age needs correction (removal of weekdays)
         if(current_time > saturday_midnight)
           {
            weeks = (int)MathCeil(((current_time - saturday_midnight) / 86400.0) / 7.0);
            age   = age - (weeks * 2 * 86400);
           }

         datetime AgeAmount = (datetime)((AgeDays * 86400) + (AgeHours * 3600) + (AgeMinutes * 60) + AgeSeconds);

         if(age > AgeAmount)
           {
            pass = true;
           }
        }

      if(pass)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };
