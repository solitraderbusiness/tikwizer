class Task_id : public Task
  {
public:
   string obj_name;

public:
                     Task_id(string name):Task(name)
     {
       obj_name = obj_name_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
         Task::run(block_id, block);

         if(obj_name != "" && ObjectFind(0, obj_name) >= 0)
            {
             loaded_object_chart_id(0);
             loaded_object_name(obj_name);
             loaded_object_subwindow(-1);
             loaded_object_type((int)ObjectGetInteger(0,obj_name,OBJPROP_TYPE));

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
