//+------------------------------------------------------------------+
//|         This is condition 1 normal                                                        |
//+------------------------------------------------------------------+
class Task10 : public Task
  {
public:

public:
                     Task10(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      initializer_1
      initializer_2

      if(var_name_1 operator var_name_2)
        {
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }
  };

