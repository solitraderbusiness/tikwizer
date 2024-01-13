//STest, not working accurately on other symbols (other than current chart itself) (?)
class Task42 : public Task
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
                     Task42(string name): Task(name)
     {
      //specified by user
      symbol = NULL;
      n = 7;
      //specified by system
      count =  0;
     }

public:
   virtual void      run(int block_id, BlockParent &block)
     {
      string msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

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
