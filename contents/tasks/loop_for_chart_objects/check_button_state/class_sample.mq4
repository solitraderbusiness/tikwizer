
class Task1 : public Task
  {
   bool                ObjState;
public:
                     Task1(string name):Task(name)
     {
      ObjState = (bool)true;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(ObjectGetInteger(loaded_object_chart_id(), loaded_object_name(), OBJPROP_STATE) == ObjState)
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
