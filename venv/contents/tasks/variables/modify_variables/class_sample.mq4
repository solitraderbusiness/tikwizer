class Task23 : public Task

  {
public:
                     Task23(string name):Task(name)
     {

     }

public:
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      MACD1 macd1;
      macd1.init();
      double valueMACD1 = macd1.calc();
      xxxx = valueMACD1;

      Value2 value2;
      value2.init();
      double valueValue2 = value2.calc();
      yyyy = valueValue2;

      block.onResult(ROUTE_1_PASSED);

     }

   virtual void      reset(int level) {}

  };
