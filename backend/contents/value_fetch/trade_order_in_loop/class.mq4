#define IN_LOOP_TRADE_ORDER_CANDLE_ID 1
#define IN_LOOP_TRADE_ORDER_CANDLE_TIME 2
#define IN_LOOP_TRADE_ORDER_CLOSE_PRICE 3
#define IN_LOOP_TRADE_ORDER_CLOSE_TIME 4
#define IN_LOOP_TRADE_ORDER_COMMENT 5
#define IN_LOOP_TRADE_ORDER_COMMISSION 6
#define IN_LOOP_TRADE_ORDER_GROUP_NUMBER 7
#define IN_LOOP_TRADE_ORDER_MAGIC_NUMBER 8
#define IN_LOOP_TRADE_ORDER_MARKET_NAME 9
#define IN_LOOP_TRADE_ORDER_OPEN_PRICE 10
#define IN_LOOP_TRADE_ORDER_OPEN_TIME 11
#define IN_LOOP_TRADE_ORDER_PROFIT 12
#define IN_LOOP_TRADE_ORDER_STOPLOSS 13
#define IN_LOOP_TRADE_ORDER_SWAP 14
#define IN_LOOP_TRADE_ORDER_TAKE_PROFIT 15
#define IN_LOOP_TRADE_ORDER_TICKET_NUMBER 16
#define IN_LOOP_TRADE_ORDER_VOLUME_SIZE_LOTS 17



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class TradeOrderInLoop_left11
  {
public:
   int               row2;
   ENUM_TIMEFRAMES   Period_candle_id; //candle id
   ENUM_TIMEFRAMES   Period_candle_time; //candle time
   int               ModeProfit; //Order profit
   string            ModeStopLoss; //Order stoploss
   string            ModeTakeProfit; //Order take profit
   int               ModeTicket; //Order ticket number
   int               ModeVolume; //Order volume

   void              init()
     {
      row2 = IN_LOOP_TRADE_ORDER_COMMISSION;
      Period_candle_id = (ENUM_TIMEFRAMES)PERIOD_CURRENT;
      Period_candle_time = (ENUM_TIMEFRAMES)PERIOD_CURRENT;
      ModeProfit = (int)0;
      ModeStopLoss = (string)"level";
      ModeTakeProfit = (string)"level";
      ModeTicket = (int)0;
      ModeVolume = (int)0;//STest: this seems to have a value from project settings set by user
     }

      template<typename T>
   T                 execute()
     {
      T retval;
      switch(row2)
        {
         case IN_LOOP_TRADE_ORDER_CANDLE_ID:
            retval = get_candle_id();
            break;
         case IN_LOOP_TRADE_ORDER_CANDLE_TIME:
            retval = get_candle_time();
            break;
         case IN_LOOP_TRADE_ORDER_CLOSE_PRICE:
            retval = get_order_close_price();
            break;
         case IN_LOOP_TRADE_ORDER_CLOSE_TIME:
            retval = get_order_close_time();
            break;
         case IN_LOOP_TRADE_ORDER_COMMENT:
            retval = get_order_comment();
            break;
         case IN_LOOP_TRADE_ORDER_COMMISSION:
            retval = get_order_commission();
            break;
         case IN_LOOP_TRADE_ORDER_GROUP_NUMBER:
            retval = get_order_group_number();
            break;
         case IN_LOOP_TRADE_ORDER_MAGIC_NUMBER:
            retval = get_order_magic_number();
            break;
         case IN_LOOP_TRADE_ORDER_MARKET_NAME:
            retval = get_order_symbol();
            break;
         case IN_LOOP_TRADE_ORDER_OPEN_PRICE:
            retval = get_order_open_price();
            break;
         case IN_LOOP_TRADE_ORDER_OPEN_TIME:
            retval = get_order_open_time();
            break;
         case IN_LOOP_TRADE_ORDER_PROFIT:
            retval = get_order_profit();
            break;
         case IN_LOOP_TRADE_ORDER_STOPLOSS:
            retval = get_order_stoploss();
            break;
         case IN_LOOP_TRADE_ORDER_SWAP:
            retval = get_order_swap();
            break;
         case IN_LOOP_TRADE_ORDER_TAKE_PROFIT:
            retval = get_order_take_profit();
            break;
         case IN_LOOP_TRADE_ORDER_TICKET_NUMBER:
            retval = get_order_ticket();
            break;
         case IN_LOOP_TRADE_ORDER_VOLUME_SIZE_LOTS:
            retval = get_order_volume();
            break;
        }
      return retval;
     }


   int               get_candle_id()
     {
      datetime orderTime = OrderOpenTime();
      string orderSymbol = OrderSymbol();
      int shift          = 0;

      while(true)
        {
         datetime candleTime[];
         int result = CopyTime(orderSymbol,getTimeframe(Period_candle_id), shift, 1, candleTime);

         if(result == 1)
           {
            if(candleTime[0] <= orderTime)
              {
               break;
              }
           }

         shift++;
        }

      return shift;
     }


   datetime          get_candle_time()
     {
      datetime time      = 0;
      datetime orderTime = OrderOpenTime();
      string orderSymbol = OrderSymbol();
      int shift          = 0;

      while(true)
        {
         datetime candleTime[];
         int result = CopyTime(orderSymbol, getTimeframe(Period_candle_time), shift, 1, candleTime);

         if(result == 1)
           {
            if(candleTime[0] <= orderTime)
              {
               time = candleTime[0];

               break;
              }
           }

         shift++;
        }

      return time;
     }


   double            get_order_close_price()
     {
      return OrderClosePrice();
     }


   datetime          get_order_close_time()
     {
      return OrderCloseTime();
     }


   string            get_order_comment()
     {
      return OrderComment();
     }


   double            get_order_commission()
     {
      return OrderCommission();
     }


   int               get_order_group_number()
     {
      return getGroupNumber(OrderMagicNumber());
     }


   int               get_order_magic_number()
     {
      return OrderMagicNumber();
     }


   string            get_order_symbol()
     {
      return OrderSymbol();
     }


   double            get_order_open_price()
     {
      return OrderOpenPrice();
     }


   datetime          get_order_open_time()
     {
      return OrderOpenTime();
     }


   double            get_order_profit()
     {
      double retval = 0;

      if(OrderType() > 1)
        {
         return 0;
        }
      int digits;
      switch(ModeProfit)
        {
         case 0:
            retval = NormalizeDouble(OrderProfit(), 2);
            break;
         case 1:
            retval = NormalizeDouble(OrderProfit() + OrderSwap() + OrderCommission(), 2);
            break;
         case 2:
           {
            digits = (int)SymbolInfoInteger(OrderSymbol(), SYMBOL_DIGITS);
            retval = OrderClosePrice() - OrderOpenPrice();
            retval = NormalizeDouble(retval, digits);
            if(IsOrderTypeSell())
              {
               retval = -1 * retval;
              }
            break;
           }
         case 3:
           {
            digits = (int)SymbolInfoInteger(OrderSymbol(), SYMBOL_DIGITS);
            retval = toPips(OrderClosePrice() - OrderOpenPrice(), OrderSymbol());
            retval = NormalizeDouble(retval, digits);
            if(IsOrderTypeSell())
              {
               retval = -1 * retval;
              }
            break;
           }
        }

      return retval;
     }


   double            get_order_stoploss()
     {
      double retval = 0;
      int digits    = (int)SymbolInfoInteger(OrderSymbol(), SYMBOL_DIGITS);

      if(ModeStopLoss == "level")
        {
         retval = OrderStopLoss();
        }
      else
         if(ModeStopLoss == "fraction")
           {
            if(OrderStopLoss() > 0)
              {
               retval = MathAbs(OrderOpenPrice()-OrderStopLoss());
              }
           }
         else
            if(ModeStopLoss == "pips")
              {
               if(OrderStopLoss() > 0)
                 {
                  double point = SymbolInfoDouble(OrderSymbol(), SYMBOL_POINT);

                  retval = MathAbs(OrderOpenPrice()-OrderStopLoss())/(PipValue(OrderSymbol())*point);
                 }
              }

      return NormalizeDouble(retval, digits);
     }


   double            get_order_swap()
     {
      return OrderSwap();
     }


   double            get_order_take_profit()
     {
      double retval = 0;
      int digits    = (int)SymbolInfoInteger(OrderSymbol(), SYMBOL_DIGITS);

      if(ModeTakeProfit == "level")
        {
         retval = OrderTakeProfit();
        }
      else
         if(ModeTakeProfit == "fraction")
           {
            if(OrderTakeProfit() > 0)
              {
               retval = MathAbs(OrderOpenPrice()-OrderTakeProfit());
              }
           }
         else
            if(ModeTakeProfit == "pips")
              {
               if(OrderTakeProfit() > 0)
                 {
                  double point = SymbolInfoDouble(OrderSymbol(), SYMBOL_POINT);

                  retval = MathAbs(OrderOpenPrice()-OrderTakeProfit())/(PipValue(OrderSymbol())*point);
                 }
              }

      return NormalizeDouble(retval, digits);
     }


   long              get_order_ticket()
     {
      long retval = OrderTicket();

      if(ModeTicket == 1)
        {
         retval = attrTicketParent(retval);
        }

      return retval;
     }


   double            get_order_volume()
     {
      if(ModeVolume == 0)
        {
         return OrderLots();
        }
      if(ModeVolume == 1)
        {
         //return attrLotsInitial(); //STest, commented cuz it needs much time and effort
        }

      return 0;
     }
  };
//+------------------------------------------------------------------+
