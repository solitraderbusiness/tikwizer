class Task_id : public Task
  {

public:
   string            message;
                     Task_id(string name):Task(name)
     {
      message = message_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(message != "")
        {
         MessageBox(message, "Self-Terminate", MB_OK);
        }

      ExpertRemove();
      ChartRedraw(); // to remove the smile face
     }
   virtual void      reset(int level)
     {

     }

  };
