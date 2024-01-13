
class Task_id : public Task
  {

public:
   int               source_history[];
   bool              allBlocksMet;
                     Task2(string name):Task(name)
     {
      allBlocksMet = false;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      if(allBlocksMet)
        {
         printf("task "+block_id+" didn't pass cuz all blocks already met!");
         block.onResult(ROUTE_2_PASSED);
        }
      Task::run(block_id, block);

      AddToArray(source_history, block.current_source_id);
      int prevs[];
      ArrayResize(prevs, ArraySize(block.prevs_true)+ArraySize(block.prevs_false), 0);
      JoinArrays(block.prevs_true, block.prevs_false, prevs);

      allBlocksMet = areAllItemsPresent(prevs, source_history);
      if(allBlocksMet)
        {
         printf("task "+block_id+" passed!");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task "+block_id+" didn't pass!");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {
      allBlocksMet = false;
      ArrayResize(source_history, 0);//STest, right way?
     }
  };

