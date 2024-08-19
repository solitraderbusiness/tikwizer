class Task_id : public Task
  {
   string                CheckBuyOrSell;
   string                CheckLimitOrStop;
public:
                     Task_id(string name):Task(name)
     {
      CheckBuyOrSell = (string)CheckBuyOrSell_val;
      CheckLimitOrStop = (string)CheckLimitOrStop_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(exit_loop)
        {
         return;
        }

      //LoopedResume();

      if (
			   (CheckBuyOrSell == "both" || (CheckBuyOrSell == "buy" && IsOrderTypeBuy()) || (CheckBuyOrSell == "sell" && IsOrderTypeSell()))
			&& (CheckLimitOrStop == "both" || (CheckLimitOrStop == "buy" && IsOrderTypeStop()) || (CheckLimitOrStop == "sell" && IsOrderTypeStop()))
		)
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
