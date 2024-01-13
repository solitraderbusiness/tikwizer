class Task_id : public Task
  {
public:
   int               months[]; //1 January, 2 February, ...

public:
                     Task_id(string name):Task(name)
     {
      int mmonths[]  = months_val;
      ArrayCopy(months, mmonths, 0, 0, WHOLE_ARRAY);
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int month = Month();
      bool result = false;
      if(ArraySize(months)>0)//STest, in case size is zero, should it return true or false?
        {
         for(int i=0; i<ArraySize(months); i++)
            if(month==months[i])
              {
               result = true;
               break;
              }
        }
      if(result)
        {
         printf("task"+block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };

