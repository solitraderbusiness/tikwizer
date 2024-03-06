

/*
all items in check trade/orders count section can be covered by this
function, except for items containing nearby in their title. for example
count_limit=0 and operator = "==" means no trade of type ... .
count_limit=10 and operator = ">" and type=[1,2,3,4,5] means all types
of trades be more than 10.
count_limit=10 and operator = ">=" and type=[3,4,5,6] means all pending
orders be at least 10.
*/
class Task_id : public Task
  {
   //specified by user
   int               symbol_mode;
   string            symbols_str;
   string            symbols[];
   int               group_mode;
   int               group_number;
   int               type[]; //0 for buy and 1 for sell
   int               count_limit;
   int               price_mode;
   int               range_mode;
   int               range_position;
   double            range_value;




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
      int mtype[] = type_val; //0 for buy and 1 for sell
      ArrayCopy(type,mtype,0,0,WHOLE_ARRAY);
      count_limit = count_limit_val;
      price_mode = price_mode_val;
      range_mode = range_mode_val;
      range_position = range_position_val;
      range_value = range_value_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);
      int count_total = OrdersTotal();
      int count = 0;
      for(int i = 0 ; i < count_total ; i++)
        {
         if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
           {
            if(filterGeneral())
              {
               int orderType = OrderType();
               double price;
               double ask = SymbolInfoDouble(OrderSymbol(), SYMBOL_ASK);
               double bid = SymbolInfoDouble(OrderSymbol(), SYMBOL_BID);
               double point = SymbolInfoDouble(OrderSymbol(), SYMBOL_POINT);
               if(price_mode==PRICE_AUTO)
                 {
                  if(MathMod(orderType,2)==0)
                     price = ask;
                  else
                     price = bid;
                 }
               else
                  if(price_mode==PRICE_MID)
                     price = (ask+bid)/2;
                  else
                     if(price_mode==PRICE_ASK)
                        price = ask;
                     else
                        if(price_mode==PRICE_BID)
                           price = bid;

               double rangeFraction;
               if(range_mode==RANGE_MODE_PIPS)
                  rangeFraction = range_value*point*10;
               else
                  if(range_mode==RANGE_MODE_PRICE_FRACTION)
                     rangeFraction = range_value;

               //Now we have range value and price, start comparison process.
               double openPrice = OrderOpenPrice();
               if(range_position==RANGE_POSITION_AROUND)  //Order type doesn't matter
                 {
                  if((price>=openPrice && price<openPrice+rangeFraction) || (price<=openPrice && price>openPrice-rangeFraction))
                     count++;
                 }
               else
                  if(range_position==RANGE_POSITION_LOSING_SIDE)
                    {
                     if(MathMod(orderType, 2)==0)   //buy
                       {
                        if(openPrice-rangeFraction<=price)
                           count++;
                       }
                     else    //sell
                       {
                        if(openPrice+rangeFraction>=price)
                           count++;
                       }

                    }
                  else
                     if(range_position==RANGE_POSITION_WINNING_SIDE)
                       {
                        if(MathMod(orderType, 2)==0)   //buy
                          {
                           if(openPrice+rangeFraction<=price)
                              count++;
                          }
                        else    //sell
                          {
                           if(openPrice-rangeFraction>=price)
                              count++;
                          }

                       }
              }

           }
        }

      bool result = count>count_limit;
      if(result)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level) {}
      bool              filterGeneral()
     {
      bool con1 = is_symbol_accepted(symbol_mode, symbols);
      bool con2 = sameOrderType(type, OrderType());
      bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());
      bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());
      return con1 && con2 && con3 && con4;
     }
  };



