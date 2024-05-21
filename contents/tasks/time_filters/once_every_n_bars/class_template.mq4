class Task_id: public Task
  {
public:
   string            symbol;
   int               timeframe;
   int               n;
   int               max_times_to_pass;

   datetime          lastSavedTime;
   int               count_n;
   int               count_max_times;

                     Task_id(string name):Task(name)
     {
      symbol = symbol_val;
      timeframe = timeframe_val;
      n = n_val;
      max_times_to_pass = max_times_to_pass_val;


      count_n = 0;
      count_max_times = 1;
      lastSavedTime = -1;
     }

   virtual void      run(int block_id, BlockParent &block)
     {
      string msymbol = getSymbol(symbol);
      int mtimeframe = getTimeframe(timeframe);

      if(iTime(msymbol, mtimeframe, 0)!=lastSavedTime)
        {
         double mod = MathMod(count_n, n);
         count_n++;
         lastSavedTime = iTime(msymbol, mtimeframe, 0);

         if(mod == 0) //do once every n bar
           {
            count_max_times = 1;
            count_n = 1;
            printf("task"+block_id + " passed route 1 ");
            block.onResult(ROUTE_1_PASSED);
           }
         else //otherwise
           {
            printf("task"+block_id + " passed route 2");
            block.onResult(ROUTE_2_PASSED);
           }
        }
      else //otherwise, it's the same candle
        {
         double mod2 = MathMod(count_n, n);
         if(count_max_times < max_times_to_pass && (mod2==1 || (mod2==0 && n==1)))
           {
            count_max_times++;
            printf("task"+block_id + " passed route 1");
            block.onResult(ROUTE_1_PASSED);
           }
         else
           {
            printf("task"+block_id + " passed route 2");
            block.onResult(ROUTE_2_PASSED);
           }
        }
     }

   virtual void      reset(int level) {}

  };
