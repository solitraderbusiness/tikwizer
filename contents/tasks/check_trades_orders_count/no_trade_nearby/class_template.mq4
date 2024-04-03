class Task_id : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell

   string            mode_base_price;
   string            mode_range;
   double            range_pips;
   double            range_fraction;
   int               range_position;

public:
                     Task_id(string name):Task(name)
     {
      //specified by user
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = {1,2}; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);

      mode_base_price = mode_base_price_val;
      mode_range = mode_range_val;
      range_pips = range_pips_val;
      range_fraction = range_fraction_val;
      range_position = range_position_val;

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      int next               = true;
      double price           = 0;
      bool use_current_price = (mode_base_price == "current");

      // prepare the time filters
      initializer_t1
      datetime t1 = variable_name_t1;
      initializer_t2
      datetime t2 = variable_name_t2;

      if(t1 >= TimeCurrent())
         t1 = 0;

      if(!use_current_price)
        {
         initializer_price
         price = variable_name_price;
        }

      for(int i = OrdersTotal()-1; i >= 0; i--)
        {

         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(filterGeneral())
              {
               // filter by time
               if((t1 < t2 && OrderOpenTime() < t1) || OrderOpenTime() > t2)
                 {
                  continue;
                 }

               // what is the distance?
               double distance = range_fraction;

               if(mode_range == "pips")
                 {
                  distance = toDigits(range_pips, OrderSymbol());
                 }

               // checking the position
               if(OrderType() == 0)  // buy?
                 {
                  if(use_current_price)
                    {
                     price = SymbolInfoDouble(OrderSymbol(), SYMBOL_ASK);
                    }

                  switch(range_position)
                    {
                     case 0:
                        if(price <= (OrderOpenPrice() + distance/2) && price >= (OrderOpenPrice() - distance/2))
                          {
                           next = false;
                          }
                        break;
                     case 1:
                        if(price <= OrderOpenPrice() + distance && price >= OrderOpenPrice())
                          {
                           next = false;
                          }
                        break;
                     case 2:
                        if(price <= OrderOpenPrice() && price >= OrderOpenPrice() - distance)
                          {
                           next = false;
                          }
                        break;
                    }
                 }
               else
                 {
                  if(use_current_price)
                    {
                     price = SymbolInfoDouble(OrderSymbol(), SYMBOL_BID);
                    }

                  switch(range_position)
                    {
                     case 0:
                        if(price <= (OrderOpenPrice() + distance/2) && price >= (OrderOpenPrice() - distance/2))
                          {
                           next = false;
                          }
                        break;
                     case 1:
                        if(price <= OrderOpenPrice() && price >= OrderOpenPrice() - distance)
                          {
                           next = false;
                          }
                        break;
                     case 2:
                        if(price <= OrderOpenPrice() + distance && price >= OrderOpenPrice())
                          {
                           next = false;
                          }
                        break;
                    }
                 }

               if(next == false)
                 {
                  break;
                 }
              }
           }
        }

      if(next)
        {
         printf("task" + block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passed route 2");
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
