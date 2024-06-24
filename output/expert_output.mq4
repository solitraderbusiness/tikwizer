#define EVENT_ON_INIT   1
#define EVENT_ON_TIMER  2
#define EVENT_ON_TICK   3
#define EVENT_ON_TRADE  4
#define EVENT_ON_CHART  5
#define EVENT_ON_DEINIT 6
#define ROUTE_1_PASSED 1
#define ROUTE_2_PASSED 0
#define RESET_LEVEL_DEFAULT 0
#define RESET_LEVEL_TICK 1
#define RESET_LEVEL_BAR 2
#define RESET_LEVEL_CUSTOM 3
#define TIME_MODE_TEXT 1
#define TIME_MODE_COMPONENT 2
#define TIME_MODE_RELATIVE 3
#define TIME_SERVER 1
#define TIME_LOCAL 2
#define TIME_GMT 3
#define ORDER_GROUP_MODE_ALL -1
#define ORDER_GROUP_MODE_NUMBER 1
#define ORDER_GROUP_MODE_MANUAL 2
#define SYMBOL_MODE_SPECIFIED 1
#define SYMBOL_MODE_ANY 2
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
#define HIGHEST_PRICE_CANDLE_PERIOD 1
#define HIGHEST_PRICE_TIME_PERIOD 2
#define LOWEST_PRICE_CANDLE_PERIOD 3
#define LOWEST_PRICE_TIME_PERIOD 4
#define  GET_CANDLE_ID  1
#define  GET_PRICE  2
#define  GET_TIME  3
#define PROFIT_MODE_MONEY "money"
#define PROFIT_MODE_PIPS "pips"
#define PROFIT_MODE_PIPS_SUM "pips-sum"
#define PROFIT_MODE_NO_MATTER "no-matter"
#define VALUE_PIPS_AS_IS 1
#define VALUE_PIPS_AS_PRICE_FRACTION 2
#define MODE_TIME_NOW 1
#define MODE_TIME_TIMESTAMP 2
#define MODE_TIME_COMPONENTS 3
#define MODE_TIME_CANDLE_TIME 4
#define MODE_TIME_TIME_VALUE 5
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
#define MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI 13
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
#define CLOSE_PARTIALLY_FIXED_VOLUME 1
#define CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME 2
#define CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME 3
#define CHECK_PROFIT_LOSS_MODE_DEPOSIT_CURRENCY 1
#define CHECK_PROFIT_LOSS_MODE_ACCOUNT_PROFIT 2
#define CHECK_PROFIT_LOSS_MODE_EQUITY 3
#define CHECK_PROFIT_LOSS_MODE_BALANCE 4
#define CHECK_PROFIT_LOSS_MODE_FREE_MARGIN 5
#define CHECK_PROFIT 1
#define CHECK_LOSS 2
#define TRAILING_DISTANCE_MODE_FIXED 1
#define TRAILING_DISTANCE_MODE_DYNAMIC 2
#define TRAILING_DISTANCE_MODE_DYNAMIC_PIPS 3
#define TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS 4
#define PRICE_RELATIVE_TO_OPEN_PRICE 1
#define PRICE_RELATIVE_TO_CURRENT_PRICE 2
#define PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL 3
#define NEW_STOPS_FIXED 1
#define NEW_STOPS_PERCENT_OF_CURRENT_TPSL 2
#define NEW_STOPS_CUSTOM_PRICE_LEVEL 3
#define PUT_IN_RANGE(A, L, H) ((H) < (L) ? (A) : ((A) < (L) ? (L) : ((A) > (H) ? (H) : (A))))
#define COLOR_IS_NONE(C) (((C) >> 24) != 0)
#define RGB_TO_COLOR(R, G, B) ((color)((((B) & 0x0000FF) << 16) + (((G) & 0x0000FF) << 8) + ((R) & 0x0000FF)))
#define ROUND_PRICE(A, P) ((int)((A) / P + 0.5))
#define NORM_PRICE(A, P) (((int)((A) / P + 0.5)) * P)
#define TLOBJPROP_TIME1 801
#define OBJPROP_TL_PRICE_BY_SHIFT 802
#define OBJPROP_TL_SHIFT_BY_PRICE 803
#define OBJPROP_FIBOVALUE 804
#define OBJPROP_FIBOPRICEVALUE 805
#define OBJPROP_BARSHIFT1 807
#define OBJPROP_BARSHIFT2 808
#define OBJPROP_BARSHIFT3 809
extern string test = ""; // 
struct MarketPropertiesResult
  {
   double            price;
   int               index;
   datetime          time;
  };

//This is used to hold onchart event for onchart blocks process
struct OnChartEventHolder
  {
   int               id;
   long              lparam;
   double            dparam;
   string            sparam;
  };class OnTradeEventDetector
  {
private:
   //--- structures
   struct EventValues
     {
      // special fields
      string   reason,
               detail;

      // order related fields
      long     magic,
               ticket;
      int            type;
      datetime timeClose,
               timeOpen,
               timeExpiration;
      double   commission,
               priceOpen,
               priceClose,
               profit,
               stopLoss,
               swap,
               takeProfit,
               volume;
      string   comment,
               symbol;
     };

   struct Position
     {
      int            type;
      long     magic,
               ticket;
      datetime timeClose,
               timeExpiration,
               timeOpen;
      double   commission,
               priceCurrent,
               priceOpen,
               profit,
               stopLoss,
               swap,
               takeProfit,
               volume;
      string   comment,
               symbol;
     };

   struct PendingOrder
     {
      int            type;
      long     magic,
               ticket;
      datetime timeClose,
               timeExpiration,
               timeOpen;
      double   priceCurrent,
               priceOpen,
               stopLoss,
               takeProfit,
               volume;
      string   comment,
               symbol;
     };

   struct PositionExpirationTimes
     {
      long           ticket;
      datetime       timeExpiration;
     };

   //--- variables and arrays
   bool              debug;

   // Because we can have multiple new events at once, the idea is
   // to run the detector repeatedly until no new event is detected.
   // When this variable is true, it means that the event detection
   // is repeated. It should stop repeating when no new event is detected.
   bool              isRepeat;

   int               eventValuesQueueIndex;
   EventValues       eventValues[];

   PendingOrder      previousPendingOrders[];
   PendingOrder      pendingOrders[];

   Position          previousPositions[];
   Position          positions[];

   PositionExpirationTimes positionExpirationTimes[];

   //--- methods

   /**
   * Like ArrayCopy(), but for any type.
   */
   template<typename T>
   void              CopyList(T &dest[], T &src[])
     {
      int size = ArraySize(src);
      ArrayResize(dest, size);

      for(int i = 0; i < size; i++)
        {
         dest[i] = src[i];
        }
     }

   /**
   * Overloaded method 1 of 2
   */
   int               MakeListOf(PendingOrder &list[])
     {
      ArrayResize(list, 0);

      int count        = OrdersTotal();
      int howManyAdded = 0;

      for(int index = 0; index < count; index++)
        {
         if(OrderSelect(index, SELECT_BY_POS) == false)
            continue;
         if(OrderType() < OP_BUYLIMIT)
            continue;

         howManyAdded++;
         ArrayResize(list, howManyAdded);
         int i = howManyAdded - 1;

         // int
         list[i].type   = OrderType();
         list[i].magic  = OrderMagicNumber();
         list[i].ticket = OrderTicket();

         // datetime
         list[i].timeClose      = OrderCloseTime();
         list[i].timeExpiration = OrderExpiration();
         list[i].timeOpen       = OrderOpenTime();

         // double
         list[i].priceCurrent = OrderClosePrice();
         list[i].priceOpen    = OrderOpenPrice();
         list[i].stopLoss     = OrderStopLoss();
         list[i].takeProfit   = OrderTakeProfit();
         list[i].volume       = OrderLots();

         // string
         list[i].comment = OrderComment();
         list[i].symbol  = OrderSymbol();
        }

      return howManyAdded;
     }

   /**
   * Overloaded method 2 of 2
   */
   int               MakeListOf(Position &list[])
     {
      ArrayResize(list, 0);

      int count        = OrdersTotal();
      int howManyAdded = 0;

      for(int index = 0; index < count; index++)
        {
         if(OrderSelect(index, SELECT_BY_POS) == false)
            continue;
         if(OrderType() > OP_SELL)
            continue;

         howManyAdded++;
         ArrayResize(list, howManyAdded);
         int i = howManyAdded - 1;

         // int
         list[i].type   = OrderType();
         list[i].magic  = OrderMagicNumber();
         list[i].ticket = OrderTicket();

         // datetime
         list[i].timeClose      = OrderCloseTime();
         list[i].timeExpiration = (datetime)0;
         list[i].timeOpen       = OrderOpenTime();

         // double
         list[i].commission   = OrderCommission();
         list[i].priceCurrent = OrderClosePrice();
         list[i].priceOpen    = OrderOpenPrice();
         list[i].profit       = OrderProfit();
         list[i].stopLoss     = OrderStopLoss();
         list[i].swap         = OrderSwap();
         list[i].takeProfit   = OrderTakeProfit();
         list[i].volume       = OrderLots();

         // string
         list[i].comment = OrderComment();
         list[i].symbol  = OrderSymbol();

         // extract expiration
         //       list[i].timeExpiration = expirationWorker.GetExpiration(list[i].ticket);
         //
         //       if (USE_VIRTUAL_STOPS)
         //       {
         //          list[i].stopLoss   = VirtualStopsDriver("get sl", list[i].ticket);
         //          list[i].takeProfit = VirtualStopsDriver("get tp", list[i].ticket);
         //       }
        }

      return howManyAdded;
     }

   /**
   * This method loops through 2 lists of items and finds a difference. This difference is the event.
   * "Items" are either pending orders or positions.
   *
   * Returns true if an event is detected or false if not.
   */
   template<typename ITEMS_TYPE>
   bool              DetectEvent(ITEMS_TYPE &previousItems[], ITEMS_TYPE &currentItems[])
     {
      ITEMS_TYPE item;
      string reason   = "";
      string detail   = "";
      int countBefore = ArraySize(previousItems);
      int countNow    = ArraySize(currentItems);

      // closed
      if(reason == "")
        {
         for(int index = 0; index < countBefore; index++)
           {
            item = FindMissingItem(previousItems, currentItems);

            if(item.ticket > 0)
              {
               DeleteItem(previousItems, item);
               reason = "close";

               break;
              }
           }
        }

      // new
      if(reason == "")
        {
         for(int index2 = 0; index2 < countNow; index2++)
           {
            item = FindMissingItem(currentItems, previousItems);

            if(item.ticket > 0)
              {
               if(
                  item.type < 2 // it's a running trade
                  && item.ticket != attrTicketParent(item.ticket)
               )
                 {
                  // In MQL4: When a trade is closed partially, the ticket changes.
                  // The original (parent) trade is closed and a new one is created,
                  // with a different ticket.
                  reason = "decrement";
                 }
               else
                 {
                  reason = "new";
                 }

               PushItem(previousItems, item);

               break;
              }
           }
        }

      // modified
      if(reason == "")
        {
         if(countBefore != countNow)
           {
            Print("OnTrade event detector: Uncovered situation reached");
           }

         for(int index3 = 0; index3 < countNow; index3++)
           {
            int previousIndex = -1;

            ITEMS_TYPE current = currentItems[index3];
            ITEMS_TYPE previous;
            previous.ticket = 0;

            for(int j = 0; j < countBefore; j++)
              {
               if(current.ticket == previousItems[j].ticket)
                 {
                  previousIndex = j;
                  previous = previousItems[j];

                  break;
                 }
              }

            if(current.ticket != previous.ticket)
              {
               Print("OnTrade event detector: Uncovered situation reached (2)");
              }

            if(previous.volume < current.volume)
              {
               previousItems[previousIndex].volume = current.volume;
               item = previousItems[previousIndex];

               reason = "increment";

               break;
              }

            if(previous.volume > current.volume)
              {
               previousItems[previousIndex].volume = current.volume;
               item = previousItems[previousIndex];

               reason = "decrement";

               break;
              }

            if(
               previous.stopLoss != current.stopLoss
               && previous.takeProfit != current.takeProfit
            )
              {
               previousItems[previousIndex].stopLoss = current.stopLoss;
               previousItems[previousIndex].takeProfit = current.takeProfit;
               item = previousItems[previousIndex];

               reason = "modify";
               detail = "sltp";

               break;
              }
            // SL modified
            else
               if(previous.stopLoss != current.stopLoss)
                 {
                  previousItems[previousIndex].stopLoss = current.stopLoss;
                  item = previousItems[previousIndex];

                  reason = "modify";
                  detail = "sl";

                  break;
                 }
               // TP modified
               else
                  if(previous.takeProfit != current.takeProfit)
                    {
                     previousItems[previousIndex].takeProfit = current.takeProfit;
                     item = previousItems[previousIndex];

                     reason = "modify";
                     detail = "tp";

                     break;
                    }

            if(previous.timeExpiration != current.timeExpiration)
              {
               previousItems[previousIndex].timeExpiration = current.timeExpiration;
               item = previousItems[previousIndex];

               reason = "modify";
               detail = "expiration";

               break;
              }
           }
        }

      if(reason == "")
        {
         return false;
        }

      UpdateValues(item, reason, detail);

      return true;
     }

   /**
   * From the source list of orders or positions, find the item that is missing
   * in the target list of orders or positions. The searching is by the item's ticket.
   *
   * If all items from the source list exist in the target list, return an empty item with ticket 0.
   * If for some item in source list there is no item in the target list, return that source item.
   */
   template<typename T>
   T                 FindMissingItem(T &source[], T &target[])
     {
      int sourceCount = ArraySize(source);
      int targetCount  = ArraySize(target);
      T item;
      item.ticket = 0;

      long ticket = 0;

      for(int i = 0; i < sourceCount; i++)
        {
         bool found = false;

         for(int j = 0; j < targetCount; j++)
           {
            if(source[i].ticket == target[j].ticket)
              {
               found = true;
               break;
              }
           }

         if(found == false)
           {
            item = source[i];
            break;
           }
        }

      return item;
     }

   /**
   * From the list of previous orders or positions, find and remove the
   * provided item.
   */
   template<typename T>
   bool              DeleteItem(T &list[], T &item)
     {
      int listCount = ArraySize(list);
      bool removed = false;

      for(int i = 0; i < listCount; i++)
        {
         if(list[i].ticket == item.ticket)
           {
            ArrayStripKey(list, i);
            removed = true;

            break;
           }
        }

      return removed;
     }

   /**
   * Push a new item in the list
   */
   template<typename T>
   void              PushItem(T &list[], T &item)
     {
      int listCount = ArraySize(list);

      ArrayResize(list, listCount + 1);

      list[listCount] = item;
     }

   /**
   * Overloaded method 1 of 2
   */
   void              UpdateValues(Position &item, string reason, string detail)
     {
      long ticket        = item.ticket;
      datetime timeOpen  = item.timeOpen;
      datetime timeClose = item.timeClose;
      double priceOpen   = item.priceOpen;
      double priceClose  = item.priceCurrent;
      double profit      = item.profit;
      double swap        = item.swap;
      double commission  = item.commission;
      double volume      = item.volume;

      if(reason == "close" || reason == "decrement")
        {
         if(OrderSelect((int)ticket, SELECT_BY_TICKET, MODE_HISTORY))
           {
            timeOpen   = OrderOpenTime();
            timeClose  = OrderCloseTime();
            priceOpen  = OrderOpenPrice();
            priceClose = OrderClosePrice();
            profit     = OrderProfit();
            swap       = OrderSwap();
            commission = OrderCommission();
            volume     = OrderLots();

            if(detail == "")
              {
               if(
                  item.timeExpiration > 0
                  && item.timeExpiration <= timeClose
               )
                 {
                  detail = "expiration";
                 }
              }

            if(detail == "")
              {
               string comment = OrderComment();

               // Try with comments, which works in the Tester, but it could not work in real
               if(comment == "[tp]")
                  detail = "tp";
               else
                  if(comment == "[sl]")
                     detail = "sl";

               // Try to detect close by SL or TP by the close price
               if(detail == "")
                 {
                  int type = item.type;

                  double sl = OrderStopLoss();
                  double tp = OrderTakeProfit();

                  if(type == 0)  // BUY
                    {
                     if(sl > 0 && priceClose <= sl)
                        detail = "sl";
                     else
                        if(tp > 0 && priceClose >= tp)
                           detail = "tp";
                    }
                  else
                     if(type == 1)  // SELL
                       {
                        if(sl > 0 && priceClose >= sl)
                           detail = "sl";
                        else
                           if(tp > 0 && priceClose <= tp)
                              detail = "tp";
                       }
                 }
              }
           }
        }

      int i = eventValuesQueueIndex;

      eventValues[i].reason = reason;
      eventValues[i].detail = detail;

      eventValues[i].priceClose     = priceClose;
      eventValues[i].timeClose      = timeClose;
      eventValues[i].comment        = item.comment;
      eventValues[i].commission     = commission;
      eventValues[i].timeExpiration = item.timeExpiration;
      eventValues[i].volume         = volume;
      eventValues[i].magic          = item.magic;
      eventValues[i].priceOpen      = priceOpen;
      eventValues[i].timeOpen       = timeOpen;
      eventValues[i].profit         = profit;
      eventValues[i].stopLoss       = item.stopLoss;
      eventValues[i].swap           = swap;
      eventValues[i].symbol         = item.symbol;
      eventValues[i].takeProfit     = item.takeProfit;
      eventValues[i].ticket         = ticket;
      eventValues[i].type           = item.type;

      if(debug)
        {
         PrintUpdatedValues();
        }
     }

   /**
   * Overloaded method 2 of 2
   */
   void              UpdateValues(PendingOrder &item, string reason, string detail)
     {
      int i = eventValuesQueueIndex;

      eventValues[i].reason = reason;
      eventValues[i].detail = detail;

      eventValues[i].priceClose     = item.priceCurrent;
      eventValues[i].timeClose      = item.timeClose;
      eventValues[i].comment        = item.comment;
      eventValues[i].commission     = 0.0;
      eventValues[i].timeExpiration = item.timeExpiration;
      eventValues[i].volume         = item.volume;
      eventValues[i].magic          = item.magic;
      eventValues[i].priceOpen      = item.priceOpen;
      eventValues[i].timeOpen       = item.timeOpen;
      eventValues[i].profit         = 0.0;
      eventValues[i].stopLoss       = item.stopLoss;
      eventValues[i].swap           = 0.0;
      eventValues[i].symbol         = item.symbol;
      eventValues[i].takeProfit     = item.takeProfit;
      eventValues[i].ticket         = item.ticket;
      eventValues[i].type           = item.type;

      if(debug)
        {
         PrintUpdatedValues();
        }
     }

   void              PrintUpdatedValues()
     {
      Print(
         " <<<"
      );

      Print(
         " | reason: ", e_Reason(),
         " | detail: ", e_ReasonDetail(),
         " | ticket: ", e_attrTicket(),
         " | type: ", EnumToString((ENUM_ORDER_TYPE)e_attrType())
      );

      Print(
         " | openTime : ", e_attrOpenTime(),
         " | openPrice : ", e_attrOpenPrice()
      );

      Print(
         " | closeTime: ", e_attrCloseTime(),
         " | closePrice: ", e_attrClosePrice()
      );

      Print(
         " | volume: ", e_attrLots(),
         " | sl: ", e_attrStopLoss(),
         " | tp: ", e_attrTakeProfit(),
         " | profit: ", e_attrProfit(),
         " | swap: ", e_attrSwap(),
         " | exp: ", e_attrExpiration(),
         " | comment: ", e_attrComment()
      );

      Print(
         ">>>"
      );
     }

   int               AddEventValues()
     {
      eventValuesQueueIndex++;
      ArrayResize(eventValues, eventValuesQueueIndex + 1);

      return eventValuesQueueIndex;
     }

   int               RemoveEventValues()
     {
      if(eventValuesQueueIndex == -1)
        {
         Print("Cannot remove event values, add them first. (in function ", __FUNCTION__, ")");
        }
      else
        {
         eventValuesQueueIndex--;
         ArrayResize(eventValues, eventValuesQueueIndex + 1);
        }

      return eventValuesQueueIndex;
     }

public:
   /**
   * Default constructor
   */
                     OnTradeEventDetector(void)
     {
      debug = false;
      isRepeat = false;
      eventValuesQueueIndex = -1;
     };

   bool              Start()
     {
      AddEventValues();

      if(isRepeat == false)
        {
         MakeListOf(pendingOrders);
         MakeListOf(positions);
        }

      bool success = false;

      if(!success)
         success = DetectEvent(previousPendingOrders, pendingOrders);

      if(!success)
         success = DetectEvent(previousPositions, positions);

      //CopyList(previousPendingOrders, pendingOrders);
      //CopyList(previousPositions, positions);

      isRepeat = success; // Repeat until no success

      return success;
     }

   void              End()
     {
      RemoveEventValues();
     }

   string            EventValueReason() {return eventValues[eventValuesQueueIndex].reason;}
   string            EventValueDetail() {return eventValues[eventValuesQueueIndex].detail;}

   int               EventValueType() {return eventValues[eventValuesQueueIndex].type;}

   datetime          EventValueTimeClose()      {return eventValues[eventValuesQueueIndex].timeClose;}
   datetime          EventValueTimeOpen()       {return eventValues[eventValuesQueueIndex].timeOpen;}
   datetime          EventValueTimeExpiration() {return eventValues[eventValuesQueueIndex].timeExpiration;}

   long              EventValueMagic()  {return eventValues[eventValuesQueueIndex].magic;}
   long              EventValueTicket() {return eventValues[eventValuesQueueIndex].ticket;}

   double            EventValueCommission() {return eventValues[eventValuesQueueIndex].commission;}
   double            EventValuePriceOpen()  {return eventValues[eventValuesQueueIndex].priceOpen;}
   double            EventValuePriceClose() {return eventValues[eventValuesQueueIndex].priceClose;}
   double            EventValueProfit()     {return eventValues[eventValuesQueueIndex].profit;}
   double            EventValueStopLoss()   {return eventValues[eventValuesQueueIndex].stopLoss;}
   double            EventValueSwap()       {return eventValues[eventValuesQueueIndex].swap;}
   double            EventValueTakeProfit() {return eventValues[eventValuesQueueIndex].takeProfit;}
   double            EventValueVolume()     {return eventValues[eventValuesQueueIndex].volume;}

   string            EventValueComment() {return eventValues[eventValuesQueueIndex].comment;}
   string            EventValueSymbol()  {return eventValues[eventValuesQueueIndex].symbol;}
  };
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

class Value7_left
  {
public:

      string               value;
   string               adjust;
   //for pips
   int               pips_mode;
   string            symbol;
   //for time (phase 2)
   //defined by user
   int               mode_time;
   int               time_source;
   string            time_stamp;
   int               time_candle_id;
   string            time_market;
   ENUM_TIMEFRAMES   time_candle_timeframe;
   int               time_component_year;
   int               time_component_month;
   double            time_component_day;
   double            time_component_hour;
   double            time_component_minute;
   int               time_component_second;
   datetime          time_value;
   int               mode_time_shift;
   int               time_shift_years;
   int               time_shift_months;
   int               time_shift_weeks;
   double            time_shift_days;
   double            time_shift_hours;
   double            time_shift_minutes;
   int               time_shift_seconds;
   bool              time_skip_weekdays;
   //defined by system
   datetime          retval;
   datetime          retval0;
   datetime          Time[];
   string            msymbol;

public:

   void              init()

     {
              value = 1;
      //for pips
      pips_mode = VALUE_PIPS_AS_IS;
      symbol = NULL;
      //for time (phase 2)
      //defined by user
      mode_time = 0;
      time_source = 0;
      time_stamp = "00:00";
      time_candle_id = 1;
      time_market = NULL;
      time_candle_timeframe = 0;
      time_component_year = 0;
      time_component_month = 0;
      time_component_day = 0.0;
      time_component_hour = 12.0;
      time_component_minute = 0.0;
      time_component_second = 0;
      time_value = 0;
      mode_time_shift = 0;
      time_shift_years = 0;
      time_shift_months = 0;
      time_shift_weeks = 0;
      time_shift_days = 0.0;
      time_shift_hours = 0.0;
      time_shift_minutes = 0.0;
      time_shift_seconds = 0;
      time_skip_weekdays = False;
      //defined by system
      retval =  0;
      retval0 =  0;

     }

   template<typename T>
   T              calc()
     {
      msymbol = getSymbol(symbol);
      double result = 0;
      string value_type = "Numeric";
      if(value_type=="Numeric" || value_type=="Boolean" || value_type=="Color" || value_type=="Text")
        {
         result = value;
        }
      else
         if(value_type=="Text_code_input")
           {
            result = "\"" + value + "\"";
           }
         else
            if(value_type=="Pips")
              {

               if(pips_mode == VALUE_PIPS_AS_IS)
                 {
                  result = value;
                 }
               else
                  if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                    {
                     double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                     result = point*10*(double)value;  //STest, *10 works for all symbols?
                    }
              }
            else
               if(value_type=="Time")
                 {

                  if(time_market == "" || time_market == NULL)
                     time_market = Symbol();

                  if(mode_time == MODE_TIME_NOW)
                    {
                     if(time_source == TIME_SERVER)
                       {
                        retval = TimeCurrent();
                       }
                     else
                        if(time_source == TIME_LOCAL)
                          {
                           retval = TimeLocal() + (TimeCurrent() - TimeLocal());
                          }
                        else
                           if(time_source == TIME_GMT)
                             {
                              retval = TimeGMT() + (TimeCurrent() - TimeGMT());
                             }
                    }
                  else
                     if(mode_time == MODE_TIME_TIMESTAMP)
                       {
                        retval  = StringToTime(time_stamp);
                        retval0 = retval;
                       }
                     else
                        if(mode_time==MODE_TIME_COMPONENTS)
                          {
                           retval = TimeFromComponents(time_source, time_component_year, time_component_month, time_component_day, time_component_hour, time_component_minute, time_component_second);
                          }
                        else
                           if(mode_time == MODE_TIME_CANDLE_TIME)
                             {
                              ArraySetAsSeries(Time,true);
                              CopyTime(time_market,time_candle_timeframe,time_candle_id,1,Time);
                              retval = Time[0];
                             }
                           else
                              if(mode_time == MODE_TIME_TIME_VALUE)
                                {
                                 retval = time_value;
                                }

                  if(mode_time_shift > 0)
                    {
                     int sh = 1;

                     if(mode_time_shift == 1)
                       {
                        sh = -1;
                       }

                     if(time_shift_years > 0 || time_shift_months > 0)
                       {
                        int year = 0, month = 0, week = 0, day = 0, hour = 0, minute = 0, second = 0;

                        if(mode_time == MODE_TIME_CANDLE_TIME) //STest, It sounds component mode is expected. A bug from fxd?
                          {
                           year   = time_component_year;
                           month  = time_component_month;
                           day    = (int)MathFloor(time_component_day);
                           hour   = (int)(MathFloor(time_component_hour) + (24 * (time_component_day - MathFloor(time_component_day))));
                           minute = (int)(MathFloor(time_component_minute) + (60 * (time_component_hour - MathFloor(time_component_hour))));
                           second = (int)(time_component_second + (60 * (time_component_minute - MathFloor(time_component_minute))));
                          }
                        else
                          {
                           year   = TimeYear(retval);
                           month  = TimeMonth(retval);
                           day    = TimeDay(retval);
                           hour   = TimeHour(retval);
                           minute = TimeMinute(retval);
                           second = TimeSeconds(retval);
                          }

                        year  = year + time_component_year * sh;
                        month = month + time_component_month * sh;

                        if(month < 0)
                          {
                           month = 12 - month;
                          }
                        else
                           if(month > 12)
                             {
                              month = month - 12;
                             }

                        retval = StringToTime(IntegerToString(year)+"."+IntegerToString(month)+"."+IntegerToString(day)+" "+IntegerToString(hour)+":"+IntegerToString(minute)+":"+IntegerToString(second));
                       }

                     retval = retval + (sh * ((604800 * time_shift_weeks) + SecondsFromComponents(time_shift_days, time_shift_hours, time_shift_minutes, time_shift_seconds)));

                     if(time_skip_weekdays == true)
                       {
                        int weekday = TimeDayOfWeek(retval);

                        if(sh > 0)    // forward
                          {
                           if(weekday == 0)
                             {
                              retval = retval + 86400;
                             }
                           else
                              if(weekday == 6)
                                {
                                 retval = retval + 172800;
                                }
                          }
                        else
                           if(sh < 0) // back
                             {
                              if(weekday == 0)
                                {
                                 retval = retval - 172800;
                                }
                              else
                                 if(weekday == 6)
                                   {
                                    retval = retval - 86400;
                                   }
                             }
                       }
                    }

                  result = retval;
                 }
      return result;
     }
  };

class Value7_right
  {
public:

      string               value;
   string               adjust;
   //for pips
   int               pips_mode;
   string            symbol;
   //for time (phase 2)
   //defined by user
   int               mode_time;
   int               time_source;
   string            time_stamp;
   int               time_candle_id;
   string            time_market;
   ENUM_TIMEFRAMES   time_candle_timeframe;
   int               time_component_year;
   int               time_component_month;
   double            time_component_day;
   double            time_component_hour;
   double            time_component_minute;
   int               time_component_second;
   datetime          time_value;
   int               mode_time_shift;
   int               time_shift_years;
   int               time_shift_months;
   int               time_shift_weeks;
   double            time_shift_days;
   double            time_shift_hours;
   double            time_shift_minutes;
   int               time_shift_seconds;
   bool              time_skip_weekdays;
   //defined by system
   datetime          retval;
   datetime          retval0;
   datetime          Time[];
   string            msymbol;

public:

   void              init()

     {
              value = 1;
      //for pips
      pips_mode = VALUE_PIPS_AS_IS;
      symbol = NULL;
      //for time (phase 2)
      //defined by user
      mode_time = 0;
      time_source = 0;
      time_stamp = "00:00";
      time_candle_id = 1;
      time_market = NULL;
      time_candle_timeframe = 0;
      time_component_year = 0;
      time_component_month = 0;
      time_component_day = 0.0;
      time_component_hour = 12.0;
      time_component_minute = 0.0;
      time_component_second = 0;
      time_value = 0;
      mode_time_shift = 0;
      time_shift_years = 0;
      time_shift_months = 0;
      time_shift_weeks = 0;
      time_shift_days = 0.0;
      time_shift_hours = 0.0;
      time_shift_minutes = 0.0;
      time_shift_seconds = 0;
      time_skip_weekdays = False;
      //defined by system
      retval =  0;
      retval0 =  0;

     }

   template<typename T>
   T              calc()
     {
      msymbol = getSymbol(symbol);
      double result = 0;
      string value_type = "Numeric";
      if(value_type=="Numeric" || value_type=="Boolean" || value_type=="Color" || value_type=="Text")
        {
         result = value;
        }
      else
         if(value_type=="Text_code_input")
           {
            result = "\"" + value + "\"";
           }
         else
            if(value_type=="Pips")
              {

               if(pips_mode == VALUE_PIPS_AS_IS)
                 {
                  result = value;
                 }
               else
                  if(pips_mode == VALUE_PIPS_AS_PRICE_FRACTION)
                    {
                     double point = SymbolInfoDouble(msymbol,SYMBOL_POINT);
                     result = point*10*(double)value;  //STest, *10 works for all symbols?
                    }
              }
            else
               if(value_type=="Time")
                 {

                  if(time_market == "" || time_market == NULL)
                     time_market = Symbol();

                  if(mode_time == MODE_TIME_NOW)
                    {
                     if(time_source == TIME_SERVER)
                       {
                        retval = TimeCurrent();
                       }
                     else
                        if(time_source == TIME_LOCAL)
                          {
                           retval = TimeLocal() + (TimeCurrent() - TimeLocal());
                          }
                        else
                           if(time_source == TIME_GMT)
                             {
                              retval = TimeGMT() + (TimeCurrent() - TimeGMT());
                             }
                    }
                  else
                     if(mode_time == MODE_TIME_TIMESTAMP)
                       {
                        retval  = StringToTime(time_stamp);
                        retval0 = retval;
                       }
                     else
                        if(mode_time==MODE_TIME_COMPONENTS)
                          {
                           retval = TimeFromComponents(time_source, time_component_year, time_component_month, time_component_day, time_component_hour, time_component_minute, time_component_second);
                          }
                        else
                           if(mode_time == MODE_TIME_CANDLE_TIME)
                             {
                              ArraySetAsSeries(Time,true);
                              CopyTime(time_market,time_candle_timeframe,time_candle_id,1,Time);
                              retval = Time[0];
                             }
                           else
                              if(mode_time == MODE_TIME_TIME_VALUE)
                                {
                                 retval = time_value;
                                }

                  if(mode_time_shift > 0)
                    {
                     int sh = 1;

                     if(mode_time_shift == 1)
                       {
                        sh = -1;
                       }

                     if(time_shift_years > 0 || time_shift_months > 0)
                       {
                        int year = 0, month = 0, week = 0, day = 0, hour = 0, minute = 0, second = 0;

                        if(mode_time == MODE_TIME_CANDLE_TIME) //STest, It sounds component mode is expected. A bug from fxd?
                          {
                           year   = time_component_year;
                           month  = time_component_month;
                           day    = (int)MathFloor(time_component_day);
                           hour   = (int)(MathFloor(time_component_hour) + (24 * (time_component_day - MathFloor(time_component_day))));
                           minute = (int)(MathFloor(time_component_minute) + (60 * (time_component_hour - MathFloor(time_component_hour))));
                           second = (int)(time_component_second + (60 * (time_component_minute - MathFloor(time_component_minute))));
                          }
                        else
                          {
                           year   = TimeYear(retval);
                           month  = TimeMonth(retval);
                           day    = TimeDay(retval);
                           hour   = TimeHour(retval);
                           minute = TimeMinute(retval);
                           second = TimeSeconds(retval);
                          }

                        year  = year + time_component_year * sh;
                        month = month + time_component_month * sh;

                        if(month < 0)
                          {
                           month = 12 - month;
                          }
                        else
                           if(month > 12)
                             {
                              month = month - 12;
                             }

                        retval = StringToTime(IntegerToString(year)+"."+IntegerToString(month)+"."+IntegerToString(day)+" "+IntegerToString(hour)+":"+IntegerToString(minute)+":"+IntegerToString(second));
                       }

                     retval = retval + (sh * ((604800 * time_shift_weeks) + SecondsFromComponents(time_shift_days, time_shift_hours, time_shift_minutes, time_shift_seconds)));

                     if(time_skip_weekdays == true)
                       {
                        int weekday = TimeDayOfWeek(retval);

                        if(sh > 0)    // forward
                          {
                           if(weekday == 0)
                             {
                              retval = retval + 86400;
                             }
                           else
                              if(weekday == 6)
                                {
                                 retval = retval + 172800;
                                }
                          }
                        else
                           if(sh < 0) // back
                             {
                              if(weekday == 0)
                                {
                                 retval = retval - 172800;
                                }
                              else
                                 if(weekday == 6)
                                   {
                                    retval = retval - 86400;
                                   }
                             }
                       }
                    }

                  result = retval;
                 }
      return result;
     }
  };

//Once per bar
class Task4 : public Task
  {
      string                   symbol;
   ENUM_TIMEFRAMES       timeframe;
   int                max_times_to_pass;
   // System parameters Parameters
   string            tokens[];
   int               passes[];
   datetime          old_values[];
public:
                     Task4(string name):Task(name)
     {
         symbol = "";
      timeframe = PERIOD_CURRENT;
      max_times_to_pass = 1;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
            Task::run(block_id, block);
     
      string msymbol = getSymbol(symbol);
      int mtimeframe = getTimeframe(timeframe);

      bool next    = false;
      string token = msymbol + IntegerToString(mtimeframe);
      int index    = ArraySearch(tokens, token);

      if(index == -1)
        {
         index = ArraySize(tokens);

         ArrayResize(tokens, index + 1);
         ArrayResize(old_values, index + 1);
         ArrayResize(passes, index + 1);

         tokens[index] = token;
         passes[index] = 0;
         old_values[index] = 0;
        }

      if(max_times_to_pass > 0)
        {

         datetime new_value = iTime(msymbol, mtimeframe, 1);

         if(new_value == 0)
           {
            Print("Failed to get the time from candle 1 on symbol ", msymbol, " and timeframe ", EnumToString((ENUM_TIMEFRAMES)mtimeframe), ". The history data needs to be fixed.");
           }

         if(new_value > old_values[index])
           {
            passes[index]++;

            if(passes[index] >= max_times_to_pass)
              {
               old_values[index]  = new_value;
               passes[index] = 0;
              }

            next = true;
           }
        }

      if(next)
        {
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level) {
      
   }
      template<typename T>
   int               ArraySearch(T &array[], T value)
     {
      int index = -1;
      int size  = ArraySize(array);

      for(int i = 0; i < size; i++)
        {
         if(array[i] == value)
           {
            index = i;
            break;
           }
        }

      return index;
     }

  };

//Formula
class Task7 : public Task
  {
   
public:
                     Task7(string name):Task(name)
     {
         
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      Value7_left value7_left;
   value7_left.init();
   double valueValue7_left = value7_left.calc<double>();
      Value7_right value7_right;
   value7_right.init();
   double valueValue7_right = value7_right.calc<double>();
      string undefined_var_1 = (valueValue7_left + valueValue7_right);
      
      //printf("task"+block_id + " passed route 1");
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
   int               event;


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
         //-1 : block id to block index
         switch (event){
            case EVENT_ON_INIT  : runBlockInit  (id, ROUTE_1_PASSED, nexts_true[i]); break;
            case EVENT_ON_TIMER : runBlockTimer (id, ROUTE_1_PASSED, nexts_true[i]); break;
            case EVENT_ON_TICK  : runBlockTick  (id, ROUTE_1_PASSED, nexts_true[i]); break;
            case EVENT_ON_TRADE : runBlockTrade (id, ROUTE_1_PASSED, nexts_true[i]); break;
            case EVENT_ON_CHART : runBlockChart (id, ROUTE_1_PASSED, nexts_true[i]); break;
            case EVENT_ON_DEINIT: runBlockDeinit(id, ROUTE_1_PASSED, nexts_true[i]); break;
        }
     }

   virtual void      next_false()
     {
      for(int i=0; i<ArraySize(nexts_false); i++)
         switch (event){
            case EVENT_ON_INIT  : runBlockInit  (id, ROUTE_2_PASSED, nexts_false[i]); break;
            case EVENT_ON_TIMER : runBlockTimer (id, ROUTE_2_PASSED, nexts_false[i]); break;
            case EVENT_ON_TICK  : runBlockTick  (id, ROUTE_2_PASSED, nexts_false[i]); break;
            case EVENT_ON_TRADE : runBlockTrade (id, ROUTE_2_PASSED, nexts_false[i]); break;
            case EVENT_ON_CHART : runBlockChart (id, ROUTE_2_PASSED, nexts_false[i]); break;
            case EVENT_ON_DEINIT: runBlockDeinit(id, ROUTE_2_PASSED, nexts_false[i]); break;
        }
     }

   virtual void              run(int source_id, int source_result)
     {
      if(!enabled)
         return;
      addToHistory(source_id, source_result);
      current_source_id = source_id;
      task.run(id_by_user, this);

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

class Block4 : public Block
  {
public:
                     Block4()
     {
      id = 0;
      id_by_user = 4;
      name = "once_per_bar";
      enabled = True;
      event = EVENT_ON_TICK;

      int mnexts_true[] = {1};
      int mnexts_false[] = {};
      int mprevs_true[] = {};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task4(name);
     }
  };
class Block7 : public Block
  {
public:
                     Block7()
     {
      id = 1;
      id_by_user = 7;
      name = "formula";
      enabled = True;
      event = EVENT_ON_TICK;

      int mnexts_true[] = {};
      int mnexts_false[] = {};
      int mprevs_true[] = {0};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task7(name);
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
OnChartEventHolder onchartEventHolder; 
OnTradeEventDetector onTradeEventDetector;bool exit_loop = false;
int timer_period = 60;//seconds
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
ArrayResize(blocks_tick, 2);
Block4 *block4 = new Block4();
Block7 *block7 = new Block7();

blocks_tick[0] = block4;
blocks_tick[1] = block7;
  }
void resetBlocksTick(int level)
{
    for(int i=0; i<ArraySize(blocks_tick); i++){
        blocks_tick[i].reset(level);
    }
}void runBlockChart(int source_id, int source_result, int dest_id)
{
blocks_chart[dest_id].run(source_id, source_result);
}void addBlocksChart()
{
ArrayResize(blocks_chart, 0);

  }
void resetBlocksChart(int level)
{
    for(int i=0; i<ArraySize(blocks_chart); i++){
        blocks_chart[i].reset(level);
    }
}void runBlockTrade(int source_id, int source_result, int dest_id)
{
blocks_trade[dest_id].run(source_id, source_result);
}void addBlocksTrade()
{
ArrayResize(blocks_trade, 0);

  }
void resetBlocksTrade(int level)
{
    for(int i=0; i<ArraySize(blocks_trade); i++){
        blocks_trade[i].reset(level);
    }
}void runBlockTimer(int source_id, int source_result, int dest_id)
{
blocks_timer[dest_id].run(source_id, source_result);
}void addBlocksTimer()
{
ArrayResize(blocks_timer, 0);

  }
void resetBlocksTimer(int level)
{
    for(int i=0; i<ArraySize(blocks_timer); i++){
        blocks_timer[i].reset(level);
    }
}void runBlockInit(int source_id, int source_result, int dest_id)
{
blocks_init[dest_id].run(source_id, source_result);
}void addBlocksInit()
{
ArrayResize(blocks_init, 0);

  }
void resetBlocksInit(int level)
{
    for(int i=0; i<ArraySize(blocks_init); i++){
        blocks_init[i].reset(level);
    }
}void runBlockDeinit(int source_id, int source_result, int dest_id)
{
blocks_deinit[dest_id].run(source_id, source_result);
}void addBlocksDeinit()
{
ArrayResize(blocks_deinit, 0);

  }
void resetBlocksDeinit(int level)
{
    for(int i=0; i<ArraySize(blocks_deinit); i++){
        blocks_deinit[i].reset(level);
    }
}string syncSymbolOverriding(string symbol) {
 return overriding_symbol == "" ? symbol : overriding_symbol;
}int syncTimeframeOverriding(int timeframe) {
 return overriding_timeframe == -1 ? timeframe : overriding_timeframe;
 }datetime TimeFromString(int mode_time, string stamp)
  {
   datetime t = 0;

   if(mode_time == 0)
      t = TimeCurrent();
   else
      if(mode_time == 1)
         t = TimeLocal();
      else
         if(mode_time == 2)
            t = TimeGMT();

   int stamplen = StringLen(stamp);

   if(stamplen < 9)
     {
      int thour    = TimeHour(t);
      int tminute  = TimeMinute(t);
      int tseconds = TimeSeconds(t);

      int hour   = (int)StringSubstr(stamp, 0, 2);
      int minute = (int)StringSubstr(stamp, 3, 2);
      int second = 0;

      if(stamplen > 5)
        {
         second = (int)StringSubstr(stamp, 6, 2);
        }

      datetime t1 = (datetime)(t - (thour-hour)*3600 - (tminute - minute)*60 - (tseconds-second));

      return t1;
     }

   return StringToTime(stamp);
  }

datetime TimeFromComponents(
   int time_src = 0,
   int    y = 0,
   int    m = 0,
   double d = 0,
   double h = 0,
   double i = 0,
   int    s = 0
)
  {
   MqlDateTime tm;
   int offset = 0;

   if(time_src == 0)
     {
      TimeCurrent(tm);
     }
   else
      if(time_src == 1)
        {
         TimeLocal(tm);
         offset = (int)(TimeLocal() - TimeCurrent());
        }
      else
         if(time_src == 2)
           {
            TimeGMT(tm);
            offset = (int)(TimeGMT() - TimeCurrent());
           }

   if(y > 0)
     {
      if(y < 100)
        {
         y = 2000 + y;
        }
      tm.year = y;
     }
   if(m > 0)
     {
      tm.mon = m;
     }
   if(d > 0)
     {
      tm.day = (int)MathFloor(d);
     }

   tm.hour = (int)(MathFloor(h) + (24 * (d - MathFloor(d))));
   tm.min  = (int)(MathFloor(i) + (60 * (h - MathFloor(h))));
   tm.sec  = (int)((double)s + (60 * (i - MathFloor(i))));

   datetime time = StructToTime(tm) - offset;

   return time;
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
   bool historyTrades  = look_up_on == LOOK_UP_HISTORY_ONLY ? true : false;

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
      string symbols[];
      AddToArray(symbols, msymbol);
      bool x = filterGeneral(symbols, SYMBOL_MODE_SPECIFIED, type, group_mode, group);
      return x;
     }

   return false;
  }
bool HistoryTradeSelectByIndex(
   int index,
   string group_mode,
   string group,
   string msymbol,
   int type[]
)
  {
   if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)
     {
      string symbols[];
      AddToArray(symbols, msymbol);
      bool x = filterGeneral(symbols, SYMBOL_MODE_SPECIFIED, type, group_mode, group);
      return x;
     }

   return false;
  }   bool              filterGeneral(string symbols[], int symbol_mode, int type[], int group_mode, int group_number)
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }int SymbolDigits(string symbol)
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

template<typename T>
string FormatValueForPrinting(T value, int digits, int timeFormat)
  {
   string outputValue = "";
   string typeName    = typename(value);

   if(typeName == "double" || typeName == "float")
     {
      if(digits >= -16 && digits <= 8)
        {
         if(value > -1.0 && value < 1.0)
           {
            /**
            * Find how many zeroes are after the point, but before the first non-zero digit.
            * For example 0.000195 has 3 zeroes
            * The function would return negative value for values bigger than 0
            *
            * @see https://stackoverflow.com/questions/31001901/how-can-i-count-the-number-of-zero-decimals-in-javascript/31002148#31002148
            */
            int zeroesAfterPoint = (int)-MathFloor(MathLog10(MathAbs(value)) + 1);

            digits = zeroesAfterPoint + digits;
           }

         T normalizedValue  = NormalizeDouble(value, digits);
         outputValue = DoubleToString(normalizedValue, digits);
        }
      else
        {
         outputValue = (string)NormalizeDouble(value, 8);
        }
     }
   else
     {
      outputValue = IntegerToString((long)value);
     }

   return outputValue;
  }




/**
* Bool overload
*/
string FormatValueForPrinting(
   bool value,
   int digits,
   int timeFormat
)
  {
   return (value) ? "true" : "false";
  }

/**
* Datetime overload
*/
string FormatValueForPrinting(
   datetime value,
   int digits,
   int timeFormat
)
  {
   if(timeFormat == (int)EMPTY_VALUE || timeFormat == EMPTY_VALUE)
      timeFormat = TIME_DATE|TIME_MINUTES;
   return TimeToString(value, timeFormat);
  }

/**
* String overload
*/
string FormatValueForPrinting(
   string value,
   int digits,
   int timeFormat
)
  {
   return value;
  }
int WindowFindVisible(long chart_id, string term)
  {
//-- the search term can be chart name, such as Force(13), or subwindow index
   if(term == "" || term == "0")
     {
      return 0;
     }

   int subwindow = (int)StringToInteger(term);

   if(subwindow == 0 && StringLen(term) > 1)
     {
      subwindow = ChartWindowFind(chart_id, term);
     }

   if(subwindow > 0 && !ChartGetInteger(chart_id, CHART_WINDOW_IS_VISIBLE, subwindow))
     {
      return -1;
     }

   return subwindow;
  }
double SymbolAsk(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return SymbolInfoDouble(symbol, SYMBOL_ASK);
  }double SymbolBid(string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return SymbolInfoDouble(symbol, SYMBOL_BID);
  }bool IsOrderTypeBuy()
  {
   int type = OrderType();

   return (type == OP_BUY || type == OP_BUYSTOP || type == OP_BUYLIMIT);
  }bool IsOrderTypeStop()
  {
   int type = OrderType();

   return (type == OP_BUYSTOP || type == OP_SELLSTOP);
  }string getSymbol(string symbol)
  {
   return (symbol==NULL || symbol=="") && overriding_symbol != "" ? overriding_symbol : (symbol==NULL || symbol=="") ? Symbol() : symbol;
  }int getTimeframe(int timeframe)
  {
   return timeframe==PERIOD_CURRENT && overriding_timeframe != -1 ? overriding_timeframe : timeframe;
  }
bool is_symbol_accepted(int symbol_mode, string &symbols[])
  {
   if(symbol_mode == SYMBOL_MODE_ANY)
     {
      return true;
     }
   else
      if(ArraySize(symbols)==0)
        {
         bool case_1 = OrderSymbol() == getSymbol("");
         bool case_2 = OrderSymbol() == Symbol() && getSymbol("")=="";
         return case_1 || case_2;   
        }
      else
        {
         for(int i=ArraySize(symbols)-1; i>=0; i--)
           {
            string smb = StringTrimRight(symbols[i]);
            smb = StringTrimLeft(smb);
            if(smb==OrderSymbol())
              {
               return true;
              }
           }
        }
   return false;
  }int SecondsFromComponents(double days, double hours, double minutes, int seconds)
  {
   int retval =
      86400 * (int)MathFloor(days)
      + 3600 * (int)(MathFloor(hours) + (24 * (days - MathFloor(days))))
      + 60 * (int)(MathFloor(minutes) + (60 * (hours - MathFloor(hours))))
      + (int)((double)seconds + (60 * (minutes - MathFloor(minutes))));

   return retval;
  }
bool load_object(int index, long chart_id,int sub_window, int obj_type)
  {
   string name = ObjectName(chart_id,index,sub_window, obj_type);

   if(name == "")
     {
      return false;
     }

   loaded_object_chart_id(chart_id);
   loaded_object_name(name);
   loaded_object_subwindow(sub_window);
   loaded_object_type((int)ObjectGetInteger(chart_id,name,OBJPROP_TYPE));

   return true;
  }
long loaded_object_chart_id(long chart_id=-1) {static long memory=-1; if(chart_id>-1) {memory=chart_id;} return(memory);}
string loaded_object_name(string name="") {static string memory=""; if(name!="") {memory=name;} return(memory);}
int loaded_object_subwindow(int sub_window=-2) {static int memory=-2; if(sub_window>-2) {memory=sub_window;} return(memory);}
int loaded_object_type(int type=-2) {static int memory=-2; if(type>-2) {memory=type;} return(memory);}
template<typename T>
bool array_ensure_value(T &array[], T value)
  {
   int size   = ArraySize(array);

   if(size > 0)
     {
      if(in_array(array, value))
        {
         // value found -> exit
         return false; // no value added
        }
     }

// value does not exists -> add it
   ArrayResize(array, size+1);
   array[size] = value;

   return true; // value added
  }
template<typename T>
bool in_array(T &array[], T value)
  {
   int size = ArraySize(array);

   if(size > 0)
     {
      for(int i = 0; i < size; i++)
        {
         if(array[i] == value)
           {
            return true;
           }
        }
     }

   return false;
  }
double ObjectGetValueByShift(long chart_id, string name, int shift)
{
	MqlRates rates[];
	CopyRates(NULL, PERIOD_CURRENT, shift, 1, rates);

	return ObjectGetValueByTime(chart_id, name, rates[0].time, 0);
}template<typename T>
bool ArrayStripKey(T &array[], int key)
  {
   int x    = 0;
   int size = ArraySize(array);

   for(int i=0; i<size; i++)
     {
      if(i != key)
        {
         array[x] = array[i];
         x++;
        }
     }

   if(x < size)
     {
      ArrayResize(array, x);

      return true; // stripped
     }

   return false; // not stripped
  }

long attrTicketParent(long ticket)
  {
   int pos = 0;
   int total = 0;
   long retval = 0;
   static long cacheTickets[];
   static long cacheValues[];

//-- return cached value if possible
   int size = ArraySize(cacheTickets);
   int idx  = -1;

   for(int i = size-1; i >= 0; i--)
     {
      if(cacheTickets[i] == ticket)
        {
         return cacheValues[i];
        }
     }

   if(!OrderSelect((int)ticket, SELECT_BY_TICKET))
     {
      retval = ticket;
     }

//-- check if trade is added to volume
   if(retval == 0)
     {
      string comment = OrderComment();
      int tagPos     = StringFind(comment, "[p=");

      if(tagPos >= 0)
        {
         string tag = StringSubstr(comment, tagPos);
         tag        = StringSubstr(tag, 0, StringFind(tag, "]") + 1);
         retval     = (int)StringToInteger(StringSubstr(tag, 3, -1));
        }
     }

   double OP   = OrderOpenPrice();
   datetime OT = OrderOpenTime();
   string S    = OrderSymbol();
   int M       = OrderMagicNumber();
   int T       = OrderType();
   double L    = OrderLots();
   int D       = (int)MarketInfo(S, MODE_DIGITS);

//-- check if trade is partially closed
   if(retval == 0)
     {
      total = OrdersHistoryTotal();

      for(pos = total-1; pos >= 0; pos--)
        {
         if(OrderSelect(pos, SELECT_BY_POS, MODE_HISTORY))
           {
            if(OrderOpenTime() < OT)
              {
               break;
              }

            if(
               (OrderMagicNumber() == M)
               && (OrderTicket() < ticket)
               && (OrderType() == T)
               && (OrderOpenTime() == OT)
               && (NormalizeDouble(OrderOpenPrice(), D) == NormalizeDouble(OP, D))
               && (OrderSymbol() == S)
            )
              {
               retval = OrderTicket();
              }
           }
        }
     }

   if(retval > 0)
     {
      size = ArraySize(cacheTickets);
      ArrayResize(cacheTickets, size + 1);
      ArrayResize(cacheValues,size + 1);
      cacheTickets[size] = ticket;
      cacheValues[size]  = retval;
     }

// Load the original trade again
   if(!OrderSelect((int)ticket,SELECT_BY_TICKET))
     {
      retval = ticket;
     }

   if(retval <= 0)
     {
      retval = ticket;
     }

   return retval;
  }
string e_Reason() {return onTradeEventDetector.EventValueReason();}

string e_ReasonDetail() {return onTradeEventDetector.EventValueDetail();}

double e_attrClosePrice() {return onTradeEventDetector.EventValuePriceClose();}

datetime e_attrCloseTime() {return onTradeEventDetector.EventValueTimeClose();}

string e_attrComment() {return onTradeEventDetector.EventValueComment();}

datetime e_attrExpiration() {return onTradeEventDetector.EventValueTimeExpiration();}

double e_attrLots() {return onTradeEventDetector.EventValueVolume();}

int e_attrMagicNumber() {return (int)onTradeEventDetector.EventValueMagic();}

double e_attrOpenPrice() {return onTradeEventDetector.EventValuePriceOpen();}

datetime e_attrOpenTime() {return onTradeEventDetector.EventValueTimeOpen();}

double e_attrProfit() {return onTradeEventDetector.EventValueProfit();}

double e_attrStopLoss() {return onTradeEventDetector.EventValueStopLoss();}

double e_attrSwap() {return onTradeEventDetector.EventValueSwap();}

string e_attrSymbol() {return onTradeEventDetector.EventValueSymbol();}

double e_attrTakeProfit() {return onTradeEventDetector.EventValueTakeProfit();}

int e_attrTicket() {return (int)onTradeEventDetector.EventValueTicket();}

int e_attrType() {return onTradeEventDetector.EventValueType();}

double toPips(double digits, string symbol)
  {
   if(symbol == "")
      symbol = Symbol();

   return digits / (PipValue(symbol) * SymbolInfoDouble(symbol, SYMBOL_POINT));
  }

int OnInit(){
addBlocksTick();addBlocksChart();addBlocksTrade();addBlocksTimer();addBlocksDeinit();addBlocksInit();resetBlocksInit(RESET_LEVEL_DEFAULT);
       if (ArraySize(blocks_timer)>0)
           EventSetTimer(timer_period);
    	return(INIT_SUCCEEDED);
}
void OnTimer(){
resetBlocksTimer(RESET_LEVEL_DEFAULT);
}
void OnTick(){
resetBlocksTick(RESET_LEVEL_TICK);runBlockTick(-1, -1, 0);   if(ArraySize(blocks_trade)>0)
      OnTrade();
}
void OnTrade(){
resetBlocksTrade(RESET_LEVEL_DEFAULT);   while(onTradeEventDetector.Start())
{
     }

    onTradeEventDetector.End();
}
void OnChartEvent(const int id,         // Event identifier
const long& lparam,   // Event parameter of long type
const double& dparam, // Event parameter of double type
const string& sparam  // Event parameter of string type
){

//hold event params then process blocks
   onchartEventHolder.id     = id;
   onchartEventHolder.lparam = lparam;
   onchartEventHolder.dparam = dparam;
   onchartEventHolder.sparam = sparam;resetBlocksChart(RESET_LEVEL_DEFAULT);
}
void OnDeinit(const int reason){
resetBlocksDeinit(RESET_LEVEL_DEFAULT);
}



//g-v: 0.2.10
