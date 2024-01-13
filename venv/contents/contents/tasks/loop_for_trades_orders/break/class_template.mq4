class Task_id : public Task
  {

public:
                     Task_id(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      exit_loop = true;
     }
   virtual void      reset(int level)
     {
      //STest, commented below cuz in fxdreema loop break works till the end. Though this is not logical.
      //exit_loop = false;
     }
  };