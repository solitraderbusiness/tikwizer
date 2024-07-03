class Task4 : public Task
  {
public:
   bool                AllowOldOrders;
   int                 memory[];
public:
                     Task4(string name):Task(name)
     {
      AllowOldOrders = (bool)false;
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



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
datetime TimeAtStart(string cmd = "server")
  {
   static datetime local  = 0;
   static datetime server = 0;

   if(cmd == "local")
     {
      return local;
     }
   else
      if(cmd == "server")
        {
         return server;
        }
      else
         if(cmd == "set")
           {
            local  = TimeLocal();
            server = TimeCurrent();
           }

   return 0;
  }

