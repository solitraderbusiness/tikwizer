//Bull candle
class Task1 : public Task
  {
   string                SignalType;
   int                   CandleID;
   double                MinBodySize;
   double                MaxBodySize;
   string                symbol;
   ENUM_TIMEFRAMES       timeframe;
   //defined by system
   datetime          bartime;
   string            msymbol;
   ENUM_TIMEFRAMES   mtimeframe;
public:
                     Task1(string name):Task(name)
     {
      SignalType = (string)"continuous";
      CandleID = (int)1;
      MinBodySize = (double)5.0;
      MaxBodySize = (double)0.0;
      symbol = (string)"";
      timeframe = (ENUM_TIMEFRAMES)PERIOD_CURRENT;
      //defined by system
      bartime =  0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      msymbol = getSymbol(symbol);
      mtimeframe = getTimeframe(timeframe);

      double cOpen  = iOpen(msymbol,mtimeframe,CandleID);
      double cClose = iClose(msymbol,mtimeframe,CandleID);

      if(SignalType == "continuous" || bartime < iTime(msymbol,mtimeframe,1))
        {
         if((cOpen < cClose)
            && (cClose-cOpen >= toDigits(MinBodySize, msymbol))
            && (MaxBodySize <= 0 || cClose-cOpen <= toDigits(MaxBodySize, msymbol)))
           {
            if(SignalType != "continuous")
              {
               bartime = iTime(msymbol,mtimeframe,1);
              }

            block.onResult(ROUTE_1_PASSED);
            return;
           }
        }

      block.onResult(ROUTE_2_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
