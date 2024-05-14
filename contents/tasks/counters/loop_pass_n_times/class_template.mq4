class Task_id : public Task
  {
public:
                     Task_id(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int n = n_val;
      for(int i=0; i<n; i++)
        {
         if(exit_loop)
            return; //Stest, logical?
         printf("loop " + i + " passed");
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
