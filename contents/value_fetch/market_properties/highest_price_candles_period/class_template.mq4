class MarketPropertiesHighestCandle_id

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

      int hi = iHighest(msymbol, mtimeframe, MODE_HIGH, range_end-range_start+1, range_start);

      T result;

      if(what_to_get == GET_PRICE)
         result = iHigh(msymbol, mtimeframe, hi);
      else
         if(what_to_get == GET_CANDLE_ID)
            result = hi;
         else
            if(what_to_get == GET_TIME)
               result = iTime(msymbol, mtimeframe, hi);

      return result;

     }
  };
