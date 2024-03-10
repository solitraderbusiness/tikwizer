class Task0 : public Task
  {
public:
   string                name_starts_with;
   string                name_contains;
   color                 obj_color;
   string                sort_mode;
   int                   max_objects;
   int                   skip_objects;

public:
                     Task0(string name):Task(name)
     {
      name_starts_with = "";
      name_contains = "";
      obj_color = EMPTY_VALUE;
      sort_mode = "z-a";
      max_objects = 0;
      skip_objects = 0;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      // STest: from FXdreema: Fix the problem with "Any color" and the EMPTY_VALUE value

      int index         = 0;
      int total         = ObjectsTotal(0,-1,-1);
      int length        = 0;
      bool deleted      = false;
      int deleted_count = 0;
      int skipped_count = 0;
      string name       = "";

      if(sort_mode == "a-z")
        {
         for(index=0; index<total; index++)
           {
            name = ObjectName(0,index);

            if(name != "")
              {
               if(max_objects > 0 && deleted_count >= max_objects)
                 {
                  break;
                 }

               deleted = false;

               // ObjColor != clrBlack below is because in MQL5 when the value is EMPTY_VALUE, it is turned into clrBlack because of the data type
               if(obj_color != EMPTY_VALUE && obj_color != clrBlack && ObjectGetInteger(0, name, OBJPROP_COLOR) != obj_color)
                 {
                  continue;
                 }

               if(name_starts_with == "" && name_contains == "")
                 {
                  if(skip_objects > 0 && skipped_count < skip_objects)
                    {
                     skipped_count++;
                     continue;
                    }

                  if(ObjectDelete(0,name))
                    {
                     deleted_count++;
                    }
                 }
               else
                 {
                  if(name_starts_with != "")
                    {
                     length = StringLen(name_starts_with);

                     if(StringSubstr(name,0,length) == name_starts_with)
                       {
                        if(skip_objects > 0 && skipped_count < skip_objects)
                          {
                           skipped_count++;
                           continue;
                          }

                        if(ObjectDelete(0,name))
                          {
                           deleted_count++;
                          }
                       }
                    }

                  if(deleted == false && name_contains != "")
                    {
                     if(StringFind(name,name_contains,0) > -1)
                       {
                        if(skip_objects > 0 && skipped_count < skip_objects)
                          {
                           skipped_count++;
                           continue;
                          }

                        if(ObjectDelete(0,name))
                          {
                           deleted_count++;
                          }
                       }
                    }
                 }
              }
           }
        }
      else
         if(sort_mode == "z-a")
           {
            for(index=total-1; index>=0; index--)
              {
               name = ObjectName(0,index);

               if(name != "")
                 {
                  if(max_objects > 0 && deleted_count >= max_objects)
                    {
                     break;
                    }

                  deleted = false;

                  // obj_color != clrBlack below is because in MQL5 when the value is EMPTY_VALUE, it is turned into clrBlack because of the data type
                  if(obj_color != EMPTY_VALUE && obj_color != clrBlack && ObjectGetInteger(0, name, OBJPROP_COLOR) != obj_color)
                    {
                     continue;
                    }

                  if(name_starts_with == "" && name_contains == "")
                    {
                     if(skip_objects > 0 && skipped_count < skip_objects)
                       {
                        skipped_count++;
                        continue;
                       }

                     if(ObjectDelete(0,name))
                       {
                        deleted_count++;
                       }
                    }
                  else
                    {
                     if(name_starts_with != "")
                       {
                        length = StringLen(name_starts_with);

                        if(StringSubstr(name,0,length) == name_starts_with)
                          {
                           if(skip_objects > 0 && skipped_count < skip_objects)
                             {
                              skipped_count++;
                              continue;
                             }

                           if(ObjectDelete(0,name))
                             {
                              deleted_count++;
                             }
                          }
                       }

                     if(deleted == false && name_contains != "")
                       {
                        if(StringFind(name,name_contains,0) > -1)
                          {
                           if(skip_objects > 0 && skipped_count < skip_objects)
                             {
                              skipped_count++;
                              continue;
                             }

                           if(ObjectDelete(0,name))
                             {
                              deleted_count++;
                             }
                          }
                       }
                    }
                 }
              }
           }

      if(deleted_count > 0)
        {
         ChartRedraw();
        }

      printf("task" + block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);

     }
   virtual void      reset(int level)
     {

     }

  };
