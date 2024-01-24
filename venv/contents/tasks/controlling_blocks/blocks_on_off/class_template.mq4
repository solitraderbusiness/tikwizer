
class Task_id : public Task
  {
public:
   string            block_ids;
   int               what;
public:
                     Task_id(string name):Task(name)
     {
      block_ids = block_ids_val;
      what = what_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string ids[];
      ushort u_sep=StringGetCharacter(",",0);
      int totalElements = StringSplit(block_ids, u_sep, ids);
      if(totalElements<=0)
         block.onResult(ROUTE_1_PASSED);
      for(int i=0; i<ArraySize(ids); i++)
        {
         string id = ids[i];
         id = StringTrimLeft(id);
         id = StringTrimRight(id);
         int mid = StrToInteger(id);

         for(int j=0; j<ArraySize(blocks_init); j++)
            if(blocks_init[j].id_by_user == mid)
               blocks_init[j].enabled = newValue(blocks_init[j].enabled);

         for(int k=0; k<ArraySize(blocks_timer); k++)
            if(blocks_timer[k].id_by_user == mid)
               blocks_timer[k].enabled = newValue(blocks_timer[k].enabled);

         for(int l=0; l<ArraySize(blocks_tick); l++)
            if(blocks_tick[l].id_by_user == mid)
               blocks_tick[l].enabled = newValue(blocks_tick[l].enabled);

         for(int m=0; m<ArraySize(blocks_trade); m++)
            if(blocks_trade[m].id_by_user == mid)
               blocks_trade[m].enabled = newValue(blocks_trade[m].enabled);

         for(int n=0; n<ArraySize(blocks_chart); n++)
            if(blocks_chart[n].id_by_user == mid)
               blocks_chart[n].enabled = newValue(blocks_chart[n].enabled);

         for(int p=0; p<ArraySize(blocks_deinit); p++)
            if(blocks_deinit[p].id_by_user == mid)
               blocks_deinit[p].enabled = newValue(blocks_deinit[p].enabled);
        }
        block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

   bool              newValue(bool currentValue)
     {
      switch(what)
        {
         case BLOCK_STATE_ENABLE:
            return true;
         case BLOCK_STATE_DISABLE:
            return false;
         case BLOCK_STATE_TOGGLE:
            return !currentValue;
         default:
            return true;
        }
     }

  };
