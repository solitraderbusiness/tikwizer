class Task1 : public Task
  {
   int                 server_or_local_time;
   int                 FirstStartSecond;
   int                 FirstEndSecond;
   bool                SecondSecondsBlock;
   int                 SecondStartSecond;
   int                 SecondEndSecond;
   bool                ThirdSecondsBlock;
   int                 ThirdStartSecond;
   int                 ThirdEndSecond;
   bool                FourthSecondsBlock;
   int                 FourthStartSecond;
   int                 FourthEndSecond;
public:
                     Task1(string name):Task(name)
     {
      server_or_local_time = server_or_local_time_val;
      FirstStartSecond = FirstStartSecond_val;
      FirstEndSecond = FirstEndSecond_val;
      SecondSecondsBlock = SecondSecondsBlock_val;
      SecondStartSecond = SecondStartSecond_val;
      SecondEndSecond = SecondEndSecond_val;
      ThirdSecondsBlock = ThirdSecondsBlock_val;
      ThirdStartSecond = ThirdStartSecond_val;
      ThirdEndSecond = ThirdEndSecond_val;
      FourthSecondsBlock = FourthSecondsBlock_val;
      FourthStartSecond = FourthStartSecond_val;
      FourthEndSecond = FourthEndSecond_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      // get the current second
      MqlDateTime time;

      if(server_or_local_time == TIME_LOCAL)
         TimeLocal(time);
      else
         if(server_or_local_time == TIME_SERVER)
            TimeCurrent(time);
         else
            if(server_or_local_time == TIME_GMT)
               TimeGMT(time);
            else
               TimeCurrent(time);

      int thisSecond = time.sec;

      // fix the end second
      if(FirstEndSecond <= 0)
         FirstEndSecond += 60;
      if(SecondEndSecond <= 0)
         SecondEndSecond += 60;
      if(ThirdEndSecond <= 0)
         ThirdEndSecond += 60;
      if(FourthEndSecond <= 0)
         FourthEndSecond += 60;

      // check and pass
      if(
         (thisSecond >= FirstStartSecond && thisSecond < FirstEndSecond)
         ||
         (FirstStartSecond > FirstEndSecond && (thisSecond >= FirstStartSecond || thisSecond < FirstEndSecond))
         ||
         (SecondSecondsBlock && thisSecond >= SecondStartSecond && thisSecond < SecondEndSecond)
         ||
         (SecondSecondsBlock && SecondStartSecond > SecondEndSecond && (thisSecond >= SecondStartSecond || thisSecond < SecondEndSecond))
         ||
         (ThirdSecondsBlock  && thisSecond >= ThirdStartSecond  && thisSecond < ThirdEndSecond)
         ||
         (ThirdSecondsBlock  && ThirdStartSecond > ThirdEndSecond && (thisSecond >= ThirdStartSecond || thisSecond < ThirdEndSecond))
         ||
         (FourthSecondsBlock && thisSecond >= FourthStartSecond && thisSecond < FourthEndSecond)
         ||
         (FourthSecondsBlock && FourthStartSecond > FourthEndSecond && (thisSecond >= FourthStartSecond || thisSecond < FourthEndSecond))
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
