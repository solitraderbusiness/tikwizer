//Volume Profile
class Task5 : public Task
  {
   bool             redraw_each_time;
   /* Calculation */
   ENUM_VP_RANGE_MODE RangeMode;    // Range mode
   int               RangeMinutes;  // Range minutes
   int               ModeStep;      // Mode step (points)
   ENUM_POINT_SCALE  HgPointScale;
   int               numberOfBars;  // Point scale
   ENUM_APPLIED_VOLUME VolumeType;  // Volume type
   ENUM_VP_SOURCE    DataSource;    // Data source

   /* Histogram */
   ENUM_VP_BAR_STYLE HgBarStyle;    // Bar style
   ENUM_VP_HG_POSITION HgPosition;  // Histogram position
   color             HgColor;       // Color 1
   color             HgColor2;      // Color 2
   int               HgLineWidth;   // Line width

   /* Levels */
   color             ModeColor;     // Mode color
   color             MaxColor;      // Maximum color
   color             MedianColor;   // Median color
   color             VwapColor;     // VWAP color
   int               ModeLineWidth; // Mode line width
   ENUM_LINE_STYLE   StatLineStyle; // Median & VWAP line style

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   color             ModeLevelColor; // Mode level line color (None=disable)
   int               ModeLevelWidth; // Mode level line width
   ENUM_LINE_STYLE   ModeLevelStyle; // Mode level line style
   color             RegionDividerColor; //Region divider lines color

   /* Service */
   string            Id_user;
   string            Id;             // Identifier
   bool              ShowHorizon;    // Show data horizon
   double            Zoom;           // Zoom (0=auto)
   int               WaitMilliseconds;// Wait milliseconds
   color             TimeFromColor;  // Left border line color
   ENUM_LINE_STYLE   TimeFromStyle;  // Left border line style
   color             TimeToColor;    // Right border line color
   ENUM_LINE_STYLE   TimeToStyle;    // Right border line style
   double            HgWidthPercent; // Histogram width, % of chart


   //////////////////////////////////////////////////////////


   string            _prefix;
   string            _tfn;
   string            _ttn;

   datetime          _drawHistory[];

   bool              shouldUpdate;

   int               _modeStep;

   color             _prevBackgroundColor;
   color             _prevHgColor1;
   color             _prevHgColor2;

   int               _rangeCount;

   ENUM_VP_BAR_STYLE _hgBarStyle;
   double            _hgPoint;
   int               _hgPointDigits;

   color             _defaultHgColor1;
   color             _defaultHgColor2;
   color             _hgColor1;
   color             _hgColor2;
   int               _hgLineWidth;

   color             _modeColor;
   color             _maxColor;
   color             _medianColor;
   color             _vwapColor;
   int               _modeLineWidth;

   ENUM_LINE_STYLE   _statLineStyle;

   color             _modeLevelColor;
   ENUM_LINE_STYLE   _modeLevelStyle;
   int               _modeLevelWidth;

   bool              _showHg;
   bool              _showModes;
   bool              _showMax;
   bool              _showMedian;
   bool              _showVwap;
   bool              _showModeLevel;

   double            _zoom;

   int               _firstVisibleBar;
   int               _lastVisibleBar;

   bool              _isTimeframeEnabled;

   bool              _updateOnTick;
   ENUM_TIMEFRAMES   _dataPeriod;


   string               timeFrom_str;
   string               timeTo_str;
   datetime               timeFrom_date;
   datetime               timeTo_date;

   int               how_many_regions;
   int               region_1_factor;
   int               region_2_factor;
   int               region_3_factor;
   int               region_4_factor;
   int               region_5_factor;

   double            volumes[];
   double            prices[];


   datetime          timeFrom_last;
   datetime          timeTo_last;


public:
                     Task5(string name):Task(name)
     {
      redraw_each_time = true;
      /* Calculations */
      RangeMode = VP_RANGE_MODE_BETWEEN_LINES;              // Range mode
      RangeMinutes = 2440;        // Range minutes
      ModeStep =    3;             // Mode step (points)
      HgPointScale = POINT_SCALE_100;        // Point scale
      numberOfBars = 80;
      VolumeType = VOLUME_TICK;            // Volume type
      DataSource = VP_SOURCE_M1;            // Data source

      /* Histogram */
      HgBarStyle = VP_BAR_STYLE_BAR;            // Bar style
      HgPosition = VP_HG_POSITION_LEFT_INSIDE;            // Histogram position
      HgColor =   clrNavy;                // Color 1
      HgColor2 =  clrSteelBlue;               // Color 2
      HgLineWidth = 2;          // Line width

      /* Levels */
      ModeColor = clrMediumBlue;              // Mode color
      MaxColor =  clrRed;               // Maximum color
      MedianColor = clrNONE;          // Median color
      VwapColor = clrNONE;              // VWAP color
      ModeLineWidth = 2;      // Mode line width
      StatLineStyle = STYLE_SOLID;      // Median & VWAP line style

      ModeLevelColor = clrNONE;    // Mode level line color (None=disable)
      ModeLevelWidth = 1;                     // Mode level line width
      ModeLevelStyle = STYLE_SOLID;    // Mode level line style
      RegionDividerColor = clrDarkBlue;   // Region divider lines color

      /* Service */
      Id_user =       "+vpr_5";                      // Identifier
      ShowHorizon = true;          // Show data horizon
      Zoom =     0;                           // Zoom (0=auto)
      WaitMilliseconds = 500;                 // Wait milliseconds
      TimeFromColor = clrDarkGreen;      // Left border line color
      TimeFromStyle = STYLE_DASH;      // Left border line style
      TimeToColor = clrDarkGreen;          // Right border line color
      TimeToStyle = STYLE_DASH;          // Right border line style
      HgWidthPercent = 15;    // Histogram width, % of chart

      /* miscellaneous */

      shouldUpdate = true;

      _modeStep =   0;

      _prevBackgroundColor = clrNONE;


      _firstVisibleBar = 0;
      _lastVisibleBar = 0;


      _isTimeframeEnabled = false;

      _updateOnTick = true;




      //Previously in OnInit

      _prefix = Id + " m" + IntegerToString(RangeMode) + " ";
      _tfn = Id + "-from";
      _ttn = Id + "-to";
      _hgPoint = _Point * HgPointScale;
      _modeStep = ModeStep / HgPointScale;

      _hgBarStyle = HgBarStyle;
      _hgPointDigits = GetPointDigits(_hgPoint);

      //Sajjad, save them here to fix color update issue in expert
      _prevHgColor1 = _defaultHgColor1;
      _prevHgColor2 = _defaultHgColor2;

      _defaultHgColor1 = HgColor;
      _defaultHgColor2 = HgColor2;

      _hgLineWidth = HgLineWidth;

      _modeColor = ModeColor;
      _maxColor = MaxColor;
      _medianColor = MedianColor;
      _vwapColor = VwapColor;
      _modeLineWidth = ModeLineWidth;

      _statLineStyle = StatLineStyle;

      _modeLevelColor = ModeLevelColor;
      _modeLevelWidth = ModeLevelWidth;
      _modeLevelStyle = ModeLevelStyle;

      _showHg = !(ColorIsNone(_hgColor1) && ColorIsNone(_hgColor2));
      _showModes = !ColorIsNone(_modeColor);
      _showMax = !ColorIsNone(_maxColor);
      _showMedian = !ColorIsNone(_medianColor);
      _showVwap = !ColorIsNone(_vwapColor);
      _showModeLevel = !ColorIsNone(_modeLevelColor);

      _zoom = MathAbs(Zoom);

      _dataPeriod = GetDataPeriod(DataSource);

      /* Boundaries and multipliers */

      timeFrom_str = "01:00";
      timeTo_str = "10:00";

      how_many_regions = 3; //max is 5
      region_1_factor = 2;
      region_2_factor = 3;
      region_3_factor = 1;
      region_4_factor = 1;
      region_5_factor = 1;


     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      static int counter = 1;
      if(!redraw_each_time)
        {
         Id = Id_user + counter;
         counter++;
        }
      else
        {
         Id = Id_user;
        }

      checkNoOfRegions();

      //check if update needed
      bool time_str_changed = false;
      bool time_date_changed = false;//time date changes while time str is fixed (at day change when time str specifies only hours like "10:00")
      bool vlines_dragged = false;


      //1_ check if time str changed (by referencing to global vars
      static string timeFrom_str_holder = "";
      static string timeTo_str_holder = "";

      if(timeFrom_str != timeFrom_str_holder || timeTo_str != timeTo_str_holder)
        {
         timeFrom_str_holder = timeFrom_str;
         timeTo_str_holder = timeTo_str;

         timeFrom_date = StrToTime(timeFrom_str);
         timeTo_date = StrToTime(timeTo_str);
         time_str_changed = true;
        }

      //2_ check if with same time str, time date changed (day change when time str is like "10:00")
      if(!time_str_changed)
        {
         datetime timeFrom_date_temp = StrToTime(timeFrom_str);
         datetime timeTo_date_temp = StrToTime(timeTo_str);

         if(timeFrom_date != timeFrom_date_temp || timeTo_date != timeTo_date_temp)
           {
            //only dates get updated, time str not changed. just day changed.
            timeFrom_date = timeFrom_date_temp;
            timeTo_date = timeTo_date_temp;

            time_date_changed = true;
           }
        }

      //3_ check if any drag happened
      if(!time_str_changed && !time_date_changed)
        {
         vlines_dragged = checkVLineDragged();
         if(vlines_dragged)
           {
            datetime d1 = GetObjectTime1(_tfn);
            datetime d2 = GetObjectTime1(_ttn);

            timeFrom_date = d1;
            timeTo_date = d2;
            timeFrom_str = TimeToStr(d1);
            timeTo_str = TimeToStr(d2);
            timeFrom_str_holder = timeFrom_str;
            timeTo_str_holder = timeTo_str;
           }
        }


      //Checks done, update objects

      //first redraw boundaries if needed
      if(time_str_changed || time_date_changed)
         redrawBoundaries();

      //finally update all other parts
      if(time_str_changed || time_date_changed || vlines_dragged)
        {
         Update();
         calcValues();
         drawRegions();
        }

      //printf("task"+block_id + " passed route 1");
      block.onResult(ROUTE_1_PASSED);
     }
   virtual void      reset(int level)
     {

     }

   void              checkNoOfRegions()
     {
      if(how_many_regions>5)
         how_many_regions = 5;
     }

   void              calcValues()
     {

      how_many_regions = 3;
      region_1_factor = 2;
      region_2_factor = 3;
      region_3_factor = 1;
      region_4_factor = 1;


      int max1=0, min1=0, multiply1=0;
      int max2=0, min2=0, multiply2=0;
      int max3=0, min3=0, multiply3=0;
      int max4=0, min4=0, multiply4=0;
      int max5=0, min5=0, multiply5=0;

      // Assuming 'volumes' is your list of double values
      double m;

      double partSize = ArraySize(volumes) /(double) how_many_regions;
      int startIndex = 0;

      for(int i = 0; i < how_many_regions; i++)
        {
         int maxPart = startIndex;
         int minPart = startIndex;
         int xIndex = -1;

         for(int j = startIndex + 1; j < startIndex + partSize; j++)
           {
            if(volumes[j] > volumes[maxPart])
               maxPart = j;
            if(volumes[j] < volumes[minPart])
               minPart = j;

            m = i==0 ? region_1_factor : i==1 ? region_2_factor : i==2 ? region_3_factor : i==3 ? region_4_factor : i==4 ? region_5_factor : 0;
            double ratioup = volumes[j-1]==0 && volumes[j]==0 ? 0 : volumes[j-1]==0 && volumes[j]!=0 ? EMPTY_VALUE : volumes[j]/volumes[j-1];
            double ratiodn = volumes[j]==0 && volumes[j-1]==0 ? 0 : volumes[j]==0 && volumes[j-1]!=0 ? EMPTY_VALUE : volumes[j-1]/volumes[j];
            double ratio = ratioup>ratiodn ? ratioup : ratiodn;
            int    index = ratioup>ratiodn ? j : j-1;
            if(ratio >= m)
              {
               if(xIndex==-1)
                 {
                  xIndex = index;
                 }
               else
                 {
                  double ratioup_x = volumes[xIndex-1]==0 && volumes[xIndex]==0 ? 0 : volumes[xIndex-1]==0 && volumes[xIndex]!=0 ? EMPTY_VALUE : volumes[xIndex]/volumes[xIndex-1];
                  double ratiodn_x = volumes[xIndex]==0 && volumes[xIndex-1]==0 ? 0 : volumes[xIndex]==0 && volumes[xIndex-1]!=0 ? EMPTY_VALUE : volumes[xIndex-1]/volumes[xIndex];
                  double ratio_x = ratioup_x>ratiodn_x ? ratioup_x : ratiodn_x;

                  if(ratio>ratio_x)
                    {
                     xIndex = index;
                    }
                 }

              }

           }

         // Save max, min, and x values for this part (you can use appropriate variables)
         //Print(" Part ", i + 1, ": Max =", maxPart, ", Min =", minPart, ", x Index =", xIndex);
         Print(" Part ", i + 1, ": Max =", prices[maxPart], ", Min =",prices[minPart], ", x Index =", prices[xIndex]);

         if(i==0)  //part 1
           {
            double max_part_1_sudo = prices[maxPart];
            double min_part_1_sudo = prices[minPart];
            double mtp_part_1_sudo = prices[xIndex];
           }
         else
            if(i==1)  //part 2
              {
               double max_part_2_sudo = prices[maxPart];
               double min_part_2_sudo = prices[minPart];
               double mtp_part_2_sudo = prices[xIndex];
              }
            else
               if(i==2)  //part 3
                 {
                  double max_part_3_sudo = prices[maxPart];
                  double min_part_3_sudo = prices[minPart];
                  double mtp_part_3_sudo = prices[xIndex];
                 }
               else
                  if(i==3)  //part 4
                    {
                     double max_part_4_sudo = prices[maxPart];
                     double min_part_4_sudo = prices[minPart];
                     double mtp_part_4_sudo = prices[xIndex];
                    }
                  else
                     if(i==4)  //part 5
                       {
                        double max_part_5_sudo = prices[maxPart];
                        double min_part_5_sudo = prices[minPart];
                        double mtp_part_5_sudo = prices[xIndex];
                       }


         startIndex = MathRound(startIndex+partSize);
        }
     }

   void              drawRegions()
     {
      //delete objects first so we are able to redraw
      for(int j=0; j<=how_many_regions; j++)
        {
         string name_to_delete = Id+"_region_dividers_"+(j+1);
         ObjectDelete(0, name_to_delete);
        }

      int timeframe = Period();
      int timeFromCandleId = iBarShift(NULL, 0, timeFrom_date);
      int timeToCandleId = iBarShift(NULL, 0, timeTo_date);

      if(timeToCandleId > timeFromCandleId)
        {
         int temp = timeFromCandleId;
         timeFromCandleId = timeToCandleId;
         timeToCandleId = temp;
        }

      int hi = iHighest(NULL, timeframe, MODE_HIGH, timeFromCandleId-timeToCandleId, timeToCandleId);
      int li = iLowest(NULL, timeframe, MODE_LOW, timeFromCandleId-timeToCandleId, timeToCandleId);
      double eachArea = (High[hi]-Low[li])/how_many_regions;

      for(int i=0; i<=how_many_regions; i++)
        {
         double level = NormalizeDouble(Low[li] + i*eachArea, _Digits);
         string name = Id+"_region_dividers_"+(i+1);
         if(!ObjectCreate(0, name,OBJ_TREND, 0,Time[timeToCandleId],level,Time[timeFromCandleId],level))
           {
            Print(__FUNCTION__, ": failed to create a trend line! Error code = ",GetLastError());
            return(false);
           }
         ObjectSetInteger(0,name,OBJPROP_COLOR,RegionDividerColor);
         ObjectSetInteger(0,name,OBJPROP_SELECTABLE,true);
         ObjectSetInteger(0,name,OBJPROP_RAY,false);
         ObjectSetInteger(0,name,OBJPROP_BACK,false);
        }
     }



   //Check if lines dragged,
   bool              checkVLineDragged()
     {
      double timeFrom;
      double timeTo;

      if(RangeMode == VP_RANGE_MODE_BETWEEN_LINES)
        {
         timeFrom = GetObjectTime1(_tfn);
         timeTo = GetObjectTime1(_ttn);
         Print(timeTo, " ", timeTo_last);
         if(timeFrom==0 || timeFrom != timeFrom_last)
           {
            timeFrom_date = timeFrom;
            timeTo_date = timeTo;
            return true;
           }
         if(timeTo==0 || timeTo != timeTo_last)
           {
            timeFrom_date = timeFrom;
            timeTo_date = timeTo;
            return true;
           }
        }
      else
         if(RangeMode == VP_RANGE_MODE_MINUTES_TO_LINE)
           {

            timeTo = GetObjectTime1(_ttn);
            if(timeTo==0 || timeTo != timeTo_last)
              {
               timeFrom_date = timeFrom;
               timeTo_date = timeTo;
               return true;
              }
           }
         else
            if(RangeMode == VP_RANGE_MODE_LAST_MINUTES)
              {
               timeFrom = GetBarTime(RangeMinutes - 1, PERIOD_M1);
               timeTo = GetBarTime(-1, PERIOD_M1);

               if(timeFrom==0 || timeFrom != timeFrom_last)
                 {
                  timeFrom_date = timeFrom;
                  timeTo_date = timeTo;
                  return true;
                 }
               if(timeTo==0 || timeTo != timeTo_last)
                 {
                  timeFrom_date = timeFrom;
                  timeTo_date = timeTo;
                  return true;
                 }
              }
            else
              {
               return true;
              }
     }



   void              redrawBoundaries()
     {

      ObjectDelete(0, _tfn);
      ObjectDelete(0, _ttn);


      datetime timeFrom;
      datetime timeTo;

      if(RangeMode == VP_RANGE_MODE_BETWEEN_LINES)
        {


         ulong timeRange = timeTo_date - timeFrom_date;

         timeFrom = timeFrom_date;
         timeTo = timeTo_date;

         DrawVLine(_tfn, timeFrom, TimeFromColor, 1, TimeFromStyle, false);
         DrawVLine(_ttn, timeTo, Crimson, 1, TimeToStyle, false);

         ObjectEnable(0, _tfn);
         ObjectEnable(0, _ttn);

         if(timeFrom > timeTo)
            Swap(timeFrom, timeTo);
        }
      else
         if(RangeMode == VP_RANGE_MODE_MINUTES_TO_LINE)
           {

            //timeTo = GetObjectTime1(_ttn);
            int bar;

            int leftBar = WindowFirstVisibleBar();
            int rightBar = WindowFirstVisibleBar() - WindowBarsPerChart();
            int barRange = leftBar - rightBar;

            bar = MathMax(0, leftBar - barRange / 3);
            timeTo = GetBarTime(bar);

            bar += RangeMinutes / (PeriodSeconds(_Period) / 60);
            timeFrom = GetBarTime(bar);

            DrawVLine(_tfn, timeFrom, TimeFromColor, 1, TimeFromStyle, false);

            if(ObjectFind(0, _ttn) == -1)
              {
               DrawVLine(_ttn, timeTo, TimeToColor, 1, TimeToStyle, false);
              }

            ObjectDisable(0, _tfn);
            ObjectEnable(0, _ttn);
           }
         else
            if(RangeMode == VP_RANGE_MODE_LAST_MINUTES)
              {
               timeFrom = GetBarTime(RangeMinutes - 1, PERIOD_M1);
               timeTo = GetBarTime(-1, PERIOD_M1);

               ObjectDelete(0, _tfn);
               ObjectDelete(0, _ttn);
              }
     }



   bool              Update()
     {

      if(redraw_each_time)
         ObjectsDeleteAll(0, _prefix);

      datetime timeFrom, timeTo;

      if(RangeMode == VP_RANGE_MODE_BETWEEN_LINES)
        {
         timeFrom = GetObjectTime1(_tfn);
         timeTo = GetObjectTime1(_ttn);

         if((timeFrom == 0) || (timeTo == 0))
           {
            //            datetime timeLeft = GetBarTime(WindowFirstVisibleBar());
            //            datetime timeRight = GetBarTime(WindowFirstVisibleBar() - WindowBarsPerChart());
            //

            ulong timeRange = timeTo_date - timeFrom_date;
            //
            //            timeFrom = (datetime)(timeLeft + timeRange / 3);
            //            timeTo = (datetime)(timeLeft + timeRange * 2 / 3);

            timeFrom = timeFrom_date;
            timeTo = timeTo_date;


            DrawVLine(_tfn, timeFrom, TimeFromColor, 1, TimeFromStyle, false);
            DrawVLine(_ttn, timeTo, Crimson, 1, TimeToStyle, false);
           }

         ObjectEnable(0, _tfn);
         ObjectEnable(0, _ttn);

         if(timeFrom > timeTo)
            Swap(timeFrom, timeTo);
         timeFrom_last = timeFrom;
         timeTo_last = timeTo;
        }
      else
         if(RangeMode == VP_RANGE_MODE_MINUTES_TO_LINE)
           {

            timeTo = GetObjectTime1(_ttn);
            int bar;

            if(timeTo == 0)
              {

               int leftBar = WindowFirstVisibleBar();
               int rightBar = WindowFirstVisibleBar() - WindowBarsPerChart();
               int barRange = leftBar - rightBar;

               bar = MathMax(0, leftBar - barRange / 3);
               timeTo = GetBarTime(bar);
              }
            else
              {
               bar = iBarShift(_Symbol, _Period, timeTo);
              }

            bar += RangeMinutes / (PeriodSeconds(_Period) / 60);
            timeFrom = GetBarTime(bar);

            DrawVLine(_tfn, timeFrom, TimeFromColor, 1, TimeFromStyle, false);

            if(ObjectFind(0, _ttn) == -1)
              {
               DrawVLine(_ttn, timeTo, TimeToColor, 1, TimeToStyle, false);
              }

            ObjectDisable(0, _tfn);
            ObjectEnable(0, _ttn);

            timeFrom_last = timeFrom;
            timeTo_last = timeTo;
           }
         else
            if(RangeMode == VP_RANGE_MODE_LAST_MINUTES)
              {
               timeFrom = GetBarTime(RangeMinutes - 1, PERIOD_M1);
               timeTo = GetBarTime(-1, PERIOD_M1);

               ObjectDelete(0, _tfn);
               ObjectDelete(0, _ttn);

               timeFrom_last = timeFrom;
               timeTo_last = timeTo;
              }
            else
              {
               return(true);
              }

      if(ShowHorizon)
        {
         datetime horizon = GetHorizon(DataSource, _dataPeriod);
         DrawHorizon(_prefix + "hz", horizon);
        }

      int barFrom, barTo;

      if(!GetRangeBars(timeFrom, timeTo, barFrom, barTo))
         return(true);

      _updateOnTick = barTo < 0;

      int modes[];
      double lowPrice;

      int count = GetHg(timeFrom, timeTo - 1, _hgPoint, _dataPeriod, VolumeType, lowPrice, volumes);

      if(count <= 0)
         return(true);


      int modeCount = _showModes ? HgModes(volumes, _modeStep, modes) : -1;
      int maxPos    = _showMax ? ArrayMax(volumes) : -1;
      int medianPos = _showMedian ? ArrayMedian(volumes) : -1;
      int vwapPos   = _showVwap ? HgVwap(volumes, lowPrice, _hgPoint) : -1;

      string prefix = _prefix + (string)((int)RangeMode) + " ";
      double hgWidthBars = ((HgPosition == VP_HG_POSITION_LEFT_INSIDE) || (HgPosition == VP_HG_POSITION_RIGHT_INSIDE))
                           ? (barFrom - barTo)
                           : WindowBarsPerChart() * (HgWidthPercent / 100.0);

      double maxVolume = volumes[ArrayMaximum(volumes)];

      if(maxVolume == 0)
         maxVolume = 1;

      double zoom = _zoom > 0 ? _zoom : hgWidthBars / maxVolume;

      int drawBarFrom, drawBarTo;

      if(HgPosition == VP_HG_POSITION_WINDOW_LEFT)
        {
         drawBarFrom = WindowFirstVisibleBar();
         drawBarTo = (int)(drawBarFrom - zoom * maxVolume);
        }
      else
         if(HgPosition == VP_HG_POSITION_WINDOW_RIGHT)
           {
            drawBarFrom = WindowFirstVisibleBar() - WindowBarsPerChart();
            drawBarTo = (int)(drawBarFrom + zoom * maxVolume);
           }
         else
            if(HgPosition == VP_HG_POSITION_LEFT_OUTSIDE)
              {
               drawBarFrom = barFrom;
               drawBarTo = (int)(drawBarFrom + zoom * maxVolume);
              }
            else
               if(HgPosition == VP_HG_POSITION_RIGHT_OUTSIDE)
                 {
                  drawBarFrom = barTo;
                  drawBarTo = (int)(drawBarFrom - zoom * maxVolume);
                 }
               else
                  if(HgPosition == VP_HG_POSITION_LEFT_INSIDE)
                    {
                     drawBarFrom = barFrom;
                     drawBarTo = barTo;
                    }
                  else //if (HgPosition == VP_HG_POSITION_RIGHT_INSIDE)
                    {
                     drawBarFrom = barTo;
                     drawBarTo = barFrom;
                    }

      DrawHg(prefix, lowPrice, volumes, drawBarFrom, drawBarTo, zoom, modes, maxPos, medianPos, vwapPos);

      return(false);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   datetime          GetObjectTime1(const string name)
     {
      datetime time;

      if(!ObjectGetInteger(0, name, OBJPROP_TIME, 0, time))
         return(0);

      return(time);
     }

   template <typename T>
   int               ArrayIndexOf(const T &arr[], const T value, const int startingFrom = 0)
     {
      int size = ArraySize(arr);

      for(int i = startingFrom; i < size; i++)
        {
         if(arr[i] == value)
            return(i);
        }

      return(-1);
     }

   template <typename T>
   bool              ArrayCheckRange(const T &arr[], int &start, int &count)
     {
      int size = ArraySize(arr);

      if(size <= 0)
         return(false);

      if(count == 0)
         return(false);

      if((start > size - 1) || (start < 0))
         return(false);

      if(count < 0)
        {
         count = size - start;
        }
      else
         if(count > size - start)
           {
            count = size - start;
           }

      return(true);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               ArrayMedian(const double &values[])
     {
      int size = ArraySize(values);
      double halfVolume = Sum(values) / 2.0;

      double v = 0;

      for(int i = 0; i < size; i++)
        {
         v += values[i];

         if(v >= halfVolume)
            return(i);
        }

      return(-1);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   string            TrimRight(string s, const ushort ch)
     {
      int len = StringLen(s);

      int cut = len;

      for(int i = len - 1; i >= 0; i--)
        {
         if(StringGetCharacter(s, i) == ch)
            cut--;
         else
            break;
        }

      if(cut != len)
        {
         if(cut == 0)
            s = "";
         else
            s = StringSubstr(s, 0, cut);
        }

      return(s);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   string            DoubleToString(const double d, const uint digits, const uchar separator)
     {
      string s = DoubleToString(d, digits) + "";

      if(separator != '.')
        {
         int p = StringFind(s, ".");

         if(p != -1)
            StringSetCharacter(s, p, separator);
        }

      return(s);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   string            DoubleToCompactString(const double d, const uint digits = 8, const uchar separator = '.')
     {
      string s = DoubleToString(d, digits, separator);

      if(StringFind(s, CharToString(separator)) != -1)
        {
         s = TrimRight(s, '0');
         s = TrimRight(s, '.');
        }

      return(s);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   double            MathRound(const double value, const double error)
     {
      return(error == 0 ? value : MathRound(value / error) * error);
     }

   template <typename T>
   void              Swap(T &value1, T &value2)
     {
      T tmp = value1;
      value1 = value2;
      value2 = tmp;
     }

   template <typename T>
   T                 Sum(const T &arr[], int start = 0, int count = -1)
     {
      if(!ArrayCheckRange(arr, start, count))
         return((T)NULL);

      T sum = (T)NULL;

      for(int i = start, end = start + count; i < end; i++)
         sum += arr[i];

      return(sum);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               GetPointDigits(const double point)
     {
      if(point == 0)
         return(_Digits);

      return(GetPointDigits(point, _Digits));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               GetPointDigits(const double point, const int maxDigits)
     {
      if(point == 0)
         return(maxDigits);

      string pointString = DoubleToCompactString(point, maxDigits);
      int pointStringLen = StringLen(pointString);
      int dotPos = StringFind(pointString, ".");

      // pointString => result:
      //   1230   => -1
      //   123    =>  0
      //   12.3   =>  1
      //   1.23   =>  2
      //   0.123  =>  3
      //   .123   =>  3

      return(dotPos < 0
             ? StringLen(TrimRight(pointString, '0')) - pointStringLen
             : pointStringLen - dotPos - 1);
     }

   template <typename T>
   int               ArrayMax(const T &array[], const int start = 0, const int count = WHOLE_ARRAY)
     {
      return(ArrayMaximum(array, count, start));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               HgModes(const double &values[], const int modeStep, int &modes[])
     {
      int modeCount = 0;
      ArrayFree(modes);

      for(int i = modeStep, count = ArraySize(values) - modeStep; i < count; i++)
        {
         int maxFrom = i - modeStep;
         int maxRange = 2 * modeStep + 1;
         int maxTo = maxFrom + maxRange - 1;

         int k = ArrayMax(values, maxFrom, maxRange);

         if(k != i)
            continue;

         for(int j = i - modeStep; j <= i + modeStep; j++)
           {
            if(values[j] != values[k])
               continue;

            modeCount++;
            ArrayResize(modes, modeCount, count);
            modes[modeCount - 1] = j;
           }
        }

      return(modeCount);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               HgVwap(const double &volumes[], const double low, const double step)
     {
      if(step == 0)
         return(-1);

      double vwap = 0;
      double totalVolume = 0;
      int size = ArraySize(volumes);

      for(int i = 0; i < size; i++)
        {
         double price = low + i * step;
         double volume = volumes[i];

         vwap += price * volume;
         totalVolume += volume;
        }

      if(totalVolume == 0)
         return(-1);

      vwap /= totalVolume;
      return((int)((vwap - low) / step + 0.5));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               GetHg(const datetime timeFrom, const datetime timeTo, const double point, const ENUM_TIMEFRAMES dataPeriod, const ENUM_APPLIED_VOLUME appliedVolume, double &low, double &volumes[])
     {
      MqlRates rates[];
      int rateCount = CopyRates(_Symbol, dataPeriod, timeFrom, timeTo, rates);

      if(rateCount <= 0)
         return(0);

      MqlRates rate = rates[0];
      low = NORM_PRICE(rate.low, point);
      double high = NORM_PRICE(rate.high, point);

      for(int i = 1; i < rateCount; i++)
        {
         rate = rates[i];

         double rateHigh =  NORM_PRICE(rate.high, point);
         double rateLow = NORM_PRICE(rate.low, point);

         if(rateLow < low)
            low = rateLow;

         if(rateHigh > high)
            high = rateHigh;
        }

      int lowIndex = ROUND_PRICE(low, point);
      int highIndex = ROUND_PRICE(high, point);
      int hgSize = highIndex - lowIndex + 1;



      double ratio = hgSize/(double)numberOfBars;
      static int hgSize_temp = 0;
      if(ratio!=1 && hgSize!=hgSize_temp)
        {
         hgSize_temp = hgSize;
         HgPointScale = HgPointScale*ratio;
         _hgPoint = _Point * HgPointScale;
         _modeStep = ModeStep / HgPointScale;
         _hgPointDigits = GetPointDigits(_hgPoint);
         Update();
         return;
        }
      hgSize_temp = hgSize;








      ArrayResize(volumes, hgSize);
      ArrayInitialize(volumes, 0);
      ArrayResize(prices, hgSize);

      int pri, oi, hi, li, ci;
      double dv, v;

      for(int j = 0; j < rateCount; j++)
        {
         rate = rates[j];

         oi = ROUND_PRICE(rate.open, point) - lowIndex;
         hi = ROUND_PRICE(rate.high, point) - lowIndex;
         li = ROUND_PRICE(rate.low, point) - lowIndex;
         ci = ROUND_PRICE(rate.close, point) - lowIndex;

         v = (appliedVolume == VOLUME_REAL) ? (double)rate.real_volume : (double)rate.tick_volume;

         if(ci >= oi)
           {

            dv = v / (oi - li + hi - li + hi - ci + 1.0);

            // open --> low
            for(pri = oi; pri >= li; pri--)
               volumes[pri] += dv;

            // low+1 ++> high
            for(pri = li + 1; pri <= hi; pri++)
               volumes[pri] += dv;

            // high-1 --> close
            for(pri = hi - 1; pri >= ci; pri--)
               volumes[pri] += dv;
           }
         else
           {

            dv = v / (hi - oi + hi - li + ci - li + 1.0);

            // open ++> high
            for(pri = oi; pri <= hi; pri++)
               volumes[pri] += dv;

            // high-1 --> low
            for(pri = hi - 1; pri >= li; pri--)
               volumes[pri] += dv;

            // low+1 ++> close
            for(pri = li + 1; pri <= ci; pri++)
               volumes[pri] += dv;
           }
        }

      return(hgSize);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   datetime          GetHorizon(ENUM_VP_SOURCE dataSource, ENUM_TIMEFRAMES dataPeriod)
     {

      return((datetime)(iTime(_Symbol, dataPeriod, Bars(_Symbol, dataPeriod) - 1)));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   ENUM_TIMEFRAMES   GetDataPeriod(ENUM_VP_SOURCE dataSource)
     {
      switch(dataSource)
        {
         case VP_SOURCE_M1:
            return(PERIOD_M1);
         case VP_SOURCE_M5:
            return(PERIOD_M5);
         case VP_SOURCE_M15:
            return(PERIOD_M15);
         case VP_SOURCE_M30:
            return(PERIOD_M30);
         default:
            return(PERIOD_M1);
        }
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   bool              ColorToRGB(const color c, int &r, int &g, int &b)
     {
      if(COLOR_IS_NONE(c))
         return(false);

      b = (c & 0xFF0000) >> 16;
      g = (c & 0x00FF00) >> 8;
      r = (c & 0x0000FF);

      return(true);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   color             MixColors(const color color1, const color color2, double mix, double step = 16)
     {
      step = PUT_IN_RANGE(step, 1.0, 255.0);
      mix = PUT_IN_RANGE(mix, 0.0, 1.0);

      int r1, g1, b1;
      int r2, g2, b2;

      ColorToRGB(color1, r1, g1, b1);
      ColorToRGB(color2, r2, g2, b2);

      int r = PUT_IN_RANGE((int)MathRound(r1 + mix * (r2 - r1), step), 0, 255);
      int g = PUT_IN_RANGE((int)MathRound(g1 + mix * (g2 - g1), step), 0, 255);
      int b = PUT_IN_RANGE((int)MathRound(b1 + mix * (b2 - b1), step), 0, 255);

      return(RGB_TO_COLOR(r, g, b));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   bool              ColorIsNone(const color c)
     {
      return(COLOR_IS_NONE(c));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              ObjectEnable(const long chartId, const string name)
     {
      ObjectSetInteger(chartId, name, OBJPROP_HIDDEN, false);
      ObjectSetInteger(chartId, name, OBJPROP_SELECTABLE, true);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              ObjectDisable(const long chartId, const string name)
     {
      ObjectSetInteger(chartId, name, OBJPROP_HIDDEN, true);
      ObjectSetInteger(chartId, name, OBJPROP_SELECTABLE, false);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   int               GetTimeBarRight(datetime time, ENUM_TIMEFRAMES period = PERIOD_CURRENT)
     {
      int bar = iBarShift(_Symbol, period, time);
      datetime t = iTime(_Symbol, period, bar);

      if((t != time) && (bar == 0))
        {
         bar = (int)((iTime(_Symbol, period, 0) - time) / PeriodSeconds(period));
        }
      else
        {
         if(t < time)
            bar--;
        }

      return(bar);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   datetime          GetBarTime(const int shift, ENUM_TIMEFRAMES period = PERIOD_CURRENT)
     {
      if(shift >= 0)
         return(iTime(_Symbol, period, shift));
      else
         return(iTime(_Symbol, period, 0) - shift * PeriodSeconds(period));
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              DrawHorizon(const string lineName, const datetime time)
     {
      DrawVLine(lineName, time, Red, 1, STYLE_DOT, false);
      ObjectDisable(0, lineName);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              DrawVLine(const string name, const datetime time1, const color lineColor, const int width, const int style, const bool back)
     {
      if(ObjectFind(0, name) >= 0)
         ObjectDelete(0, name);
      ObjectCreate(0, name, OBJ_VLINE, 0, time1, 0);
      ObjectSetInteger(0, name, OBJPROP_COLOR, lineColor);
      ObjectSetInteger(0, name, OBJPROP_BACK, back);
      ObjectSetInteger(0, name, OBJPROP_STYLE, style);
      ObjectSetInteger(0, name, OBJPROP_WIDTH, width);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              DrawBar(const string name, const datetime time1, const datetime time2, const double price, double vol,
                             const color lineColor, const int width, const ENUM_VP_BAR_STYLE barStyle, const ENUM_LINE_STYLE lineStyle, bool back)
     {
      ObjectDelete(0, name);
      if(barStyle == VP_BAR_STYLE_BAR)
        {
         ObjectCreate(0, name, OBJ_TREND, 0, time2, price - _hgPoint / 2.0, time2, price + _hgPoint / 2.0);
         ObjectCreate(0, name + "+1", OBJ_TREND, 0, time1, price - _hgPoint / 2.0, time2, price - _hgPoint / 2.0);
         ObjectCreate(0, name + "+2", OBJ_TREND, 0, time1, price + _hgPoint / 2.0, time2, price + _hgPoint / 2.0);
         ObjectCreate(0, name + "+3", OBJ_TREND, 0, time1, price - _hgPoint / 2.0, time1, price + _hgPoint / 2.0);
        }
      else
         if((barStyle == VP_BAR_STYLE_FILLED) || (barStyle == VP_BAR_STYLE_COLOR))
           {
            ObjectCreate(0, name, OBJ_RECTANGLE, 0, time1, price - _hgPoint / 2.0, time2, price + _hgPoint / 2.0);
           }
         else
            if(barStyle == VP_BAR_STYLE_OUTLINE)
              {
               ObjectCreate(0, name, OBJ_TREND, 0, time1, price, time2, price + _hgPoint);
              }
            else
              {
               ObjectCreate(0, name, OBJ_TREND, 0, time1, price, time2, price);
              }
      if(vol>=0)
         drawText(DoubleToString(vol, 2), name + "_vol", shiftDatetime(time1, 5), price, lineColor, 6);
      SetBarStyle(name, lineColor, width, barStyle, lineStyle, back);

      if(barStyle == VP_BAR_STYLE_BAR)
        {
         SetBarStyle(name + "+1", lineColor, width, barStyle, lineStyle, back);
         SetBarStyle(name + "+2", lineColor, width, barStyle, lineStyle, back);
         SetBarStyle(name + "+3", lineColor, width, barStyle, lineStyle, back);
        }
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              drawText(string txt, string objName, datetime time, double price, color clr, int size)
     {
      ObjectCreate(0, objName, OBJ_TEXT, 0, time, price);
      // Set the text for the object
      ObjectSetText(objName, txt, size, "Arial", clr);
      ObjectSetInteger(0, objName, OBJPROP_ANCHOR, ANCHOR_CENTER);


     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   datetime          shiftDatetime(datetime current, int shift)
     {
      // Get the shift of the current candle
      int currentShift = iBarShift(Symbol(), Period(), current);

      // Get the shift of the previous candle
      int secondShift = currentShift + shift;

      // Get the datetime of the previous candle
      datetime secondCandleTime = iTime(Symbol(), Period(), secondShift);
      return secondCandleTime;
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              SetBarStyle(const string name, const color lineColor, const int width, const ENUM_VP_BAR_STYLE barStyle, const ENUM_LINE_STYLE lineStyle, bool back)
     {
      ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
      ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
      ObjectSetInteger(0, name, OBJPROP_COLOR, lineColor);
      ObjectSetInteger(0, name, OBJPROP_STYLE, lineStyle);
      ObjectSetInteger(0, name, OBJPROP_WIDTH, lineStyle == STYLE_SOLID ? width : 1);

      ObjectSetInteger(0, name, OBJPROP_RAY, false);
      ObjectSetInteger(0, name, OBJPROP_RAY_RIGHT, false);

      if((barStyle == VP_BAR_STYLE_FILLED) || (barStyle == VP_BAR_STYLE_COLOR))
         back = true;

      ObjectSetInteger(0, name, OBJPROP_BACK, back);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              DrawLevel(const string name, const double price)
     {
      ObjectDelete(0, name);
      ObjectCreate(0, name, OBJ_HLINE, 0, 0, price);

      ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
      ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
      ObjectSetInteger(0, name, OBJPROP_COLOR, _modeLevelColor);
      ObjectSetInteger(0, name, OBJPROP_STYLE, _modeLevelStyle);
      ObjectSetInteger(0, name, OBJPROP_WIDTH, _modeLevelStyle== STYLE_SOLID ? _modeLevelWidth : 1);

      ObjectSetInteger(0, name, OBJPROP_BACK, false);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   void              DrawHg(const string prefix, const double lowPrice, const double &volumes[], const int barFrom, const int barTo,
                            double zoom, const int &modes[], const int max = -1, const int median = -1, const int vwap = -1)
     {
      if(ArraySize(volumes) == 0)
         return;

      if(barFrom > barTo)
         zoom = -zoom;

      color cl = _hgColor1;
      double maxValue = volumes[ArrayMaximum(volumes)];

      if(maxValue == 0)
         maxValue = 1;

      double volume;
      double nextVolume = 0;
      bool isOutline = _hgBarStyle == VP_BAR_STYLE_OUTLINE;

      int bar1 = barFrom;
      int bar2 = barTo;
      int modeBar2 = barTo;

      for(int i = 0, size = ArraySize(volumes); i < size; i++)
        {
         double price = NormalizeDouble(lowPrice + i * _hgPoint, _hgPointDigits);
         string priceString = DoubleToString(price, _hgPointDigits);
         string name = prefix + priceString;
         volume = volumes[i];
         prices[i] = price;
         double mvolume = ArraySize(volumes) <= 100 ? volume : -1;
         if(isOutline)
           {
            if(i < size - 1)
              {
               nextVolume = volumes[i + 1];
               bar1 = (int)(barFrom + volume * zoom);
               bar2 = (int)(barFrom + nextVolume * zoom);
               modeBar2 = bar1;
              }
           }
         else
            if(_hgBarStyle != VP_BAR_STYLE_COLOR)
              {
               bar2 = (int)(barFrom + volume * zoom);
               modeBar2 = bar2;
              }

         datetime timeFrom = GetBarTime(barFrom);
         datetime timeTo = GetBarTime(barTo);
         datetime t1 = GetBarTime(bar1);
         datetime t2 = GetBarTime(bar2);
         datetime mt2 = GetBarTime(modeBar2);

         if(_showModeLevel && (ArrayIndexOf(modes, i) != -1))
            DrawLevel(name + " level", price);

         if(_showHg && !(isOutline && (i == size - 1)))
           {
            if(_hgColor1 != _hgColor2)
               cl = MixColors(_hgColor1, _hgColor2, (isOutline ? MathMax(volume, nextVolume) : volume) / maxValue, 8);

            DrawBar(name, t1, t2, price, mvolume, cl, _hgLineWidth, _hgBarStyle, STYLE_SOLID, true);
           }

         if(_showMedian && (i == median))
           {
            DrawBar(name + " median", timeFrom, timeTo, price, mvolume, _medianColor, _modeLineWidth, VP_BAR_STYLE_LINE, _statLineStyle, false);
           }
         else
            if(_showVwap && (i == vwap))
              {
               DrawBar(name + " vwap", timeFrom, timeTo, price, mvolume, _vwapColor, _modeLineWidth, VP_BAR_STYLE_LINE, _statLineStyle, false);
              }
            else
               if((_showMax && (i == max)) || (_showModes && (ArrayIndexOf(modes, i) != -1)))
                 {
                  color modeColor = (_showMax && (i == max)) ? _maxColor : _modeColor;

                  if(_hgBarStyle == VP_BAR_STYLE_LINE)
                     DrawBar(name, timeFrom, mt2, price, mvolume, modeColor, _modeLineWidth, VP_BAR_STYLE_LINE, STYLE_SOLID, false);
                  else
                     if(_hgBarStyle == VP_BAR_STYLE_BAR)
                        DrawBar(name, timeFrom, mt2, price, mvolume, modeColor, _modeLineWidth, VP_BAR_STYLE_BAR, STYLE_SOLID, false);
                     else
                        if(_hgBarStyle == VP_BAR_STYLE_FILLED)
                           DrawBar(name, timeFrom, mt2, price, mvolume, modeColor, _modeLineWidth, VP_BAR_STYLE_FILLED, STYLE_SOLID, false);
                        else
                           if(_hgBarStyle == VP_BAR_STYLE_OUTLINE)
                              DrawBar(name + "+", timeFrom, mt2, price, mvolume, modeColor, _modeLineWidth, VP_BAR_STYLE_LINE, STYLE_SOLID, false);
                           else
                              if(_hgBarStyle == VP_BAR_STYLE_COLOR)
                                 DrawBar(name, timeFrom, mt2, price, mvolume, modeColor, _modeLineWidth, VP_BAR_STYLE_FILLED, STYLE_SOLID, false);
                 }
        }
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   bool              GetRangeBars(const datetime timeFrom, const datetime timeTo, int &barFrom, int &barTo)
     {
      barFrom = GetTimeBarRight(timeFrom);
      barTo = GetTimeBarRight(timeTo);
      return(true);
     }

   //+------------------------------------------------------------------+
   //|                                                                  |
   //+------------------------------------------------------------------+
   bool              UpdateAutoColors()
     {
      if(!_showHg)
         return(false);

      bool isNone1 = ColorIsNone(_defaultHgColor1);
      bool isNone2 = ColorIsNone(_defaultHgColor2);
      if(isNone1 && isNone2)
         return(false);

      color newBgColor = (color)ChartGetInteger(0, CHART_COLOR_BACKGROUND);

      if(newBgColor == _prevBackgroundColor && _prevHgColor1==_defaultHgColor1 && _prevHgColor2==_defaultHgColor2)
         return(false);

      //Sajjad, save them here to fix color update issue in expert
      _prevHgColor1 = _defaultHgColor1;
      _prevHgColor2 = _defaultHgColor2;

      _hgColor1 = isNone1 ? newBgColor : _defaultHgColor1;
      _hgColor2 = isNone2 ? newBgColor : _defaultHgColor2;

      _prevBackgroundColor = newBgColor;
      return(true);
     }


  };
