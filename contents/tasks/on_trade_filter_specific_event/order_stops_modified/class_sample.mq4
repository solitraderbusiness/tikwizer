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

      group_mode = ORDER_GROUP_MODE_ALL;
      group_number = 15;

      stops_mode = "some";
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
      ArrayResize(type, 0, 0);
      int mtype[] = {1,0};
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      if(
         e_Reason() == "modify"
         && e_attrType() >= 2
         && (
				   (stops_mode == "sltp" && e_ReasonDetail() == "sltp")
				|| (stops_mode == "sl" && (e_ReasonDetail() == "sl" || e_ReasonDetail() == "sltp"))
				|| (stops_mode == "tp" && (e_ReasonDetail() == "tp" || e_ReasonDetail() == "sltp"))
				|| (stops_mode == "slonly" && e_ReasonDetail() == "sl")
				|| (stops_mode == "tponly" && e_ReasonDetail() == "tp")
				|| (stops_mode == "slortp" && (e_ReasonDetail() == "sl" || e_ReasonDetail() == "tp"))
				|| (stops_mode == "some" && (e_ReasonDetail() == "sl" || e_ReasonDetail() == "tp" || e_ReasonDetail() == "sltp"))
			)
         && filterOnTrade())
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
   bool              filterOnTrade()
     {
      bool con1 = is_symbol_accepted_on_trade(symbol_mode, symbols);
      bool con2 = sameOrderType(type, e_attrType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(e_attrMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(e_attrMagicNumber());
      return con1 && con2 && con3 && con4;
     }


  };
