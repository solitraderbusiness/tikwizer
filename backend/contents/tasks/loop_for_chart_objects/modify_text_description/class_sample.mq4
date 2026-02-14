class Task2 : public Task
  {

public:
                     Task2(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      Value1_time_2 value1_time_2;
      value1_time_2.init();
      string valueValue1_time_2 = value1_time_2.calc<string>();
      bool success = ObjectSetString(loaded_object_chart_id(), loaded_object_name(), OBJPROP_TEXT, valueValue1_time_2);
      if(success)
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
