class MarketPropertiesAskBidMid2_left

  {

public:
   string            Price;
   int               TickID;
   string            symbol;

   string            msymbol;

public:
   void              init()
     {
      Price = (string)"ASK";
      TickID = (int)0;
      symbol = (string)"";
     }

   template<typename T>
   T                 calc()
     {
      msymbol = getSymbol(symbol);

      int digits = (int)SymbolInfoInteger(msymbol, SYMBOL_DIGITS);

      double retval = 0;
      int tID       = TickID ;

      if(Price == "ASK")
        {
         retval = TicksData(msymbol,SYMBOL_ASK,tID);
        }
      else
         if(Price == "BID")
           {
            retval = TicksData(msymbol,SYMBOL_BID,tID);
           }
         else
            if(Price == "MID")
              {
               retval = ((TicksData(msymbol,SYMBOL_ASK,tID)+TicksData(msymbol,SYMBOL_BID,tID))/2);
              }
            else
               if(Price == "BIDHIGH")
                 {
                  retval = SymbolInfoDouble(msymbol,SYMBOL_BIDHIGH);
                 }
               else
                  if(Price == "BIDLOW")
                    {
                     retval = SymbolInfoDouble(msymbol,SYMBOL_BIDLOW);
                    }
                  else
                     if(Price == "ASKHIGH")
                       {
                        retval = SymbolInfoDouble(msymbol,SYMBOL_ASKHIGH);
                       }
                     else
                        if(Price == "ASKLOW")
                          {
                           retval = SymbolInfoDouble(msymbol,SYMBOL_ASKLOW);
                          }
                        else
                           if(Price == "LAST")
                             {
                              retval = SymbolInfoDouble(msymbol,SYMBOL_LAST);
                             }
                           else
                              if(Price == "LASTHIGH")
                                {
                                 retval = SymbolInfoDouble(msymbol,SYMBOL_LASTHIGH);
                                }
                              else
                                 if(Price == "LASTLOW")
                                   {
                                    retval = SymbolInfoDouble(msymbol,SYMBOL_LASTLOW);
                                   }
      double result = NormalizeDouble(retval, digits);

      return result;

     }
  };
