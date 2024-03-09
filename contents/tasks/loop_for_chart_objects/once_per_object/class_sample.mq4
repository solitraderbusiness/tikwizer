class Task0 : public Task
  {
public:
   string            memory[];

public:
                     Task0(string name):Task(name)
     {

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);


      string value = IntegerToString(loaded_object_chart_id() + loaded_object_name());

      if(in_array(memory, value) == false)
        {
         array_ensure_value(memory, value);

         printf("task" + block_id + " passed route 1");
         block.onResult(ROUTE_1_PASSED);
        }
      else
        {
         printf("task" + block_id + " passed route 2");
         block.onResult(ROUTE_2_PASSED);
        }

     }
   virtual void      reset(int level)
     {

     }

  };

template<typename T>
bool in_array(T &array[], T value)
  {
   int size = ArraySize(array);

   if(size > 0)
     {
      for(int i = 0; i < size; i++)
        {
         if(array[i] == value)
           {
            return true;
           }
        }
     }

   return false;
  }


template<typename T>
bool array_ensure_value(T &array[], T value)
  {
   int size   = ArraySize(array);

   if(size > 0)
     {
      if(in_array(array, value))
        {
         // value found -> exit
         return false; // no value added
        }
     }

// value does not exists -> add it
   ArrayResize(array, size+1);
   array[size] = value;

   return true; // value added
  }
