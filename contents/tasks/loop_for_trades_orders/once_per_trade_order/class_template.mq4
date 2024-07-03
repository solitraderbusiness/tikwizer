class Task_id : public Task
  {
public:
   bool                AllowOldOrders;
   int                 memory[];
public:
                     Task_id(string name):Task(name)
     {
      AllowOldOrders = (bool)AllowOldOrders_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      if(exit_loop)
         return;

      //LoopedResume(); //STest, necessary?

      bool next = false;

      if(AllowOldOrders || OrderOpenTime() >= TimeAtStart())
        {
         int ticket = (int)attrTicketParent(OrderTicket());

         if(in_array(memory, ticket) == false)
           {
            array_ensure_value(memory, ticket);
            next = true;
           }
        }

      if(next)
        {
         //printf("task"+block_id + " passed route 1 ");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2 ");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }
  };
