constants = [

    ########################## Blocks ##########################

    "#define ROUTE_1_PASSED 1",
    "#define ROUTE_2_PASSED 0",

    "#define RESET_LEVEL_DEFAULT 0",
    "#define RESET_LEVEL_TICK 1",
    "#define RESET_LEVEL_BAR 2",
    "#define RESET_LEVEL_CUSTOM 3",

    ########################## Time filter ############################

    "#define TIME_SERVER 1",
    "#define TIME_LOCAL 2",
    "#define TIME_GMT 3",

    ###################### Trade/Order filter ########################

    "#define ORDER_GROUP_MODE_NONE -1",  # STest, better name is ORDER_GROUP_MODE_ALL
    "#define ORDER_GROUP_MODE_NUMBER 1",
    "#define ORDER_GROUP_MODE_AUTOMATED 2",
    ##################### Candle ##########################
    # price modes
    "#define  CANDLE_OPEN  1",
    "#define  CANDLE_HIGH  2",
    "#define  CANDLE_LOW  3",
    "#define  CANDLE_CLOSE  4",
    "#define  CANDLE_MEDIAN  5",
    "#define  CANDLE_HLC3  6",
    "#define  CANDLE_AVERAGE  7",
    "#define  CANDLE_GAP_TO_PREV  8",

    "#define  CANDLE_TOTAL_SIZE  9",
    "#define  CANDLE_BODY_SIZE  10",
    "#define  CANDLE_TOP_WICK  11",
    "#define  CANDLE_BOTTOM_WICK  12",

    "#define  BULL_CANDLE_TOTAL_SIZE  13",
    "#define  BULL_CANDLE_BODY_SIZE  14",
    "#define  BULL_CANDLE_TOP_WICK  15",
    "#define  BULL_CANDLE_BOTTOM_WICK  16",

    "#define  BEAR_CANDLE_TOTAL_SIZE  17",
    "#define  BEAR_CANDLE_BODY_SIZE  18",
    "#define  BEAR_CANDLE_TOP_WICK  19",
    "#define  BEAR_CANDLE_BOTTOM_WICK  20",

    # find methods
    "#define  FIND_BY_ID  1",
    "#define  FIND_BY_DATE  2",

    ###################### Market Properties ########################

    # price modes
    "#define  HIGHEST_PRICE  1",
    "#define  LOWEST_PRICE  2",

    # find methods
    "#define  TIME_PERIOD  1",
    "#define  CANDLE_PERIOD  2",

    # what to get
    "#define  GET_CANDLE_ID  1",
    "#define  GET_PRICE  2",
    "#define  GET_TIME  3",
    ###################### check trades orders nearby ########################

    "#define PRICE_AUTO 1",  # auto means ask for buy and bid for sell
    "#define PRICE_ASK 2",
    "#define PRICE_BID 3",
    "#define PRICE_MID 4",

    "#define RANGE_MODE_PIPS 1",
    "#define RANGE_MODE_PRICE_FRACTION 2",

    "#define RANGE_POSITION_AROUND 1",
    "#define RANGE_POSITION_WINNING_SIDE 2",
    "#define RANGE_POSITION_LOSING_SIDE 3",

    ###################### profit unrealized ########################
    "#define PROFIT_MODE_PIPS 1",
    "#define PROFIT_MODE_MONEY 2",

    ###################### for each trade ##########################
    "#define LOOP_DIRECTION_NEWEST_TO_OLDEST 1",
    "#define LOOP_DIRECTION_OLDEST_TO_NEWEST 2",
    "#define LOOP_DIRECTION_PROFITABLE_FIRST 3",
    "#define LOOP_DIRECTION_PROFITABLE_LAST 4",

    ###################### value ##########################
    "#define VALUE_TYPE_NUMERIC 1",
    "#define VALUE_TYPE_BOOLEAN 2",
    "#define VALUE_TYPE_COLOR 3",
    "#define VALUE_TYPE_PIPS 4",
    "#define VALUE_TYPE_TEXT 5",
    "#define VALUE_TYPE_TEXT_CODE_INPUT 6",
    "#define VALUE_TYPE_TIME 7",

    "#define VALUE_PIPS_AS_IS 1",
    "#define VALUE_PIPS_AS_PRICE_FRACTION 2",

    ###################### Blocks On/Off/Toggle ##########################
    "#define BLOCK_STATE_ENABLE 1",
    "#define BLOCK_STATE_DISABLE 2",
    "#define BLOCK_STATE_TOGGLE 3",

    ###################### Spread filter ##########################   
    "#define SPREAD_BENCHMARK_AVERAGE 1",
    "#define SPREAD_BENCHMARK_FIX 2",

    ###################### Buy Sell ##########################  
    "#define ORDER_BUY 1",
    "#define ORDER_SELL 2",
    "#define ORDER_BUY_PENDING 3",
    "#define ORDER_SELL_PENDING 4",

    "#define OPEN_AT_ASK 1",
    "#define OPEN_AT_BID 2",
    "#define OPEN_AT_MID 3",
    "#define OPEN_AT_CUSTOM_PRICE 4",

    "#define LOOK_UP_RUNNING_THEN_HISTORY 0",
    "#define LOOK_UP_RUNNING_ONLY 1",
    "#define LOOK_UP_HISTORY_ONLY 2",

    # TP SL modes are different only at items 1&2 and 5&6
    "#define TPSL_MODE_NO_TP 1",
    "#define TPSL_MODE_NO_SL 2",
    "#define TPSL_MODE_FIXED_PIPS 3",
    "#define TPSL_MODE_PERCENT_OF_PRICE 4",
    "#define TPSL_MODE_PERCENT_FROM_SL 5",
    "#define TPSL_MODE_PERCENT_FROM_TP 6",
    "#define TPSL_MODE_CUSTOM_PRICE_LEVEL 7",
    "#define TPSL_MODE_CUSTOM_PIPS 8",
    "#define TPSL_MODE_CUSTOM_PRICE_FRACTION 9",

    "#define MONEY_MANAGEMENT_FIXED_VOLUME 1",
    "#define MONEY_MANAGEMENT_PERCENT_OF_EQUITY 2",
    "#define MONEY_MANAGEMENT_PERCENT_OF_BALANCE 3",
    "#define MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN 4",
    "#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY 5",
    "#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE 6",
    "#define MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN 7",
    "#define MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY 8",
    "#define MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE 9",
    "#define MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN 10",
    "#define MONEY_MANAGEMENT_RISK_FIXED_AMOUNT_OF_MONEY 11",
    "#define MONEY_MANAGEMENT_FIXED_RATIO_BY_RYAN_JONES 12",
    "#define MONEY_MANAGEMENT_BETTING_MARTINGLE_PAROLI 13",
    "#define MONEY_MANAGEMENT_CUSTOM_VALUE 14",

    "#define POINT_FORMAT_RULES \"0.001=0.01,0.00001=0.0001,0.000001=0.0001\"",

    ###################### break even ##########################

    "#define ON_PROFIT_MODE_FIXED_VALUE 1",
    "#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_SL 2",
    "#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_TP 3",

    "#define BEP_OFFSET_MODE_NONE 1",
    "#define BEP_OFFSET_MODE_PIPS_OFFSET 2",

    ######################  ##########################

    ######################  ##########################

    ######################  ##########################
]


def get_constants():
    mconsts = constants.copy()
    for i in range(len(mconsts)):
        mconsts[i] = mconsts[i] + "\n"
    return mconsts
