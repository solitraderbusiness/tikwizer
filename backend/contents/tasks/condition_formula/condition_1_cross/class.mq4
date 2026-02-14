//+------------------------------------------------------------------+
//|         This is condition 1 cross                                                        |
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

      initializer_11
      initializer_12
      initializer_21
      initializer_22

      if(var_name_11 operator_1 var_name_21 && var_name_12 operator_2 var_name_22)
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


