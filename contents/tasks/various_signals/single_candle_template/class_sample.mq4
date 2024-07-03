class Task5 : public Task
  {
   string                SignalType;
   string                CandleType;
   int                   CandleID;
   string                symbol;
   ENUM_TIMEFRAMES       timeframe;
   string                UpperWickMode;
   double                UpWickFrom;
   double                UpWickTo;
   string                LowerWickMode;
   double                LoWickFrom;
   double                LoWickTo;
   double                CandleMinSize;
   double                CandleMaxSize;
   //defined by system
   datetime          time0;
   string            msymbol;
   ENUM_TIMEFRAMES   mtimeframe;
public:
                     Task5(string name):Task(name)
     {
      SignalType = (string)"continuous";
      CandleType = (string)"both";
      CandleID = (int)1;
      symbol = (string)"";
      timeframe = (ENUM_TIMEFRAMES)PERIOD_CURRENT;
      UpperWickMode = (string)"between";
      UpWickFrom = (double)10.0;
      UpWickTo = (double)20.0;
      LowerWickMode = (string)"between";
      LoWickFrom = (double)10.0;
      LoWickTo = (double)20.0;
      CandleMinSize = (double)0.0;
      CandleMaxSize = (double)0.0;
      //defined by system
      time0 =  0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = getSymbol(symbol);
      mtimeframe = getTimeframe(timeframe);


      bool pass = false;

      if(SignalType == "continuous" || time0 < iTime(msymbol,mtimeframe,1))
        {
         double h = iHigh(msymbol,mtimeframe,CandleID);
         double l = iLow(msymbol,mtimeframe,CandleID);
         double C = iClose(msymbol,mtimeframe,CandleID);
         double o = iOpen(msymbol,mtimeframe,CandleID);
         double w = h-l;

         string type = (o > C) ? "bear" : "bull";

         if(
            // Candle size is inside the limits
            (CandleMinSize <= 0 || w >= toDigits(CandleMinSize,msymbol))
            &&
            (CandleMaxSize <= 0 || w <= toDigits(CandleMaxSize,msymbol))
            &&
            (
               // In case of long candle
               (
                  (CandleType != "bear" && type == "bull") // bull candle
                  &&
                  ((UpperWickMode == "no" || UpperWickMode == "to") || C <= (h-(w*(UpWickFrom)/100))) // from
                  &&
                  ((UpperWickMode == "no" || UpperWickMode == "from") || C >= (h-(w*(UpWickTo)/100))) // to
                  &&
                  ((LowerWickMode == "no" || LowerWickMode == "to") || o >= (l+(w*(LoWickFrom)/100))) // from
                  &&
                  ((LowerWickMode == "no" || LowerWickMode == "from") || o <= (l+(w*(LoWickTo)/100))) // to
               )
               ||
               // In case of short candle
               (
                  (CandleType != "bull" && type == "bear") // bear candle
                  &&
                  ((UpperWickMode == "no" || UpperWickMode == "to") || o <= (h-(w*(UpWickFrom)/100))) // from
                  &&
                  ((UpperWickMode == "no" || UpperWickMode == "from") || o >= (h-(w*(UpWickTo)/100))) // to
                  &&
                  ((LowerWickMode == "no" || LowerWickMode == "to") || C >= (l+(w*(LoWickFrom)/100))) // from
                  &&
                  ((LowerWickMode == "no" || LowerWickMode == "from") || C <= (l+(w*(LoWickTo)/100))) // to
               )
            )
         )
           {
            if(SignalType != "continuous")
              {
               time0 = iTime(msymbol,mtimeframe,1);
              }

            pass = true;
           }
        }


      if(pass)
        {
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };
