class Task_id : public Task
  {
   //values set by user
   string            symbol;
   int               group;
   int               order_type;
   int               money_management;
   double            how_much_volume;
   double            volume_upper_limit;
   int               open_at_price;
   double            price_offset;
   bool              price_offset_as_pip;
   int               slippage;
   int               stop_loss_mode;
   int               take_profit_mode;
   double            stoploss;
   double            takeprofit;
   string            comment;
   int               magic;
   datetime          expiration;
   color             arrow_color;
   //values set by system
   int               cmd;
   double            price;
   double            volume;
   int               ticket;
   double            slPrice;
   double            tpPrice;
   double            mstoploss;
   double            mtakeprofit;
   bool              initialized;
   string            msymbol;
   //martingale inputs
   int               look_up_on;
   double            martingale_init_vol;
   double            martingale_multiply_on_loss;
   double            martingale_multiply_on_profit;
   double            martingale_addlots_on_loss;
   double            martingale_addlots_on_profit;
   double            martingale_reset_on_n_losses;
   double            martingale_reset_on_n_profits;
   int               type[];
public:
                     Task_id(string name):Task(name)
     {
      symbol = symbol_val;
      group = group_val;
      order_type = order_type_val;
      money_management = money_management_val;
      how_much_volume = how_much_volume_val;
      volume_upper_limit = volume_upper_limit_val;
      open_at_price = open_at_price_val;
      price_offset = price_offset_val;
      price_offset_as_pip = price_offset_as_pip_val;

      slippage = slippage_val;
      stoploss = stoploss_val;
      takeprofit = takeprofit_val;
      take_profit_mode = take_profit_mode_val;
      stop_loss_mode = stop_loss_mode_val;
      comment = comment_val;
      expiration = expiration_val;
      arrow_color = arrow_color_val;

      //martingale
      look_up_on = look_up_on_val;
      int mtype[] = type_val;//This doesn't seem to be an input. So this remains static forever.
      ArrayCopy(type, mtype, 0, 0, WHOLE_ARRAY);
      martingale_init_vol = martingale_init_vol_val;
      martingale_multiply_on_loss = martingale_multiply_on_loss_val;
      martingale_multiply_on_profit = martingale_multiply_on_profit_val;
      martingale_addlots_on_loss = martingale_addlots_on_loss_val;
      martingale_addlots_on_profit = martingale_addlots_on_profit_val;
      martingale_reset_on_n_losses = martingale_reset_on_n_losses_val;
      martingale_reset_on_n_profits = martingale_reset_on_n_profits_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = overriding_symbol=="" ? Symbol() : overriding_symbol;

      calc();
      if(!initialized)
        {
         printf("Not initialized");
         //block.onResult(ROUTE_2_PASSED);
         return;
        }
      ticket=OrderSend(msymbol,cmd,volume,price,slippage,slPrice,tpPrice,comment,magic,expiration,arrow_color);
      if(ticket == ERR_NO_ERROR)
        {
         printf("task"+block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }
private:
   //does needed calculations
   void              calc()
     {
      slippage = (int)(slippage * PipValue(msymbol));
      fitGroup();
      buildMagic();
      if(order_type==ORDER_BUY)
        {
         cmd = OP_BUY;
        }
      else
         if(order_type==ORDER_SELL)
           {
            cmd = OP_SELL;
           }
         else
            if(order_type==ORDER_BUY_PENDING)
              {
               if(price_offset>=0)
                  cmd = OP_BUYSTOP;
               else
                  cmd = OP_BUYLIMIT;
              }
            else
               if(order_type==ORDER_SELL_PENDING)
                 {
                  if(price_offset>=0)
                     cmd = OP_SELLSTOP;
                  else
                     cmd = OP_SELLLIMIT;
                 }

      calcVolume();
      calc_entry_price();
      if(cmd==OP_BUY || cmd==OP_BUYLIMIT ||cmd==OP_BUYSTOP)
        {
         calc_tp_buy();
         calc_sl_buy();
        }
      else
         if(cmd==OP_SELL || cmd==OP_SELLLIMIT || cmd==OP_SELLSTOP)
           {
            calc_tp_sell();
            calc_sl_sell();
           }

      if(MathAbs(tpPrice-slPrice)/Point()<MarketInfo(Symbol(), MODE_SPREAD))
        {
         printf("Takeprofit and Stoploss too close");
         initialized = false;
         return;
        }
      initialized = true;
     }

   void              calc_entry_price()
     {
      if(cmd==OP_BUY)
        {
         price = Ask;
        }
      else
         if(cmd==OP_SELL)
           {
            price = Bid;
           }
         else
           {
            switch(open_at_price)
              {
               case OPEN_AT_ASK:
                  price = SymbolInfoDouble(msymbol, SYMBOL_ASK);
                  break;
               case OPEN_AT_BID:
                  price = SymbolInfoDouble(msymbol, SYMBOL_BID);
                  break;
               case OPEN_AT_MID:
                  price = (SymbolInfoDouble(msymbol, SYMBOL_ASK)+SymbolInfoDouble(msymbol, SYMBOL_BID))/2;
                  break;
               case OPEN_AT_CUSTOM_PRICE:
                  initializer_oacp
                  price = variable_name_oacp;
                  break;
              }
           }


      double offset = price_offset;
      if(price_offset_as_pip)
         offset = price_offset * Point() * 10;

      if(cmd==OP_SELLLIMIT || cmd==OP_SELLSTOP)
         price -= offset;
      else if (cmd==OP_BUYLIMIT || cmd==OP_BUYSTOP)
         price += offset;
     }

   ////////////////////////////////////////////////////////////

   void              calc_tp_buy()
     {
      switch(take_profit_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mtakeprofit = NormalizeDouble(takeprofit*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            tpPrice = price + mtakeprofit;
            break;
         case TPSL_MODE_NO_TP:
            tpPrice = 0;
            break;
        }
     }

   void              calc_sl_buy()
     {
      switch(stop_loss_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mstoploss = NormalizeDouble(stoploss*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            slPrice = price - mstoploss;
            break;
         case TPSL_MODE_NO_SL:
            slPrice = 0;
            break;
        }
     }

   void              calc_tp_sell()
     {
      switch(take_profit_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mtakeprofit = NormalizeDouble(takeprofit*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            tpPrice = price - mtakeprofit;
            break;
         case TPSL_MODE_NO_TP:
            tpPrice = 0;
            break;
        }
     }

   void              calc_sl_sell()
     {
      switch(stop_loss_mode)
        {
         case TPSL_MODE_FIXED_PIPS:
            mstoploss = NormalizeDouble(stoploss*MarketInfo(msymbol, MODE_POINT)*10,SymbolInfoInteger(msymbol, SYMBOL_DIGITS));
            slPrice = price + mstoploss;
            break;
         case TPSL_MODE_NO_SL:
            slPrice = 0;
            break;
        }
     }

   void              calcVolume()
     {
      if(money_management == MONEY_MANAGEMENT_FIXED_VOLUME)
        {
         volume = DynamicLots(msymbol, money_management, how_much_volume);
        }
      else
         if(money_management == MONEY_MANAGEMENT_PERCENT_OF_EQUITY)
           {
            volume = DynamicLots(msymbol, money_management, how_much_volume);
           }
         else
            if(money_management == MONEY_MANAGEMENT_PERCENT_OF_BALANCE)
              {
               //lots = DynamicLots(Symbol, money_management, VolumeBlockPercent);
              }
            else
               if(money_management == MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN)
                 {
                  //lots = DynamicLots(Symbol, money_management, VolumeBlockPercent);
                 }
               else
                  if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY)
                    {
                     //lots = DynamicLots(Symbol, money_management, VolumePercent);
                    }
                  else
                     if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE)
                       {
                        //lots = DynamicLots(Symbol, money_management, VolumePercent);
                       }
                     else
                        if(money_management == MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN)
                          {
                           //lots = DynamicLots(Symbol, money_management, VolumePercent);
                          }
                        else
                           if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY)
                             {
                              //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                             }
                           else
                              if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE)
                                {
                                 //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                                }
                              else
                                 if(money_management == MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN)
                                   {
                                    //lots = DynamicLots(Symbol, money_management, VolumeRisk, pre_sl_pips);
                                   }
                                 else
                                    if(money_management == MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY)
                                      {
                                       //lots = DynamicLots(Symbol, money_management, VolumeSizeRisk, pre_sl_pips);
                                      }
                                    else
                                       if(money_management == MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES)
                                         {
                                          //lots = DynamicLots(Symbol, money_management, FixedRatioUnitSize, FixedRatioDelta);
                                         }
                                       else
                                          if(money_management == MONEY_MANAGEMENT_BETTING_MARTINGLE_PAROLI)
                                            {
                                             volume = BetMartingale(msymbol, look_up_on, group, type, martingale_init_vol, martingale_multiply_on_loss, martingale_multiply_on_profit, martingale_addlots_on_loss, martingale_addlots_on_profit, martingale_reset_on_n_losses, martingale_reset_on_n_profits);
                                            }
                                          else
                                             if(money_management == MONEY_MANAGEMENT_CUSTOM_VALUE)
                                               {
                                                //lots = _dVolumeSize_();
                                               }


      if(volume_upper_limit>0 && volume>volume_upper_limit)
         volume = volume_upper_limit;
     }

   void              fitGroup()
     {
      //STest, take care of group number rules later
      if(group<11)
         group = 11;
      if(group>99)
         group = 99;
     }

   void              buildMagic()
     {
         magic = StrToInteger(group + "72" + "000"); //72 shows it's automated (opened by the expert).
     }

  };
