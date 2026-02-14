class Task_id : public Task
  {
   //defined by user
   bool              object_per_bar;
   bool              object_update;
   string            obj_name;
   ENUM_OBJECT       object_type;
   int               obj_x;
   int               obj_y;
   bool              obj_fill;
   int               obj_x_size;
   int               obj_y_size;
   int               obj_border_type;
   color             obj_bg_color;
   int               obj_corner;
   color             obj_color;
   ENUM_LINE_STYLE   obj_style;
   int               obj_width;
   bool              obj_back;
   bool              obj_selectable;
   bool              obj_selected;
   bool              obj_hidden;
   int               obj_z_order;
   string            obj_chart_subwindow;
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
      obj_x = obj_x_val;
      obj_y = obj_y_val;
      obj_fill = obj_fill_val;
      obj_x_size = obj_x_size_val;
      obj_y_size = obj_y_size_val;
      obj_border_type = obj_border_type_val;
      obj_bg_color = obj_bg_color_val;
      obj_corner = obj_corner_val;
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

      string obj_name_prefix = "tikwiser_shape_";
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
               Print(__FUNCTION__,": Object failed to create! Error code = ",GetLastError());
              }

            double p1=0, p2=0, p3=0;
            datetime t1=0, t2=0, t3=0;

            switch(object_type)
              {
               case OBJ_RECTANGLE_LABEL :
                 {break;}
               case OBJ_RECTANGLE       :
                 {t1=1; p1=1; t2=1; p2=1; break;}
               case OBJ_TRIANGLE        :
                 {t1=1; p1=1; t2=1; p2=1; t3=1; p3=1; break;}
               case OBJ_ELLIPSE         :
                 {t1=1; p1=1; t2=1; p2=1; t3=1; p3=1; break;}
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
            if(t3 == 1)
              {
               initializer_time_3
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,2,variable_name_time_3);
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
            if(p3 == 1)
              {
               initializer_price_3
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,2,variable_name_price_3);
              }

            if(object_type==OBJ_RECTANGLE_LABEL)
              {
               ObjectSetInteger(obj_chart_id,name,OBJPROP_XDISTANCE,obj_x);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_YDISTANCE,obj_y);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_XSIZE,obj_x_size);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_YSIZE,obj_y_size);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_BGCOLOR,obj_bg_color);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_BORDER_TYPE,obj_border_type);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_CORNER,obj_corner);
              }
            else
              {
               ObjectSetInteger(obj_chart_id,name,OBJPROP_FILL,obj_fill);
              }

            ObjectSetInteger(obj_chart_id,name,OBJPROP_STYLE,obj_style);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_COLOR,obj_color);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_BACK,obj_back);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_WIDTH,obj_width);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_SELECTABLE,obj_selectable);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_SELECTED,obj_selected);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_HIDDEN,obj_hidden);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_ZORDER,obj_z_order);

            ChartRedraw();
           }
        }

      //printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

  };
