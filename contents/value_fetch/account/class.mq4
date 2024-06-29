
#define ACCOUNT_INFO_BALLANCE 1
#define ACCOUNT_INFO_CREDIT 2
#define ACCOUNT_INFO_EQUITY 3
#define ACCOUNT_INFO_FREE_MARGIN 4
#define ACCOUNT_INFO_FREE_MARGIN_CHECK 5
#define ACCOUNT_INFO_LEVERAGE 6
#define ACCOUNT_INFO_LOGIN_NUMBER 7
#define ACCOUNT_INFO_MARGIN 8
#define ACCOUNT_INFO_MARGIN_LEVEL 9
#define ACCOUNT_INFO_NAME_BROKER 10
#define ACCOUNT_INFO_NAME_CLIENT 11
#define ACCOUNT_INFO_NAME_DEPOSIT_CURRENCY 12
#define ACCOUNT_INFO_NAME_SERVER 13
#define ACCOUNT_INFO_PROFIT_EQUITY_BALLANCE 14
#define ACCOUNT_INFO_STOPOUT_LEVEL 15
#define ACCOUNT_INFO_MARGIN_CALL_LEVEL 16
#define ACCOUNT_INFO_ORDERS_TRADES_LIMIT 17



//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
class Account25
  {
public:
   int               row2;
   int               margin_check_OP_TYPE;
   double            margin_check_VOLUME;
   string            symbol;
   int               margin_level_WhenNoTrades;

   void              init()
     {
      row2 = ACCOUNT_INFO_BALLANCE;
      margin_check_OP_TYPE = (int)0;
      margin_check_VOLUME = (double)0.10;
      symbol = (string)"";
      margin_level_WhenNoTrades = (int)0;
     }

   template<typename T>
   T                 execute()
     {
      T retval;
      switch(row2)
        {
         case ACCOUNT_INFO_BALLANCE:
            retval = get_ballance();
            break;
         case ACCOUNT_INFO_CREDIT:
            retval = get_credit();
            break;
         case ACCOUNT_INFO_EQUITY:
            retval = get_equity();
            break;
         case ACCOUNT_INFO_FREE_MARGIN:
            retval = get_free_margin();
            break;
         case ACCOUNT_INFO_FREE_MARGIN_CHECK:
            retval = get_free_margin_check();
            break;
         case ACCOUNT_INFO_LEVERAGE:
            retval = get_ballance();
            break;
         case ACCOUNT_INFO_LOGIN_NUMBER:
            retval = get_account_number();
            break;
         case ACCOUNT_INFO_MARGIN:
            retval = get_margin();
            break;
         case ACCOUNT_INFO_MARGIN_LEVEL:
            retval = get_margin_level();
            break;
         case ACCOUNT_INFO_NAME_BROKER:
            retval = get_company();
            break;
         case ACCOUNT_INFO_NAME_CLIENT:
            retval = get_client();
            break;
         case ACCOUNT_INFO_NAME_DEPOSIT_CURRENCY:
            retval = get_currency();
            break;
         case ACCOUNT_INFO_NAME_SERVER:
            retval = get_server();
            break;
         case ACCOUNT_INFO_PROFIT_EQUITY_BALLANCE:
            retval = get_profit();
            break;
         case ACCOUNT_INFO_STOPOUT_LEVEL:
            retval = get_stopout_level();
            break;
         case ACCOUNT_INFO_MARGIN_CALL_LEVEL:
            retval = get_margin_call();
            break;
         case ACCOUNT_INFO_ORDERS_TRADES_LIMIT:
            retval = get_pending_orders_limit();
            break;
        }

      return retval;
     }




   double            get_ballance()
     {
      return NormalizeDouble(AccountInfoDouble(ACCOUNT_BALANCE), 2);
     }


   double            get_credit()
     {
      return NormalizeDouble(AccountInfoDouble(ACCOUNT_CREDIT), 2);
     }


   double            get_equity()
     {
      return NormalizeDouble(AccountInfoDouble(ACCOUNT_EQUITY), 2);
     }


   double            get_free_margin()
     {
      return NormalizeDouble(AccountInfoDouble(ACCOUNT_MARGIN_FREE), 2);
     }


   double            get_free_margin_check()
     {
      return AccountFreeMarginCheck(getSymbol(symbol), margin_check_OP_TYPE, margin_check_VOLUME);
     }


   long              get_leverage()
     {
      return (long)AccountInfoInteger(ACCOUNT_LEVERAGE);
     }


   long              get_account_number()
     {
      return (long)AccountInfoInteger(ACCOUNT_LOGIN);
     }


   double            get_margin()
     {
      return NormalizeDouble(AccountInfoDouble(ACCOUNT_MARGIN), 2);
     }


   double            get_margin_level()
     {
      if(AccountInfoDouble(ACCOUNT_MARGIN) > 0)
        {
         return AccountInfoDouble(ACCOUNT_MARGIN_LEVEL);
        }

      return margin_level_WhenNoTrades;
     }


   string            get_company()
     {
      return AccountInfoString(ACCOUNT_COMPANY);
     }


   string            get_client()
     {
      return AccountInfoString(ACCOUNT_NAME);
     }


   string            get_currency()
     {
      return AccountInfoString(ACCOUNT_CURRENCY);
     }


   string            get_server()
     {
      return AccountInfoString(ACCOUNT_SERVER);
     }


   double            get_profit()
     {
      return NormalizeDouble(AccountInfoDouble(ACCOUNT_PROFIT), 2);
     }


   double            get_stopout_level()
     {
      return AccountInfoDouble(ACCOUNT_MARGIN_SO_SO);
     }


   double            get_margin_call()
     {
      return AccountInfoDouble(ACCOUNT_MARGIN_SO_CALL);
     }


   int               get_pending_orders_limit()
     {
      return (int)AccountInfoInteger(ACCOUNT_LIMIT_ORDERS);
     }

  };
