
class ZigZag_id
  {
public: /* Input Parameters */
   field_body

public:
   void              init()
     {
    init_body
     }

   double            calc()
     {

      string symbol =  getSymbol(this.symbol);
      ENUM_TIMEFRAMES timeframe = getTimeframe(this.timeframe);

      int sh        = shift;
      int reverseID = (ZigZagReverseID >= 0) ? ZigZagReverseID : 0;

      double HH[];
      ArrayResize(HH,0);
      double LL[];
      ArrayResize(LL,0);

      double result = 0;
      int size = 0;
      int revH = 0; // reverse id when detecting High
      int revL = 0; // reverse id when detecting Low

      int hhll     = 0; // 1 - High was set last; 2 - Low was set last
      double hh    = -EMPTY_VALUE;
      double ll    = EMPTY_VALUE;
      double last  = 0;
      double value = 0;

      while(true)
        {
         if(sh >= iBars(_Symbol,_Period))
           {
            if(ModeZigZag == 0)
              {
               result = value;
              }
            else
               if(ModeZigZag == 1 || ModeZigZag == 3)
                 {
                  result = HH[ArraySize(HH)-1];
                 }
               else
                  if(ModeZigZag == 2 || ModeZigZag == 4)
                    {
                     result = LL[ArraySize(LL)-1];
                    }

            break;
           }

         value = iZigZag(symbol, timeframe, ZigZagDepth, ZigZagDeviation, ZigZagBackstep, 0, sh);

         if(ModeZigZag == 0)
           {
            result = value;

            break;
           }

         sh++;

         if(value > 0)
           {
            if(last > 0)
              {
               if(value > last)
                 {
                  if(hhll == 1 || hhll == 0)
                    {
                     size = ArraySize(LL);
                     hhll = 2;

                     if(
                        (ModeZigZag < 3) // High or Low
                        || (size == 0 || last<LL[size-1]) // HH or LL
                     )
                       {
                        ArrayResize(LL,size+1);
                        LL[size] = last;
                        revL++;

                        if((ModeZigZag == 2 || ModeZigZag == 4) && revL > reverseID)
                          {
                           result = last;
                           break;
                          }
                       }
                    }
                  else
                    {
                     size = ArraySize(HH);
                     ArrayResize(HH,size+1);
                     HH[size] = last;
                     hhll     = 1;
                    }
                 }
               else
                  if(value < last)
                    {
                     if(hhll == 2 || hhll == 0)
                       {
                        size = ArraySize(HH);
                        hhll = 1;

                        if(
                           (ModeZigZag < 3) // High or Low
                           || (size == 0 || last > HH[size-1]) // HH or LL
                        )
                          {
                           ArrayResize(HH,size+1);
                           HH[size] = last;
                           revH++;

                           if((ModeZigZag == 1 || ModeZigZag == 3) && revH > reverseID)
                             {
                              result = last;

                              break;
                             }
                          }
                       }
                     else
                       {
                        size = ArraySize(LL);
                        ArrayResize(LL,size+1);
                        LL[size] = last;
                        hhll     = 2;
                       }
                    }
              }

            last = value;
           }
        }
      fun_body //trick to comply with indicator template
      return result;
     }

  };


//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
double iZigZag(
   string symbol = NULL,
   ENUM_TIMEFRAMES timeframe = 0,
   int InpDepth = 12,
   int InpDeviation = 5,
   int InpBackstep = 3,
   int mode = 0,
   int shift = 0
)
  {
   int digits = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);

   double value = iCustom(
                     symbol,
                     timeframe,
                     "ZigZag",
                     InpDepth,
                     InpDeviation,
                     InpBackstep,
                     mode,
                     shift
                  );

   return NormalizeDouble(value, 10);
  }
