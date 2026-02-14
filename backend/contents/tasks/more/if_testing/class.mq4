
class Task0 : public Task
  {
public:
                     Task0(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      if(MQLInfoInteger(MQL_TESTER))
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
