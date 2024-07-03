class Task1 : public Task
  {
   string                DirectionMode;
   int                   PipsAwayReferencePrice;
   int                   OpenPriceMode;
   string                PipsAwayMode;
   double                PipsAway;
   double                PipsAwayPercent;

public:
                     Task1(string name):Task(name)
     {
      DirectionMode = (string)"trading";
      PipsAwayReferencePrice = (int)0;
      OpenPriceMode = (int)0;
      PipsAwayMode = (string)"fixed";
      PipsAway = (double)50.0;
      PipsAwayPercent = (double)150.0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(exit_loop)
         return;

      //LoopedResume(); //STest, commented

      string symbol      = OrderSymbol();
      int digits         = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
      double price       = 0;
      double digits_away = 0;
      bool next          = false;
      bool success       = false;

      // the OpenPrice. In case of children trades, their OpenPrice is the same as the OpenPrice of the parent trade.
      // So, if I want their individual OpenPrice, I can get the ClosePrice of their previous sibling.
      double op     = OrderOpenPrice();
      ulong ticket0 = 0;

      if(OpenPriceMode == 0)
        {
         ulong parent = attrTicketParent(OrderTicket());
         ticket0    = OrderTicket();

         success = OrderSelect((int)parent, SELECT_BY_TICKET, MODE_TRADES) && OrderType() < 2;

         op = OrderOpenPrice();

         success = OrderSelect((int)ticket0, SELECT_BY_TICKET, MODE_TRADES) && OrderType() < 2; // select the trade that was selected
        }
      else
         if(OpenPriceMode == 1)
           {
            op = OrderOpenPriceAsChild();
           }

      if(PipsAwayMode == "fixed")
        {
         digits_away = toDigits(PipsAway, symbol);
        }
      else
         if(PipsAwayMode == "percentSL")
           {
            double sl = NormalizeDouble(MathAbs(OrderStopLoss()-op), digits);
            digits_away  = sl *(PipsAwayPercent/100);
           }
         else
            if(PipsAwayMode == "percentTP")
              {
               double tp = NormalizeDouble(MathAbs(OrderTakeProfit()-op), digits);
               digits_away  = tp *(PipsAwayPercent/100);
              }
            else
               if(PipsAwayMode == "function")
                 {
                  Value5pips value5pips;
                  value5pips.init();
                  double valueValue5pips = value5pips.calc();
                  digits_away = toDigits(valueValue5pips, symbol);
                 }
               else
                  if(PipsAwayMode == "functionFraction")
                    {
                     Value5price_fraction value5price_fraction;
                     value5price_fraction.init();
                     double valueValue5price_fraction = value5price_fraction.calc();
                     digits_away = valueValue5price_fraction;
                    }

      if(IsOrderTypeBuy())
        {
         if(PipsAwayReferencePrice == 0)
            price = SymbolAsk(symbol);
         else
            if(PipsAwayReferencePrice == 1)
               price = SymbolBid(symbol);
            else
               if(PipsAwayReferencePrice == 2)
                  price = (SymbolAsk(symbol) + SymbolBid(symbol)) / 2;

         if(
            (DirectionMode == "single" && digits_away >= 0 && NormalizeDouble(price-op, digits) >= digits_away)
            || (DirectionMode == "single" && digits_away < 0 && NormalizeDouble(price-op, digits) <= digits_away)
            || (DirectionMode == "double" && MathAbs(NormalizeDouble(price-op, digits)) >= MathAbs(digits_away))
            || (DirectionMode == "trading" && digits_away >= 0 && NormalizeDouble(price-op, digits) >= digits_away)
            || (DirectionMode == "trading" && digits_away < 0 && NormalizeDouble(price-op, digits) <= digits_away)
         )
           {
            next = true;
           }
        }
      else
        {
         if(PipsAwayReferencePrice == 0)
            price = SymbolBid(symbol);
         else
            if(PipsAwayReferencePrice == 1)
               price = SymbolAsk(symbol);
            else
               if(PipsAwayReferencePrice == 2)
                  price = (SymbolAsk(symbol) + SymbolBid(symbol)) / 2;

         if(
            (DirectionMode == "single" && digits_away >= 0 && NormalizeDouble(price-op, digits) >= digits_away)
            || (DirectionMode == "single" && digits_away < 0 && NormalizeDouble(price-op, digits) <= digits_away)
            || (DirectionMode == "double" && MathAbs(NormalizeDouble(op-price, digits)) >= MathAbs(digits_away))
            || (DirectionMode == "trading" && digits_away >= 0 && NormalizeDouble(op-price, digits) >= digits_away)
            || (DirectionMode == "trading" && digits_away < 0 && NormalizeDouble(op-price, digits) <= digits_away)
         )
           {
            next = true;
           }
        }


      if(next)
        {
         //printf("task"+block_id + " passed route 1 ");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2 ");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };
