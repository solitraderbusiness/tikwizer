struct SpreadHolder
  {
   double            spread;
   datetime          time;
  };

SpreadHolder spreads[];

#define SPREAD_MODE_AVERAGE 1
#define SPREAD_MODE_FIX 2



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
//void OnTick()
//  {
//   addSpread();
//   removeSpreadExtra();
//
//
//
//  }


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task15 : public Task
  {
public:
   string              symbol;
   bool              spread_mode;
   double            spread_limit;
   int               average_spread_time_period;

   string            msymbol;
public:
                     Task15(string name):Task(name)
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


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void addSpread()
  {
   SpreadHolder sph;
   sph.spread = MarketInfo(NULL,MODE_SPREAD);
   sph.time = TimeCurrent();
   ArrayResize(spreads, ArraySize(spreads)+1, 0);
   spreads[ArraySize(spreads)-1] = sph;
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void removeSpreadExtra()
  {
   int size = ArraySize(spreads);
   if(size==0)
      return;
   for(int i=size-1; i>=0; i--)
     {
      int timeDiff = TimeCurrent() - spreads[i].time;
      if(timeDiff>20)
         RemoveIndexFromArray(spreads, i);
     }
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double spreadAverage()
  {
   double spreadTotal = 0;
   int size = ArraySize(spreads);
   if(size==0)
      return 0;
   for(int i=size-1; i>=0; i--)
      spreadTotal += spreads[i].spread;
   return spreadTotal/size;
  }
