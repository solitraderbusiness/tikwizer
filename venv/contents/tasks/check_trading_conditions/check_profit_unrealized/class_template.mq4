class Task_id : public Task
  {
public:
   //defined by user
   string            symbol;
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               profit_mode;
   double            profit_benchmark_filter;
   double            profit_benchmark_comparison;
   //defined by system
   string            msymbol;

public:
   void              Task_id(string name): Task(name)
     {
      symbol = symbol_val;//STest, no lists yet, also all is not supported yet.
      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      profit_mode = profit_mode_val;
      profit_benchmark_filter = profit_benchmark_filter_val;
      profit_benchmark_comparison = profit_benchmark_comparison_val;
     }


   virtual void      run(int block_id, BlockParent &block)
     {
      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;

      double profitTotal=0;
      for(int i = 0 ; i < OrdersTotal() ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;

            double profit = getProfit();

            if(!filterSpecific(profit))
               continue;

            profitTotal += profit;
           }
        }

      bool result = profitTotal >= profit_benchmark_comparison;
      if(result)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }

   bool              filterGeneral()
     {
      bool con1 = (msymbol==NULL && OrderSymbol()==Symbol()) || msymbol==OrderSymbol();
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

   bool              filterSpecific(double profit)
     {
      return profit != profit_benchmark_filter;
     }

   double              getProfit()
     {
      double tradeProfit;
      if(profit_mode == PROFIT_MODE_MONEY)
        {
         tradeProfit = NormalizeDouble(OrderProfit() + OrderSwap() + OrderCommission(), 2); //STest, sure about + ?
        }
      else
         if(profit_mode == PROFIT_MODE_PIPS)
           {
            double profitVal = OrderType()==OP_BUY ? OrderClosePrice() - OrderOpenPrice() : OrderOpenPrice() - OrderClosePrice(); //STest, commission and swap
            tradeProfit = toPips(profitVal, OrderSymbol());
           }
      return tradeProfit;
     }

   double            toPips(double price, string symbol)
     {
      if(msymbol == "")
         msymbol = Symbol();
      return price/SymbolInfoDouble(msymbol, SYMBOL_POINT)/10;
     }
  };
