constants = [

    ########################## Blocks ##########################

    "#define ROUTE_1_PASSED 1",
    "#define ROUTE_2_PASSED 0",

    "#define RESET_LEVEL_DEFAULT 0",
    "#define RESET_LEVEL_TICK 1",
    "#define RESET_LEVEL_BAR 2",
    "#define RESET_LEVEL_CUSTOM 3",

    ########################## Time filter ############################
    "#define TIME_MODE_TEXT 1",
    "#define TIME_MODE_COMPONENT 2",
    "#define TIME_MODE_RELATIVE 3",

    "#define TIME_SERVER 1",
    "#define TIME_LOCAL 2",
    "#define TIME_GMT 3",

    ###################### Trade/Order filter ########################

    "#define ORDER_GROUP_MODE_ALL -1",  # STest, better name is ORDER_GROUP_MODE_ALL
    "#define ORDER_GROUP_MODE_NUMBER 1",
    "#define ORDER_GROUP_MODE_MANUAL 2",
    "#define SYMBOL_MODE_SPECIFIED 1",
    "#define SYMBOL_MODE_ANY 2",

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
    "#define PROFIT_MODE_MONEY \"money\"",
    "#define PROFIT_MODE_PIPS \"pips\"",
    "#define PROFIT_MODE_PIPS_SUM \"pips-sum\"",
    "#define PROFIT_MODE_NO_MATTER \"no-matter\"",

    ###################### for each trade ##########################
    "#define LOOP_DIRECTION_NEWEST_TO_OLDEST 1",
    "#define LOOP_DIRECTION_OLDEST_TO_NEWEST 2",
    "#define LOOP_DIRECTION_PROFITABLE_FIRST 3",
    "#define LOOP_DIRECTION_PROFITABLE_LAST 4",

    ###################### value ##########################

    "#define VALUE_PIPS_AS_IS 1",
    "#define VALUE_PIPS_AS_PRICE_FRACTION 2",

    "#define MODE_TIME_NOW 1",
    "#define MODE_TIME_TIMESTAMP 2",
    "#define MODE_TIME_COMPONENTS 3",
    "#define MODE_TIME_CANDLE_TIME 4",
    "#define MODE_TIME_TIME_VALUE 5",

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
    "#define MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI 13",
    "#define MONEY_MANAGEMENT_CUSTOM_VALUE 14",

    "#define POINT_FORMAT_RULES \"0.001=0.01,0.00001=0.0001,0.000001=0.0001\"",

    ###################### break even ##########################

    "#define ON_PROFIT_MODE_FIXED_VALUE 1",
    "#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_SL 2",
    "#define ON_PROFIT_MODE_PERCENT_OF_CURRENT_TP 3",

    "#define BEP_OFFSET_MODE_NONE 1",
    "#define BEP_OFFSET_MODE_PIPS_OFFSET 2",

    ###################### Trailing stop (each trade) ##########################

    "#define TRAILING_STOP_MODE_PIP \"fixed\"",
    "#define TRAILING_STOP_MODE_MULTIPLE_LEVELS \"multiple\"",
    "#define TRAILING_STOP_MODE_MONEY \"money\"",
    "#define TRAILING_STOP_MODE_PERCENT_OF_OPPOSITE_STOP \"percentTP\"",
    "#define TRAILING_STOP_MODE_PERCENT_OF_PROFIT \"percentProfit\"",
    "#define TRAILING_STOP_MODE_CUSTOM_LEVEL \"dynamic\"",
    "#define TRAILING_STOP_MODE_CUSTOM_PIPS \"dynamicSize\"",
    "#define TRAILING_STOP_MODE_CUSTOM_PRICE_FRACTION \"dynamicDigits\"",

    "#define TRAILING_START_MODE_OFF \"none\"",
    "#define TRAILING_START_MODE_OPEN_PRICE \"zero\"",
    "#define TRAILING_START_MODE_PIPS_OFFSET \"fixed\"",
    "#define TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP \"percentTS\"",
    "#define TRAILING_START_MODE_PERCENT_OF_OPPOSITE_STOP \"percentTP\"",
    "#define TRAILING_START_MODE_PERCENT_OF_STOP \"percentSL\"",
    "#define TRAILING_START_MODE_CUSTOM_PIPS \"function\"",
    "#define TRAILING_START_MODE_CUSTOM_PRICE_FRACTION \"functionFraction\"",

    "#define TRAILING_STEP_MODE_PIPS \"fixed\"",
    "#define TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP \"percentTS\"",

    "#define TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE \"none\"",
    "#define TRAILING_OPPOSITE_STOP_MODE_CLEAR_STOP \"clear\"",
    "#define TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE \"fixed\"",
    "#define TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP \"percentTS\"",
    "#define TRAILING_OPPOSITE_STOP_MODE_CUSTOM \"function\"",

    ###################### Close partially ##########################
    "#define CLOSE_PARTIALLY_FIXED_VOLUME 1",
    "#define CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME 2",
    "#define CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME 3",
    ###################### check profit/loss ##########################
    "#define CHECK_PROFIT_LOSS_MODE_DEPOSIT_CURRENCY 1",
    "#define CHECK_PROFIT_LOSS_MODE_ACCOUNT_PROFIT 2",
    "#define CHECK_PROFIT_LOSS_MODE_EQUITY 3",
    "#define CHECK_PROFIT_LOSS_MODE_BALANCE 4",
    "#define CHECK_PROFIT_LOSS_MODE_FREE_MARGIN 5",

    "#define CHECK_PROFIT 1",
    "#define CHECK_LOSS 2",

    ###################### trailing pending orders ##########################

    "#define TRAILING_DISTANCE_MODE_FIXED 1",
    "#define TRAILING_DISTANCE_MODE_DYNAMIC 2",
    "#define TRAILING_DISTANCE_MODE_DYNAMIC_PIPS 3",
    "#define TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS 4",

    ###################### modify stops of trades ##########################

    "#define PRICE_RELATIVE_TO_OPEN_PRICE 1",
    "#define PRICE_RELATIVE_TO_CURRENT_PRICE 2",
    "#define PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL 3",

    "#define NEW_STOPS_FIXED 1",
    "#define NEW_STOPS_PERCENT_OF_CURRENT_TPSL 2",
    "#define NEW_STOPS_CUSTOM_PRICE_LEVEL 3",

    ######################  ##########################
]


def get_constants():
    mconsts = constants.copy()
    for i in range(len(mconsts)):
        mconsts[i] = mconsts[i] + "\n"
    return mconsts
