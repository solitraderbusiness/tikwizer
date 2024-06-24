//Set "Current Timeframe" for next blocks
class Task5 : public Task
  {
   int               timeframe_1;
   int               timeframe_2;
   int               timeframe_3;
   int               timeframe_4;
   int               timeframe_5;
   int               timeframe_6;
   int               timeframe_7;
   int               timeframe_8;
   int               timeframe_9;
   int               timeframe_10;


public:
                     Task5(string name):Task(name)
     {
      timeframe_1  = PERIOD_D1;
      timeframe_2  = PERIOD_M1;
      timeframe_3  = -1;
      timeframe_4  = PERIOD_D1;
      timeframe_5  = PERIOD_M15;
      timeframe_6  = -1;
      timeframe_7  = -1;
      timeframe_8  = PERIOD_H1;
      timeframe_9  = -1;
      timeframe_10 = -1;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int               timeframes[];
      if(timeframe_1>-1)
         AddToArray(timeframes, timeframe_1);
      if(timeframe_2>-1)
         AddToArray(timeframes, timeframe_2);
      if(timeframe_3>-1)
         AddToArray(timeframes, timeframe_3);
      if(timeframe_4>-1)
         AddToArray(timeframes, timeframe_4);
      if(timeframe_5>-1)
         AddToArray(timeframes, timeframe_5);
      if(timeframe_6>-1)
         AddToArray(timeframes, timeframe_6);
      if(timeframe_7>-1)
         AddToArray(timeframes, timeframe_7);
      if(timeframe_8>-1)
         AddToArray(timeframes, timeframe_8);
      if(timeframe_9>-1)
         AddToArray(timeframes, timeframe_9);
      if(timeframe_10>-1)
         AddToArray(timeframes, timeframe_10);



      int size = ArraySize(timeframes);
      if(size==0)
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
         return;
        }


      for(int i=0; i<size; i++)
        {
         overriding_timeframe = timeframes[i];
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }

      overriding_timeframe = -1;
      //printf("task"+block_id + " passed route 2");
      block.onResult(ROUTE_2_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
