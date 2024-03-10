class Task_id : public Task
  {
public:
   int                candle_id;

public:
                     Task_id(string name):Task(name)
     {
      candle_id = candle_id_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      double value = ObjectGetValueByShift(loaded_object_chart_id(), loaded_object_name(), candle_id);

      initializer_price_level

      if(value operator_val variable_name_price_level)
        {
         printf("task" + block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };


