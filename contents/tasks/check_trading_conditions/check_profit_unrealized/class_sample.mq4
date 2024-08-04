
#define PROFIT_MODE_MONEY "money"
#define PROFIT_MODE_PIPS "pips"
#define PROFIT_MODE_PIPS_SUM "pips-sum"
#define PROFIT_MODE_NO_MATTER "no-matter"



class Task5 : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   string            profit_mode_each;
   double            profit_amount_each;
   string            profit_mode;
   double            profit_amount;

public:
                     Task5(string name):Task(name)
     {
      //specified by user
      symbol_mode = SYMBOL_MODE_ANY;
      symbols_str = "";

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 25;

      each_profit_mode = PROFIT_MODE_NO_MATTER;
      each_profit_amount = 0.0;
      profit_mode = PROFIT_MODE_MONEY;
      profit_amount = 0.0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
      ArrayResize(type, 0, 0);
      int mtype[] = {1,0}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      double avgPrice    = 0;
      double avgLoad     = 0;
      double avgLots     = 0;
      double profitMoney = 0;
      double profitPips  = 0;
      double pipsSum     = 0;
      int tradesCount    = 0;

      for(int index = OrdersTotal()-1; index >= 0; index--)
        {
        if(OrderSelect(index, SELECT_BY_POS, MODE_TRADES))
           {
         if(filterGeneral())
           {
            double OrderOpenPrice = OrderOpenPrice();//STest, this should be replaced with another value which is more exact
            double tradeProfit    = NormalizeDouble(OrderProfit() + OrderSwap() + OrderCommission(), 2);

            // Filter out individual trades
            if(each_profit_mode == PROFIT_MODE_MONEY)
              {
               if(tradeProfit > each_profit_amount)
                 {
                 }
               else
                 {
                  continue;
                 }
              }
            else
               if(each_profit_mode == PROFIT_MODE_PIPS)
                 {
                  double individual_profit = toPips(OrderClosePrice() - OrderOpenPrice, OrderSymbol());

                  if(OrderType() == 1)
                    {
                     individual_profit = -1 * individual_profit;
                    }

                  if(individual_profit <= each_profit_amount)
                    {

                    }
                  else
                    {
                     continue;
                    }
                 }

            profitMoney += tradeProfit;

            if(profit_mode == PROFIT_MODE_PIPS || profit_mode == PROFIT_MODE_PIPS_SUM)
              {
               if(IsOrderTypeBuy())
                 {
                  pipsSum += toPips(OrderClosePrice() - OrderOpenPrice, OrderSymbol());
                  avgLoad += OrderOpenPrice * OrderLots();
                  avgLots += OrderLots();
                 }
               else
                 {
                  pipsSum += toPips(OrderOpenPrice - OrderClosePrice(), OrderSymbol());
                  avgLoad -= OrderOpenPrice * OrderLots();
                  avgLots -= OrderLots();
                 }
              }

            tradesCount += 1;
           }
           }
        }

      //+------------------------------------------------------------------+
      //|                                                                  |
      //+------------------------------------------------------------------+
      if(profit_mode == PROFIT_MODE_PIPS)
        {
         avgPrice = 0;

         if(avgLots != 0)
           {
            avgPrice = (avgLoad / avgLots);
           }

         if(avgPrice != 0)
           {
            if(avgLots > 0)
              {
               profitPips = SymbolInfoDouble(getSymbol(OrderSymbol()), SYMBOL_BID) - avgPrice;
              }
            else
              {
               profitPips = avgPrice - SymbolInfoDouble(getSymbol(OrderSymbol()), SYMBOL_ASK);
              }

            profitPips = toPips(profitPips, getSymbol(OrderSymbol()));
           }
        }

      //+------------------------------------------------------------------+
      //|                                                                  |
      //+------------------------------------------------------------------+
      if(
         (profit_mode == PROFIT_MODE_MONEY    && (profitMoney >= profit_amount))
         || (profit_mode == PROFIT_MODE_PIPS     && (profitPips <= profit_amount))
         || (profit_mode == PROFIT_MODE_PIPS_SUM && (pipsSum == profit_amount))
      )
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
   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   virtual void      reset(int level)
     {

     }
   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }
  };
