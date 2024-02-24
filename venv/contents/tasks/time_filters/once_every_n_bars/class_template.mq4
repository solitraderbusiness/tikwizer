class Task_id: public Task
  {
public:
   string            symbol;
   int               timeframe;
   int               n;

   datetime          lastSavedTime;
   int               count;

                     Task_id(string name):Task(name)
     {
      symbol = symbol_val;
      timeframe = timeframe_val;
      n = n_val;
      count = 0;
      lastSavedTime = -1;
     }

   virtual void      run(int block_id, BlockParent &block)
     {
      string msymbol = getSymbol(symbol);
      int mtimeframe = getTimeframe(timeframe);

      if(iTime(msymbol, mtimeframe, 0)!=lastSavedTime)
        {
         //do once per bar
         double mod = MathMod(count, n);
         count++;
         lastSavedTime = iTime(msymbol, mtimeframe, 0);
         if(mod == 0) //do once every n bar
           {
            printf(Bars + " " + mtimeframe);
            block.onResult(ROUTE_1_PASSED);
           }
         else //otherwise
           {
            block.onResult(ROUTE_2_PASSED);
           }
        }
      else //otherwise
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }

   virtual void      reset(int level) {}

  };
