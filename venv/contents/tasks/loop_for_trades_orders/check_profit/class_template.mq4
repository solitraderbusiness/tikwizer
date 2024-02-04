#define CHECK_PROFIT_MODE_DEPOSIT_CURRENCY 1
#define CHECK_PROFIT_MODE_ACCOUNT_PROFIT 2
#define CHECK_PROFIT_MODE_EQUITY 3
#define CHECK_PROFIT_MODE_BALANCE 4
#define CHECK_PROFIT_MODE_FREE_MARGIN 5



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Task0 : public Task
  {
   int               check_mode;
   double            check_value;
public:
                     Task0(string name):Task(name)
     {
      check_mode = CHECK_PROFIT_LOSS_MODE_ACCOUNT_PROFIT;
      check_value = 50.0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      double profit = NormalizeDouble(OrderProfit() + OrderSwap() + OrderCommission(), 2);

      double amount = 0;

      if(check_mode == CHECK_PROFIT_LOSS_MODE_DEPOSIT_CURRENCY)
         amount = check_value;
      else
         if(check_mode == CHECK_PROFIT_LOSS_MODE_ACCOUNT_PROFIT)
            amount = AccountProfit()*check_value/100;
         else
            if(check_mode == CHECK_PROFIT_LOSS_MODE_EQUITY)
               amount = AccountEquity()*check_value/100;
            else
               if(check_mode == CHECK_PROFIT_LOSS_MODE_BALANCE)
                  amount = AccountBalance()*check_value/100;
               else
                  if(check_mode == CHECK_PROFIT_LOSS_MODE_FREE_MARGIN)
                     amount = AccountFreeMargin()*check_value/100;

      bool result = profit operator_val amount;

      if(result)
        {
         printf("task" + block_id + " passsed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passsed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }
  };
