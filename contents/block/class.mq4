class Block : BlockParent
  {


public:
   int               id;
   int               id_by_user;
   string            name;
   bool              enabled;


   int               next_true_history[];//dynamic, filled at runtime
   int               next_false_history[];//dynamic, filled at runtime
   int               prevs_true_history[];//dynamic, filled at runtime
   int               prevs_false_history[];//dynamic, filled at runtime

   Task              *task;



public:
                     Block()
     {

     }

   virtual void      next_true()
     {
      for(int i=0; i<ArraySize(nexts_true); i++)
         runBlockTick(id, ROUTE_1_PASSED, nexts_true[i]);//-1 : block id to block index
     }

   virtual void      next_false()
     {
      for(int i=0; i<ArraySize(nexts_false); i++)
         runBlockTick(id, ROUTE_2_PASSED, nexts_false[i]);
     }

   virtual void              run(int source_id, int source_result)
     {
      if(!enabled)
         return;
      addToHistory(source_id, source_result);
      current_source_id = source_id;
      task.run(id_by_user, this);

     };

   void              addToHistory(int source_id, int source_result)
     {
      if(true) //STest, this is to prevent excessive memory usage
         return;
      if(source_id<0)
         return;

      if(source_result == ROUTE_1_PASSED)
        {
         AddToArray(prevs_true_history, source_id);
        }
      else
         if(source_result == ROUTE_2_PASSED)
           {
            AddToArray(prevs_false_history, source_id);
           }
     }

   virtual void      onResult(int result)
     {
      if(result == ROUTE_1_PASSED)
         next_true();
      else
         if(result == ROUTE_2_PASSED)
            next_false();
     }

   virtual void              reset(int level)
     {
      task.reset(level);
     };

   void              populateNextsTrue(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(nexts_true, items[i]);
     }
   void              populateNextsFalse(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(nexts_false, items[i]);
     }
   void              populatePrevsTrue(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(prevs_true, items[i]);
     }
   void              populatePrevsFalse(int &items[])
     {
      for(int i=0; i<ArraySize(items); i++)
         AddToArray(prevs_false, items[i]);
     }

  };

