class Task_id : public Task
  {
public:
   long              obj_chart_id;
   int               obj_subwindow;
   ENUM_OBJECT       obj_type; //-1 for any type, and ENUM_OBJECT items for other object types
   int               is_arrow_type;
   int               arrow_code; //search arrow code in MQL4 documentation
   color             obj_color;
   string            obj_name_prefix;
   string            obj_name_contains;
   string            loop_direction;
   int               loop_skip;
   int               loop_limit;

public:
                     Task_id(string name):Task(name)
     {
      obj_chart_id = obj_chart_id_val;
      obj_subwindow = obj_subwindow_val;
      obj_type = obj_type_val;
      is_arrow_type = is_arrow_type_val;
      arrow_code = arrow_code_val;
      obj_color = obj_color_val;
      obj_name_prefix = obj_name_prefix_val;
      obj_name_contains = obj_name_contains_val;
      loop_direction = loop_direction_val;
      loop_skip = loop_skip_val;
      loop_limit = loop_limit_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      long chart_id  = obj_chart_id;
      int sub_window = obj_subwindow;

      int count = 0;
      int skip  = -1;
      string name;
      ENUM_OBJECT type;

      int i_start = ObjectsTotal(chart_id) - 1;
      int i_stop  = 0;
      int i_inc   = -1;

      if(loop_direction == "a-z")
        {
         i_stop  = i_start;
         i_start = 0;
         i_inc   = 1;
        }

      int i = i_start - i_inc;

      while(true)
        {
         if(i == i_stop)
           {
            break;
           }
         i = i + i_inc;

         if(load_object(i,chart_id,sub_window,obj_type))
           {
            name = loaded_object_name();
            type = (ENUM_OBJECT)ObjectGetInteger(chart_id,name,OBJPROP_TYPE);

            if(obj_color != clrNONE && ObjectGetInteger(chart_id,name,OBJPROP_COLOR) != obj_color)
              {
               continue;
              }

            if(
               obj_type < 0
               || (type != OBJ_ARROW && type == obj_type)
               || (type == OBJ_ARROW && is_arrow_type == -1 && (arrow_code == 0 || arrow_code == ObjectGetInteger(chart_id,name,OBJPROP_ARROWCODE)))
               || (type == OBJ_ARROW && ObjectGetInteger(chart_id,name,OBJPROP_ARROWCODE) == is_arrow_type)
            )
              {
               if(obj_name_prefix != "" && StringSubstr(name,0,StringLen(obj_name_prefix)) != obj_name_prefix)
                 {
                  continue;
                 }
               if(obj_name_contains != "" && StringFind(name,obj_name_contains) == -1)
                 {
                  continue;
                 }

               skip++;

               if(loop_skip <= skip && (count < loop_limit || loop_limit == 0))
                 {
                  count++;

                  //printf("task"+block_id + " passed route 1");
                  block.onResult(ROUTE_1_PASSED);

                  if(count == loop_limit)
                     break;
                 }
              }
           }
        }


      //printf("task"+block_id + " passed route 2");
      block.onResult(ROUTE_2_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
bool load_object(int index, long chart_id,int sub_window, int obj_type)
  {
   string name = ObjectName(chart_id,index,sub_window, obj_type);

   if(name == "")
     {
      return false;
     }

   loaded_object_chart_id(chart_id);
   loaded_object_name(name);
   loaded_object_subwindow(sub_window);
   loaded_object_type((int)ObjectGetInteger(chart_id,name,OBJPROP_TYPE));

   return true;
  }
