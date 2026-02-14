#define CLOSE_PARTIALLY_FIXED_VOLUME 1
#define CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME 2
#define CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME 3

struct Order
  {
   int               orderTicket;
   double            orderVolume;

  };


Order orders[];

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+



//+--------------------------------------------------------------------------------------------+
//|           Close partially (Works inside loop for trades. Order must be selected already.   |
//+--------------------------------------------------------------------------------------------+
class Task0 : public Task
  {
public:
   int               part_vol_mode;
   double            part_vol_value;
   double            slippage;
   color             arrow_color;
public:
                     Task0(string name):Task(name)
     {
      part_vol_mode = CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME;
      part_vol_value = 20;
      slippage = 4;
      arrow_color = clrDeepPink;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      removeClosedTrades(OrderTicket());

      if(OrderType() > 2 || OrderType() < 0) //is pending or is nothing is selected
        {
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
         return;
        }

      double lots_to_close = 0;

      if(part_vol_mode == CLOSE_PARTIALLY_FIXED_VOLUME)
        {
         lots_to_close = part_vol_value;
        }
      else
         if(part_vol_mode == CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME)
           {
            lots_to_close = (OrderLots()*part_vol_value)/100;
           }
         else
            if(part_vol_mode == CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME)
              {
               double lotsInit = lotsInitial();
               lots_to_close = (lotsInit*part_vol_value)/100;
              }


      bool maxExceeded = (part_vol_mode == CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME ||
                          part_vol_mode == CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME) && part_vol_value>=100;
      if(maxExceeded)
         lots_to_close = OrderLots();

      if(lots_to_close>=OrderLots())//Close the whole order
         lots_to_close = OrderLots();

      int ticket = OrderTicket();
      bool updateTicket = lots_to_close<OrderLots();
      bool success = OrderClose(OrderTicket(), lots_to_close, OrderClosePrice(),slippage,arrow_color);

      if(success)
        {
         if(updateTicket) //new ticket number is old ticket + 1. So update ticket number in static orders list
            updateTicket(ticket);

         OnTrade();
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level)
     {

     }

   double            lotsInitial()
     {
      if(ArraySize(orders)>0)
        {
         for(int i=ArraySize(orders)-1; i>=0; i--)
           {
            int ticket = orders[i].orderTicket;
            if(ticket == OrderTicket())
               return orders[i].orderVolume;
           }
        }
      //when code reaches here, it means list is either empty or
      //item not present in the list. So we add item to the list
      Order order;
      order.orderTicket = OrderTicket();
      order.orderVolume = OrderLots();

      ArrayResize(orders, ArraySize(orders)+1);
      orders[ArraySize(orders)-1] = order;

      return OrderLots();
     }


   void              updateTicket(int ticket)
     {
      if(ArraySize(orders)<=0)
         return;
      //This is an update call. update and return.
      for(int p=ArraySize(orders)-1; p>=0; p--)
        {
         if(ticket==orders[p].orderTicket)  //order is closed already, remove from list
           {
            orders[p].orderTicket = ticket+1;
            return;
           }
        }
     }


   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              removeClosedTrades(int ticket)   //now just remove closed trades
     {
      if(ArraySize(orders)<=0)
         return;
      for(int i=ArraySize(orders)-1; i>=0; i--)
        {
         if(!OrderSelect(orders[i].orderTicket,SELECT_BY_TICKET,MODE_TRADES))  //order is closed already, remove from list
           {
            RemoveIndexFromArray(orders, i);
           }
        }
      //again select the initially selected order
      OrderSelect(ticket,SELECT_BY_TICKET,MODE_TRADES);
     }


  };
