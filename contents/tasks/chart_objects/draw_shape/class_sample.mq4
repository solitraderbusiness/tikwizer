class Task0 : public Task
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
                     Task0(string name):Task(name)
     {
      //defined by user
      object_per_bar = false;
      object_update = true;
      obj_name = "";
      object_type = OBJ_RECTANGLE;
      obj_x = 10;
      obj_y = 10;
      obj_fill = false;
      obj_x_size = 100;
      obj_y_size = 100;
      obj_border_type = BORDER_FLAT;
      obj_bg_color = clrSkyBlue;
      obj_corner = CORNER_LEFT_UPPER;
      obj_color = clrDeepPink;
      obj_style = STYLE_SOLID;
      obj_width = 1;
      obj_back = false;
      obj_selectable = true;
      obj_selected = false;
      obj_hidden = false;
      obj_z_order = 0;
      obj_chart_subwindow = "";
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
               Value1_right value0_time_1;
               value0_time_1.init();
               datetime valueValue0_time_1 = value0_time_1.calc();
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,0,Time[10]);
              }
            if(t2 == 1)
              {
               Value1_right value0_time_2;
               value0_time_2.init();
               datetime valueValue0_time_2 = value0_time_2.calc();
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,1,Time[20]);
              }
            if(t3 == 1)
              {
               Value1_right value0_time_3;
               value0_time_3.init();
               datetime valueValue0_time_3 = value0_time_3.calc();
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,2,Time[30]);
              }
            if(p1 == 1)
              {
               Value1_right value0_price_1;
               value0_price_1.init();
               datetime valueValue0_price_1 = value0_price_1.calc();
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,0,Close[10]);
              }
            if(p2 == 1)
              {
               Value1_right value0_price_2;
               value0_price_2.init();
               datetime valueValue0_price_2 = value0_price_2.calc();
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,1,Close[20]);
              }
            if(p3 == 1)
              {
               Value1_right value0_price_3;
               value0_price_3.init();
               datetime valueValue0_price_3 = value0_price_3.calc();
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,2,Close[30]);
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
