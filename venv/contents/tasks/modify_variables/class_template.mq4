class Task_id : public Task

  {
public:
                     Task_id(string name):Task(name)
     {

     }

public:
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      modify_variables

      block.onResult(ROUTE_1_PASSED);
     }

   virtual void      reset(int level) {}

  };
