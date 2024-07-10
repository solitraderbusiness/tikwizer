class Task0 : public Task
  {
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[];
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
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(
         e_Reason() == "new"
         && e_attrType() < 2
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
