

class MarketProperties_id

  {

public:
    field_body

public:

   void              init()

     {
      init_body
     }



   int               calc(MarketPropertiesResult &result)
     {
      msymbol = getSymbol(symbol);
      mtimeframe = overriding_timeframe==-1 ? timeframe : overriding_timeframe;

      //In time mode, first calc range start and range end, then calc the result just like range mode
      //STest, what is the effect of time mode? For now, it is ignored.
      //STest, in iBarsShift, exact = false?
      if(find_method == TIME_PERIOD)
        {
         datetime timeStart = StrToTime(timestr_start) - 86400*day_offset;
         datetime timeEnd   = StrToTime(timestr_end) - 86400*day_offset;
         range_start = iBarShift(msymbol, mtimeframe, timeStart, false);
         range_end   = iBarShift(msymbol, mtimeframe, timeEnd, false);
        }
      getHiLo(result);
     }


   void              getHiLo(MarketPropertiesResult &result)
     {
      if(price_mode == HIGHEST_PRICE)
         getHighest(result);
      else
         if(price_mode == LOWEST_PRICE)
            getLowest(result);
     }



   void              getHighest(MarketPropertiesResult &result)
     {
      int hi = iHighest(msymbol, mtimeframe, MODE_HIGH, range_end-range_start+1, range_start);
      result.price = iHigh(msymbol, mtimeframe, hi);
      result.index = hi;
      result.time = iTime(msymbol, mtimeframe, hi);
     }


   void              getLowest(MarketPropertiesResult &result)
     {
      int li = iLowest(msymbol, mtimeframe, MODE_LOW, range_end-range_start+1, range_start);
      result.price = iLow(msymbol, mtimeframe, li);
      result.index = li;
      result.time = iTime(msymbol, mtimeframe, li);
     }

  };
