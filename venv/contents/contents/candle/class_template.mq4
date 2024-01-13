class Candle_id

  {

public:

   field_body

public:

   void              init()

     {
      init_body
     }



   double            calc()

     {
      msymbol = overriding_symbol=="" ? symbol : overriding_symbol;
      mtimeframe = overriding_timeframe==-1 ? timeframe : overriding_timeframe;

      int index = get_index();
      double value = get_value(index);
      return value;
     }

private:
   int               get_index()
     {
      int index = -1;
      if(find_method==FIND_BY_DATE)
        {
         datetime date = StrToTime(timestr);
         index = iBarShift(symbol, timeframe, date, false);
        }
      else
         if(find_method==FIND_BY_ID)
           {
            index = shift;
           }
      return index;
     }

   double            get_value(int index)
     {
      switch(price_mode)
        {
         case CANDLE_OPEN:
            return iOpen(msymbol, mtimeframe, index);
         case CANDLE_HIGH:
            return iHigh(msymbol, mtimeframe, index);
         case CANDLE_LOW:
            return iLow(msymbol, mtimeframe, index);;
         case CANDLE_CLOSE:
            return iClose(msymbol, mtimeframe, index);;
         case CANDLE_MEDIAN:
            return (iHigh(msymbol, mtimeframe, index)+iLow(msymbol, mtimeframe, index))/2;
         case CANDLE_HLC3:
            return (iHigh(msymbol, mtimeframe, index)+iLow(msymbol, mtimeframe, index)+iClose(msymbol, mtimeframe, index))/3;
         case CANDLE_AVERAGE:
            return (iOpen(msymbol, mtimeframe, index)+iHigh(msymbol, mtimeframe, index)+iLow(msymbol, mtimeframe, index)+iClose(msymbol, mtimeframe, index))/4;
         case CANDLE_GAP_TO_PREV:
            //STest, is this calc right?
            double gapup = iLow(msymbol, mtimeframe, index+1)-iHigh(msymbol, mtimeframe, index);
            double gapdn = iLow(msymbol, mtimeframe, index)-iHigh(msymbol, mtimeframe, index+1);
            double gap = gapup>0 ? gapup : gapdn>0 ? gapdn : 0;
            return gap;


            double val, valPips;
            double point = SymbolInfoDouble(msymbol, SYMBOL_POINT);

         case CANDLE_TOTAL_SIZE:
            val = length(index);
            valPips = val/point/10;
            return valPips;
         case CANDLE_BODY_SIZE:
            val = body(index);
            valPips = val/point/10;
            return valPips;
         case CANDLE_TOP_WICK:
            val = wickup(index);
            valPips = val/point/10;
            return valPips;
         case CANDLE_BOTTOM_WICK:
            val = wickdn(index);
            valPips = val/point/10;
            return valPips;



         //STest, effect of bull here compared to code above
         case BULL_CANDLE_TOTAL_SIZE:
            val = isGreen(index) ? length(index) : 0;
            valPips = val/point/10;
            return valPips;
         case BULL_CANDLE_BODY_SIZE:
            val = isGreen(index) ? body(index) : 0;
            valPips = val/point/10;
            return valPips;
         case BULL_CANDLE_TOP_WICK:
            val = isGreen(index) ? wickup(index) : 0;
            valPips = val/point/10;
            return valPips;
         case BULL_CANDLE_BOTTOM_WICK:
            val = isGreen(index) ? wickdn(index) : 0;
            valPips = val/point/10;
            return valPips;



         //STest, effect of bull here compared to code above
         case BEAR_CANDLE_TOTAL_SIZE:
            val = isRed(index) ? length(index) : 0;
            valPips = val/point/10;
            return valPips;
         case BEAR_CANDLE_BODY_SIZE:
            val = isRed(index) ? body(index) : 0;
            valPips = val/point/10;
            return valPips;
         case BEAR_CANDLE_TOP_WICK:
            val = isRed(index) ? wickup(index) : 0;
            valPips = val/point/10;
            return valPips;
         case BEAR_CANDLE_BOTTOM_WICK:
            val = isRed(index) ? wickdn(index) : 0;
            valPips = val/point/10;
            return valPips;
        }
      return -1;
     }




   double            length(int i)
     {
      return iHigh(msymbol, mtimeframe, i)-iLow(msymbol, mtimeframe, i);
     }
   double            body(int i)
     {
      return MathMax(iOpen(msymbol, mtimeframe, i),iClose(msymbol, mtimeframe, i)) - MathMin(iOpen(msymbol, mtimeframe, i),iClose(msymbol, mtimeframe, i));
     }
   double            wickup(int i)
     {
      return iHigh(msymbol, mtimeframe, i)-MathMax(iOpen(msymbol, mtimeframe, i),iClose(msymbol, mtimeframe, i));
     }
   double            wickdn(int i)
     {
      return MathMin(iOpen(msymbol, mtimeframe, i),iClose(msymbol, mtimeframe, i))-iLow(msymbol, mtimeframe, i);
     }
   bool              isGreen(int i)
     {
      return iOpen(msymbol, mtimeframe, i)<iClose(msymbol, mtimeframe, i);
     }
   bool              isRed(int i)
     {
      return iOpen(msymbol, mtimeframe, i)>iClose(msymbol, mtimeframe, i);
     }
   bool              isDoji(int i)
     {
      return iOpen(msymbol, mtimeframe, i)==iClose(msymbol, mtimeframe, i);
     }

  };
