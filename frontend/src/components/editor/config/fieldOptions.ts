/**
 * Comprehensive mapping of parameter field names to their dropdown options.
 * Used by GenericConfig to auto-detect which fields should render as <select>.
 */

export type FieldOption = { value: string; label: string };

// --- Reusable option sets ---

const COMPARISON_OPERATORS: FieldOption[] = [
  { value: '>', label: '> (Greater Than)' },
  { value: '>=', label: '>= (Greater or Equal)' },
  { value: '<', label: '< (Less Than)' },
  { value: '<=', label: '<= (Less or Equal)' },
  { value: '==', label: '== (Equal To)' },
  { value: '!=', label: '!= (Not Equal)' },
];

const TIMEFRAME_NUMERIC: FieldOption[] = [
  { value: '0', label: 'Current Timeframe' },
  { value: '1', label: 'M1 (1 Minute)' },
  { value: '5', label: 'M5 (5 Minutes)' },
  { value: '15', label: 'M15 (15 Minutes)' },
  { value: '30', label: 'M30 (30 Minutes)' },
  { value: '60', label: 'H1 (1 Hour)' },
  { value: '240', label: 'H4 (4 Hours)' },
  { value: '1440', label: 'D1 (Daily)' },
  { value: '10080', label: 'W1 (Weekly)' },
  { value: '43200', label: 'MN1 (Monthly)' },
];

const PERIOD_STRING: FieldOption[] = [
  { value: 'PERIOD_CURRENT', label: 'Current Timeframe' },
  { value: 'PERIOD_M1', label: 'M1 (1 Minute)' },
  { value: 'PERIOD_M5', label: 'M5 (5 Minutes)' },
  { value: 'PERIOD_M15', label: 'M15 (15 Minutes)' },
  { value: 'PERIOD_M30', label: 'M30 (30 Minutes)' },
  { value: 'PERIOD_H1', label: 'H1 (1 Hour)' },
  { value: 'PERIOD_H4', label: 'H4 (4 Hours)' },
  { value: 'PERIOD_D1', label: 'D1 (Daily)' },
  { value: 'PERIOD_W1', label: 'W1 (Weekly)' },
  { value: 'PERIOD_MN1', label: 'MN1 (Monthly)' },
];

const LINE_STYLE: FieldOption[] = [
  { value: 'STYLE_SOLID', label: 'Solid' },
  { value: 'STYLE_DASH', label: 'Dashed' },
  { value: 'STYLE_DOT', label: 'Dotted' },
  { value: 'STYLE_DASHDOT', label: 'Dash-Dot' },
  { value: 'STYLE_DASHDOTDOT', label: 'Dash-Dot-Dot' },
];

const MQL_COLORS: FieldOption[] = [
  { value: 'clrNONE', label: 'None' },
  { value: 'clrRed', label: 'Red' },
  { value: 'clrBlue', label: 'Blue' },
  { value: 'clrGreen', label: 'Green' },
  { value: 'clrYellow', label: 'Yellow' },
  { value: 'clrWhite', label: 'White' },
  { value: 'clrBlack', label: 'Black' },
  { value: 'clrOrange', label: 'Orange' },
  { value: 'clrDeepPink', label: 'Deep Pink' },
  { value: 'clrSkyBlue', label: 'Sky Blue' },
  { value: 'clrDarkGray', label: 'Dark Gray' },
  { value: 'clrLightGray', label: 'Light Gray' },
  { value: 'clrGold', label: 'Gold' },
  { value: 'clrCyan', label: 'Cyan' },
  { value: 'clrMagenta', label: 'Magenta' },
  { value: 'clrLime', label: 'Lime' },
  { value: 'clrPurple', label: 'Purple' },
  { value: 'clrDodgerBlue', label: 'Dodger Blue' },
  { value: 'clrTomato', label: 'Tomato' },
  { value: 'clrAqua', label: 'Aqua' },
  { value: 'clrSilver', label: 'Silver' },
  { value: 'clrCoral', label: 'Coral' },
  { value: 'clrChartreuse', label: 'Chartreuse' },
  { value: 'EMPTY_VALUE', label: 'Empty / Disabled' },
  { value: 'Red', label: 'Red (simple)' },
  { value: 'Blue', label: 'Blue (simple)' },
  { value: 'White', label: 'White (simple)' },
];

// --- Main field → options map ---

const FIELD_MAP: Record<string, FieldOption[]> = {
  // ── Shared trade/order filter fields ──
  symbol_mode: [
    { value: 'SYMBOL_MODE_SPECIFIED', label: 'Specified Symbols' },
    { value: 'SYMBOL_MODE_ANY', label: 'Any Symbol' },
  ],
  group_mode: [
    { value: 'ORDER_GROUP_MODE_ALL', label: 'All Groups' },
    { value: 'ORDER_GROUP_MODE_NUMBER', label: 'Specific Group Number' },
    { value: 'ORDER_GROUP_MODE_MANUAL', label: 'Manual Trades Only' },
  ],
  operator: COMPARISON_OPERATORS,
  compare: COMPARISON_OPERATORS,
  compare_each: COMPARISON_OPERATORS,

  // ── Buy / Sell ──
  order_type: [
    { value: 'ORDER_BUY', label: 'Market Buy' },
    { value: 'ORDER_SELL', label: 'Market Sell' },
    { value: 'ORDER_BUY_PENDING', label: 'Pending Buy' },
    { value: 'ORDER_SELL_PENDING', label: 'Pending Sell' },
  ],
  open_at_price: [
    { value: 'OPEN_AT_ASK', label: 'Ask Price' },
    { value: 'OPEN_AT_BID', label: 'Bid Price' },
    { value: 'OPEN_AT_MID', label: 'Mid Price' },
    { value: 'OPEN_AT_CUSTOM_PRICE', label: 'Custom Price' },
  ],
  money_management: [
    { value: 'MONEY_MANAGEMENT_FIXED_VOLUME', label: 'Fixed Lot Size' },
    { value: 'MONEY_MANAGEMENT_PERCENT_OF_EQUITY', label: '% of Equity' },
    { value: 'MONEY_MANAGEMENT_PERCENT_OF_BALANCE', label: '% of Balance' },
    { value: 'MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN', label: '% of Free Margin' },
    { value: 'MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY', label: 'Freeze % of Equity' },
    { value: 'MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE', label: 'Freeze % of Balance' },
    { value: 'MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN', label: 'Freeze % of Free Margin' },
    { value: 'MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY', label: 'Risk % of Equity' },
    { value: 'MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE', label: 'Risk % of Balance' },
    { value: 'MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN', label: 'Risk % of Free Margin' },
    { value: 'MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY', label: 'Risk Fixed Amount' },
    { value: 'MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES', label: 'Fixed Ratio (Ryan Jones)' },
    { value: 'MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI', label: 'Martingale / Paroli' },
    { value: 'MONEY_MANAGEMENT_CUSTOM_VALUE', label: 'Custom Value' },
  ],
  take_profit_mode: [
    { value: 'TPSL_MODE_NO_TP', label: 'No Take Profit' },
    { value: 'TPSL_MODE_FIXED_PIPS', label: 'Fixed Pips' },
    { value: 'TPSL_MODE_PERCENT_OF_PRICE', label: '% of Price' },
    { value: 'TPSL_MODE_PERCENT_OF_SL', label: '% of Stop Loss' },
    { value: 'TPSL_MODE_CUSTOM_PRICE_LEVEL', label: 'Custom Price Level' },
    { value: 'TPSL_MODE_CUSTOM_PIPS', label: 'Custom Pips' },
    { value: 'TPSL_MODE_CUSTOM_PRICE_FRACTION', label: 'Custom Price Fraction' },
  ],
  stop_loss_mode: [
    { value: 'TPSL_MODE_NO_SL', label: 'No Stop Loss' },
    { value: 'TPSL_MODE_FIXED_PIPS', label: 'Fixed Pips' },
    { value: 'TPSL_MODE_PERCENT_OF_PRICE', label: '% of Price' },
    { value: 'TPSL_MODE_PERCENT_OF_TP', label: '% of Take Profit' },
    { value: 'TPSL_MODE_CUSTOM_PRICE_LEVEL', label: 'Custom Price Level' },
    { value: 'TPSL_MODE_CUSTOM_PIPS', label: 'Custom Pips' },
    { value: 'TPSL_MODE_CUSTOM_PRICE_FRACTION', label: 'Custom Price Fraction' },
  ],
  look_up_on: [
    { value: 'LOOK_UP_RUNNING_THEN_HISTORY', label: 'Running Then History' },
    { value: 'LOOK_UP_RUNNING_ONLY', label: 'Running Only' },
    { value: 'LOOK_UP_HISTORY_ONLY', label: 'History Only' },
  ],

  // ── Trailing Stop Each Trade ──
  TrailingStopMode: [
    { value: 'TRAILING_STOP_MODE_PIP', label: 'Fixed Pips' },
    { value: 'TRAILING_STOP_MODE_MULTIPLE_LEVELS', label: 'Multiple Levels' },
    { value: 'TRAILING_STOP_MODE_MONEY', label: 'Money-Based' },
    { value: 'TRAILING_STOP_MODE_PERCENT_OF_OPPOSITE_STOP', label: '% of TP' },
    { value: 'TRAILING_STOP_MODE_PERCENT_OF_PROFIT', label: '% of Profit' },
    { value: 'TRAILING_STOP_MODE_CUSTOM_LEVEL', label: 'Custom Price Level' },
    { value: 'TRAILING_STOP_MODE_CUSTOM_PIPS', label: 'Custom Pips' },
    { value: 'TRAILING_STOP_MODE_CUSTOM_PRICE_FRACTION', label: 'Custom Price Fraction' },
  ],
  TrailingStepMode: [
    { value: 'TRAILING_STEP_MODE_PIPS', label: 'Fixed Pips' },
    { value: 'TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP', label: '% of Trailing Stop' },
  ],
  TrailingStartMode: [
    { value: 'TRAILING_START_MODE_OFF', label: 'Off (Always Trail)' },
    { value: 'TRAILING_START_MODE_OPEN_PRICE', label: 'At Open Price (Breakeven)' },
    { value: 'TRAILING_START_MODE_PIPS_OFFSET', label: 'After N Pips' },
    { value: 'TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP', label: '% of Trailing Stop' },
    { value: 'TRAILING_START_MODE_PERCENT_OF_OPPOSITE_STOP', label: '% of TP' },
    { value: 'TRAILING_START_MODE_PERCENT_OF_STOP', label: '% of SL' },
    { value: 'TRAILING_START_MODE_CUSTOM_PIPS', label: 'Custom Pips' },
    { value: 'TRAILING_START_MODE_CUSTOM_PRICE_FRACTION', label: 'Custom Price Fraction' },
  ],
  TrailingTPmode: [
    { value: 'TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE', label: 'Keep TP Unchanged' },
    { value: 'TRAILING_OPPOSITE_STOP_MODE_CLEAR_STOP', label: 'Remove TP' },
    { value: 'TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE', label: 'Pips From Open Price' },
    { value: 'TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP', label: '% of Trailing Stop' },
    { value: 'TRAILING_OPPOSITE_STOP_MODE_CUSTOM', label: 'Custom Function' },
  ],
  TrailWhat: [
    { value: '0', label: 'Trail Stop Loss' },
    { value: '1', label: 'Trail Take Profit' },
  ],
  TrailingReferencePrice: [
    { value: '0', label: 'Current Price (Bid/Ask)' },
    { value: '1', label: 'Custom Reference' },
  ],

  // ── Trailing Pending Orders ──
  trailing_distance_mode: [
    { value: 'TRAILING_DISTANCE_MODE_FIXED', label: 'Fixed Pips' },
    { value: 'TRAILING_DISTANCE_MODE_DYNAMIC', label: 'Dynamic Price Level' },
    { value: 'TRAILING_DISTANCE_MODE_DYNAMIC_PIPS', label: 'Dynamic Pips' },
    { value: 'TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS', label: 'Dynamic Price Fraction' },
  ],

  // ── Break Even ──
  on_profit_mode: [
    { value: 'ON_PROFIT_MODE_FIXED_VALUE', label: 'Fixed Pip Value' },
    { value: 'ON_PROFIT_MODE_PERCENT_OF_CURRENT_SL', label: '% of Current SL' },
    { value: 'ON_PROFIT_MODE_PERCENT_OF_CURRENT_TP', label: '% of Current TP' },
  ],
  bep_offset_mode: [
    { value: 'BEP_OFFSET_MODE_NONE', label: 'No Offset (Exact Breakeven)' },
    { value: 'BEP_OFFSET_MODE_PIPS_OFFSET', label: 'Pips Offset' },
  ],

  // ── Modify Stops of Trades ──
  relative_to: [
    { value: 'PRICE_RELATIVE_TO_OPEN_PRICE', label: 'Relative to Open Price' },
    { value: 'PRICE_RELATIVE_TO_CURRENT_PRICE', label: 'Relative to Current Price' },
    { value: 'PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL', label: 'Custom Price Level' },
  ],
  new_tpsl_mode: [
    { value: 'NEW_STOPS_FIXED', label: 'Fixed Pips' },
    { value: 'NEW_STOPS_PERCENT_OF_CURRENT_TPSL', label: '% of Current TP/SL' },
    { value: 'NEW_STOPS_CUSTOM_PRICE_LEVEL', label: 'Custom Price Level' },
  ],

  // ── Close Partially ──
  part_vol_mode: [
    { value: 'CLOSE_PARTIALLY_FIXED_VOLUME', label: 'Fixed Volume' },
    { value: 'CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME', label: '% of Current Volume' },
    { value: 'CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME', label: '% of Initial Volume' },
  ],

  // ── Check Profit/Loss (in-loop) ──
  check_mode: [
    { value: 'CHECK_PROFIT_LOSS_MODE_DEPOSIT_CURRENCY', label: 'Deposit Currency' },
    { value: 'CHECK_PROFIT_LOSS_MODE_ACCOUNT_PROFIT', label: 'Account Profit' },
    { value: 'CHECK_PROFIT_LOSS_MODE_EQUITY', label: 'Equity' },
    { value: 'CHECK_PROFIT_LOSS_MODE_BALANCE', label: 'Balance' },
    { value: 'CHECK_PROFIT_LOSS_MODE_FREE_MARGIN', label: 'Free Margin' },
  ],

  // ── Check Profit Unrealized ──
  profit_mode_each: [
    { value: 'PROFIT_MODE_NO_MATTER', label: 'No Per-Trade Filter' },
    { value: 'PROFIT_MODE_MONEY', label: 'Money' },
    { value: 'PROFIT_MODE_PIPS', label: 'Pips' },
  ],
  profit_mode: [
    { value: 'PROFIT_MODE_MONEY', label: 'Money' },
    { value: 'PROFIT_MODE_PIPS', label: 'Pips' },
    { value: 'PROFIT_MODE_PIPS_SUM', label: 'Sum of Pips' },
  ],

  // ── Loop for Trades/Orders ──
  loop_direction: [
    { value: 'newest_first', label: 'Newest First' },
    { value: 'oldest_first', label: 'Oldest First' },
  ],
  second_output: [
    { value: '', label: 'No Second Output' },
    { value: 'if_not_empty', label: 'If Found Trades' },
    { value: 'if_empty', label: 'If No Trades Found' },
  ],

  // ── Loop – Check Type ──
  CheckBuyOrSell: [
    { value: 'buy', label: 'Buy' },
    { value: 'sell', label: 'Sell' },
  ],
  CheckLimitOrStop: [
    { value: 'both', label: 'Both' },
    { value: 'limit', label: 'Limit Only' },
    { value: 'stop', label: 'Stop Only' },
  ],

  // ── Loop – Check Age ──
  AgeRelativeTo: [
    { value: 'open-time', label: 'From Open Time' },
    { value: 'close-time', label: 'From Close Time' },
  ],

  // ── Loop – Modify Stops (in-loop) ──
  RelativeTo: [
    { value: 'openprice', label: 'Relative to Open Price' },
    { value: 'currentprice', label: 'Relative to Current Price' },
  ],
  NewSLmode: [
    { value: 'fixed', label: 'Fixed Pips' },
    { value: 'percent', label: '% of Price' },
    { value: 'percentTP', label: '% of Take Profit' },
    { value: 'function', label: 'Custom Function' },
  ],
  NewTPmode: [
    { value: 'fixed', label: 'Fixed Pips' },
    { value: 'percent', label: '% of Price' },
    { value: 'percentSL', label: '% of Stop Loss' },
    { value: 'function', label: 'Custom Function' },
  ],

  // ── Loop – Pips Away ──
  DirectionMode: [
    { value: 'trading', label: 'In Trading Direction' },
    { value: 'against', label: 'Against Trading Direction' },
    { value: 'either', label: 'Either Direction' },
  ],
  PipsAwayMode: [
    { value: 'fixed', label: 'Fixed Pips' },
    { value: 'percent', label: 'Percentage' },
  ],

  // ── Time Filters ──
  server_or_local_time: [
    { value: 'TIME_SERVER', label: 'Server Time' },
    { value: 'TIME_LOCAL', label: 'Local Time' },
    { value: 'TIME_GMT', label: 'GMT Time' },
  ],
  time_start_mode: [
    { value: 'TIME_MODE_TEXT', label: 'Text (HH:MM)' },
    { value: 'TIME_MODE_COMPONENT', label: 'Component (Y/M/D/H/M/S)' },
    { value: 'TIME_MODE_RELATIVE', label: 'Relative Offset' },
  ],
  time_end_mode: [
    { value: 'TIME_MODE_TEXT', label: 'Text (HH:MM)' },
    { value: 'TIME_MODE_COMPONENT', label: 'Component (Y/M/D/H/M/S)' },
    { value: 'TIME_MODE_RELATIVE', label: 'Relative Offset' },
  ],
  spread_mode: [
    { value: 'SPREAD_BENCHMARK_FIX', label: 'Fixed Spread Value' },
    { value: 'SPREAD_BENCHMARK_AVERAGE', label: 'Average Spread' },
  ],

  // ── Various Signals ──
  SignalType: [
    { value: 'continuous', label: 'Continuous' },
    { value: 'once', label: 'Once Per Occurrence' },
  ],
  CandleType: [
    { value: 'both', label: 'Any Candle' },
    { value: 'bull', label: 'Bullish Only' },
    { value: 'bear', label: 'Bearish Only' },
  ],
  UpperWickMode: [
    { value: 'no_matter', label: 'Any Size' },
    { value: 'between', label: 'Between Min/Max' },
    { value: 'minimum', label: 'Minimum Size' },
  ],
  LowerWickMode: [
    { value: 'no_matter', label: 'Any Size' },
    { value: 'between', label: 'Between Min/Max' },
    { value: 'minimum', label: 'Minimum Size' },
  ],

  // ── Volume Profile ──
  RangeMode: [
    { value: 'VP_RANGE_MODE_BETWEEN_LINES', label: 'Between Lines' },
    { value: 'VP_RANGE_MODE_LAST_MINUTES', label: 'Last N Minutes' },
    { value: 'VP_RANGE_MODE_MINUTES_TO_LINE', label: 'Minutes to Line' },
  ],
  VolumeType: [
    { value: 'VOLUME_TICK', label: 'Tick Volume' },
    { value: 'VOLUME_REAL', label: 'Real Volume' },
  ],
  DataSource: [
    { value: 'VP_SOURCE_M1', label: 'M1 Bars' },
    { value: 'VP_SOURCE_M5', label: 'M5 Bars' },
    { value: 'VP_SOURCE_M15', label: 'M15 Bars' },
    { value: 'VP_SOURCE_M30', label: 'M30 Bars' },
  ],
  HgBarStyle: [
    { value: 'VP_BAR_STYLE_LINE', label: 'Line' },
    { value: 'VP_BAR_STYLE_BAR', label: 'Empty Bar' },
    { value: 'VP_BAR_STYLE_FILLED', label: 'Filled Bar' },
    { value: 'VP_BAR_STYLE_OUTLINE', label: 'Outline' },
    { value: 'VP_BAR_STYLE_COLOR', label: 'Color' },
  ],
  HgPosition: [
    { value: 'VP_HG_POSITION_WINDOW_LEFT', label: 'Window Left' },
    { value: 'VP_HG_POSITION_WINDOW_RIGHT', label: 'Window Right' },
    { value: 'VP_HG_POSITION_LEFT_OUTSIDE', label: 'Left Outside Range' },
    { value: 'VP_HG_POSITION_RIGHT_OUTSIDE', label: 'Right Outside Range' },
    { value: 'VP_HG_POSITION_LEFT_INSIDE', label: 'Left Inside Range' },
    { value: 'VP_HG_POSITION_RIGHT_INSIDE', label: 'Right Inside Range' },
  ],

  // ── Chart Objects ──
  object_type: [
    { value: 'OBJ_ARROW_UP', label: 'Arrow Up' },
    { value: 'OBJ_ARROW_DOWN', label: 'Arrow Down' },
    { value: 'OBJ_ARROW_BUY', label: 'Arrow Buy' },
    { value: 'OBJ_ARROW_SELL', label: 'Arrow Sell' },
    { value: 'OBJ_ARROW_STOP', label: 'Arrow Stop' },
    { value: 'OBJ_ARROW_CHECK', label: 'Arrow Check' },
    { value: 'OBJ_ARROW_LEFT_PRICE', label: 'Arrow Left Price' },
    { value: 'OBJ_ARROW_RIGHT_PRICE', label: 'Arrow Right Price' },
    { value: 'OBJ_ARROW_THUMB_UP', label: 'Thumb Up' },
    { value: 'OBJ_ARROW_THUMB_DOWN', label: 'Thumb Down' },
    { value: 'OBJ_ARROW', label: 'Custom Arrow Code' },
    { value: 'OBJ_TREND', label: 'Trend Line' },
    { value: 'OBJ_TRENDBYANGLE', label: 'Trend by Angle' },
    { value: 'OBJ_HLINE', label: 'Horizontal Line' },
    { value: 'OBJ_VLINE', label: 'Vertical Line' },
    { value: 'OBJ_CYCLES', label: 'Cycles' },
    { value: 'OBJ_CHANNEL', label: 'Channel' },
    { value: 'OBJ_STDDEVCHANNEL', label: 'Std Dev Channel' },
    { value: 'OBJ_REGRESSION', label: 'Regression' },
    { value: 'OBJ_PITCHFORK', label: 'Pitchfork' },
    { value: 'OBJ_GANNLINE', label: 'Gann Line' },
    { value: 'OBJ_GANNFAN', label: 'Gann Fan' },
    { value: 'OBJ_GANNGRID', label: 'Gann Grid' },
    { value: 'OBJ_RECTANGLE', label: 'Rectangle' },
    { value: 'OBJ_RECTANGLE_LABEL', label: 'Rectangle Label' },
    { value: 'OBJ_TRIANGLE', label: 'Triangle' },
    { value: 'OBJ_ELLIPSE', label: 'Ellipse' },
    { value: 'OBJ_TEXT', label: 'Text' },
    { value: 'OBJ_LABEL', label: 'Label' },
    { value: 'OBJ_FIBO', label: 'Fibonacci' },
  ],
  obj_style: LINE_STYLE,
  StatLineStyle: LINE_STYLE,
  ModeLevelStyle: LINE_STYLE,
  TimeFromStyle: LINE_STYLE,
  TimeToStyle: LINE_STYLE,
  obj_corner: [
    { value: 'CORNER_LEFT_UPPER', label: 'Top Left' },
    { value: 'CORNER_RIGHT_UPPER', label: 'Top Right' },
    { value: 'CORNER_LEFT_LOWER', label: 'Bottom Left' },
    { value: 'CORNER_RIGHT_LOWER', label: 'Bottom Right' },
  ],
  obj_anchor: [
    { value: 'ANCHOR_TOP', label: 'Top' },
    { value: 'ANCHOR_BOTTOM', label: 'Bottom' },
    { value: 'ANCHOR_LEFT', label: 'Left' },
    { value: 'ANCHOR_RIGHT', label: 'Right' },
    { value: 'ANCHOR_LEFT_UPPER', label: 'Top Left' },
    { value: 'ANCHOR_LEFT_LOWER', label: 'Bottom Left' },
    { value: 'ANCHOR_RIGHT_UPPER', label: 'Top Right' },
    { value: 'ANCHOR_RIGHT_LOWER', label: 'Bottom Right' },
    { value: 'ANCHOR_CENTER', label: 'Center' },
  ],
  obj_align: [
    { value: 'ALIGN_LEFT', label: 'Left' },
    { value: 'ALIGN_CENTER', label: 'Center' },
    { value: 'ALIGN_RIGHT', label: 'Right' },
  ],
  obj_border_type: [
    { value: 'BORDER_FLAT', label: 'Flat' },
    { value: 'BORDER_RAISED', label: 'Raised' },
    { value: 'BORDER_SUNKEN', label: 'Sunken' },
  ],

  // ── Play Sound ──
  MTsound: [
    { value: 'ok', label: 'OK' },
    { value: 'connect', label: 'Connect' },
    { value: 'disconnect', label: 'Disconnect' },
    { value: 'email', label: 'Email' },
    { value: 'expert', label: 'Expert' },
    { value: 'news', label: 'News' },
    { value: 'tick', label: 'Tick' },
    { value: 'timeout', label: 'Timeout' },
    { value: 'wait', label: 'Wait' },
    { value: 'alert', label: 'Alert' },
    { value: 'alert2', label: 'Alert 2' },
  ],

  // ── Check Type Last Closed ──
  LastOrderType: [
    { value: '0', label: 'Buy' },
    { value: '1', label: 'Sell' },
  ],

  // ── Indicator fields (shared across indicator input.json) ──
  applied_price: [
    { value: 'PRICE_CLOSE', label: 'Close' },
    { value: 'PRICE_OPEN', label: 'Open' },
    { value: 'PRICE_HIGH', label: 'High' },
    { value: 'PRICE_LOW', label: 'Low' },
    { value: 'PRICE_MEDIAN', label: 'Median (H+L)/2' },
    { value: 'PRICE_TYPICAL', label: 'Typical (H+L+C)/3' },
    { value: 'PRICE_WEIGHTED', label: 'Weighted (H+L+C+C)/4' },
  ],
  ma_method: [
    { value: 'MODE_SMA', label: 'Simple (SMA)' },
    { value: 'MODE_EMA', label: 'Exponential (EMA)' },
    { value: 'MODE_SMMA', label: 'Smoothed (SMMA)' },
    { value: 'MODE_LWMA', label: 'Linear Weighted (LWMA)' },
  ],
  method: [
    { value: 'MODE_SMA', label: 'Simple (SMA)' },
    { value: 'MODE_EMA', label: 'Exponential (EMA)' },
    { value: 'MODE_SMMA', label: 'Smoothed (SMMA)' },
    { value: 'MODE_LWMA', label: 'Linear Weighted (LWMA)' },
  ],
  mode: [
    { value: 'MODE_MAIN', label: 'Main Line' },
    { value: 'MODE_SIGNAL', label: 'Signal Line' },
    { value: 'MODE_UPPER', label: 'Upper Band' },
    { value: 'MODE_LOWER', label: 'Lower Band' },
    { value: 'MODE_GATORJAW', label: 'Jaw (Blue)' },
    { value: 'MODE_GATORTEETH', label: 'Teeth (Red)' },
    { value: 'MODE_GATORLIPS', label: 'Lips (Green)' },
    { value: 'MODE_TENKANSEN', label: 'Tenkan-sen' },
    { value: 'MODE_KIJUNSEN', label: 'Kijun-sen' },
    { value: 'MODE_SENKOUSPANA', label: 'Senkou Span A' },
    { value: 'MODE_SENKOUSPANB', label: 'Senkou Span B' },
    { value: 'MODE_CHIKOUSPAN', label: 'Chikou Span' },
    { value: 'MODE_PLUSDI', label: '+DI Line' },
    { value: 'MODE_MINUSDI', label: '-DI Line' },
  ],
  price_field: [
    { value: '0', label: 'Low/High' },
    { value: '1', label: 'Close/Close' },
  ],

  // ── On Trade Event filter fields ──
  sl_only: [
    { value: 'no', label: 'No' },
    { value: 'yes', label: 'Yes' },
  ],
  tp_only: [
    { value: 'no', label: 'No' },
    { value: 'yes', label: 'Yes' },
  ],
  close_mode: [
    { value: '', label: 'Any Close' },
    { value: 'sl', label: 'Closed by Stop Loss' },
    { value: 'tp', label: 'Closed by Take Profit' },
    { value: 'manual', label: 'Manual Close' },
  ],
  name_filter_mode: [
    { value: '', label: 'No Name Filter' },
    { value: 'starts_with', label: 'Starts With' },
    { value: 'contains', label: 'Contains' },
    { value: 'equals', label: 'Equals' },
  ],
  stops_mode: [
    { value: 'some', label: 'Some Stops Modified' },
    { value: 'both', label: 'Both SL and TP Modified' },
  ],

  // ── Value ──
  pips_mode: [
    { value: 'VALUE_PIPS_AS_IS', label: 'Pips As-Is' },
    { value: 'VALUE_PIPS_AS_PRICE_FRACTION', label: 'Pips as Price Fraction' },
  ],

  // ── Period (string-based timeframe) ──
  Period: PERIOD_STRING,
};

/** Detect color fields by field name pattern */
function isColorField(name: string): boolean {
  const lower = name.toLowerCase();
  return (
    lower.endsWith('color') ||
    lower === 'arrow_color' ||
    lower === 'level_color' ||
    lower === 'levelcolor'
  );
}

/** Detect boolean fields by current value */
function isBooleanValue(value: string): boolean {
  const v = value.toLowerCase().trim();
  return v === 'true' || v === 'false';
}

const BOOLEAN_OPTIONS: FieldOption[] = [
  { value: 'true', label: 'True' },
  { value: 'false', label: 'False' },
];

/**
 * Look up dropdown options for a given field.
 * Returns null if the field should remain a text input.
 */
export function getFieldOptions(fieldName: string, currentValue: string): FieldOption[] | null {
  // Color fields detected by name pattern
  if (isColorField(fieldName)) return MQL_COLORS;

  // Boolean detection by value
  if (isBooleanValue(currentValue)) return BOOLEAN_OPTIONS;

  // Numeric timeframe: field is "timeframe" with numeric-looking value
  if (fieldName === 'timeframe') {
    if (currentValue.startsWith('PERIOD_')) return PERIOD_STRING;
    return TIMEFRAME_NUMERIC;
  }

  // Direct lookup
  return FIELD_MAP[fieldName] ?? null;
}
