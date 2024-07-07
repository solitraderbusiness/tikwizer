class Task1 : public Task
  {

   string                MTsound;
   string                MYsound;

public:
                     Task1(string name):Task(name)
     {
      MTsound = (string)MTsound_val;
      MYsound = (string)MYsound_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string filename = MTsound;

      if(MTsound == "custom")
        {
         filename = MYsound;
        }
      else
         if(StringSubstr(filename, StringLen(filename)-4) != ".wav")
           {
            filename += ".wav";
           }

      bool success = PlaySound(filename);

      if(!success)
        {
         Print("Play Sound Error: " + ErrorMessage());
        }

      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }
  };
