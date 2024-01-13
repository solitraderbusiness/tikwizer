//SNote: to be able to disable some intervals, it's enough to consider "00:00:00"
//as start and end. This way it will have no effect.
class Task26 : public Task
  {
private:
   string            time_mode;

   string            start_time_1;
   string            end_time_1;

   string            start_time_2;
   string            end_time_2;

   string            start_time_3;
   string            end_time_3;

   string            start_time_4;
   string            end_time_4;

public:
                     Task26(string name):Task(name)
     {
      //Specified by user
      time_mode = TIME_SERVER;

      start_time_1 = "09:00:00";
      end_time_1 = "10:10:00";

      start_time_2 = "12:00:00";
      end_time_2 = "13:50:00";

      start_time_3 = "18:00:00";
      end_time_3 = "22:30:20";

      start_time_4 = "23:00:00";
      end_time_4 = "23:59:59";
     }

   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      //Calculations
      datetime now;

      if(time_mode==TIME_SERVER)
         now = TimeCurrent();
      else
         if(time_mode==TIME_LOCAL)
            now = TimeLocal();
         else
            if(time_mode==TIME_GMT)
               now = TimeGMT();


      datetime start1 = TimeFromString(time_mode, start_time_1);
      datetime end1   = TimeFromString(time_mode, end_time_1);

      datetime start2 = TimeFromString(time_mode, start_time_2);
      datetime end2   = TimeFromString(time_mode, end_time_2);

      datetime start3 = TimeFromString(time_mode, start_time_3);
      datetime end3   = TimeFromString(time_mode, end_time_3);

      datetime start4 = TimeFromString(time_mode, start_time_4);
      datetime end4   = TimeFromString(time_mode, end_time_4);

      bool inTime1 = now>=start1 && now<end1;
      bool inTime2 = now>=start2 && now<end2;
      bool inTime3 = now>=start3 && now<end3;
      bool inTime4 = now>=start4 && now<end4;

      bool inTime = inTime1 || inTime2 || inTime3 || inTime4;


      if(inTime)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level) {}
  };

