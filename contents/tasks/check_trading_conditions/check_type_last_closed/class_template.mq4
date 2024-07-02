class Task_id : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;

   int               LastOrderType;
   bool              OncePerTrade;
   /* Static Parameters */
   ulong             memory[];

public:
                     Task_id (string name):Task(name)
     {
      //specified by user
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = group_mode_val;
      group_number = group_number_val;

      LastOrderType = (int)LastOrderType_val;
      OncePerTrade = (bool)OncePerTrade_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int total         = 0;
      int total_tr      = 0;
      int total_po      = 0;
      ulong last_ticket = 0;
      int last_type     = -1;
      bool next         = false;

      //-- check history trades ----------------------------------------------------
      total_tr = OrdersHistoryTotal();

      for(int index = total_tr-1; index >= 0; index--)
        {
         if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)
           {
            if(!filterSpecific())
               continue;

            last_ticket = OrderTicket();
            last_type   = OrderType();

            break;
           }
        }

      //-- check history pending orders --------------------------------------------
      total_po = OrdersHistoryTotal();

      for(int index2 = total_po-1; index2 >= 0; index2--)
        {
         if(OrderSelect((int)index2, SELECT_BY_POS, MODE_HISTORY) && OrderType() >= 2)
           {
            if(!filterSpecific())
               continue;
            if((ulong)OrderTicket() > last_ticket)
              {
               last_ticket = OrderTicket();
               last_type   = OrderType();
              }

            break;
           }
        }

      //-- process the results -----------------------------------------------------
      if(total_tr == 0 && total_po == 0)
        {
         next = true;
        }
      else
        {
         if(OncePerTrade == true && in_array(memory, (ulong)OrderTicket()))
           {
            next = false;
           }
         else
           {
            if(OncePerTrade == true)
              {
               array_ensure_value(memory, (ulong)OrderTicket());
              }

            if(last_type == LastOrderType)
              {
               next = true;
              }
           }
        }

      //-- pass ---------------------------------------------------------------------
      if(next == true)
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
   bool              filterSpecific()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      //bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_MANUAL || !isAutomated(OrderMagicNumber());
      return con1 && con3 && con4;
     }
  };
