class MarketPropertiesLowestCandle_id

  {

public:
    field_body

public:
   void              init()
     {
    init_body
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
