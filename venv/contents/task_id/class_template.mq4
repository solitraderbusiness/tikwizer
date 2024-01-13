class Task_id : public Task
  {
   field_data
public:
                     Task_id(string name):Task(name)
     {
         constructor_data
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      run_data
     }
   virtual void      reset(int level) {
      reset_data
   }
   function_data
  };
