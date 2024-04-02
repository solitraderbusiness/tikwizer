
// Delete pending orders
class Task20 : public Task
  {
   //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   color             arrow_color;

public:
                     Task20(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = "EURUSD,BTCUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.
      arrow_color = clrPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      for(int i = OrdersTotal()-1 ; i >= 0 ; i--)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            DeleteOrder(OrderTicket(), arrow_color);
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

