class Task1 : public Task
  {
   string                RelativeTo;
   string                NewSLmode;
   double                NewStopLoss;
   double                NewStopLossPercentPrice;
   double                NewStopLossPercent;
   double                NewStopLossPercentTP;
   string               NewTPmode;
   double               NewTakeProfit;
   double               NewTakeProfitPercentPrice;
   double               NewTakeProfitPercent;
   double               NewTakeProfitPercentSL;
   color               LevelColor;
public:
                     Task1(string name):Task(name)
     {
      RelativeTo = (string)"openprice";
      NewSLmode = (string)"fixed";
      NewStopLoss = (double)50.0;
      NewStopLossPercentPrice = (double)0.55;
      NewStopLossPercent = (double)50.0;
      NewStopLossPercentTP = (double)50.0;
      NewTPmode = (string)"fixed";
      NewTakeProfit = (double)50.0;
      NewTakeProfitPercentPrice = (double)0.55;
      NewTakeProfitPercent = (double)50.0;
      NewTakeProfitPercentSL = (double)50.0;
      LevelColor = (color)clrDeepPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(exit_loop)
        {
         return;
        }

      //LoopedResume();

      string symbol = OrderSymbol();
      int digits    = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);
      int polarity  = (IsOrderTypeBuy()) ? 1 : -1;
      double price  = (IsOrderTypeBuy()) ? SymbolAsk(symbol) : SymbolBid(symbol);

      //-- New Price level ------------------------------------------------------------------------------------------------------------------------
      if(RelativeTo == "openprice")
        {
         price = OrderOpenPrice();
        }
      else
         if(RelativeTo == "dynamic")
           {
            Value4_price_fraction val;
            val.init();
            double valueValue = val.calc<double>();
            price = valueValue;

           }
         else
            if(RelativeTo == "current-reverse")
              {
               price = (IsOrderTypeBuy()) ? SymbolBid(symbol) : SymbolAsk(symbol);
              }

      //-- Stop Loss and Take Profit --------------------------------------------------------------------------------------------------------------
      double oldSL = NormalizeDouble(OrderStopLoss(), digits);
      double oldTP = NormalizeDouble(OrderTakeProfit(), digits);
      double SL = oldSL;
      double TP = oldTP;

      if(NewSLmode == "fixed")
        {
         SL = (NewStopLoss == 0.0) ? 0.0 : price - (polarity * toDigits(NewStopLoss, symbol));
        }
      else
         if(NewSLmode == "percentPrice")
           {
            SL = (NewStopLossPercentPrice == 0.0) ? 0.0 : price - (polarity * price * NewStopLossPercentPrice / 100);
           }
         else
            if(NewSLmode == "percent")
              {
               SL = (NewStopLossPercent == 0.0) ? 0.0 : price - (polarity * MathAbs(price-oldSL)*NewStopLossPercent/100);
              }
            else
               if(NewSLmode == "percentTP")
                 {
                  SL = (NewStopLossPercentTP == 0.0) ? 0.0 : price - (polarity * MathAbs(price-oldTP)*NewStopLossPercentTP/100);
                 }
               else
                  if(NewSLmode == "function")
                    {
                     Value4_price_fraction val;
                     val.init();
                     double valueValuex = val.calc<double>();
                     SL = valueValuex;
                    }
                  else
                     if(NewSLmode == "dynamicPips")
                       {
                        Value4_price_fraction val;
                        val.init();
                        double valueValuey = val.calc<double>();
                        SL = toDigits(valueValuey, symbol);
                        SL = (SL == 0.0) ? 0.0 : price - (polarity * SL);
                       }
                     else
                        if(NewSLmode == "dynamicDigits")
                          {
                           Value4_price_fraction val;
                           val.init();
                           double valueValuer = val.calc<double>();
                           SL = valueValuer;
                           SL = (SL == 0.0) ? 0.0 : price - (polarity * SL);
                          }

      if(NewTPmode == "fixed")
        {
         TP = (NewTakeProfit == 0.0) ? 0.0 : price + (polarity * toDigits(NewTakeProfit, symbol));
        }
      else
         if(NewSLmode == "percentPrice")
           {
            TP = (NewTakeProfitPercentPrice == 0.0) ? 0.0 : price + (polarity * price * NewTakeProfitPercentPrice / 100);
           }
         else
            if(NewTPmode == "percent")
              {
               TP = (NewTakeProfitPercent == 0.0) ? 0.0 : price + (polarity * MathAbs(price-oldTP)*NewTakeProfitPercent/100);
              }
            else
               if(NewTPmode == "percentSL")
                 {
                  TP = (NewTakeProfitPercentSL == 0.0) ? 0.0 : price + (polarity * MathAbs(price-oldSL)*NewTakeProfitPercentSL/100);
                 }
               else
                  if(NewTPmode == "function")
                    {
                     Value4_price_fraction val;
                     val.init();
                     double valueValue12 = val.calc<double>();
                     TP = valueValue12;
                    }
                  else
                     if(NewTPmode == "dynamicPips")
                       {
                        Value4_price_fraction val;
                        val.init();
                        double valueValue232 = val.calc<double>();
                        TP = toDigits(valueValue232, symbol);
                        TP = (TP == 0.0) ? 0.0 : price + (polarity * TP);
                       }
                     else
                        if(NewTPmode == "dynamicDigits")
                          {
                           Value4_price_fraction val;
                           val.init();
                           double valueValue87 = val.calc<double>();
                           TP = valueValue87;
                           TP = (TP == 0.0) ? 0.0 : price + (polarity * TP);
                          }

      //-- Send -----------------------------------------------------------------------------------------------------------------------------------
      bool success = false;

      if(SL != oldSL || TP != oldTP)
        {

         SL = NormalizeDouble(SL, digits);
         TP = NormalizeDouble(TP, digits);
         success = OrderModify(OrderTicket(), OrderOpenPrice(), SL, TP, OrderExpiration(), LevelColor);
         OrderSelect(OrderTicket(),SELECT_BY_TICKET);
        }

      if(success)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };
