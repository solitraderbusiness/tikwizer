class Task7 : public Task
  {
   int                TimesToPass;
   int                CounterID;
public:
                     Task7(string name):Task(name)
     {
      TimesToPass = 3;
      CounterID = 1;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int passes = Counter(CounterID, "increment");

      if(passes < TimesToPass)
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

   int               Counter(int id, string cmd = "", int set_passes = 0)
     {
      static int idx[]; // index list
      static int pl[];  // passes list
      int size    = 0;
      int passes  = 0;
      int cnt_idx = ArraySearch(idx, id);

      if(cnt_idx == -1)
        {
         // Counter not found
         size = ArraySize(idx);

         ArrayResize(idx, size + 1);
         ArrayResize(pl, size + 1);

         idx[size] = id;
         pl[size]  = 0;
         cnt_idx   = size;
        }

      passes = pl[cnt_idx];

      if(cmd != "")
        {
         if(cmd == "increment")
           {
            pl[cnt_idx] = pl[cnt_idx] + 1;
           }
         else
            if(cmd == "reset")
              {
               pl[cnt_idx] = 0;
              }
        }

      return passes;
     }

   template<typename T>
   int               ArraySearch(T &array[], T value)
     {
      int index = -1;
      int size  = ArraySize(array);

      for(int i = 0; i < size; i++)
        {
         if(array[i] == value)
           {
            index = i;
            break;
           }
        }

      return index;
     }


  };
