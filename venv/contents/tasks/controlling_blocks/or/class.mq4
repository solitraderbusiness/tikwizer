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
      if(firstBlockMet)
        {
         printf("task "+block_id+" didn't pass cuz first block already met!");
         block.onResult(ROUTE_2_PASSED);
         return;
        }
      Task::run(block_id, block);


      printf("task "+block_id+" passed!");
      firstBlockMet = true;
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {
      firstBlockMet = false;
     }
  };

