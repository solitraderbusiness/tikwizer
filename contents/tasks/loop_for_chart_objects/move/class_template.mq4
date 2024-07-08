class Task_id : public Task
  {
   bool                SetObjTime1;
   bool                SetObjPrice1;
   bool                SetObjTime2;
   bool                SetObjPrice2;
   bool                SetObjTime3;
   bool                SetObjPrice3;

public:
                     Task_id(string name):Task(name)
     {
      SetObjTime1 = (bool)SetObjTime1_val;
      SetObjPrice1 = (bool)SetObjPrice1_val;
      SetObjTime2 = (bool)SetObjTime2_val;
      SetObjPrice2 = (bool)SetObjPrice2_val;
      SetObjTime3 = (bool)SetObjTime3_val;
      SetObjPrice3 = (bool)SetObjPrice3_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string name   = loaded_object_name();
      long chart_id = loaded_object_chart_id();

      if(SetObjTime1)
        {
         initializer_time_1
         ObjectSetInteger(chart_id,name,OBJPROP_TIME,0,variable_name_time_1);//time1
        }
      if(SetObjPrice1)
        {
         initializer_price_1
         ObjectSetDouble(chart_id,name,OBJPROP_PRICE,0,variable_name_price_1);//price1
        }

      if(SetObjTime2)
        {
         initializer_time_2
         ObjectSetInteger(chart_id,name,OBJPROP_TIME,1,variable_name_time_2);//time2
        }
      if(SetObjPrice2)
        {
         initializer_price_2
         ObjectSetDouble(chart_id,name,OBJPROP_PRICE,1,variable_name_price_2);//price2
        }

      if(SetObjTime3)
        {
         initializer_time_3
         ObjectSetInteger(chart_id,name,OBJPROP_TIME,2,variable_name_time_3);//time3
        }
      if(SetObjPrice3)
        {
         initializer_price_3
         ObjectSetDouble(chart_id,name,OBJPROP_PRICE,2,variable_name_price_3);//price3
        }

      //printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
