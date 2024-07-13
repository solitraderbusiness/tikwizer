class Task1 : public Task
  {
   string                AlertTitle;
   string                AlertLabel1;
   string                AlertLabel2;
   string                AlertLabel3;
   string                AlertLabel4;
   string               AlertLabel5;
   string               AlertLabel6;
   string               AlertLabel7;
   string               AlertLabel8;
   string               AlertLabel9;
   string               AlertLabel10;
   bool               AlsoSendNotification;
public:
                     Task1(string name):Task(name)
     {
      AlertTitle = (string)"Alert Message";
      AlertLabel1 = (string)"";
      AlertLabel2 = (string)"";
      AlertLabel3 = (string)"";
      AlertLabel4 = (string)"";
      AlertLabel5 = (string)"";
      AlertLabel6 = (string)"";
      AlertLabel7 = (string)"";
      AlertLabel8 = (string)"";
      AlertLabel9 = (string)"";
      AlertLabel10 = (string)"";
      AlsoSendNotification = (bool)false;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      string text = "";

      if(AlertLabel1 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value1 = value.calc<string>();
         text += "\n" + AlertLabel1 + ": " + (string)(value1);
        }
      if(AlertLabel2 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value2 = value.calc<string>();
         text += "\n" + AlertLabel2 + ": " + (string)(value2);
        }
      if(AlertLabel3 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value3 = value.calc<string>();
         text += "\n" + AlertLabel3 + ": " + (string)(value3);
        }
      if(AlertLabel4 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value4 = value.calc<string>();
         text += "\n" + AlertLabel4 + ": " + (string)(value4);
        }
      if(AlertLabel5 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value5 = value.calc<string>();
         text += "\n" + AlertLabel5 + ": " + (string)(value5);
        }
      if(AlertLabel6 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value6 = value.calc<string>();
         text += "\n" + AlertLabel6 + ": " + (string)(value6);
        }
      if(AlertLabel7 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value7 = value.calc<string>();
         text += "\n" + AlertLabel7 + ": " + (string)(value7);
        }
      if(AlertLabel8 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value8 = value.calc<string>();
         text += "\n" + AlertLabel8 + ": " + (string)(value8);
        }
      if(AlertLabel9 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value9 = value.calc<string>();
         text += "\n" + AlertLabel9 + ": " + (string)(value9);
        }
      if(AlertLabel10 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value10 = value.calc<string>();
         text += "\n" + AlertLabel10 + ": " + (string)(value10);
        }

      text = AlertTitle + "\n" + text;

      Alert(text);

      if(AlsoSendNotification==true)
         SendNotification(text);

      block.onResult(ROUTE_1_PASSED);

     }
   virtual void      reset(int level)
     {

     }

  };
