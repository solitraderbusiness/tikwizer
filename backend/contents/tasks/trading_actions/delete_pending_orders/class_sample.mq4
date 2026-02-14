
// Delete pending orders
class Task20 : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[];
   color             arrow_color;

public:
                     Task20(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      arrow_color = clrPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
      ArrayResize(type, 0, 0);
      int mtype[] = {1,0};
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      for(int i = OrdersTotal()-1 ; i >= 0 ; i--)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            bool success = DeleteOrder(OrderTicket(), arrow_color);
            if (success)
                OnTrade();
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
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

  };

