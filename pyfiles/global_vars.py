TEMPLATE_BLOCKS_INIT = "Block *blocks_init[];\n"
TEMPLATE_BLOCKS_TIMER = "Block *blocks_timer[];\n"
TEMPLATE_BLOCKS_TICK = "Block *blocks_tick[];\n"
TEMPLATE_BLOCKS_TRADE = "Block *blocks_trade[];\n"
TEMPLATE_BLOCKS_CHART = "Block *blocks_chart[];\n"
TEMPLATE_BLOCKS_DEINIT = "Block *blocks_deinit[];\n"

TEMPLATE_EXIT_LOOP = "bool exit_loop = false;\n"
TEMPLATE_TIMER_PERIOD = "int timer_period = 60;//seconds\n"

TEMPLATE_OVERRIDING_SYMBOL = "string overriding_symbol = \"\";\n"
TEMPLATE_OVERRIDING_TIMEFRAME = "int overriding_timeframe = -1;\n"

TEMPLATE_ONCHART_EVENT_HOLDER = "OnChartEventHolder onchartEventHolder; \n"


def get__blocks():
    return TEMPLATE_BLOCKS_INIT + TEMPLATE_BLOCKS_TIMER + TEMPLATE_BLOCKS_TICK + TEMPLATE_BLOCKS_TRADE + TEMPLATE_BLOCKS_CHART + TEMPLATE_BLOCKS_DEINIT


def get__overriding_symbol():
    return TEMPLATE_OVERRIDING_SYMBOL


def get__overriding_timeframe():
    return TEMPLATE_OVERRIDING_TIMEFRAME


def get__onchart_event_holder():
    return TEMPLATE_ONCHART_EVENT_HOLDER


def get__exit_loop():
    return TEMPLATE_EXIT_LOOP


def get__timer_period():
    return TEMPLATE_TIMER_PERIOD
