class MarketPropertiesLowestTimePeriod1cm_r1

  {

public:
   string            symbol;
   int               timeframe;
   int               what_to_get;
   string            timestr_start;
   string            timestr_end;
   int               day_offset;

   string            msymbol;
   int               mtimeframe;

public:
   void              init()
     {
      symbol = "";
      timeframe = PERIOD_CURRENT;
      what_to_get = GET_PRICE;
      timestr_start = "2023.11.23 7:30:30";
      timestr_end   = "2023.11.23 5:30:00";
      day_offset = 0;
     }

   template<typename T>
   T                 calc()
     {
      msymbol = getSymbol(symbol);
      mtimeframe = getTimeframe(timeframe);


      datetime timeStart = StrToTime(timestr_start) - 86400*day_offset;
      datetime timeEnd   = StrToTime(timestr_end) - 86400*day_offset;

      if (timeStart >= timeEnd) //say according to user timestart is 22:00 and timeend is 10:00. They mean from 22:00 yesterday up to 10:00 today.
        timeStart -= 86400;

      int range_start = iBarShift(msymbol, mtimeframe, timeEnd, false);
      int range_end   = iBarShift(msymbol, mtimeframe, timeStart, false);


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
