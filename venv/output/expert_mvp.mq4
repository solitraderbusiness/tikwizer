#define ROUTE_1_PASSED 1
#define ROUTE_2_PASSED 0
#define RESET_LEVEL_DEFAULT 0
#define RESET_LEVEL_TICK 1
#define RESET_LEVEL_BAR 2
#define RESET_LEVEL_CUSTOM 3
#define TIME_SERVER 1
#define TIME_LOCAL 2
#define TIME_GMT 3
#define ORDER_GROUP_MODE_NONE -1
#define ORDER_GROUP_MODE_NUMBER 1
#define ORDER_GROUP_MODE_AUTOMATED 2
#define  CANDLE_OPEN  1
#define  CANDLE_HIGH  2
#define  CANDLE_LOW  3
#define  CANDLE_CLOSE  4
#define  CANDLE_MEDIAN  5
#define  CANDLE_HLC3  6
#define  CANDLE_AVERAGE  7
#define  CANDLE_GAP_TO_PREV  8
#define  CANDLE_TOTAL_SIZE  9
#define  CANDLE_BODY_SIZE  10
#define  CANDLE_TOP_WICK  11
#define  CANDLE_BOTTOM_WICK  12
#define  BULL_CANDLE_TOTAL_SIZE  13
#define  BULL_CANDLE_BODY_SIZE  14
#define  BULL_CANDLE_TOP_WICK  15
#define  BULL_CANDLE_BOTTOM_WICK  16
#define  BEAR_CANDLE_TOTAL_SIZE  17
#define  BEAR_CANDLE_BODY_SIZE  18
#define  BEAR_CANDLE_TOP_WICK  19
#define  BEAR_CANDLE_BOTTOM_WICK  20
#define  FIND_BY_ID  1
#define  FIND_BY_DATE  2
#define  HIGHEST_PRICE  1
#define  LOWEST_PRICE  2
#define  TIME_PERIOD  1
#define  CANDLE_PERIOD  2
#define  GET_CANDLE_ID  1
#define  GET_PRICE  2
#define  GET_TIME  3
#define PRICE_AUTO 1
#define PRICE_ASK 2
#define PRICE_BID 3
#define PRICE_MID 4
#define RANGE_MODE_PIPS 1
#define RANGE_MODE_PRICE_FRACTION 2
#define RANGE_POSITION_AROUND 1
#define RANGE_POSITION_WINNING_SIDE 2
#define RANGE_POSITION_LOSING_SIDE 3
#define PROFIT_MODE_PIPS 1
#define PROFIT_MODE_MONEY 2
#define LOOP_DIRECTION_NEWEST_TO_OLDEST 1
#define LOOP_DIRECTION_OLDEST_TO_NEWEST 2
#define LOOP_DIRECTION_PROFITABLE_FIRST 3
#define LOOP_DIRECTION_PROFITABLE_LAST 4
#define VALUE_TYPE_NUMERIC 1
#define VALUE_TYPE_BOOLEAN 2
#define VALUE_TYPE_COLOR 3
#define VALUE_TYPE_PIPS 4
#define VALUE_TYPE_TEXT 5
#define VALUE_TYPE_TEXT_CODE_INPUT 6
#define VALUE_TYPE_TIME 7
#define VALUE_PIPS_AS_IS 1
#define VALUE_PIPS_AS_PRICE_FRACTION 2
extern int bbbbbbb = 21; // 
extern int rsishort = 7; // 
extern double lot = 0.1; // 
double aaaaaaa = 78; // 
class BlockParent
  {
public:
   int               current_source_id;
   int               nexts_true[];//static, filled by generator
   int               nexts_false[];//static, filled by generator
   int               prevs_true[];//static, filled by generator
   int               prevs_false[];//static, filled by generator

public:
   virtual void      onResult(int result) = NULL;
  };
class Task
  {
public:
   string            name;
public:
                     Task(string name)
     {
        this.name = name;
     }

   virtual void               run(int block_id, BlockParent &block)
     {

     }

   virtual void      reset(int level) = NULL;

  };

class RSI1_left
  {
   string            symbol;
   int               timeframe;
   int               period;
   int               applied_price;
   int               shift;
    
   int              buy_threshold;
   int              sell_threshold;

public:
   void              init()
     {
      symbol = NULL;
      timeframe = 0;
      period = 14;
      applied_price = PRICE_CLOSE;
      shift = 1;
      buy_threshold = 70;
      sell_threshold = 30;
     }

   double            calc()
     {
      double result = iRSI(symbol,timeframe,period, applied_price, shift);
      return result;
     }

  };
class Value1_right
  {
public:
       int               type;
   int               value;
   string               adjust;
   //for pips
   int               pips_mode;
   string            symbol;
   //for time (phase 2)
   
   string            msymbol;

public:

   void              init()

     {
      type = VALUE_TYPE_PIPS;
      value = 10;
      adjust = 20;
      //for pips
      pips_mode = VALUE_PIPS_AS_IS;
      symbol = NULL;
      //for time (phase 2)
     }

   string              calc()
     {

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      switch(type)
        {
         case VALUE_TYPE_NUMERIC:
         case VALUE_TYPE_BOOLEAN:
         case VALUE_TYPE_COLOR:
         case VALUE_TYPE_TEXT:
            return (string)value;

         case VALUE_TYPE_TEXT_CODE_INPUT:
            return "\"" + value + "\"";

         case VALUE_TYPE_PIPS:
            if(pips_mode == VALUE_PIPS_AS_IS)
              {
               return (string) value;
              }
            else
               if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                 {
                  double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                  return (string)(point*10*value);  //STest, *10 works for all symbols?
                 }
            return "";

         case VALUE_TYPE_TIME:
            return "";
        }
     }
  };

class RSI2_left
  {
   string            symbol;
   int               timeframe;
   int               period;
   int               applied_price;
   int               shift;
    
   int              buy_threshold;
   int              sell_threshold;

public:
   void              init()
     {
      symbol = NULL;
      timeframe = 0;
      period = 14;
      applied_price = PRICE_CLOSE;
      shift = 1;
      buy_threshold = 70;
      sell_threshold = 30;
     }

   double            calc()
     {
      double result = iRSI(symbol,timeframe,period, applied_price, shift);
      return result;
     }

  };
class Value2_right
  {
public:
       int               type;
   int               value;
   string               adjust;
   //for pips
   int               pips_mode;
   string            symbol;
   //for time (phase 2)
   
   string            msymbol;

public:

   void              init()

     {
      type = VALUE_TYPE_PIPS;
      value = 10;
      adjust = 20;
      //for pips
      pips_mode = VALUE_PIPS_AS_IS;
      symbol = NULL;
      //for time (phase 2)
     }

   string              calc()
     {

      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      switch(type)
        {
         case VALUE_TYPE_NUMERIC:
         case VALUE_TYPE_BOOLEAN:
         case VALUE_TYPE_COLOR:
         case VALUE_TYPE_TEXT:
            return (string)value;

         case VALUE_TYPE_TEXT_CODE_INPUT:
            return "\"" + value + "\"";

         case VALUE_TYPE_PIPS:
            if(pips_mode == VALUE_PIPS_AS_IS)
              {
               return (string) value;
              }
            else
               if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                 {
                  double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                  return (string)(point*10*value);  //STest, *10 works for all symbols?
                 }
            return "";

         case VALUE_TYPE_TIME:
            return "";
        }
     }
  };

class MACD3_left1
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_MAIN;
      shift = 1;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD3_left2
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_MAIN;
      shift = 2;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD3_right1
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_SIGNAL;
      shift = 1;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD3_right2
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_SIGNAL;
      shift = 2;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD4_left1
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_MAIN;
      shift = 1;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD4_left2
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_MAIN;
      shift = 2;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD4_right1
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_SIGNAL;
      shift = 1;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };
class MACD4_right2
  {
   string            symbol;
   int               timeframe;
   int               fast_ema_period;
   int               slow_ema_period;
   int               signal_period;
   int               applied_price;
   int               mode;
   int               shift;

public:
   void              init()
     {
       symbol = NULL;
      timeframe = 0;
      fast_ema_period = 9;
      slow_ema_period = 29;
      signal_period = 12;
      applied_price = PRICE_CLOSE;
      mode = MODE_SIGNAL;
      shift = 2;
     }

   double            calc()
     {
      double result = iMACD(symbol,timeframe,fast_ema_period,slow_ema_period,signal_period, applied_price, mode, shift);
      return result;
     }

  };class Task0 : public Task
  {
      int               sleep_seconds;
   bool              sleep_tester_normal;
   bool              sleep_tester_visual;
public:
                     Task0(string name):Task(name)
     {
         sleep_seconds = 7;
      sleep_tester_normal = True;
      sleep_tester_visual = True;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      if(MQLInfoInteger(MQL_TESTER) == false)
        {
         Sleep(sleep_seconds*1000);
        }
      else
        {
         if(
            (sleep_tester_visual == true && MQLInfoInteger(MQL_VISUAL_MODE) == true)
            || (sleep_tester_normal == true && MQLInfoInteger(MQL_VISUAL_MODE) == false)
         )
           {
            SleepEx(sleep_seconds*1000,false);
           }
        }
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level) {
      
   }
   
  };
class Task1 : public Task
  {
   
public:
                     Task1(string name):Task(name)
     {
         
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      RSI1_left rsi1_left;
   rsi1_left.init();
   double valueRSI1_left = rsi1_left.calc();
      Value1_right value1_right;
   value1_right.init();
   double valueValue1_right = value1_right.calc();

      if(valueRSI1_left > valueValue1_right)
        {
         printf("task"+block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level) {
      
   }
   
  };
class Task2 : public Task
  {
   
public:
                     Task2(string name):Task(name)
     {
         
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      RSI2_left rsi2_left;
   rsi2_left.init();
   double valueRSI2_left = rsi2_left.calc();
      Value2_right value2_right;
   value2_right.init();
   double valueValue2_right = value2_right.calc();

      if(valueRSI2_left < valueValue2_right)
        {
         printf("task"+block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level) {
      
   }
   
  };
class Task3 : public Task
  {
   
public:
                     Task3(string name):Task(name)
     {
         
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

         MACD3_left1 macd3_left1;
   macd3_left1.init();
   double valueMACD3_left1 = macd3_left1.calc();
         MACD3_left2 macd3_left2;
   macd3_left2.init();
   double valueMACD3_left2 = macd3_left2.calc();
         MACD3_right1 macd3_right1;
   macd3_right1.init();
   double valueMACD3_right1 = macd3_right1.calc();
         MACD3_right2 macd3_right2;
   macd3_right2.init();
   double valueMACD3_right2 = macd3_right2.calc();
      
      if(valueMACD3_left1 < valueMACD3_right1 && valueMACD3_left2 > valueMACD3_right2)
        {
         printf("task"+block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level) {
      
   }
   
  };
class Task4 : public Task
  {
   
public:
                     Task4(string name):Task(name)
     {
         
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

         MACD4_left1 macd4_left1;
   macd4_left1.init();
   double valueMACD4_left1 = macd4_left1.calc();
         MACD4_left2 macd4_left2;
   macd4_left2.init();
   double valueMACD4_left2 = macd4_left2.calc();
         MACD4_right1 macd4_right1;
   macd4_right1.init();
   double valueMACD4_right1 = macd4_right1.calc();
         MACD4_right2 macd4_right2;
   macd4_right2.init();
   double valueMACD4_right2 = macd4_right2.calc();
      
      if(valueMACD4_left1 > valueMACD4_right1 && valueMACD4_left2 < valueMACD4_right2)
        {
         printf("task"+block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level) {
      
   }
   
  };
class Task5 : public Task
  {
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
   double            mstoploss;
   double            mtakeprofit;
   bool              initialized;

public:
                     Task5(string name):Task(name)
     {
         symbol = NULL;
      cmd = OP_SELL;
      volume = 0.1;
      price = Bid;
      slippage = 4;
      stoploss = 50;
      takeprofit = 10;
      comment = 0;
      magic = 10203015;
      expiration = 0;
      arrow_color = Red;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
     calc();
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
   virtual void      reset(int level) {
      
   }
   private:
   //does needed calculations
   void              calc()
     {
      if(MathAbs(takeprofit+stoploss)*10<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      mstoploss=NormalizeDouble(stoploss*Point*10,Digits);
      mtakeprofit=NormalizeDouble(takeprofit*Point*10,Digits);
      if(cmd==OP_BUY)
        {
         price = Ask;
         slPrice = price-mstoploss;
         tpPrice = price+mtakeprofit;
        }
      else
         if(cmd==OP_SELL)
           {
            price = Bid;
            slPrice = price+mstoploss;
            tpPrice = price-mtakeprofit;
           }

      initialized = true;
     }

  };
class Task6 : public Task
  {
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
   double            mstoploss;
   double            mtakeprofit;
   bool              initialized;

public:
                     Task6(string name):Task(name)
     {
         symbol = NULL;
      cmd = OP_BUY;
      volume = 0.1;
      price = Ask;
      slippage = 4;
      stoploss = 50;
      takeprofit = 10;
      comment = 0;
      magic = 10203015;
      expiration = 0;
      arrow_color = Blue;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
     calc();
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
   virtual void      reset(int level) {
      
   }
   private:
   //does needed calculations
   void              calc()
     {
      if(MathAbs(takeprofit+stoploss)*10<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      mstoploss=NormalizeDouble(stoploss*Point*10,Digits);
      mtakeprofit=NormalizeDouble(takeprofit*Point*10,Digits);
      if(cmd==OP_BUY)
        {
         price = Ask;
         slPrice = price-mstoploss;
         tpPrice = price+mtakeprofit;
        }
      else
         if(cmd==OP_SELL)
           {
            price = Bid;
            slPrice = price+mstoploss;
            tpPrice = price-mtakeprofit;
           }

      initialized = true;
     }

  };
class Block : BlockParent
  {


public:
   int               id;
   int               id_by_user;
   string            name;
   bool              enabled;


   int               next_true_history[];//dynamic, filled at runtime
   int               next_false_history[];//dynamic, filled at runtime
   int               prevs_true_history[];//dynamic, filled at runtime
   int               prevs_false_history[];//dynamic, filled at runtime

   Task              *task;



public:
                     Block()
     {

     }

   virtual void      next_true()
     {
      for(int i=0; i<ArraySize(nexts_true); i++)
         runBlockTick(id, ROUTE_1_PASSED, nexts_true[i]);//-1 : block id to block index
     }

   virtual void      next_false()
     {
      for(int i=0; i<ArraySize(nexts_false); i++)
         runBlockTick(id, ROUTE_2_PASSED, nexts_false[i]);
     }

   virtual void              run(int source_id, int source_result)
     {
      if(!enabled)
         return;
      addToHistory(source_id, source_result);
      current_source_id = source_id;
      task.run(id, this);

     };

   void              addToHistory(int source_id, int source_result)
     {
      if(true) //STest, this is to prevent excessive memory usage
         return;
      if(source_id<0)
         return;

      if(source_result == ROUTE_1_PASSED)
        {
         AddToArray(prevs_true_history, source_id);
        }
      else
         if(source_result == ROUTE_2_PASSED)
           {
            AddToArray(prevs_false_history, source_id);
           }
     }

   virtual void      onResult(int result)
     {
      if(result == ROUTE_1_PASSED)
         next_true();
      else
         if(result == ROUTE_2_PASSED)
            next_false();
     }

   virtual void              reset(int level)
     {
      task.reset(level);
     };

   void              populateNextsTrue(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(nexts_true, items[i]);
     }
   void              populateNextsFalse(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(nexts_false, items[i]);
     }
   void              populatePrevsTrue(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(prevs_true, items[i]);
     }
   void              populatePrevsFalse(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(prevs_false, items[i]);
     }

  };

class Block0 : public Block
  {
public:
                     Block0()
     {
      id = 0;
      id_by_user = 20;
      name = "delay";
      enabled = True;

      int mnexts_true[] = {1, 2};
      int mnexts_false[] = {};
      int mprevs_true[] = {};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task0(name);
     }
  };
class Block1 : public Block
  {
public:
                     Block1()
     {
      id = 1;
      id_by_user = 1;
      name = "condition_1_normal";
      enabled = True;

      int mnexts_true[] = {4};
      int mnexts_false[] = {};
      int mprevs_true[] = {0};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task1(name);
     }
  };
class Block2 : public Block
  {
public:
                     Block2()
     {
      id = 2;
      id_by_user = 1;
      name = "condition_1_normal";
      enabled = True;

      int mnexts_true[] = {3};
      int mnexts_false[] = {};
      int mprevs_true[] = {0};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task2(name);
     }
  };
class Block3 : public Block
  {
public:
                     Block3()
     {
      id = 3;
      id_by_user = 1;
      name = "condition_1_cross";
      enabled = True;

      int mnexts_true[] = {5};
      int mnexts_false[] = {};
      int mprevs_true[] = {2};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task3(name);
     }
  };
class Block4 : public Block
  {
public:
                     Block4()
     {
      id = 4;
      id_by_user = 1;
      name = "condition_1_cross";
      enabled = True;

      int mnexts_true[] = {6};
      int mnexts_false[] = {};
      int mprevs_true[] = {1};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task4(name);
     }
  };
class Block5 : public Block
  {
public:
                     Block5()
     {
      id = 5;
      id_by_user = 53;
      name = "Sell now";
      enabled = True;

      int mnexts_true[] = {};
      int mnexts_false[] = {};
      int mprevs_true[] = {3};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task5(name);
     }
  };
class Block6 : public Block
  {
public:
                     Block6()
     {
      id = 6;
      id_by_user = 50;
      name = "Buy now";
      enabled = True;

      int mnexts_true[] = {};
      int mnexts_false[] = {};
      int mprevs_true[] = {4};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task6(name);
     }
  };
Block *blocks_tick[];
string overriding_symbol = "";
int overriding_timeframe = -1;
template <typename T>
 void AddToArray(T& A[], T &value) {
 ArrayResize(A, ArraySize(A)+1);
 A[ArraySize(A)-1] = value;
 }template <typename T>
 void RemoveIndexFromArray(T& A[], int iPos) {
 int iLast;
 for(iLast = ArraySize(A) - 1; iPos < iLast; ++iPos)
 A[iPos] = A[iPos + 1];
 ArrayResize(A, iLast);
 }// Function to join two arrays into one
 void JoinArrays(const int& array1[], const int& array2[], int& arrayJoined[]) {
 int size1 = ArraySize(array1);
 int size2 = ArraySize(array2);
 int newSize = size1 + size2;
 ArrayCopy(arrayJoined, array1, 0, 0, size1);
 ArrayCopy(arrayJoined, array2, 0, size1, size2);
 }
// Check if all items in arrayB are in ArrayA
 bool areAllItemsPresent(int &arrayA[], int &arrayB[]) {
 for(int i = 0; i < ArraySize(arrayA); i++) {
 bool isPresent = false;
 for(int j = 0; j < ArraySize(arrayB); j++) {
 if(arrayA[i] == arrayB[j]) {
 isPresent = true;
 break;
 }
 }
 if(!isPresent) {
 return false;
 }
 } 
return true;
 }
void runBlockTick(int source_id, int source_result, int dest_id)
{
blocks_tick[dest_id].run(source_id, source_result);
}void addBlocksTick()
{
ArrayResize(blocks_tick, 7);
Block0 *block0 = new Block0();
Block1 *block1 = new Block1();
Block2 *block2 = new Block2();
Block3 *block3 = new Block3();
Block4 *block4 = new Block4();
Block5 *block5 = new Block5();
Block6 *block6 = new Block6();

blocks_tick[0] = block0;
blocks_tick[1] = block1;
blocks_tick[2] = block2;
blocks_tick[3] = block3;
blocks_tick[4] = block4;
blocks_tick[5] = block5;
blocks_tick[6] = block6;
  }
void resetBlocksTick(int level)
{
    for(int i=0; i<ArraySize(blocks_tick); i++){
        blocks_tick[i].reset(level);
    }
}string syncSymbolOverriding(string symbol) {
 return overriding_symbol == "" ? symbol : overriding_symbol;
}int syncTimeframeOverriding(int timeframe) {
 return overriding_timeframe == -1 ? timeframe : overriding_timeframe;
 }//stamp is like: "2023.04.15 18:25:40"
datetime TimeFromString(int time_mode, string stamp)
  {
   datetime t = 0;

   if(time_mode == TIME_SERVER)
      t = TimeCurrent();
   else
      if(time_mode == TIME_LOCAL)
         t = TimeLocal();
      else
         if(time_mode == TIME_GMT)
            t = TimeGMT();

   int stamplen = StringLen(stamp);

   if(stamplen < 9)
     {
      int thour    = TimeHour(t);
      int tminute  = TimeMinute(t);
      int tseconds = TimeSeconds(t);

      int hour   = (int)StringSubstr(stamp, 0, 2);
      int minute = (int)StringSubstr(stamp, 3, 2);
      int second = (int)StringSubstr(stamp, 6, 2);

      datetime t1 = (datetime)(t - (thour-hour)*3600 - (tminute - minute)*60 - (tseconds-second));

      return t1;
     }

   return StringToTime(stamp);
  }
//Considering each magic number is a 7 digit number like 2088100,
//I choose to take first two digits as group number.
int getGroupNumber (int magic){
   return (int)(magic/1000000);
}//This just checks if order is buy or sell
bool sameOrderType (int type[], int orderType){
   for (int i=0; i<ArraySize(type); i++)
      if (orderType==type[i])
         return true;
   return false;
}//72 is the number in magic 3rd and 4th
//digits that show it is opened by the expert
bool isAutomated (int magic){
   return MathMod((int)(magic/1000), 1000) == 72;
}
void ReverseList(int &arr[])
  {
   int size = ArraySize(arr);
   ArraySetAsSeries(arr, true);

   for(int i = 0; i < size / 2; i++)
     {
      int temp = arr[i];
      arr[i] = arr[size - 1 - i];
      arr[size - 1 - i] = temp;
     }
  }
#import "kernel32.dll"
bool SleepEx(int ms, bool bAlertable);
#import

int init(){
addBlocksTick();
}
void OnTimer(){

}
void OnTick(){
resetBlocksTick(RESET_LEVEL_TICK);runBlockTick(-1, -1, 0);
}
void OnTrade(){

}
void OnChartEvent(const int id,         // Event identifier
const long& lparam,   // Event parameter of long type
const double& dparam, // Event parameter of double type
const string& sparam  // Event parameter of string type
){

}
void deinit(const int reason){

}
