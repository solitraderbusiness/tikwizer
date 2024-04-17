class Task0 : public Task
  {
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[];

   string            stops_mode;
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

      stops_mode = "some";
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(
         e_Reason() == "modify"
         && e_attrType() < 2
         && (
				   (stops_mode == "sltp" && e_ReasonDetail() == "sltp")
				|| (stops_mode == "sl" && (e_ReasonDetail() == "sl" || e_ReasonDetail() == "sltp"))
				|| (stops_mode == "tp" && (e_ReasonDetail() == "tp" || e_ReasonDetail() == "sltp"))
				|| (stops_mode == "slonly" && e_ReasonDetail() == "sl")
				|| (stops_mode == "tponly" && e_ReasonDetail() == "tp")
				|| (stops_mode == "slortp" && (e_ReasonDetail() == "sl" || e_ReasonDetail() == "tp"))
				|| (stops_mode == "some" && (e_ReasonDetail() == "sl" || e_ReasonDetail() == "tp" || e_ReasonDetail() == "sltp"))
			)
         && filterGeneral())
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
