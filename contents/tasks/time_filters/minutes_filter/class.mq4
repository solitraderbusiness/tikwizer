class Task2 : public Task
  {
public:
   int                 server_or_local_time;
   int                 FirstStartMinute;
   int                 FirstEndMinute;
   bool                SecondMinutesBlock;
   int                 SecondStartMinute;
   int                 SecondEndMinute;
   bool                ThirdMinutesBlock;
   int                 ThirdStartMinute;
   int                 ThirdEndMinute;
   bool                FourthMinutesBlock;
   int                 FourthStartMinute;
   int                 FourthEndMinute;
public:
                     Task2(string name):Task(name)
     {
      server_or_local_time = TIME_SERVER;
      FirstStartMinute = 5;
      FirstEndMinute = 10;
      SecondMinutesBlock = false;
      SecondStartMinute = 20;
      SecondEndMinute = 25;
      ThirdMinutesBlock = false;
      ThirdStartMinute = 30;
      ThirdEndMinute = 35;
      FourthMinutesBlock = false;
      FourthStartMinute = 50;
      FourthEndMinute = 55;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      // get the current minute
      MqlDateTime time;

      if(server_or_local_time == TIME_SERVER)
         TimeCurrent(time);
      else
         if(server_or_local_time == TIME_LOCAL)
            TimeLocal(time);
         else
            if(server_or_local_time == TIME_GMT)
               TimeGMT(time);
            else
               TimeCurrent(time);

      int minute = time.min;

      // fix the end minute
      if(FirstEndMinute <= 0)
         FirstEndMinute += 60;
      if(SecondEndMinute <= 0)
         SecondEndMinute += 60;
      if(ThirdEndMinute <= 0)
         ThirdEndMinute += 60;
      if(FourthEndMinute <= 0)
         FourthEndMinute += 60;

      // check and pass
      if(
         (minute >= FirstStartMinute && minute < FirstEndMinute)
         ||
         (FirstStartMinute > FirstEndMinute && (minute >= FirstStartMinute || minute < FirstEndMinute))
         ||
         (SecondMinutesBlock && minute >= SecondStartMinute && minute < SecondEndMinute)
         ||
         (SecondMinutesBlock && SecondStartMinute > SecondEndMinute && (minute >= SecondStartMinute || minute < SecondEndMinute))
         ||
         (ThirdMinutesBlock  && minute >= ThirdStartMinute  && minute < ThirdEndMinute)
         ||
         (ThirdMinutesBlock  && ThirdStartMinute > ThirdEndMinute && (minute >= ThirdStartMinute || minute < ThirdEndMinute))
         ||
         (FourthMinutesBlock && minute >= FourthStartMinute && minute < FourthEndMinute)
         ||
         (FourthMinutesBlock && FourthStartMinute > FourthEndMinute && (minute >= FourthStartMinute || minute < FourthEndMinute))
      )
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

