class Task0 : public Task
  {
public:
   int                candle_id;

public:
                     Task0(string name):Task(name)
     {
      candle_id = 0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      double value = ObjectGetValueByShift(loaded_object_chart_id(), loaded_object_name(), candle_id);

      Value1_right1 value1_price_level;
      value1_price_level.init();
      double valueValue1_price_level = value1_price_level.calc();

      if(value > valueValue1_price_level)
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


double ObjectGetValueByShift(long chart_id, string name, int shift)
{
	MqlRates rates[];
	CopyRates(NULL, PERIOD_CURRENT, shift, 1, rates);

	return ObjectGetValueByTime(chart_id, name, rates[0].time, 0);
}
