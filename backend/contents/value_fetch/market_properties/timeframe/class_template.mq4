class MarketPropertiesTimeframe_id

  {
    field_body
public:
   void              init()
     {
        init_body
     }

   template<typename T>
   T                 calc()
     {
        ENUM_TIMEFRAMES result = getTimeframe(PERIOD_CURRENT);
		if (result == PERIOD_CURRENT) {result = ChartPeriod();}
		return result;
     }
  };
