class Task_id : public Task
  {
public:
   double            slippage;
   color             arrow_color;
public:
                     Task_id(string name):Task(name)
     {
      slippage = slippage_val;
      arrow_color = arrow_color_val;
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
         OnTrade();
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
