class MarketPropertiesHighestTimePeriod_id

  {

public:
    field_body

   string            msymbol;
   int               mtimeframe;

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


      datetime timeStart = StrToTime(timestr_start) - 86400*day_offset;
      datetime timeEnd   = StrToTime(timestr_end) - 86400*day_offset;
      int range_start = iBarShift(msymbol, mtimeframe, timeEnd, false);
      int range_end   = iBarShift(msymbol, mtimeframe, timeStart, false);


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
