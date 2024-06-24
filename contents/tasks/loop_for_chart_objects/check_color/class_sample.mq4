class Task0 : public Task
  {
   color                obj_color;
public:
                     Task0(string name):Task(name)
     {
      obj_color = clrRed;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(ObjectGetInteger(loaded_object_chart_id(), loaded_object_name(), OBJPROP_COLOR) == obj_color)
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
