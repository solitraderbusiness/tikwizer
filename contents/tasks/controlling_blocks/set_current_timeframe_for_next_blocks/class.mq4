class Task0 : public Task
  {
   int               timeframes[];
public:
                     Task0(string name):Task(name)
     {
      int mtimeframes[] = {15, 30};
      ArrayCopy(timeframes, mtimeframes, 0, 0, WHOLE_ARRAY);
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int size = ArraySize(timeframes);
      if(size==0)
        {
         printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
         return;
        }


      for(int i=0; i<size; i++)
        {
         overriding_timeframe = timeframes[i];
         printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }

      overriding_timeframe = -1;
      printf("task"+block_id + " passed route 2");
      block.onResult(ROUTE_2_PASSED);

     }
   virtual void      reset(int level)
     {

     }

  };
