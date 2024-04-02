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

   int               trailing_distance_mode;
   double            t_distance_pips;
   double            t_step_pips;

public:
                     Task_id(string name):Task(name)
     {
      symbol_mode = symbol_mode_val;
      symbols_str = symbols_str_val;
      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);

      group_mode = group_mode_val;
      group_number = group_number_val;
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);//This way of initialization is due to the fact MQL4 doesn't support a direct way of initializing an array field.

      trailing_distance_mode = trailing_distance_mode_val;
      t_distance_pips = t_distance_pips_val;
      t_step_pips = t_step_pips_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      for(int m = OrdersTotal()-1 ; m >= 0 ; m--)
        {
         if(OrderSelect(m, SELECT_BY_POS, MODE_TRADES))
           {
            if(!filterGeneral())
               continue;

            string symbol   = OrderSymbol();
            double price    = (IsOrderTypeBuy()) ? SymbolAsk(symbol) : SymbolBid(symbol);
            double distance = 0;
            int digits      = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);

            if(trailing_distance_mode == TRAILING_DISTANCE_MODE_FIXED)
               distance = toDigits(t_distance_pips, symbol);
            else
               if(trailing_distance_mode == TRAILING_DISTANCE_MODE_DYNAMIC)
                 {
                  initializer_dynamic
                  distance = price - variable_name_dynamic;
                 }
               else
                  if(trailing_distance_mode == TRAILING_DISTANCE_MODE_DYNAMIC_PIPS)
                    {
                     initializer_dynamic_pips
                     distance = toDigits(variable_name_dynamic_pips, OrderSymbol());
                    }
                  else
                     if(trailing_distance_mode == TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS)
                       {
                        initializer_dynamic_digits
                        distance = variable_name_dynamic_digits;
                       }


            distance = NormalizeDouble(MathAbs(distance), digits);

            double old_op = 0, old_sl = 0, old_tp = 0;
            double new_op = 0, new_sl = 0, new_tp = 0;

            if(MathAbs(price - OrderOpenPrice()) >= MathAbs(distance + toDigits(t_step_pips, symbol)))
              {
               old_sl = OrderStopLoss();
               old_tp = OrderTakeProfit();
               old_op = OrderOpenPrice();

               if(IsOrderTypeBuy() == true)
                 {
                  new_op = IsOrderTypeStop() ? price + distance : price - distance;

                  if(old_sl > 0)
                     new_sl = new_op - (old_op - old_sl);
                  if(old_tp > 0)
                     new_tp = new_op + (old_tp - old_op);
                 }
               else
                 {
                  new_op = IsOrderTypeStop() ? price - distance : price + distance;

                  if(old_sl > 0)
                     new_sl = new_op + (old_sl - old_op);
                  if(old_tp > 0)
                     new_tp = new_op - (old_op - old_tp);
                 }

               OrderModify(OrderTicket(), new_op, new_sl, new_tp, 0, clrBlack);
              }
           }
        }
         printf("task"+block_id + " passed route 1");
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
