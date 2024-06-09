class Task_id : public Task
  {

public:
    //defined by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   double            older_than;//in minutes
   color             arrow_color;
   double            slippage;

   int               retryCount;
   string            msymbol;
public:
   void              Task_id(string name): Task(name)
     {
      //specified by user
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      older_than = older_than_val;//in minutes
      arrow_color = arrow_color_val;
      slippage = slippage_val;
      //specified by system
      retryCount = 0;
     }


   virtual void      run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      //STest, trades not sorted by newest
      for(int i = 0 ; i < OrdersTotal() ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;
            if(!filterAge(older_than))
               continue;
            bool result = OrderClose(OrderTicket(),OrderLots(),OrderClosePrice(),slippage,arrow_color);
            if(!result)  //STest, if fatal error, skip retry, otherwise retry.
              {
               int err = GetLastError();
              } else {
                OnTrade();
              }
           }
        }
      retryCount++;
      block.onResult(ROUTE_1_PASSED);
     }

   bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

   bool              filterAge(double mins)
     {
      datetime openTime = OrderOpenTime();
      return TimeCurrent() - OrderOpenTime() >= mins*60;
     }
  };

