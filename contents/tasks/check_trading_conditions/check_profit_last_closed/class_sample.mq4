class Task3 : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   double                ProfitAmount;
   bool                  OncePerTrade;
   //specified by system
   ulong             memory[];
public:
                     Task3(string name):Task(name)
     {
      //specified by user
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "";

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 25;

      ProfitAmount = (double)0.0;
      OncePerTrade = (bool)false;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
      ArrayResize(type, 0, 0);
      int mtype[] = {1,0}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      double last_profit = 0;
      int total          = OrdersHistoryTotal();

      for(int index = total-1; index >= 0; index--)
        {
         if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)
           {
            if(OncePerTrade == false || in_array(memory, (ulong)OrderTicket()) == false)
              {
               if(!filterGeneral())
                  continue;
               last_profit = NormalizeDouble(OrderProfit() + OrderCommission() + OrderSwap(), 2);

               if(OncePerTrade == true)
                 {
                  array_ensure_value(memory, (ulong)OrderTicket());
                 }

               break;
              }
           }
        }

      if(total == 0 || last_profit>ProfitAmount)
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

   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

  };

