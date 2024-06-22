//STest, not working accurately on other symbols (other than current chart itself) (?)
class Task_id : public Task
  {
private:
   //specified by user
   string                symbol;
   int                n;
   //specified by system
   double            a0;
   double            b0;
   int               t0;
   int               count;

public:
                     Task_id(string name): Task(name)
     {
      //specified by user
      symbol = symbol_val;
      n = n_val;
      //specified by system
      count =  0;
     }

public:
   virtual void      run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      string msymbol = getSymbol(symbol);

      bool pass = false;
      double a  = SymbolInfoDouble(msymbol, SYMBOL_ASK);
      double b  = SymbolInfoDouble(msymbol, SYMBOL_BID);
      int t     = (int)SymbolInfoInteger(msymbol, SYMBOL_TIME);

      if(t != t0 || a != a0 || b != b0)
        {
         t0 = t;
         a0 = a;
         b0 = b;

         count++;

         if(count >= n)
           {
            count = 0;
            pass   = true;
           }
        }

      if(pass)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level) {}
  };
