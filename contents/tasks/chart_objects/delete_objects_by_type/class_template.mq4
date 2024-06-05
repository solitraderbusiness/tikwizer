class Task_id : public Task
  {
public:
   int                window;
   int                type;
public:
                     Task_id(string name):Task(name)
     {
      window = window_val;
      type = type_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(ObjectsDeleteAll(0, window, type) > 0)
        {
         ChartRedraw();
        }

      printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
