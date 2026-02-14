class MarketPropertiesTimeframe2_left
  {

public:
   void              init()
     {

     }

   template<typename T>
   T                 calc()
     {
        ENUM_TIMEFRAMES result = getTimeframe(PERIOD_CURRENT);
		if (result == PERIOD_CURRENT) {result = ChartPeriod();}
		return result;
     }
  };
