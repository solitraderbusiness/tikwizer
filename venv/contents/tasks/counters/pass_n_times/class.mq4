class Task1 : public Task
  {
public:
                     Task1(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int n = 2;
      for(int i_id=0; i_id<n; i_id++)
        {
         if(exit_loop)
            return;//STest, logical?
         printf("loop " + i_id + " passed");
         block.onResult(ROUTE_1_PASSED);
        }
      printf("Whole loop passed");
      block.onResult(ROUTE_2_PASSED);//STest, key name is misleading. In fact the task passes at this stage.

     }
   virtual void      reset(int level)
     {
      //STest: should "exit_loop" get reset here? cuz in fx dreema, break block terminates loop forever (even in other ticks the loop won't run)
      //if (level == RESET_LEVEL_TICK){
      //   exit_loop = false;
      //}
     }
  };
