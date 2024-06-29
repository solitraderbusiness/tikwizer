//+------------------------------------------------------------------+
//|                                                      ProjectName |
//|                                      Copyright 2018, CompanyName |
//|                                       http://www.companyname.net |
//+------------------------------------------------------------------+



//what to get
#define  GET_CANDLE_ID  1
#define  GET_PRICE  2
#define  GET_TIME  3

//Time mode
#define  TIME_SERVER  1
#define  TIME_LOCAL  2
#define  TIME_GMT  3

#define HIGHEST_PRICE_CANDLE_PERIOD 1
#define HIGHEST_PRICE_TIME_PERIOD 2
#define LOWEST_PRICE_CANDLE_PERIOD 3
#define LOWEST_PRICE_TIME_PERIOD 4
#define TIMEFRAME 5



struct MarketPropertiesResult
  {
   double            price;
   int               index;
   datetime          time;
  };



class MarketProperties3_right

  {

public:
   string            symbol;
   int               timeframe;
   int               time_mode;
   int            which;
   //what to return
   int               what_to_get;
   //used for time period
   string            timestr_start;
   string            timestr_end;
   int               day_offset;
   //used for candle period
   int               range_start;
   int               range_end;

   string            msymbol;
   int               mtimeframe;

public:

   void              init()

     {
      symbol = NULL;
      timeframe = 0;
      which = HIGHEST_PRICE_CANDLE_PERIOD;
      what_to_get = GET_PRICE;
      timestr_start = "2023.11.23 7:30:30";
      timestr_end   = "2023.11.20 8:00:00";
      day_offset = 0;
      range_start = 50;
      range_end   = 100;
     }



   int               calc(MarketPropertiesResult &result)
     {
      msymbol = getSymbol(symbol);
      mtimeframe = getTimeframe(timeframe);

      //In time mode, first calc range start and range end, then calc the result just like range mode
      //STest, what is the effect of time mode? For now, it is ignored.
      //STest, in iBarsShift, exact = false?
      if(which == HIGHEST_PRICE_TIME_PERIOD || which == LOWEST_PRICE_TIME_PERIOD)
        {
         datetime timeStart = StrToTime(timestr_start) - 86400*day_offset;
         datetime timeEnd   = StrToTime(timestr_end) - 86400*day_offset;
         range_start = iBarShift(msymbol, mtimeframe, timeEnd, false);
         range_end   = iBarShift(msymbol, mtimeframe, timeStart, false);
        }
      getHiLo(result);

     }


   void              getHiLo(MarketPropertiesResult &result)
     {
      if(which == HIGHEST_PRICE_CANDLE_PERIOD || which == HIGHEST_PRICE_TIME_PERIOD)
         getHighest(result);
      else
         if(which == LOWEST_PRICE_CANDLE_PERIOD || which == LOWEST_PRICE_TIME_PERIOD)
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

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void OnTick()
  {
   MarketProperties3_right mp;
   mp.init();
   MarketPropertiesResult result;
   mp.calc(result);
   printf(result.price);
  }
//+------------------------------------------------------------------+
