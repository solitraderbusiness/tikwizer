class Task_id : public Task
  {
public:
   string            memory[];

public:
                     Task_id(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      string value = IntegerToString(loaded_object_chart_id() + loaded_object_name());

      if(in_array(memory, value) == false)
        {
         array_ensure_value(memory, value);

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

