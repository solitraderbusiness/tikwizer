class Task_id : public Task
  {
   color                SetObjColor;
public:
                     Task_id(string name):Task(name)
     {
      SetObjColor = (color)SetObjColor_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(ObjectSetInteger(loaded_object_chart_id(), loaded_object_name(), OBJPROP_COLOR, SetObjColor))
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
