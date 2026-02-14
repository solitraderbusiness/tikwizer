class Task3 : public Task
  {
   bool                DistanceIsAbsolute;

public:
                     Task3(string name):Task(name)
     {
      DistanceIsAbsolute = (bool)false;

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      Value3_upper_level value3_upper_level;
      value3_upper_level.init();
      double valuevalue3_upper_level = value3_upper_level.calc();
      double upper_level = valuevalue3_upper_level;

      Value3_lower_level value3_lower_level;
      value3_lower_level.init();
      double valuevalue3_lower_level = value3_lower_level.calc();
      double lower_level = valuevalue3_lower_level;


      Value3_checking_distance value3_checking_distance;
      value3_checking_distance.init();
      double valuevalue3_checking_distance = value3_checking_distance.calc();
      double distance = valuevalue3_checking_distance;

      double diff = upper_level - lower_level;

      if(DistanceIsAbsolute == true && diff < 0)
        {
         diff = -1 * diff;
        }

      if(diff > distance)
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
