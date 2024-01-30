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
#define BLOCK_STATE_ENABLE 1
#define BLOCK_STATE_DISABLE 2
#define BLOCK_STATE_TOGGLE 3
#define SPREAD_BENCHMARK_AVERAGE 1
#define SPREAD_BENCHMARK_FIX 2
#define ORDER_BUY 1
#define ORDER_SELL 2
#define ORDER_BUY_PENDING 3
#define ORDER_SELL_PENDING 4
#define OPEN_AT_ASK 1
#define OPEN_AT_BID 2
#define OPEN_AT_MID 3
#define OPEN_AT_CUSTOM_PRICE 4
#define LOOK_UP_RUNNING_THEN_HISTORY 0
#define LOOK_UP_RUNNING_ONLY 1
#define LOOK_UP_HISTORY_ONLY 2
#define TPSL_MODE_NO_TP 1
#define TPSL_MODE_NO_SL 2
#define TPSL_MODE_FIXED_PIPS 3
#define TPSL_MODE_PERCENT_OF_PRICE 4
#define TPSL_MODE_PERCENT_FROM_SL 5
#define TPSL_MODE_PERCENT_FROM_TP 6
#define TPSL_MODE_CUSTOM_PRICE_LEVEL 7
#define TPSL_MODE_CUSTOM_PIPS 8
#define TPSL_MODE_CUSTOM_PRICE_FRACTION 9
#define MONEY_MANAGEMENT_FIXED_VOLUME 1
#define MONEY_MANAGEMENT_PERCENT_OF_EQUITY 2
#define MONEY_MANAGEMENT_PERCENT_OF_BALANCE 3
#define MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN 4
#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY 5
#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE 6
#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN 7
#define MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY 8
#define MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE 9
#define MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN 10
#define MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY 11
#define MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES 12
#define MONEY_MANAGEMENT_BETTING_MARTINGLE_PAROLI 13
#define MONEY_MANAGEMENT_CUSTOM_VALUE 14
#define POINT_FORMAT_RULES "0.001=0.01,0.00001=0.0001,0.000001=0.0001"
#define ON_PROFIT_MODE_FIXED_VALUE 1
#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_SL 2
#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_TP 3
#define BEP_OFFSET_MODE_NONE 1
#define BEP_OFFSET_MODE_PIPS_OFFSET 2
#define TRAILING_STOP_MODE_PIP "fixed"
#define TRAILING_STOP_MODE_MULTIPLE_LEVELS "multiple"
#define TRAILING_STOP_MODE_MONEY "money"
#define TRAILING_STOP_MODE_PERCENT_OF_OPPOSITE_STOP "percentTP"
#define TRAILING_STOP_MODE_PERCENT_OF_PROFIT "percentProfit"
#define TRAILING_STOP_MODE_CUSTOM_LEVEL "dynamic"
#define TRAILING_STOP_MODE_CUSTOM_PIPS "dynamicSize"
#define TRAILING_STOP_MODE_CUSTOM_PRICE_FRACTION "dynamicDigits"
#define TRAILING_START_MODE_OFF "none"
#define TRAILING_START_MODE_OPEN_PRICE "zero"
#define TRAILING_START_MODE_PIPS_OFFSET "fixed"
#define TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP "percentTS"
#define TRAILING_START_MODE_PERCENT_OF_OPPOSITE_STOP "percentTP"
#define TRAILING_START_MODE_PERCENT_OF_STOP "percentSL"
#define TRAILING_START_MODE_CUSTOM_PIPS "function"
#define TRAILING_START_MODE_CUSTOM_PRICE_FRACTION "functionFraction"
#define TRAILING_STEP_MODE_PIPS "fixed"
#define TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP "percentTS"
#define TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE "none"
#define TRAILING_OPPOSITE_STOP_MODE_CLEAR_STOP "clear"
#define TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE "fixed"
#define TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP "percentTS"
#define TRAILING_OPPOSITE_STOP_MODE_CUSTOM "function"
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

class RSI0tsm_cl
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
      symbol = 14;
      timeframe = PRICE_CLOSE;
      period = PRICE_CLOSE;
      applied_price = PRICE_CLOSE;
      shift = PRICE_CLOSE;
      buy_threshold = PRICE_CLOSE;
      sell_threshold = PRICE_CLOSE;
     }

   double            calc()
     {
      double result = iRSI(symbol,timeframe,period, applied_price, shift);
      return result;
     }

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
   //defined by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   int               TrailWhat;
   int               TrailingReferencePrice;
   string            TrailingStopMode;
   double            tStopPips;
   double            tStopMoney;
   string            tStopMultiple;
   double            tStopPercentTP;
   double            tStopPercentProfit;
   string            TrailingStepMode;
   double            tStepPips;
   double            tStepPercentTS;
   string            TrailingStartMode;
   double            tStartPips;
   double            tStartPercentTS;
   double            tStartPercentSL;
   double            tStartPercentTP;
   string            TrailingTPmode;
   double            tTPpips;
   double            tTPpercentTS;
   color             LevelColor;

   //defined by system
   string            msymbol;
public:
                     Task0(string name):Task(name)
     {
         symbol = NULL;//STest, no lists yet, also all is not suported yet.
      group_mode = ORDER_GROUP_MODE_NONE;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.

      TrailWhat = 1;
      TrailingReferencePrice = 0;
      TrailingStopMode = TRAILING_STOP_MODE_CUSTOM_LEVEL;
      tStopPips = 40.0;
      tStopMoney = 10.0;
      tStopMultiple = "20/5, 30/10";
      tStopPercentTP = 100.0;
      tStopPercentProfit = 50.0;
      TrailingStepMode = TRAILING_STEP_MODE_PIPS;
      tStepPips = 1;
      tStepPercentTS = 10.0;
      TrailingStartMode = TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP;
      tStartPips = 10.0;
      tStartPercentTS = 100.0;
      tStartPercentSL = 10.0;
      tStartPercentTP = 10.0;
      TrailingTPmode = TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE;
      tTPpips = 20.0;
      tTPpercentTS = 200.0;
      LevelColor = clrDeepPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
            msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      for(int m = OrdersTotal() ; m >= 0 ; m--)
        {
         if(OrderSelect(m, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;

            string symbol     = OrderSymbol();//STest, conflict with symbol in filed (?)
            double ask        = SymbolInfoDouble(symbol, SYMBOL_ASK);
            double bid        = SymbolInfoDouble(symbol, SYMBOL_BID);
            double stopslevel = (double)SymbolInfoInteger(symbol, SYMBOL_TRADE_STOPS_LEVEL);
            int digits        = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
            int polarity      = 1;   // 1 = buy, -1 = sell
            double askbid     = ask; // could be Ask or Bid
            double bidask     = bid; // the opposite of askbid
            double sltp       = 0;   // could be SL or TP
            double tpsl       = 0;   // the opposite of sltp
            double fsl        = 0;   // Freeze Level
            double limit      = 0;
            double t_stop     = 0;   // trailing STOP
            double t_start    = 0;   // trailing START
            double t_step     = 0;   // trailing STEP
            double t_opp      = 0;   // trailing Opposite (TP when trailing SL or SL when trailing TP)

            if(TrailWhat > 0)
              {
               sltp = OrderStopLoss();
               tpsl = OrderTakeProfit();
              }
            else
              {
               sltp = OrderTakeProfit();
               tpsl = OrderStopLoss();
              }

            if(OrderType() == 0)
              {
               polarity = 1;

               if(TrailingReferencePrice == 1)
                 {
                  askbid = bid;
                  bidask = ask;
                 }
              }
            else
               if(OrderType() == 1)
                 {
                  polarity = -1;
                  askbid   = bid;
                  bidask   = ask;

                  if(TrailingReferencePrice == 1)
                    {
                     askbid = ask;
                     bidask = bid;
                    }
                 }

            if(TrailingReferencePrice == 2)
              {
               askbid = (ask + bid) / 2;
               bidask = (ask + bid) / 2;
              }

            // Trailing Stop Size
            if(TrailingStopMode == TRAILING_STOP_MODE_PIP)
              {
               t_stop = toDigits(tStopPips, symbol);
              }
            else
               if(TrailingStopMode == TRAILING_STOP_MODE_PERCENT_OF_OPPOSITE_STOP)
                 {
                  t_stop = (MathAbs(OrderOpenPrice() - tpsl)) * (tStopPercentTP / 100);
                 }
               else
                  if(TrailingStopMode == TRAILING_STOP_MODE_PERCENT_OF_PROFIT)
                    {
                     t_stop = (MathAbs(askbid - OrderOpenPrice())) * (tStopPercentProfit / 100);
                    }
                  else
                     if(TrailingStopMode == TRAILING_STOP_MODE_CUSTOM_PIPS)
                       {
                        //t_stop = toDigits(_ftStop_(), symbol);
                       }
                     else
                        if(TrailingStopMode == TRAILING_STOP_MODE_CUSTOM_PRICE_FRACTION)
                          {
                           //t_stop = _ftDigits_();
                          }
                        else
                           if(TrailingStopMode == TRAILING_STOP_MODE_CUSTOM_LEVEL)
                             {
                                RSI0tsm_cl rsi0tsm_cl;
   rsi0tsm_cl.init();
   double valueRSI0tsm_cl = rsi0tsm_cl.calc();
                                t_stop = valueRSI0tsm_cl;
    
                                t_stop = (polarity == 1) ? ask - t_stop : t_stop - bid;
                             }
                           else
                              if(TrailingStopMode == TRAILING_STOP_MODE_MONEY)
                                {
                                 t_stop = tStopMoney;

                                 double lotsize   = SymbolInfoDouble(symbol, SYMBOL_TRADE_CONTRACT_SIZE);
                                 double tickvalue = (SymbolInfoDouble(symbol, SYMBOL_TRADE_TICK_VALUE) / SymbolInfoDouble(symbol, SYMBOL_TRADE_TICK_SIZE)) * SymbolInfoDouble(symbol, SYMBOL_POINT);
                                 t_stop = t_stop / (OrderLots() * PipValue(symbol));
                                 // TODO: remove this toDigits(), the calculation should be made directly into digits
                                 t_stop = toDigits(t_stop / tickvalue, symbol);
                                }

            // Trailing Start Level
            if(TrailingStartMode == TRAILING_START_MODE_OFF)
              {
               t_start = -EMPTY_VALUE;
              }
            else
               if(TrailingStartMode == TRAILING_START_MODE_OPEN_PRICE)
                 {
                  t_start = 0;
                 }
               else
                  if(TrailingStartMode == TRAILING_START_MODE_PIPS_OFFSET)
                    {
                     t_start = toDigits(tStartPips, symbol);
                    }
                  else
                     if(TrailingStartMode == TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP)
                       {
                        t_start = t_stop * (tStartPercentTS / 100);
                       }
                     else
                        if(TrailingStartMode == TRAILING_START_MODE_PERCENT_OF_OPPOSITE_STOP)
                          {
                           t_start = (MathAbs(OrderOpenPrice() - tpsl)) * (tStartPercentTP / 100);
                          }
                        else
                           if(TrailingStartMode == TRAILING_START_MODE_PERCENT_OF_STOP)
                             {
                              t_start = (MathAbs(OrderOpenPrice() - sltp)) * (tStartPercentSL / 100);
                             }
                           else
                              if(TrailingStartMode == TRAILING_START_MODE_CUSTOM_PIPS)
                                {
                                 //t_start = toDigits(_ftStart_(), symbol);
                                }
                              else
                                 if(TrailingStartMode == TRAILING_START_MODE_CUSTOM_PRICE_FRACTION)
                                   {
                                    //t_start = _ftStartFraction_();
                                   }

            // Trailing Step Size
            if(TrailingStepMode == TRAILING_STEP_MODE_PIPS)
              {
               t_step = toDigits(tStepPips, symbol);
              }
            else
               if(TrailingStepMode == TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP)
                 {
                  t_step = t_stop * (tStepPercentTS / 100);
                 }

            // Trailing Opposite Size
            if(TrailingTPmode == TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE)
              {
               t_opp = tpsl;
              }
            else
               if(TrailingTPmode == TRAILING_OPPOSITE_STOP_MODE_CLEAR_STOP)
                 {
                  t_opp = 0;
                 }
               else
                  if(TrailingTPmode == TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE)
                    {
                     t_opp = TrailWhat * (OrderOpenPrice() + (polarity * toDigits(tTPpips, symbol)));
                    }
                  else
                     if(TrailingTPmode == TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP)
                       {
                        t_opp = TrailWhat * (OrderOpenPrice() + (polarity * toDigits(t_stop * (tTPpercentTS / 100), symbol)));
                       }
                     else
                        if(TrailingTPmode == TRAILING_OPPOSITE_STOP_MODE_CUSTOM)
                          {
                           //t_opp = _ftTP_();
                          }

            // this mode is located here because it overrides Start, Stop and Step
            // the idea here is to use Start as target profits
            if(TrailingStopMode == TRAILING_STOP_MODE_MULTIPLE_LEVELS)
              {
               bool next = false;
               string tmp1[];
               string tmp2[];

               StringExplode(",", tStopMultiple, tmp1);

               for(int i = ArraySize(tmp1)-1; i >= 0; i--)
                 {
                  StringExplode("/", tmp1[i], tmp2);

                  if(ArraySize(tmp2) != 2)
                    {
                     continue;
                    }

                  // trailing start will be used as the treshold level
                  double new_start = toDigits(StringToDouble(StringTrim(tmp2[0])), symbol);

                  // the regular trailing start is bigger than this level -> skip
                  if(new_start < t_start)
                    {
                     continue;
                    }

                  // check whether the current price<->op distance is bigger than some of the desired levels
                  double diff = NormalizeDouble(askbid - OrderOpenPrice(), digits);

                  if(polarity * TrailWhat * diff >= new_start)
                    {
                     // and setup parameters so SL will be moved
                     t_start = new_start;
                     t_stop  = polarity * TrailWhat * diff - toDigits(StringToDouble(StringTrim(tmp2[1])), symbol);

                     next = true;
                     break;
                    }
                 }

               if(next == false)
                 {
                  continue;
                 }
              }

            stopslevel   = stopslevel * SymbolInfoDouble(symbol, SYMBOL_POINT);

            if(t_stop <= 0)
              {
               continue;
              }

            if(OrderType() == 0 && TrailWhat * (askbid - OrderOpenPrice()) > t_start)
              {
               if((TrailWhat * (askbid - sltp) >= t_stop + t_step) || sltp == 0)
                 {
                  // consider minimum stop
                  fsl   = MathAbs(askbid - t_stop);
                  limit = bidask - stopslevel * TrailWhat;

                  if(fsl > limit)
                    {
                     fsl = limit;
                    }

                  if(TrailWhat == 1)  // trail SL
                    {
                     if(sltp == 0 || sltp < fsl)
                       {
                        OrderModify(OrderTicket(), OrderOpenPrice(), askbid - t_stop, t_opp, 0, LevelColor);
                       }
                    }
                  else   // trail TP
                    {
                     if(sltp == 0 || sltp > fsl)
                       {
                        OrderModify(OrderTicket(), OrderOpenPrice(), t_opp, askbid + t_stop, 0, LevelColor);
                       }
                    }
                 }
              }
            else
               if(OrderType() == 1 && TrailWhat * (OrderOpenPrice() - askbid) > t_start)
                 {
                  if((TrailWhat * (sltp - askbid) >= t_stop + t_step) || sltp == 0)
                    {
                     // consider minimum stop
                     fsl   = MathAbs(askbid + t_stop);
                     limit = bidask + stopslevel * TrailWhat;

                     if(fsl < limit)
                       {
                        fsl = limit;
                       }

                     if(TrailWhat == 1)
                       {
                        // trail SL
                        if(sltp == 0 || sltp > fsl)
                          {
                           OrderModify(OrderTicket(), OrderOpenPrice(), askbid + t_stop, t_opp, 0, LevelColor);
                          }
                       }
                     else
                       {
                        // trail TP
                        if(sltp == 0 || sltp < fsl)
                          {
                           OrderModify(OrderTicket(), OrderOpenPrice(), t_opp, askbid - t_stop, 0, LevelColor);
                          }
                       }
                    }
                 }
           }
        }
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level) {
      
   }
   bool              filterGeneral()
     {
      bool con1 = (msymbol==NULL && OrderSymbol()==Symbol()) || msymbol==OrderSymbol();
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
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
   //values set by user
   string            symbol;
   int               group;
   int               order_type;
   int               money_management;
   double            how_much_volume;
   double            volume_upper_limit;
   int               open_at_price;
   double            price_offset;
   bool              price_offset_as_pip;
   int               slippage;
   int               stop_loss_mode;
   int               take_profit_mode;
   double            stoploss;
   double            takeprofit;
   string            comment;
   int               magic;
   datetime          expiration;
   color             arrow_color;
   //values set by system
   int               cmd;
   double            price;
   double            volume;
   int               ticket;
   double            slPrice;
   double            tpPrice;
   double            mstoploss;
   double            mtakeprofit;
   bool              initialized;
   string            msymbol;
   //martingale inputs
   int               look_up_on;
   double            martingale_init_vol;
   double            martingale_multiply_on_loss;
   double            martingale_multiply_on_profit;
   double            martingale_addlots_on_loss;
   double            martingale_addlots_on_profit;
   double            martingale_reset_on_n_losses;
   double            martingale_reset_on_n_profits;
   int               type[];
public:
                     Task5(string name):Task(name)
     {
         symbol = NULL;
      group = 11;
      order_type = ORDER_BUY_PENDING;
      money_management = MONEY_MANAGEMENT_BETTING_MARTINGLE_PAROLI;
      how_much_volume = 35;
      volume_upper_limit = 10;
      open_at_price = OPEN_AT_ASK;
      price_offset = 10;
      price_offset_as_pip = True;

      slippage = 4;
      stoploss = 20;
      takeprofit = 20;
      take_profit_mode = TPSL_MODE_FIXED_PIPS;
      stop_loss_mode = TPSL_MODE_FIXED_PIPS;
      comment = "";
      expiration = 0;
      arrow_color = clrYellow;

      //martingale
      look_up_on = LOOK_UP_RUNNING_ONLY;
      int mtype[] = {0, 1};//This doesn't seem to be an input. So this remains static forever.
      ArrayCopy(type, mtype, 0, 0, WHOLE_ARRAY);
      martingale_init_vol = 0.1;
      martingale_multiply_on_loss = 0;
      martingale_multiply_on_profit = 0;
      martingale_addlots_on_loss = 0.1;
      martingale_addlots_on_profit = 0.1;
      martingale_reset_on_n_losses = 5;
      martingale_reset_on_n_profits = 5;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
            Task::run(block_id, block);

      msymbol = overriding_symbol=="" ? Symbol() : overriding_symbol;

      calc();
      if(!initialized)
        {
         printf("Not initialized");
         //block.onResult(ROUTE_2_PASSED);
         return;
        }
      ticket=OrderSend(msymbol,cmd,volume,price,slippage,slPrice,tpPrice,comment,magic,expiration,arrow_color);
      if(ticket == ERR_NO_ERROR)
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
   private:
   //does needed calculations
   void              calc()
     {
      fitGroup();
      buildMagic();
      if(order_type==ORDER_BUY)
        {
         cmd = OP_BUY;
        }
      else
         if(order_type==ORDER_SELL)
           {
            cmd = OP_SELL;
           }
         else
            if(order_type==ORDER_BUY_PENDING)
              {
               if(price_offset>=0)
                  cmd = OP_BUYSTOP;
               else
                  cmd = OP_BUYLIMIT;
              }
            else
               if(order_type==ORDER_SELL_PENDING)
                 {
                  if(price_offset>=0)
                     cmd = OP_SELLSTOP;
                  else
                     cmd = OP_SELLLIMIT;
                 }

      calcVolume();
      calc_entry_price();
      if(cmd==OP_BUY || cmd==OP_BUYLIMIT ||cmd==OP_BUYSTOP)
        {
         calc_tp_buy();
         calc_sl_buy();
        }
      else
         if(cmd==OP_SELL || cmd==OP_SELLLIMIT || cmd==OP_SELLSTOP)
           {
            calc_tp_sell();
            calc_sl_sell();
           }

      if(MathAbs(tpPrice-slPrice)/Point()<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      initialized = true;
     }

   void              calc_entry_price()
     {
      if(cmd==OP_BUY)
        {
         price = Ask;
        }
      else
         if(cmd==OP_SELL)
           {
            price = Bid;
           }
         else
           {
            switch(open_at_price)
              {
               case OPEN_AT_ASK:
                  price = SymbolInfoDouble(msymbol, SYMBOL_ASK);
                  break;
               case OPEN_AT_BID:
                  price = SymbolInfoDouble(msymbol, SYMBOL_BID);
                  break;
               case OPEN_AT_MID:
                  price = (SymbolInfoDouble(msymbol, SYMBOL_ASK)+SymbolInfoDouble(msymbol, SYMBOL_BID))/2;
                  break;
               case OPEN_AT_CUSTOM_PRICE:
                  RSI1_left rsi1_left;
                  rsi1_left.init();
                  double valueRsi1_left = rsi1_left.calc();
                  price = valueRsi1_left;
                  break;
              }
           }


      double offset = price_offset;
      if(price_offset_as_pip)
         offset = price_offset * Point() * 10;

      if(order_type==ORDER_BUY_PENDING || order_type==ORDER_SELL_PENDING)
         price += offset;
     }

   ////////////////////////////////////////////////////////////

   void              calc_tp_buy()
     {
      switch(take_profit_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mtakeprofit = NormalizeDouble(takeprofit*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            tpPrice = price + mtakeprofit;
            break;
         case TPSL_MODE_NO_TP:
            tpPrice = 0;
            break;
        }
     }

   void              calc_sl_buy()
     {
      switch(stop_loss_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mstoploss = NormalizeDouble(stoploss*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            slPrice = price - mstoploss;
            break;
         case TPSL_MODE_NO_SL:
            slPrice = 0;
            break;
        }
     }

   void              calc_tp_sell()
     {
      switch(take_profit_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mtakeprofit = NormalizeDouble(takeprofit*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            tpPrice = price - mtakeprofit;
            break;
         case TPSL_MODE_NO_TP:
            tpPrice = 0;
            break;
        }
     }

   void              calc_sl_sell()
     {
      switch(stop_loss_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mstoploss = NormalizeDouble(stoploss*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            slPrice = price + mstoploss;
            break;
         case TPSL_MODE_NO_SL:
            slPrice = 0;
            break;
        }
     }

   void              calcVolume()
     {
      if(money_management == MONEY_MANAGEMENT_FIXED_VOLUME)
        {
         volume = DynamicLots(msymbol, money_management, how_much_volume);
        }
      else
         if(money_management == MONEY_MANAGEMENT_PERCENT_OF_EQUITY)
           {
            volume = DynamicLots(msymbol, money_management, how_much_volume);
           }
         else
            if(money_management == MONEY_MANAGEMENT_PERCENT_OF_BALANCE)
              {
               //lots = DynamicLots(Symbol, money_management, VolumeBlockPercent);
              }
            else
               if(money_management == MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN)
                 {
                  //lots = DynamicLots(Symbol, money_management, VolumeBlockPercent);
                 }
               else
                  if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY)
                    {
                     //lots = DynamicLots(Symbol, money_management, VolumePercent);
                    }
                  else
                     if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE)
                       {
                        //lots = DynamicLots(Symbol, money_management, VolumePercent);
                       }
                     else
                        if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN)
                          {
                           //lots = DynamicLots(Symbol, money_management, VolumePercent);
                          }
                        else
                           if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY)
                             {
                              //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                             }
                           else
                              if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE)
                                {
                                 //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                                }
                              else
                                 if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN)
                                   {
                                    //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                                   }
                                 else
                                    if(money_management == MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY)
                                      {
                                       //lots = DynamicLots(Symbol, money_management, VolumeSizeRisk, pre_sl_pips);
                                      }
                                    else
                                       if(money_management == MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES)
                                         {
                                          //lots = DynamicLots(Symbol, money_management, FixedRatioUnitSize, FixedRatioDelta);
                                         }
                                       else
                                          if(money_management == MONEY_MANAGEMENT_BETTING_MARTINGLE_PAROLI)
                                            {
                                             volume = BetMartingale(msymbol, look_up_on, group, type, martingale_init_vol, martingale_multiply_on_loss, martingale_multiply_on_profit, martingale_addlots_on_loss, martingale_addlots_on_profit, martingale_reset_on_n_losses, martingale_reset_on_n_profits);
                                            }
                                          else
                                             if(money_management == MONEY_MANAGEMENT_CUSTOM_VALUE)
                                               {
                                                //lots = _dVolumeSize_();
                                               }


      if(volume_upper_limit>0 && volume>volume_upper_limit)
         volume = volume_upper_limit;
     }

   void              fitGroup()
     {
      //STest, take care of group number rules later
      if(group<11)
         group = 11;
      if(group>99)
         group = 99;
     }

   void              buildMagic()
     {
         magic = StrToInteger(group + "72" + "000"); //72 shows it's automated (opened by the expert).
     }
  };
class Task6 : public Task
  {
   
public:
                     Task6(string name):Task(name)
     {
         
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level) {
      
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
      name = "trailing_stop_each_trade";
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
      name = "buy_sell";
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
      name = "pass";
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
Block *blocks_init[];
Block *blocks_timer[];
Block *blocks_tick[];
Block *blocks_trade[];
Block *blocks_chart[];
Block *blocks_deinit[];
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
   return (int)(magic/100000);
}//This just checks if order is buy or sell
bool sameOrderType (int type[], int orderType){
   for (int i=0; i<ArraySize(type); i++)
      if (orderType==type[i])
         return true;
   return false;
}//72 is the number in magic 3rd and 4th
//digits that show it is opened by the expert
bool isAutomated (int magic){
   return MathMod((int)(magic/1000), 100) == 72;
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

bool DeleteOrder(ulong ticket, color arrowcolor=clrNONE)
  {
   bool success=false;
   if(!OrderSelect((int)ticket,SELECT_BY_TICKET,MODE_TRADES))
     {
      return(false);
     }

   while(true)
     {
      //-- wait if needed -----------------------------------------------
      WaitTradeContextIfBusy();
      //-- delete -------------------------------------------------------
      success=OrderDelete((int)ticket,arrowcolor);
      //-- error check --------------------------------------------------
      int erraction=CheckForTradingError(GetLastError(), "Deleting order #"+(string)ticket+" error");
      switch(erraction)
        {
         case 0:
            break;    // no error
         case 1:
            continue; // overcomable error
         case 2:
            break;    // fatal error
        }
      break;
     }
   return(false);
  }

void WaitTradeContextIfBusy()
  {
   if(IsTradeContextBusy())
     {
      while(true)
        {
         Sleep(1);
         if(!IsTradeContextBusy())
           {
            RefreshRates();
            break;
           }
        }
     }
   return;
  }
int CheckForTradingError(int error_code=-1, string msg_prefix="")
  {
// return 0 -> no error
// return 1 -> overcomable error
// return 2 -> fatal error

   if(error_code<0)
     {
      error_code=GetLastError();
     }

   int retval=0;
   static int tryouts=0;

//-- error check -----------------------------------------------------
   switch(error_code)
     {
      //-- no error
      case 0:
         retval=0;
         break;
      //-- overcomable errors
      case 1: // No error returned
         RefreshRates();
         retval=1;
         break;
      case 4: //ERR_SERVER_BUSY
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         Sleep(1000);
         RefreshRates();
         retval=1;
         break;
      case 6: //ERR_NO_CONNECTION
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         while(!IsConnected())
           {
            Sleep(100);
           }
         while(IsTradeContextBusy())
           {
            Sleep(50);
           }
         RefreshRates();
         retval=1;
         break;
      case 128: //ERR_TRADE_TIMEOUT
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         RefreshRates();
         retval=1;
         break;
      case 129: //ERR_INVALID_PRICE
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         if(!IsTesting())
           {
            while(RefreshRates()==false)
              {
               Sleep(1);
              }
           }
         retval=1;
         break;
      case 130: //ERR_INVALID_STOPS
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Waiting for a new tick to retry.."));
           }
         if(!IsTesting())
           {
            while(RefreshRates()==false)
              {
               Sleep(1);
              }
           }
         retval=1;
         break;
      case 135: //ERR_PRICE_CHANGED
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Waiting for a new tick to retry.."));
           }
         if(!IsTesting())
           {
            while(RefreshRates()==false)
              {
               Sleep(1);
              }
           }
         retval=1;
         break;
      case 136: //ERR_OFF_QUOTES
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Waiting for a new tick to retry.."));
           }
         if(!IsTesting())
           {
            while(RefreshRates()==false)
              {
               Sleep(1);
              }
           }
         retval=1;
         break;
      case 137: //ERR_BROKER_BUSY
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         Sleep(1000);
         retval=1;
         break;
      case 138: //ERR_REQUOTE
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Waiting for a new tick to retry.."));
           }
         if(!IsTesting())
           {
            while(RefreshRates()==false)
              {
               Sleep(1);
              }
           }
         retval=1;
         break;
      case 142: //This code should be processed in the same way as error 128.
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         RefreshRates();
         retval=1;
         break;
      case 143: //This code should be processed in the same way as error 128.
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         RefreshRates();
         retval=1;
         break;
      /*case 145: //ERR_TRADE_MODIFY_DENIED
         if (msg_prefix!="") {Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Waiting for a new tick to retry.."));}
         while(RefreshRates()==false) {Sleep(1);}
         return(1);
      */
      case 146: //ERR_TRADE_CONTEXT_BUSY
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code),". Retrying.."));
           }
         while(IsTradeContextBusy())
           {
            Sleep(50);
           }
         RefreshRates();
         retval=1;
         break;
      //-- critical errors
      default:
         if(msg_prefix!="")
           {
            Print(StringConcatenate(msg_prefix,": ",ErrorMessage(error_code)));
           }
         retval=2;
         break;
     }

   if(retval==0)
     {
      tryouts=0;
     }
   else
      if(retval==1)
        {
         tryouts++;
         if(tryouts>=10)
           {
            tryouts=0;
            retval=2;
           }
         else
           {
            Print("retry #"+(string)tryouts+" of 10");
           }
        }

   return(retval);
  }
string ErrorMessage(int error_code=-1)
  {
   string e = "";

   if(error_code < 0)
     {
      error_code = GetLastError();
     }

   switch(error_code)
     {
      //-- codes returned from trade server
      case 0:
         return("");
      case 1:
         e = "No error returned";
         break;
      case 2:
         e = "Common error";
         break;
      case 3:
         e = "Invalid trade parameters";
         break;
      case 4:
         e = "Trade server is busy";
         break;
      case 5:
         e = "Old version of the client terminal";
         break;
      case 6:
         e = "No connection with trade server";
         break;
      case 7:
         e = "Not enough rights";
         break;
      case 8:
         e = "Too frequent requests";
         break;
      case 9:
         e = "Malfunctional trade operation (never returned error)";
         break;
      case 64:
         e = "Account disabled";
         break;
      case 65:
         e = "Invalid account";
         break;
      case 128:
         e = "Trade timeout";
         break;
      case 129:
         e = "Invalid price";
         break;
      case 130:
         e = "Invalid Sl or TP";
         break;
      case 131:
         e = "Invalid trade volume";
         break;
      case 132:
         e = "Market is closed";
         break;
      case 133:
         e = "Trade is disabled";
         break;
      case 134:
         e = "Not enough money";
         break;
      case 135:
         e = "Price changed";
         break;
      case 136:
         e = "Off quotes";
         break;
      case 137:
         e = "Broker is busy (never returned error)";
         break;
      case 138:
         e = "Requote";
         break;
      case 139:
         e = "Order is locked";
         break;
      case 140:
         e = "Only long trades allowed";
         break;
      case 141:
         e = "Too many requests";
         break;
      case 145:
         e = "Modification denied because order too close to market";
         break;
      case 146:
         e = "Trade context is busy";
         break;
      case 147:
         e = "Expirations are denied by broker";
         break;
      case 148:
         e = "Amount of open and pending orders has reached the limit";
         break;
      case 149:
         e = "Hedging is prohibited";
         break;
      case 150:
         e = "Prohibited by FIFO rules";
         break;

      //-- mql4 errors
      case 4000:
         e = "No error";
         break;
      case 4001:
         e = "Wrong function pointer";
         break;
      case 4002:
         e = "Array index is out of range";
         break;
      case 4003:
         e = "No memory for function call stack";
         break;
      case 4004:
         e = "Recursive stack overflow";
         break;
      case 4005:
         e = "Not enough stack for parameter";
         break;
      case 4006:
         e = "No memory for parameter string";
         break;
      case 4007:
         e = "No memory for temp string";
         break;
      case 4008:
         e = "Not initialized string";
         break;
      case 4009:
         e = "Not initialized string in array";
         break;
      case 4010:
         e = "No memory for array string";
         break;
      case 4011:
         e = "Too long string";
         break;
      case 4012:
         e = "Remainder from zero divide";
         break;
      case 4013:
         e = "Zero divide";
         break;
      case 4014:
         e = "Unknown command";
         break;
      case 4015:
         e = "Wrong jump";
         break;
      case 4016:
         e = "Not initialized array";
         break;
      case 4017:
         e = "dll calls are not allowed";
         break;
      case 4018:
         e = "Cannot load library";
         break;
      case 4019:
         e = "Cannot call function";
         break;
      case 4020:
         e = "Expert function calls are not allowed";
         break;
      case 4021:
         e = "Not enough memory for temp string returned from function";
         break;
      case 4022:
         e = "System is busy";
         break;
      case 4050:
         e = "Invalid function parameters count";
         break;
      case 4051:
         e = "Invalid function parameter value";
         break;
      case 4052:
         e = "String function internal error";
         break;
      case 4053:
         e = "Some array error";
         break;
      case 4054:
         e = "Incorrect series array using";
         break;
      case 4055:
         e = "Custom indicator error";
         break;
      case 4056:
         e = "Arrays are incompatible";
         break;
      case 4057:
         e = "Global variables processing error";
         break;
      case 4058:
         e = "Global variable not found";
         break;
      case 4059:
         e = "Function is not allowed in testing mode";
         break;
      case 4060:
         e = "Function is not confirmed";
         break;
      case 4061:
         e = "Send mail error";
         break;
      case 4062:
         e = "String parameter expected";
         break;
      case 4063:
         e = "Integer parameter expected";
         break;
      case 4064:
         e = "Double parameter expected";
         break;
      case 4065:
         e = "Array as parameter expected";
         break;
      case 4066:
         e = "Requested history data in update state";
         break;
      case 4099:
         e = "End of file";
         break;
      case 4100:
         e = "Some file error";
         break;
      case 4101:
         e = "Wrong file name";
         break;
      case 4102:
         e = "Too many opened files";
         break;
      case 4103:
         e = "Cannot open file";
         break;
      case 4104:
         e = "Incompatible access to a file";
         break;
      case 4105:
         e = "No order selected";
         break;
      case 4106:
         e = "Unknown symbol";
         break;
      case 4107:
         e = "Invalid price parameter for trade function";
         break;
      case 4108:
         e = "Invalid ticket";
         break;
      case 4109:
         e = "Trade is not allowed in the expert properties";
         break;
      case 4110:
         e = "Longs are not allowed in the expert properties";
         break;
      case 4111:
         e = "Shorts are not allowed in the expert properties";
         break;

      //-- objects errors
      case 4200:
         e = "Object is already exist";
         break;
      case 4201:
         e = "Unknown object property";
         break;
      case 4202:
         e = "Object is not exist";
         break;
      case 4203:
         e = "Unknown object type";
         break;
      case 4204:
         e = "No object name";
         break;
      case 4205:
         e = "Object coordinates error";
         break;
      case 4206:
         e = "No specified subwindow";
         break;
      case 4207:
         e = "Graphical object error";
         break;
      case 4210:
         e = "Unknown chart property";
         break;
      case 4211:
         e = "Chart not found";
         break;
      case 4212:
         e = "Chart subwindow not found";
         break;
      case 4213:
         e = "Chart indicator not found";
         break;
      case 4220:
         e = "Symbol select error";
         break;
      case 4250:
         e = "Notification error";
         break;
      case 4251:
         e = "Notification parameter error";
         break;
      case 4252:
         e = "Notifications disabled";
         break;
      case 4253:
         e = "Notification send too frequent";
         break;

      //-- ftp errors
      case 4260:
         e = "FTP server is not specified";
         break;
      case 4261:
         e = "FTP login is not specified";
         break;
      case 4262:
         e = "FTP connection failed";
         break;
      case 4263:
         e = "FTP connection closed";
         break;
      case 4264:
         e = "FTP path not found on server";
         break;
      case 4265:
         e = "File not found in the MQL4\\Files directory to send on FTP server";
         break;
      case 4266:
         e = "Common error during FTP data transmission";
         break;

      //-- filesystem errors
      case 5001:
         e = "Too many opened files";
         break;
      case 5002:
         e = "Wrong file name";
         break;
      case 5003:
         e = "Too long file name";
         break;
      case 5004:
         e = "Cannot open file";
         break;
      case 5005:
         e = "Text file buffer allocation error";
         break;
      case 5006:
         e = "Cannot delete file";
         break;
      case 5007:
         e = "Invalid file handle (file closed or was not opened)";
         break;
      case 5008:
         e = "Wrong file handle (handle index is out of handle table)";
         break;
      case 5009:
         e = "File must be opened with FILE_WRITE flag";
         break;
      case 5010:
         e = "File must be opened with FILE_READ flag";
         break;
      case 5011:
         e = "File must be opened with FILE_BIN flag";
         break;
      case 5012:
         e = "File must be opened with FILE_TXT flag";
         break;
      case 5013:
         e = "File must be opened with FILE_TXT or FILE_CSV flag";
         break;
      case 5014:
         e = "File must be opened with FILE_CSV flag";
         break;
      case 5015:
         e = "File read error";
         break;
      case 5016:
         e = "File write error";
         break;
      case 5017:
         e = "String size must be specified for binary file";
         break;
      case 5018:
         e = "Incompatible file (for string arrays-TXT, for others-BIN)";
         break;
      case 5019:
         e = "File is directory, not file";
         break;
      case 5020:
         e = "File does not exist";
         break;
      case 5021:
         e = "File cannot be rewritten";
         break;
      case 5022:
         e = "Wrong directory name";
         break;
      case 5023:
         e = "Directory does not exist";
         break;
      case 5024:
         e = "Specified file is not directory";
         break;
      case 5025:
         e = "Cannot delete directory";
         break;
      case 5026:
         e = "Cannot clean directory";
         break;

      //-- other errors
      case 5027:
         e = "Array resize error";
         break;
      case 5028:
         e = "String resize error";
         break;
      case 5029:
         e = "Structure contains strings or dynamic arrays";
         break;

      //-- http request
      case 5200:
         e = "Invalid URL";
         break;
      case 5201:
         e = "Failed to connect to specified URL";
         break;
      case 5202:
         e = "Timeout exceeded";
         break;
      case 5203:
         e = "HTTP request failed";
         break;

      default:
         e = "Unknown error";
     }

   e = StringConcatenate(e, " (", error_code, ")");

   return e;
  }double BetMartingale(
   string symbol,
   int look_up_on,
   int group,
   int &type[],
   double initialLots,
   double multiplyOnLoss,
   double multiplyOnProfit,
   double addOnLoss,
   double addOnProfit,
   int resetOnLoss,
   int resetOnProfit
)
  {
   double info[];
   GetBetTradesInfo(info, symbol, look_up_on, group, type, true);

   double lots         = info[0];
   double profitOrLoss = info[1]; // 0 - unknown, 1 - profit, -1 - loss
   double consecutive  = info[2];

//-- Martingale Logic
   if(lots == 0)
     {
      lots = initialLots;
     }
   else
     {
      if(profitOrLoss == 1)
        {
         if(resetOnProfit > 0 && consecutive >= resetOnProfit)
           {
            lots = initialLots;
           }
         else
           {
            if(multiplyOnProfit <= 0)
              {
               multiplyOnProfit = 1;
              }

            lots = (lots * multiplyOnProfit) + addOnProfit;
           }
        }
      else
        {
         if(resetOnLoss > 0 && consecutive >= resetOnLoss)
           {
            lots = initialLots;
           }
         else
           {
            if(multiplyOnLoss <= 0)
              {
               multiplyOnLoss = 1;
              }

            lots = (lots * multiplyOnLoss) + addOnLoss;
           }
        }
     }

   return lots;
  }void GetBetTradesInfo(
   double &output[],
   string symbol,
   int look_up_on, // 0: try running trades first and then history trades, 1: try running only, 2: try history only
   int group,
   int &type[],
   bool findConsecutive = false
)
  {
   if(ArraySize(output) < 4)
     {
      ArrayResize(output, 4);
      ArrayInitialize(output, 0.0);
     }

   double lots         = output[0]; // will be the lot size of the first loaded trade
   double profitOrLoss = output[1]; // 0 is initial value, 1 is profit, -1 is loss
   double consecutive  = output[2]; // the number of consecutive profitable or losable trades
   double profit       = output[3]; // will be the profit of the first loaded trade
   bool historyTrades  = look_up_on == LOOK_UP_RUNNING_ONLY ? false : true;

   int total = (historyTrades) ? OrdersHistoryTotal() : OrdersTotal();

   for(int pos = total - 1; pos >= 0; pos--)
     {
      bool con1 = !historyTrades && TradeSelectByIndex(pos, ORDER_GROUP_MODE_NUMBER, group, symbol, type);
      bool con2 = historyTrades && HistoryTradeSelectByIndex(pos, ORDER_GROUP_MODE_NUMBER, group, symbol, type);
      if(con1 || con2)
        {
         bool skipCon1 = ((look_up_on == 0 || look_up_on == 1) && TimeCurrent() - OrderOpenTime() < 3); // skip for brand new trades
         bool skipCon2 = !historyTrades && OrderExpiration() > 0 && OrderExpiration() <= OrderCloseTime(); // exclude expired pending orders
         if(skipCon1 || skipCon2)
            continue;
         if(lots == 0.0)
           {
            lots = OrderLots();
           }

         profit = OrderClosePrice() - OrderOpenPrice();
         profit = NormalizeDouble(profit, SymbolDigits(OrderSymbol()));

         if(profit == 0.0)
           {
            // Consider a trade with zero profit as non existent
            continue;
           }

         if(IsOrderTypeSell())
           {
            profit = -1 * profit;
           }

         if(profitOrLoss == 0)
           {
            // We enter here only for the first trade
            profitOrLoss = (profit < 0.0) ? -1 : 1;

            consecutive++;
            if(findConsecutive == false)
               break;
           }
         else
           {
            // For the trades after the first one, if its profit is the opposite of profitOrLoss, we need to break
            if(
               (profitOrLoss > 0.0 && profit < 0.0)
               || (profitOrLoss < 0.0 && profit > 0.0)
            )
              {
               break;
              }

            consecutive++;
           }
        }
     }

   output[0] = lots;
   output[1] = profitOrLoss;
   output[2] = consecutive;
   output[3] = profit;

   if(look_up_on == 0 && (findConsecutive || profitOrLoss == 0))
     {
      // running trades tried, continue with the history trades
      look_up_on = 2;
      GetBetTradesInfo(output, symbol, look_up_on, group, type, findConsecutive);
     }
  }
bool TradeSelectByIndex(
   int index,
   string group_mode,
   string group,
   string msymbol,
   int type[]
)
  {
   if(OrderSelect(index, SELECT_BY_POS, MODE_TRADES))
     {
      bool x = filterGeneral(msymbol, type, group_mode, group);
      return x;
     }

   return false;



  }bool HistoryTradeSelectByIndex(
   int index,
   string group_mode,
   string group,
   string msymbol,
   int type[]
)
  {
   if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)
     {
      bool x = filterGeneral(msymbol, type, group_mode, group);
      return x;
     }

   return false;
  }
bool              filterGeneral(string symbol, int type[], int group_mode, int group_number)
  {
   bool con1 = (symbol==NULL && OrderSymbol()==Symbol()) || symbol==OrderSymbol();
   bool con2 = sameOrderType(type, OrderType());
   bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
   bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
   return con1 && con2 && con3 && con4;
  }
int SymbolDigits(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
  }bool IsOrderTypeSell()
  {
   int type = OrderType();

   return (type == OP_SELL || type == OP_SELLSTOP || type == OP_SELLLIMIT);
  }double DynamicLots(string symbol, int mode, double value=0, double sl=0, string align="align", double RJFR_initial_lots=0)
  {
   double size=0;
   double LotStep=MarketInfo(symbol,MODE_LOTSTEP);
   double LotSize=MarketInfo(symbol,MODE_LOTSIZE);
   double MinLots=MarketInfo(symbol,MODE_MINLOT);
   double MaxLots=MarketInfo(symbol,MODE_MAXLOT);
   double TickValue=MarketInfo(symbol,MODE_TICKVALUE);
   double point=MarketInfo(symbol,MODE_POINT);
   double ticksize=MarketInfo(symbol,MODE_TICKSIZE);
   double margin_required=MarketInfo(symbol,MODE_MARGINREQUIRED);

   if(mode==MONEY_MANAGEMENT_FIXED_VOLUME)
     {
      size=value;

     }
   else
      if(mode==MONEY_MANAGEMENT_PERCENT_OF_EQUITY)
        {
         size=(value/100)*AccountEquity()/margin_required;
        }
      else
         if(mode==MONEY_MANAGEMENT_PERCENT_OF_BALANCE)
           {
            size=(value/100)*AccountBalance()/margin_required;
           }
         else
            if(mode==MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN)
              {
               size=(value/100)*AccountFreeMargin()/margin_required;
              }
            else
               if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY)
                 {
                  size=(value/100)*AccountEquity()/(LotSize*TickValue);
                 }
               else
                  if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE)
                    {
                     size=(value/100)*AccountBalance()/(LotSize*TickValue);
                    }
                  else
                     if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN)
                       {
                        size=(value/100)*AccountFreeMargin()/(LotSize*TickValue);
                       }
                     else
                        if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY)
                          {
                           size=((value/100)*AccountEquity())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                          }
                        else
                           if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE)
                             {
                              size=((value/100)*AccountBalance())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                             }
                           else
                              if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN)
                                {
                                 size=((value/100)*AccountFreeMargin())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                                }
                              else
                                 if(mode=="fixedRisk")
                                   {
                                    size=(value)/(sl*((TickValue/ticksize)*point)*PipValue(symbol));
                                   }
                                 else
                                    if(mode=="fixedRatio" || mode=="RJFR")
                                      {

                                       /////
                                       // Ryan Jones Fixed Ratio MM static data
                                       static double RJFR_start_lots=0;
                                       static double RJFR_delta=0;
                                       static double RJFR_units=1;
                                       static double RJFR_target_lower=0;
                                       static double RJFR_target_upper=0;
                                       /////

                                       if(RJFR_start_lots<=0)
                                         {
                                          RJFR_start_lots=value;
                                         }
                                       if(RJFR_start_lots<MinLots)
                                         {
                                          RJFR_start_lots=MinLots;
                                         }
                                       if(RJFR_delta<=0)
                                         {
                                          RJFR_delta=sl;
                                         }
                                       if(RJFR_target_upper<=0)
                                         {
                                          RJFR_target_upper=AccountEquity()+(RJFR_units*RJFR_delta);
                                          Print("Fixed Ratio MM: Units=>",RJFR_units,"; Delta=",RJFR_delta,"; Upper Target Equity=>",RJFR_target_upper);
                                         }
                                       if(AccountEquity()>=RJFR_target_upper)
                                         {
                                          while(true)
                                            {
                                             Print("Fixed Ratio MM going up to ",(RJFR_start_lots*(RJFR_units+1))," lots: Equity is above Upper Target Equity (",AccountEquity(),">=",RJFR_target_upper,")");
                                             RJFR_units++;
                                             RJFR_target_lower=RJFR_target_upper;
                                             RJFR_target_upper=RJFR_target_upper+(RJFR_units*RJFR_delta);
                                             Print("Fixed Ratio MM: Units=>",RJFR_units,"; Delta=",RJFR_delta,"; Lower Target Equity=>",RJFR_target_lower,"; Upper Target Equity=>",RJFR_target_upper);
                                             if(AccountEquity()<RJFR_target_upper)
                                               {
                                                break;
                                               }
                                            }
                                         }
                                       else
                                          if(AccountEquity()<=RJFR_target_lower)
                                            {
                                             while(true)
                                               {
                                                if(AccountEquity()>RJFR_target_lower)
                                                  {
                                                   break;
                                                  }
                                                if(RJFR_units>1)
                                                  {
                                                   Print("Fixed Ratio MM going down to ",(RJFR_start_lots*(RJFR_units-1))," lots: Equity is below Lower Target Equity | ", AccountEquity()," <= ",RJFR_target_lower,")");
                                                   RJFR_target_upper=RJFR_target_lower;
                                                   RJFR_target_lower=RJFR_target_lower-((RJFR_units-1)*RJFR_delta);
                                                   RJFR_units--;
                                                   Print("Fixed Ratio MM: Units=>",RJFR_units,"; Delta=",RJFR_delta,"; Lower Target Equity=>",RJFR_target_lower,"; Upper Target Equity=>",RJFR_target_upper);
                                                  }
                                                else
                                                  {
                                                   break;
                                                  }
                                               }
                                            }
                                       size=RJFR_start_lots*RJFR_units;
                                      }
   if(size==EMPTY_VALUE)
     {
      size=0;
     }

   size=MathRound(size/LotStep)*LotStep;
   return (size);
  }
double PipValue(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return CustomPoint(symbol) / SymbolInfoDouble(symbol, SYMBOL_POINT);
  }double CustomPoint(string symbol)
  {
   static string symbols[];
   static double points[];
   static string last_symbol = "-";
   static double last_point  = 0;
   static int last_i         = 0;
   static int size           = 0;

//-- variant A) use the cache for the last used symbol
   if(symbol == last_symbol)
     {
      return last_point;
     }

//-- variant B) search in the array cache
   int i       = last_i;
   int start_i = i;
   bool found  = false;

   if(size > 0)
     {
      while(true)
        {
         if(symbols[i] == symbol)
           {
            last_symbol = symbol;
            last_point  = points[i];
            last_i      = i;

            return last_point;
           }

         i++;

         if(i >= size)
           {
            i = 0;
           }
         if(i == start_i)
           {
            break;
           }
        }
     }

//-- variant C) add this symbol to the cache
   i     = size;
   size  = size + 1;

   ArrayResize(symbols, size);
   ArrayResize(points, size);

   symbols[i]  = symbol;
   points[i]   = 0;
   last_symbol = symbol;
   last_i      = i;

//-- unserialize rules from FXD_POINT_FORMAT_RULES
   string rules[];
   StringExplode(",", POINT_FORMAT_RULES, rules);

   int rules_count = ArraySize(rules);

   if(rules_count > 0)
     {
      string rule[];

      for(int r = 0; r < rules_count; r++)
        {
         StringExplode("=", rules[r], rule);

         //-- a single rule must contain 2 parts, [0] from and [1] to
         if(ArraySize(rule) != 2)
           {
            continue;
           }

         double from = StringToDouble(rule[0]);
         double to   = StringToDouble(rule[1]);

         //-- "to" must be a positive number, different than 0
         if(to <= 0)
           {
            continue;
           }

         //-- "from" can be a number or a string
         // a) string
         if(from == 0 && StringLen(rule[0]) > 0)
           {
            string s_from = rule[0];
            int pos       = StringFind(s_from, "?");

            if(pos < 0)  // ? not found
              {
               if(StringFind(symbol, s_from) == 0)
                 {
                  points[i] = to;
                 }
              }
            else
               if(pos == 0)  // ? is the first symbol => match the second symbol
                 {
                  if(StringFind(symbol, StringSubstr(s_from, 1), 3) == 3)
                    {
                     points[i] = to;
                    }
                 }
               else
                  if(pos > 0)  // ? is the second symbol => match the first symbol
                    {
                     if(StringFind(symbol, StringSubstr(s_from, 0, pos)) == 0)
                       {
                        points[i] = to;
                       }
                    }
           }

         // b) number
         if(from == 0)
           {
            continue;
           }

         if(SymbolInfoDouble(symbol, SYMBOL_POINT) == from)
           {
            points[i] = to;
           }
        }
     }

   if(points[i] == 0)
     {
      points[i] = SymbolInfoDouble(symbol, SYMBOL_POINT);
     }

   last_point = points[i];

   return last_point;
  }

template<typename T>
void StringExplode(string delimiter, string inputString, T &output[])
  {
   int begin   = 0;
   int end     = 0;
   int element = 0;
   int length  = StringLen(inputString);
   int length_delimiter = StringLen(delimiter);
   T empty_val  = (typename(T) == "string") ? (T)"" : (T)0;

   if(length > 0)
     {
      while(true)
        {
         end = StringFind(inputString, delimiter, begin);

         ArrayResize(output, element + 1);
         output[element] = empty_val;

         if(end != -1)
           {
            if(end > begin)
              {
               output[element] = (T)StringSubstr(inputString, begin, end - begin);
              }
           }
         else
           {
            output[element] = (T)StringSubstr(inputString, begin, length - begin);
            break;
           }

         begin = end + 1 + (length_delimiter - 1);
         element++;
        }
     }
   else
     {
      ArrayResize(output, 1);
      output[element] = empty_val;
     }
  }
double toDigits(double pips, string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   int digits   = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
   double point = SymbolInfoDouble(symbol, SYMBOL_POINT);

   return NormalizeDouble(pips * PipValue(symbol) * point, digits);
  }
string StringTrim(string str)
  {
   str = StringTrimRight(str);
   str = StringTrimLeft(str);

   return str;
  }
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
