
class Task_id : public Task
  {
   string            symbols_str;
   string            symbols[];
public:
                     Task_id(string name):Task(name)
     {
      symbols_str = symbols_str_val;

      ushort u_sep=StringGetCharacter(",",0);
      StringSplit(symbols_str, u_sep, symbols);
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int size = ArraySize(symbols);
      if(size==0) {
        //printf("task"+block_id + " passed route 2");
        block.onResult(ROUTE_2_PASSED);
        return;
      }


      for(int i=0; i<size; i++)
        {
         overriding_symbol = symbols[i];
         //printf("task"+block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }

      overriding_symbol = "";
      //printf("task"+block_id + " passed route 2");
      block.onResult(ROUTE_2_PASSED);

     }
   virtual void      reset(int level)
     {

     }

  };
