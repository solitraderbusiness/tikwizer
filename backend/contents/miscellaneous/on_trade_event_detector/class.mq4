class OnTradeEventDetector
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
