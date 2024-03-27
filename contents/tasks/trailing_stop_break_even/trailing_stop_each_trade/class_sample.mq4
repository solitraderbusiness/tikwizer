

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


// Tailing stop each trade
class Task0 : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   //////////////////////////////////////////////////
   //////////////////////////////////////////////////
   //////////////////////////////////////////////////
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
   //////////////////////////////////////////////////
   //////////////////////////////////////////////////
   //////////////////////////////////////////////////

public:
                     Task0(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.


      //////////////////////////////////////////////////
      //////////////////////////////////////////////////
      //////////////////////////////////////////////////

      TrailWhat = 1;
      TrailingReferencePrice = 0;
      TrailingStopMode = TRAILING_STOP_MODE_PERCENT_OF_OPPOSITE_STOP;
      tStopPips = 40.0;
      tStopMoney = 10.0;
      tStopMultiple = "20/5, 30/10";
      tStopPercentTP = 100.0;
      tStopPercentProfit = 50.0;
      TrailingStepMode = TRAILING_STEP_MODE_PIPS;
      tStepPips = 1.0;
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

      //////////////////////////////////////////////////
      //////////////////////////////////////////////////
      //////////////////////////////////////////////////

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      for(int m = OrdersTotal()-1 ; m >= 0 ; m--)
        {
         if(OrderSelect(m, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;

            //////////////////////////////////////////////////
            //////////////////////////////////////////////////
            //////////////////////////////////////////////////
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

                              MACD3_left1 macd_left1;
                              macd_left1.init();
                              double valueMacd_left1 = macd_left1.calc();
                              t_stop = valueMacd_left1;

                              //                              initializer_tradiling_stop_mode_
                              //                              t_stop = variable_name;
                              //
                              //                              t_stop = (polarity == 1) ? ask - t_stop : t_stop - bid;
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


            //////////////////////////////////////////////////
            //////////////////////////////////////////////////
            //////////////////////////////////////////////////

           }
        }
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }
   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

  };


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
string StringTrim(string str)
  {
   str = StringTrimRight(str);
   str = StringTrimLeft(str);

   return str;
  }
