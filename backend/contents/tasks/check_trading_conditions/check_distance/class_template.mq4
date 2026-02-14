class Task_id : public Task
  {
   bool                DistanceIsAbsolute;

public:
                     Task_id(string name):Task(name)
     {
      DistanceIsAbsolute = (bool)DistanceIsAbsolute_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      initializer_upper_level
      double upper_level = variable_name_upper_level;

      initializer_lower_level
      double lower_level = variable_name_lower_level;

      initializer_checking_distance
      double distance = variable_name_checking_distance;

      double diff = upper_level - lower_level;

      if(DistanceIsAbsolute == true && diff < 0)
        {
         diff = -1 * diff;
        }

      if(diff compare_val distance)
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         block.onResult(ROUTE_2_PASSED);
        }
     }

   virtual void      reset(int level)
     {
     }
  };
