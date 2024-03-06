class Task0 : public Task
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
                     Task0(string name):Task(name)
     {
      //defined by user
      object_per_bar = false;
      object_update = true;
      obj_name = "";
      object_type = OBJ_TREND;
      obj_angle = 45.0;
      obj_ray = true;
      obj_ray_left = false;
      obj_ray_right = false;
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

      string obj_name_prefix = "goldbox_line_";
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
               Value0_time_1 value0_time_1;
               value0_time_1.init();
               datetime valueValue0_time_1 = value0_time_1.calc();
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,0,Time[1]);
              }
            if(t2 == 1)
              {
               Value0_time_2 value0_time_2;
               value0_time_2.init();
               datetime valueValue0_time_2 = value0_time_2.calc();
               ObjectSetInteger(obj_chart_id,name,OBJPROP_TIME,1,Time[100]);
              }
            if(p1 == 1)
              {
               Candle0_price_1 candle0_price_1;
               candle0_price_1.init();
               double valueCandle0_price_1 = candle0_price_1.calc();
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,0,Close[1]);
              }
            if(p2 == 1)
              {
               Candle0_price_2 candle0_price_2;
               candle0_price_2.init();
               double valueCandle0_price_2 = candle0_price_2.calc();
               ObjectSetDouble(obj_chart_id,name,OBJPROP_PRICE,1,Close[100]);
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
