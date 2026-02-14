class Task1 : public Task
  {
   string                Title;
   string                Label1;
   string                Label2;
   string                Label3;
   string                Label4;
   string               Label5;
   string               Label6;
   string               Label7;
   string               Label8;

public:
                     Task1(string name):Task(name)
     {
      Title = (string)"Notification";
      Label1 = (string)"";
      Label2 = (string)"";
      Label3 = (string)"";
      Label4 = (string)"";
      Label5 = (string)"";
      Label6 = (string)"";
      Label7 = (string)"";
      Label8 = (string)"";
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string text = "";

      if(Label1 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value1 = value.calc<string>();
         text += "\n" + Label1 + ": " + (string)(value1);
        }
      if(Label2 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value2 = value.calc<string>();
         text += "\n" + Label2 + ": " + (string)(value2);
        }
      if(Label3 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value3 = value.calc<string>();
         text += "\n" + Label3 + ": " + (string)(value3);
        }
      if(Label4 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value4 = value.calc<string>();
         text += "\n" + Label4 + ": " + (string)(value4);
        }
      if(Label5 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value5 = value.calc<string>();
         text += "\n" + Label5 + ": " + (string)(value5);
        }
      if(Label6 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value6 = value.calc<string>();
         text += "\n" + Label6 + ": " + (string)(value6);
        }
      if(Label7 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value7 = value.calc<string>();
         text += "\n" + Label7 + ": " + (string)(value7);
        }
      if(Label8 != "")
        {
         Value4_price_fraction value;
         value.init();
         string value8 = value.calc<string>();
         text += "\n" + Label8 + ": " + (string)(value8);
        }

      bool success = SendNotification(Title + "\n" + text);

      if(success == true)
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
