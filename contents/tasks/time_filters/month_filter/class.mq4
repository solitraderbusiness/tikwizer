class Task2 : public Task
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
                     Task2(string name):Task(name)
     {
      january = true;
      february = true;
      march = true;
      april = true;
      may = true;
      june = true;
      july = true;
      august = true;
      september = true;
      october = true;
      november = true;
      december = true;
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
         printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task"+block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }
     }
   virtual void      reset(int level)
     {

     }

  };

