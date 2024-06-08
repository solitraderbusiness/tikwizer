class Task_id : public Task
  {
   //defined by user
   bool                object_per_bar;
   bool                object_update;
   string              obj_name;
   ENUM_OBJECT         object_type;
   double              obj_angle;
   bool                obj_ray;
   bool                obj_ray_left;
   bool                obj_ray_right;
   color               obj_color;
   ENUM_LINE_STYLE     obj_style;
   int                 obj_width;
   bool                obj_back;
   bool                obj_selectable;
   bool                obj_selected;
   bool                obj_hidden;
   int                 obj_z_order;
   string              obj_chart_subwindow;
   //defined by system
   int               count;
   datetime          time0;


public:
                     Task_id(string name):Task(name)
     {
      //defined by user
      object_per_bar = object_per_bar_val;
      object_update = object_update_val;
      obj_name = obj_name_val;
      object_type = object_type_val;
      obj_angle = obj_angle_val;
      obj_ray = obj_ray_val;
      obj_ray_left = obj_ray_left_val;
      obj_ray_right = obj_ray_right_val;
      obj_color = obj_color_val;
      obj_style = obj_style_val;
      obj_width = obj_width_val;
      obj_back = obj_back_val;
      obj_selectable = obj_selectable_val;
      obj_selected = obj_selected_val;
      obj_hidden = obj_hidden_val;
      obj_z_order = obj_z_order_val;
      obj_chart_subwindow = obj_chart_subwindow_val;
      //defined by system
      count =  0;
      time0 =  0;

     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      string obj_name_prefix = "goldblox_line_";
      long obj_chart_id      = 0;
      int subwindow_id     = WindowFindVisible(obj_chart_id, obj_chart_subwindow);

      if(subwindow_id >= 0)
        {
         string name       = "";
         string name_base  = "";
         bool get_new_name = false;
         bool do_update    = true;

         if(object_per_bar == true)
           {
            datetime time = iTime(Symbol(),0,1);

            if(time0 < time)
              {
               time0        = time;
               get_new_name = true;
              }
            else
              {
               if(object_update == false)
                 {
                  do_update = false;
                 }
              }
           }
         else
           {
            if(object_update == false)
              {
               get_new_name = true;
              }
           }

         if(do_update)
           {
            if(obj_name != "")
              {
               name_base = obj_name;
              }
            else
              {
               Block *mblock = (Block*) GetPointer(block);
               name_base = obj_name_prefix + mblock.id_by_user + "_";
              }

            if(get_new_name == false)
              {
               name = name_base + IntegerToString(count);
              }
            else
              {
               while(true)
                 {
                  count++;
                  name = name_base + IntegerToString(count);

                  if(ObjectFind(obj_chart_id,name) < 0)
                    {
                     break;
                    }
                 }
              }

            if(obj_name != "" && count == 0)
              {
               name = obj_name;
              }

            if(ObjectFind(obj_chart_id,name) < 0 && !ObjectCreate(obj_chart_id,name,(ENUM_OBJECT)object_type,subwindow_id,0,0))
              {
               Print(__FUNCTION__,": failed to create line object! Error code = ",GetLastError());
              }

            double p1=0, p2=0;
            datetime t1=0, t2=0;

            switch(object_type)
              {
               case OBJ_VLINE        :
                 {t1=1; break;}
               case OBJ_HLINE        :
                 {p1=1; break;}
               case OBJ_TREND        :
                 {t1=1; p1=1; t2=1; p2=1; break;}
               case OBJ_TRENDBYANGLE :
                 {t1=1; p1=1; break;}
               case OBJ_CYCLES       :
                 {t1=1; p1=1; t2=1; p2=1; break;}
              }

            if(t1 == 1)
              {
               initializer_time_1
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,0,variable_name_time_1);
              }
            if(t2 == 1)
              {
               initializer_time_2
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,1,variable_name_time_2);
              }
            if(p1 == 1)
              {
               initializer_price_1
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,0,variable_name_price_1);
              }
            if(p2 == 1)
              {
               initializer_price_2
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,1,variable_name_price_2);
              }

            ObjectSetInteger(obj_chart_id,name,OBJPROP_STYLE,obj_style);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_COLOR,obj_color);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_BACK,obj_back);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_WIDTH,obj_width);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_SELECTABLE,obj_selectable);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_SELECTED,obj_selected);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_HIDDEN,obj_hidden);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_ZORDER,obj_z_order);

            ObjectSetDouble(obj_chart_id,name,OBJPROP_ANGLE,obj_angle);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_RAY,obj_ray);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_RAY_LEFT,obj_ray_left);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_RAY_RIGHT,obj_ray_right);

            ChartRedraw();
           }
        }

      printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
