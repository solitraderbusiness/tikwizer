
class Task_id : public Task
  {
public:
   string              symbol;
   bool              spread_mode;
   double            spread_benchmark_fix_value;
   int               average_spread_time_period;
   SpreadHolder      spreads[];
   string            msymbol;
public:
                     Task_id(string name):Task(name)
     {
      symbol = symbol_val;
      spread_mode = spread_mode_val;
      average_spread_time_period = average_spread_time_period_val;
      spread_benchmark_fix_value = spread_benchmark_fix_value_val;
     }

   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      removeSpreadExtra();
      addSpread();

      double spread_benchmark = spread_mode==SPREAD_BENCHMARK_AVERAGE ? spreadAverage() : spread_benchmark_fix_value;
      double spread_current = MarketInfo(msymbol, MODE_SPREAD);

      bool result = spread_current operator_val spread_benchmark;
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
   void              addSpread()
     {
      SpreadHolder sph;
      sph.spread = MarketInfo(msymbol,MODE_SPREAD);
      sph.time = TimeCurrent();
      ArrayResize(spreads, ArraySize(spreads)+1, 0);
      spreads[ArraySize(spreads)-1] = sph;
     }
   void              removeSpreadExtra()
     {
      int size = ArraySize(spreads);
      if(size==0)
         return;

      for(int i=size-1; i>=0; i--)
        {
         int timeDiff = TimeCurrent() - spreads[i].time;
         if(timeDiff>average_spread_time_period)
            RemoveIndexFromArray(spreads, i);
        }
     }
   double            spreadAverage()
     {
      double spreadTotal = 0;
      int size = ArraySize(spreads);
      if(size==0)
         return 0;
      for(int i=size-1; i>=0; i--)
         spreadTotal += spreads[i].spread;
      return spreadTotal/size;
     }
  };
