
class Task_id : public Task
  {
public:
   string              symbol;
   bool              spread_mode;
   double            spread_limit;
   int               average_spread_time_period;

   string            msymbol;
public:
                     Task_id(string name):Task(name)
     {
      symbol = NULL;
      spread_mode = SPREAD_MODE_AVERAGE;
      average_spread_time_period = 20;
      spread_limit = 18;
     }

   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;


      double spread_bound = spread_mode==SPREAD_MODE_FIX ? spreadAverage() : spread_limit;
      double spread = MarketInfo(msymbol, MODE_SPREAD);

      bool result = spread >= spread_bound;
      if(result)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }

   virtual void      reset(int level)
     {

     }
  };
