
class Task_id : public Task
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
                     Task_id(string name):Task(name)
     {
      SignalType = (string)SignalType_val;
      CandleID = (int)CandleID_val;
      MinBodySize = (double)MinBodySize_val;
      MaxBodySize = (double)MaxBodySize_val;
      symbol = (string)symbol_val;
      timeframe = (ENUM_TIMEFRAMES)timeframe_val;
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
