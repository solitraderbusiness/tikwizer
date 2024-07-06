class Task_id : public Task
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
   string               AlsoSendNotification;
public:
                     Task_id(string name):Task(name)
     {
      AlertTitle  = (string)AlertTitle_val;
      AlertLabel1 = (string)AlertLabel1_val;
      AlertLabel2 = (string)AlertLabel2_val;
      AlertLabel3 = (string)AlertLabel3_val;
      AlertLabel4 = (string)AlertLabel4_val;
      AlertLabel5 = (string)AlertLabel5_val;
      AlertLabel6 = (string)AlertLabel6_val;
      AlertLabel7 = (string)AlertLabel7_val;
      AlertLabel8 = (string)AlertLabel8_val;
      AlertLabel9 = (string)AlertLabel9_val;
      AlertLabel10 =(string)AlertLabel10_val;
      AlsoSendNotification = (bool)AlsoSendNotification_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      string text = "";

      if(AlertLabel1 != "")
        {
         initializer_1
         text += "\n" + AlertLabel1 + ": " + (string)(variable_name_1);
        }
      if(AlertLabel2 != "")
        {
         initializer_2
         text += "\n" + AlertLabel2 + ": " + (string)(variable_name_2);
        }
      if(AlertLabel3 != "")
        {
        initializer_3
         text += "\n" + AlertLabel3 + ": " + (string)(variable_name_3);
        }
      if(AlertLabel4 != "")
        {
         initializer_4
         text += "\n" + AlertLabel4 + ": " + (string)(variable_name_4);
        }
      if(AlertLabel5 != "")
        {
         initializer_5
         text += "\n" + AlertLabel5 + ": " + (string)(variable_name_5);
        }
      if(AlertLabel6 != "")
        {
         initializer_6
         text += "\n" + AlertLabel6 + ": " + (string)(variable_name_6);
        }
      if(AlertLabel7 != "")
        {
         initializer_7
         text += "\n" + AlertLabel7 + ": " + (string)(variable_name_7);
        }
      if(AlertLabel8 != "")
        {
         initializer_8
         text += "\n" + AlertLabel8 + ": " + (string)(variable_name_8);
        }
      if(AlertLabel9 != "")
        {
         initializer_9
         text += "\n" + AlertLabel9 + ": " + (string)(variable_name_9);
        }
      if(AlertLabel10 != "")
        {
         initializer_10
         text += "\n" + AlertLabel10 + ": " + (string)(variable_name_10);
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
