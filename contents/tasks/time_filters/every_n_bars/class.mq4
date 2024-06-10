class Task2 : public Task
  {
   string                symbol;
   ENUM_TIMEFRAMES                timeframe;
   int                n;
   /* Static Parameters */
   datetime          barTime;
   int               barCount;
public:
                     Task2(string name):Task(name)
     {
      symbol = "";
      timeframe = PERIOD_CURRENT;
      n = 5;
      //system parameters
      barTime =  0;
      barCount =  0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      bool pass = false;

      string msymbol = getSymbol(symbol);
      int mtimeframe = getTimeframe(timeframe);

      if(barTime < iTime(msymbol, mtimeframe, 1))
        {
         barCount++;

         if(barCount == n || barTime == 0)
           {
            barCount = 0;
            pass     = true;
           }

         barTime = iTime(msymbol, mtimeframe, 1);
        }

      if(pass)
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
