class Task1 : public Task
  {
   bool                SetObjTime1;
   bool                SetObjPrice1;
   bool                SetObjTime2;
   bool                SetObjPrice2;
   bool                SetObjTime3;
   bool                SetObjPrice3;

public:
                     Task1(string name):Task(name)
     {
      SetObjTime1 = (bool)true;
      SetObjPrice1 = (bool)false;
      SetObjTime2 = (bool)false;
      SetObjPrice2 = (bool)false;
      SetObjTime3 = (bool)false;
      SetObjPrice3 = (bool)false;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string name   = loaded_object_name();
      long chart_id = loaded_object_chart_id();

      if(SetObjTime1)
        {
         Value4_price_fraction value_time_1;
         value_time_1.init();
         double valueValueTime1 = value_time_1.calc<double>();
         ObjectSetInteger(chart_id,name,OBJPROP_TIME,0,valueValueTime1);//time1
        }
      if(SetObjPrice1)
        {
         Value4_price_fraction value_price_1;
         value_price_1.init();
         double valueValuePrice1 = value_price_1.calc<double>();
         ObjectSetDouble(chart_id,name,OBJPROP_PRICE,0,valueValuePrice1);//price1
        }

      if(SetObjTime2)
        {
         Value4_price_fraction value_time_2;
         value_time_2.init();
         double valueValueTime2 = value_time_2.calc<double>();
         ObjectSetInteger(chart_id,name,OBJPROP_TIME,1,valueValueTime2);//time2
        }
      if(SetObjPrice2)
        {
         Value4_price_fraction value_price_2;
         value_price_2.init();
         double valueValuePrice2 = value_price_2.calc<double>();
         ObjectSetDouble(chart_id,name,OBJPROP_PRICE,1,valueValuePrice2);//price2
        }

      if(SetObjTime3)
        {
         Value4_price_fraction value_time_3;
         value_time_3.init();
         double valueValueTime3 = value_time_3.calc<double>();
         ObjectSetInteger(chart_id,name,OBJPROP_TIME,2,valueValueTime3);//time3
        }
      if(SetObjPrice3)
        {
         Value4_price_fraction value_price_3;
         value_price_3.init();
         double valueValuePrice3 = value_price_3.calc<double>();
         ObjectSetDouble(chart_id,name,OBJPROP_PRICE,2,valueValuePrice3);//price3
        }

      //printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
