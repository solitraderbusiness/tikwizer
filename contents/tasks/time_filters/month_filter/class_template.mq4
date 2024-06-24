class Task_id : public Task
  {
public:
   bool                january;
   bool                february;
   bool                march;
   bool                april;
   bool                may;
   bool                june;
   bool                july;
   bool                august;
   bool                september;
   bool                october;
   bool                november;
   bool                december;
public:
                     Task_id(string name):Task(name)
     {
      january = january_val;
      february = february_val;
      march = march_val;
      april = april_val;
      may = may_val;
      june = june_val;
      july = july_val;
      august = august_val;
      september = september_val;
      october = october_val;
      november = november_val;
      december = december_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      if(
         (january   && Month() == 1)
         || (february  && Month() == 2)
         || (march     && Month() == 3)
         || (april     && Month() == 4)
         || (may       && Month() == 5)
         || (june      && Month() == 6)
         || (july      && Month() == 7)
         || (august    && Month() == 8)
         || (september && Month() == 9)
         || (october   && Month() == 10)
         || (november  && Month() == 11)
         || (december  && Month() == 12)
      )
        {
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         //printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };

