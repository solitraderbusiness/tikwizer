class Task_id : public Task
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
                     Task_id(string name):Task(name)
     {
      RelativeTo = (string)RelativeTo_val;
      NewSLmode = (string)NewSLmode_val;
      NewStopLoss = (double)NewStopLoss_val;
      NewStopLossPercentPrice = (double)NewStopLossPercentPrice_val;
      NewStopLossPercent = (double)NewStopLossPercent_val;
      NewStopLossPercentTP = (double)NewStopLossPercentTP_val;
      NewTPmode = (string)NewTPmode_val;
      NewTakeProfit = (double)NewTakeProfit_val;
      NewTakeProfitPercentPrice = (double)NewTakeProfitPercentPrice_val;
      NewTakeProfitPercent = (double)NewTakeProfitPercent_val;
      NewTakeProfitPercentSL = (double)NewTakeProfitPercentSL_val;
      LevelColor = (color)LevelColor_val;
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
            initializer_rtd
            price = variable_name_rtd;

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
                     initializer_nsmf
                     SL = variable_name_nsmf;
                    }
                  else
                     if(NewSLmode == "dynamicPips")
                       {
                        initializer_nsmdp
                        SL = toDigits(variable_name_nsmdp, symbol);
                        SL = (SL == 0.0) ? 0.0 : price - (polarity * SL);
                       }
                     else
                        if(NewSLmode == "dynamicDigits")
                          {
                           initializer_nsmdd
                           SL = variable_name_nsmdd;
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
                     initializer_ntmf
                     TP = variable_name_ntmf;
                    }
                  else
                     if(NewTPmode == "dynamicPips")
                       {
                        initializer_ntmdp
                        TP = toDigits(variable_name_ntmdp, symbol);
                        TP = (TP == 0.0) ? 0.0 : price + (polarity * TP);
                       }
                     else
                        if(NewTPmode == "dynamicDigits")
                          {
                           initializer_ntmdd
                           TP = variable_name_ntmdd;
                           TP = (TP == 0.0) ? 0.0 : price + (polarity * TP);
                          }

      //-- Send -----------------------------------------------------------------------------------------------------------------------------------
      bool success = false;

      if(SL != oldSL || TP != oldTP)
        {

         SL = NormalizeDouble(SL, digits);
         TP = NormalizeDouble(TP, digits);
         success = OrderModify(OrderTicket(), OrderOpenPrice(), SL, TP, OrderExpiration(), LevelColor);
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
