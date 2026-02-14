class Task_id : public Task
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
                     Task_id(string name):Task(name)
     {
      Title  = (string)Title_val;
      Label1 = (string)Label1_val;
      Label2 = (string)Label2_val;
      Label3 = (string)Label3_val;
      Label4 = (string)Label4_val;
      Label5 = (string)Label5_val;
      Label6 = (string)Label6_val;
      Label7 = (string)Label7_val;
      Label8 = (string)Label8_val;

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string text = "";

      if(Label1 != "")
        {
         initializer_1
         text += "\n" + Label1 + ": " + (string)(variable_name_1);
        }
      if(Label2 != "")
        {
         initializer_2
         text += "\n" + Label2 + ": " + (string)(variable_name_2);
        }
      if(Label3 != "")
        {
        initializer_3
         text += "\n" + Label3 + ": " + (string)(variable_name_3);
        }
      if(Label4 != "")
        {
         initializer_4
         text += "\n" + Label4 + ": " + (string)(variable_name_4);
        }
      if(Label5 != "")
        {
         initializer_5
         text += "\n" + Label5 + ": " + (string)(variable_name_5);
        }
      if(Label6 != "")
        {
         initializer_6
         text += "\n" + Label6 + ": " + (string)(variable_name_6);
        }
      if(Label7 != "")
        {
         initializer_7
         text += "\n" + Label7 + ": " + (string)(variable_name_7);
        }
      if(Label8 != "")
        {
         initializer_8
         text += "\n" + Label8 + ": " + (string)(variable_name_8);
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
