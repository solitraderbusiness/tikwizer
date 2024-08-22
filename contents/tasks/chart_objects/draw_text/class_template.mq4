//Draw Text
class Task3 : public Task
  {
   //defined by user
   bool                  object_per_bar;
   bool                  object_update;
   string                obj_name;
   ENUM_OBJECT           object_type;
   int                   obj_x;
   int                   obj_y;
   string                obj_font;
   int                   obj_font_size;
   double                obj_angle;
   ENUM_BASE_CORNER      obj_corner;
   int                   obj_anchor;
   color                 obj_color;
   bool                  obj_back;
   bool                  obj_selectable;
   bool                  obj_selected;
   bool                  obj_hidden;
   int                   obj_z_order;
   string                obj_chart_subwindow;
   //defined by system
   int               count;
   datetime          time0;

public:
                     Task3(string name):Task(name)
     {
      //defined by user
      object_per_bar = object_per_bar_val;
      object_update = object_update_val;
      obj_name = obj_name_val;
      object_type = object_type_val;
      obj_x = obj_x_val;
      obj_y = obj_y_val;
      obj_font = obj_font_val;
      obj_font_size = obj_font_size_val;
      obj_angle = obj_angle_val;
      obj_corner = obj_corner_val;
      obj_anchor = obj_anchor_val;
      obj_color = obj_color_val;
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

      string obj_name_prefix = "tikwiser_text_";
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
               Print(__FUNCTION__,": failed to create text object! Error code = ",GetLastError());
              }

            double p1=0, p2=0;
            datetime t1=0, t2=0;

            if(object_type == OBJ_TEXT)
              {
               initializer_time_1
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,0,(long)variable_name_time_1);

               initializer_price_1
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,0,(double)variable_name_price_1);
              }
            else
              {
               ObjectSetInteger(obj_chart_id,name,OBJPROP_XDISTANCE,obj_x);
               ObjectSetInteger(obj_chart_id,name,OBJPROP_YDISTANCE,obj_y);
              }

            initializer_text

            ObjectSetString(obj_chart_id,name,OBJPROP_TEXT,(string)variable_name_text);
            ObjectSetString(obj_chart_id,name,OBJPROP_FONT,obj_font);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_FONTSIZE,obj_font_size);
            ObjectSetDouble(obj_chart_id,name,OBJPROP_ANGLE,obj_angle);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_CORNER,obj_corner);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_ANCHOR,obj_anchor);

            //ObjectSetInteger(ObjChartID,name,OBJPROP_STYLE,ObjStyle);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_COLOR,obj_color);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_BACK,obj_back);
            //ObjectSetInteger(ObjChartID,name,OBJPROP_WIDTH,ObjWidth);
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
