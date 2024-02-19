class Task20 : public Task
  {
public:
   double            slippage;
   color             arrow_color;
public:
                     Task20(string name):Task(name)
     {
      slippage = 4;
      arrow_color = clrDeepPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      bool success;

      if(OrderType() < 2)
        {
         success = OrderClose(OrderTicket(), OrderLots(), OrderClosePrice(),slippage,arrow_color);
        }
      else
        {
         success = OrderDelete(OrderTicket(), arrow_color);
        }


      if(success)
        {
         printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };
