struct SpreadHolder
  {
   double            spread;
   datetime          time;
  };


#define SPREAD_BENCHMARK_AVERAGE 1
#define SPREAD_BENCHMARK_FIX 2


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task0 : public Task
  {
public:
   string              symbol;
   bool              spread_mode;
   double            spread_benchmark_fix_value;
   int               average_spread_time_period;
   double            average_spread_adjust;
   SpreadHolder      spreads[];
   string            msymbol;
public:
                     Task0(string name):Task(name)
     {
      symbol = NULL;
      spread_mode = SPREAD_BENCHMARK_FIX;
      average_spread_time_period = 40;
      spread_benchmark_fix_value = 14;
      average_spread_adjust = -25;
     }

   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      removeSpreadExtra();
      addSpread();

      double spread_benchmark = spread_mode==SPREAD_BENCHMARK_AVERAGE ? spreadAverage() : spread_benchmark_fix_value;
      double spread_current = MarketInfo(msymbol, MODE_SPREAD);

      bool result = spread_current >= spread_benchmark;
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
      return spreadTotal/size + average_spread_adjust;
     }
  };
