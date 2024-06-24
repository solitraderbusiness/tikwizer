class Task0 : public Task
  {

public:
   //defined by user
   bool                  object_per_bar;
   bool                  object_update;
   string                obj_name;
   int                   obj_x;
   int                   obj_y;
   string                obj_font;
   int                   obj_font_size;
   int                   obj_x_size;
   int                   obj_y_size;
   color                 obj_bg_color;
   color                 obj_border_color;
   int                   obj_corner;
   bool                  obj_state;
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
                     Task0(string name):Task(name)
     {
      //defined by user
      object_per_bar = false;
      object_update = true;
      obj_name = "";
      obj_x = 10;
      obj_y = 10;
      obj_font = "Arial";
      obj_font_size = 10;
      obj_x_size = 100;
      obj_y_size = 20;
      obj_bg_color = clrWhite;
      obj_border_color = clrNONE;
      obj_corner = CORNER_LEFT_UPPER;
      obj_state = false;
      obj_color = clrDeepPink;
      obj_back = false;
      obj_selectable = false;
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

      string obj_name_prefix = "goldblox_button_";
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

            if(ObjectFind(obj_chart_id,name) < 0 && !ObjectCreate(obj_chart_id,name,OBJ_BUTTON,subwindow_id,0,0))
              {
               Print(__FUNCTION__,": button failed to create! Error code = ",GetLastError());
              }


            //_ObjText_()
            Value1_right value1__btn_txt;
            string valueValue1_btn_txt = value1__btn_txt.calc();


            ObjectSetInteger(obj_chart_id,name,OBJPROP_XDISTANCE,obj_x);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_YDISTANCE,obj_y);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_XSIZE,obj_x_size);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_YSIZE,obj_y_size);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_BGCOLOR,obj_bg_color);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_BORDER_COLOR,obj_border_color);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_CORNER,obj_corner);
            ObjectSetString(obj_chart_id,name,OBJPROP_FONT,obj_font);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_FONTSIZE,obj_font_size);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_STATE,obj_state);
            ObjectSetString(obj_chart_id,name,OBJPROP_TEXT, "hello");

            ObjectSetInteger(obj_chart_id,name,OBJPROP_COLOR,obj_color);
            ObjectSetInteger(obj_chart_id,name,OBJPROP_BACK,obj_back);
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
