class MarketPropertiesLowestCandle1cm_r1

  {

public:
   string            symbol;
   int               timeframe;
   int               what_to_get;
   int               range_start;
   int               range_end;

   string            msymbol;
   int               mtimeframe;

public:
   void              init()
     {
      symbol = "";
      timeframe = PERIOD_CURRENT;
      what_to_get = GET_PRICE;
      range_start = 0;
      range_end   = 10;
     }

   template<typename T>
   T                 calc()
     {
      msymbol = getSymbol(symbol);
      mtimeframe = getTimeframe(timeframe);

      int li = iLowest(msymbol, mtimeframe, MODE_LOW, range_end-range_start+1, range_start);

      T result;

      if(what_to_get == GET_PRICE)
         result = iLow(msymbol, mtimeframe, li);
      else
         if(what_to_get == GET_CANDLE_ID)
            result = li;
         else
            if(what_to_get == GET_TIME)
               result = iTime(msymbol, mtimeframe, li);

      return result;
     }
  };
