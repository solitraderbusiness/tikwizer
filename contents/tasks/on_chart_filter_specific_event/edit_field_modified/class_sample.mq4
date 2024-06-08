class Task0 : public Task
  {
public:
   string            name_filter_mode;
   string            obj_name;
public:
                     Task0(string name):Task(name)
     {
      name_filter_mode = "";
      obj_name = "";
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      bool next = false;
      if(onchartEventHolder.id == CHARTEVENT_OBJECT_ENDEDIT)
        {
         if(name_filter_mode == "name" || name_filter_mode == "names")
           {
            string names[];

            if(obj_name != "")
              {
               StringExplode(",", obj_name, names);
               int size = ArraySize(names);

               for(int i = 0; i < size; i++)
                 {
                  if(onchartEventHolder.sparam == StringTrim(names[i]))
                    {
                     next = true;
                     break;
                    }
                 }
              }
           }
         else
           {
            next = true;
           }
        }


      if(next)
        {
         printf("task" + block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };
