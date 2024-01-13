class Task23 : public Task

  {
public:
   string            symbol;
   int               cmd;
   double            volume;
   double            price;
   int               slippage;
   double            stoploss;
   double            takeprofit;
   string            comment;
   int               magic;
   datetime          expiration;
   color             arrow_color;
   //These are calculated
   int               ticket;
   double            slPrice;
   double            tpPrice;
   bool              initialized;

public:

public:
                     Task23(string name):Task(name)
     {
      symbol = NULL;
      cmd = OP_SELL;
      volume = 1;
      price = Bid;
      slippage = 2;
      stoploss = 20;
      takeprofit = 20;
      comment = "This is my trade";
      magic = 2154;
      expiration = 0;
      arrow_color = clrNONE;

      calc();
     }

   //does needed calculations
private:
   void              calc()
     {
      if(MathAbs(takeprofit+stoploss)*10<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      stoploss=NormalizeDouble(stoploss*Point*10,Digits);
      takeprofit=NormalizeDouble(takeprofit*Point*10,Digits);
      if(cmd==OP_BUY)
        {
         slPrice = price-stoploss;
         tpPrice = price+takeprofit;
        }
      else
         if(cmd==OP_SELL)
           {
            slPrice = price+stoploss;
            tpPrice = price-takeprofit;
           }

      initialized = true;
     }

public:
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      if(!initialized)
        {
         printf("Not initialized");
         block.onResult(ROUTE_2_PASSED);
         return;
        }

      ticket=OrderSend(symbol,cmd,volume,price,slippage,slPrice,tpPrice,comment,magic,expiration,arrow_color);

      if(ticket == ERR_NO_ERROR)
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
