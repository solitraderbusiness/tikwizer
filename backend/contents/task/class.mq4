class Task
  {
public:
   string            name;
public:
                     Task(string name)
     {
        this.name = name;
     }

   virtual void               run(int block_id, BlockParent &block)
     {

     }

   virtual void      reset(int level) = NULL;

  };
