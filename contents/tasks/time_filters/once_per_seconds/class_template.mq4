class Task_id : public Task
  {
public:
   int               n;
   datetime          timenext;

public:
                     Task_id(string name) :Task(name)
     {
      n = n_val;
      timenext =  0;
     }

   virtual void              run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      datetime now = TimeCurrent();

      if(now >= timenext)
        {
         while(true)
           {
            if(now >= timenext)
              {
               if(timenext == 0)
                 {
                  timenext = (datetime)(MathFloor(now / 86400.0) * 86400.0); //Using this we get 00:00 at today
                 }

               timenext = timenext + n;
              }
            else
              {
               break;
              }
           }
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }

   virtual void      reset(int level) {}
  };
