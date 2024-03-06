//+------------------------------------------------------------------+
//|       this is the OR task                                       |
//+------------------------------------------------------------------+
class Task20 : public Task
  {

public:
   bool              firstBlockMet;
                     Task20(string name):Task(name)
     {
      firstBlockMet = false;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      if(firstBlockMet)
        {
         printf("task "+block_id+" didn't pass cuz first block already met!");
         block.onResult(ROUTE_2_PASSED);
         return;
        }


      printf("task "+block_id+" passed!");
      firstBlockMet = true;
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {
      firstBlockMet = false;
     }
  };

