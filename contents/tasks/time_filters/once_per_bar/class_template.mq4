//Once per bar
class Task_id : public Task
  {
   string                   symbol;
   ENUM_TIMEFRAMES       timeframe;
   int                max_times_to_pass;
   // System parameters Parameters
   string            tokens[];
   int               passes[];
   datetime          old_values[];
public:
                     Task_id(string name):Task(name)
     {
      symbol = symbol_val;
      timeframe = timeframe_val;
      max_times_to_pass = max_times_to_pass_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string msymbol = getSymbol(symbol);
      int mtimeframe = getTimeframe(timeframe);

      bool next    = false;
      string token = msymbol + IntegerToString(mtimeframe);
      int index    = ArraySearch(tokens, token);

      if(index == -1)
        {
         index = ArraySize(tokens);

         ArrayResize(tokens, index + 1);
         ArrayResize(old_values, index + 1);
         ArrayResize(passes, index + 1);

         tokens[index] = token;
         passes[index] = 0;
         old_values[index] = 0;
        }

      if(max_times_to_pass > 0)
        {

         datetime new_value = iTime(msymbol, mtimeframe, 1);

         if(new_value == 0)
           {
            Print("Failed to get the time from candle 1 on symbol ", msymbol, " and timeframe ", EnumToString((ENUM_TIMEFRAMES)mtimeframe), ". The history data needs to be fixed.");
           }

         if(new_value > old_values[index])
           {
            passes[index]++;

            if(passes[index] >= max_times_to_pass)
              {
               old_values[index]  = new_value;
               passes[index] = 0;
              }

            next = true;
           }
        }

      if(next)
        {
         printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

   template<typename T>
   int               ArraySearch(T &array[], T value)
     {
      int index = -1;
      int size  = ArraySize(array);

      for(int i = 0; i < size; i++)
        {
         if(array[i] == value)
           {
            index = i;
            break;
           }
        }

      return index;
     }

  };

