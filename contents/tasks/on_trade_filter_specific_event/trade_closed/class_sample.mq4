class Task0 : public Task
  {
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[];
   string            close_mode;
   int               close_partial_mode;
public:
                     Task0(string name):Task(name)
     {
      symbol_mode = SYMBOL_MODE_SPECIFIED;
      symbols_str = ",EURUSD,GBPUSD";
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;
      int mtype[] = {0, 1}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.

      close_mode = "";
      close_partial_mode = 0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      bool next = false;

      if(
         (e_Reason() == "close" || e_Reason() == "decrement")
         && e_attrType() < 2
         && filterGeneral()
      )
        {
         string closedBy = e_ReasonDetail();

         if(
            (
               (close_mode == "")
               || (close_mode == closedBy)
               || (close_mode == "sltp" && (closedBy == "sl" || closedBy == "tp"))
               || (close_mode == "nosltp" && (closedBy != "sl" && closedBy != "tp"))
               || (close_mode == "exp" && closedBy == "expiration")
            )
            && (
               (close_partial_mode == 0)
               || (close_partial_mode == 1 && e_Reason() == "close") // fully closed
               || (close_partial_mode == 2 && e_Reason() == "decrement") // partially closed
            )
         )
           {
            next = true;
           }
        }

      if(next)
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
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }

  };
