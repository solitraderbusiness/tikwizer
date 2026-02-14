class Task40 : public Task
  {

public:
   string            message;
                     Task40(string name):Task(name)
     {
      message = "Expert terminated successfully";
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
