from . import task_constructor
from . import block_constructor
from . import task_dynamic_constructor
from . import global_functions
from . import constants_constructor
from . import global_vars
from . import indicator_class_constructor
from . import candle_class_constructor
from . import value_class_constructor
from . import market_properties_class_constructor
from . import spread_filter_struct_constructor
from . import close_partially_items

header = ""
properties = []
consts_system = []
consts_user = []
vars_system = []
vars_user = []
structs = []
block_parent_blueprint = ""
task_blueprint = ""
task_elements = []
tasks = []
block_blueprint = ""
blocks = []
functions = []
on_init = []
on_timer = []
on_tick = []
on_trade = []
on_chart = []
on_deinit = []


def process_input(data):

    add_global_functions(data)
    add_global_structs()
    add_consts_system()
    add_consts_user(data.get("constants"))
    add_vars_system()
    add_vars_user(data.get("variables"))
    add_blueprints(block_parent_blueprint)
    process_tick_blocks(data.get("events").get("on_tick"))
    # process on init blocks
    # process on trade blocks ...

    # last thing to do
    reset_vars()
    return build()


def reset_vars():
    add_task_elements_common.pass_n_times_done = False
    add_task_elements_common.and_done = False
    add_task_elements_common.spread_filter_done = False
    add_task_elements_common.close_partially_done = False


def add_blueprints(block_parent_blueprint):
    # Add block_parent and task class blueprint
    block_parent_blueprint += block_constructor.get_block_parent()
    task_blueprint = task_constructor.get_task()
    classes.append(task_blue_print)

def process_tick_blocks(data):
    nodes = data.get("nodes")
    edges = data.get("edges")



    # Find entries
    entries = get_entries_sorted(nodes, edges)

    add_task_elements_common(nodes)
    add_task_elements_specific(nodes)

    # Add tasks
    for node in nodes:
        task = get_task_child(node)
        classes.append(task)

    # Add block blueprint
    block_blue_print = block_constructor.get_block()
    classes.append(block_blue_print)

    # Add blocks and tasks
    for node in nodes:
        block = get_block_child(node.get("input_dic_block"), node.get("id"))
        classes.append(block)

    # addBlocks call
    call_add_blocks = global_functions.get_call__add_blocks_tick()
    on_init.append(call_add_blocks)

    # resetBlocks call
    call_reset_blocks = global_functions.get_call__reset_blocks_tick()
    on_tick.append(call_reset_blocks)

    # runBlocks call
    for id_block in entries:
        call_run_block = global_functions.get_call__run_block_tick(-1, -1, id_block)
        on_tick.append(call_run_block)


def process_on_chart_blocks(data):
    nodes = data.get("nodes")
    edges = data.get("edges")

    # Find entries
    entries = get_entries_sorted(nodes, edges)

    add_task_elements_common(nodes)
    add_task_elements_specific(nodes)

    # Add tasks
    for node in nodes:
        task = get_task_child(node)
        classes.append(task)

    # Add block blueprint
    block_blue_print = block_constructor.get_block()
    classes.append(block_blue_print)

    # Add blocks and tasks
    for node in nodes:
        block = get_block_child(node.get("input_dic_block"), node.get("id"))
        classes.append(block)

    # addBlocks call
    call_add_blocks = global_functions.get_call__add_blocks_tick()
    on_init.append(call_add_blocks)

    # resetBlocks call
    call_reset_blocks = global_functions.get_call__reset_blocks_tick()
    on_tick.append(call_reset_blocks)

    # runBlocks call
    for id_block in entries:
        call_run_block = global_functions.get_call__run_block_tick(-1, -1, id_block)
        on_tick.append(call_run_block)


def add_vars_system():
    # blocks_tick var
    blocks_vars = global_vars.get__blocks()
    vars_system.append(blocks_vars)

    # overriding_symbol
    overriding_symbol = global_vars.get__overriding_symbol()
    vars_system.append(overriding_symbol)

    # overriding_timeframe
    overriding_timeframe = global_vars.get__overriding_timeframe()
    vars_system.append(overriding_timeframe)


def add_vars_user(vars):
    for var in vars:
        var_str = var.get("type") + " " + var.get("name") + " = " + var.get("value") + "; // " + var.get(
            "description") + "\n"
        vars_user.append(var_str)


def add_consts_system():
    consts_system.extend(constants_constructor.get_constants())


def add_consts_user(const_inputs):  # Defined by user
    for input in const_inputs:
        input_str = "extern " + input.get("type") + " " + input.get("name") + " = " + str(
            input.get("value")) + "; // " + input.get("description") + "\n"
        consts_user.append(input_str)


def add_global_functions(data):
    # AddToArray function
    fun_add_to_array = global_functions.get_fun__add_to_array()
    functions.append(fun_add_to_array)

    # RemoveIndexFromArray function
    fun_remove_index_from_array = global_functions.get_fun__remove_index_from_array()
    functions.append(fun_remove_index_from_array)

    # joinArrays function
    fun_join_arrays = global_functions.get_fun__join_arrays()
    functions.append(fun_join_arrays)

    # areAllItemsPresent function
    are_all_items_present = global_functions.get_fun__are_all_items_present()
    functions.append(are_all_items_present)

    # runBlock function
    fun_run_block = global_functions.get_fun__run_block_tick()
    functions.append(fun_run_block)

    # addBlocks function
    fun_add_blocks = global_functions.get_fun__add_blocks_tick(len(data.get("events").get("on_tick").get("nodes")))
    functions.append(fun_add_blocks)

    # resetBlocks function
    fun_reset_blocks = global_functions.get_fun__reset_blocks_tick()
    functions.append(fun_reset_blocks)

    # syncSymbolOverriding function
    fun_sync_symbol_overriding = global_functions.get_fun__sync_symbol_overriding()
    functions.append(fun_sync_symbol_overriding)

    # syncTimeframeOverriding function
    fun_sync_timeframe_overriding = global_functions.get_fun__sync_timeframe_overriding()
    functions.append(fun_sync_timeframe_overriding)

    # TimeFromString function
    fun_time_from_string = global_functions.get_fun__time_from_string()
    functions.append(fun_time_from_string)

    # TimeFromComponent function
    fun_time_from_components = global_functions.get_fun__time_from_components()
    functions.append(fun_time_from_components)

    # getGroupNumber function
    fun_get_group_number = global_functions.get_fun__get_group_number()
    functions.append(fun_get_group_number)

    # sameOrderType function
    fun_same_order_type = global_functions.get_fun__same_order_type()
    functions.append(fun_same_order_type)

    # isAutomated function
    fun_is_automated = global_functions.get_fun__is_automated()
    functions.append(fun_is_automated)

    # ReverseList function
    fun_reverse_list = global_functions.get_fun__reverse_list()
    functions.append(fun_reverse_list)

    # sleepex function
    fun_sleepex = global_functions.get_fun__sleepex()
    functions.append(fun_sleepex)

    # delete order function
    delete_order = global_functions.get_fun__delete_order()
    functions.append(delete_order)

    # wait trade context if busy function
    wait_trade_context_if_busy = global_functions.get_fun__wait_trade_context_if_busy()
    functions.append(wait_trade_context_if_busy)

    # check for trading error function
    check_for_trading_error = global_functions.get_fun__check_for_trading_error()
    functions.append(check_for_trading_error)

    # error message function
    error_message = global_functions.get_fun__error_message()
    functions.append(error_message)

    # Buy Sell + Pending + Money Management functions

    bet_martingale = global_functions.get_fun__bet_martingale()
    functions.append(bet_martingale)

    get_bet_trades_info = global_functions.get_fun__get_bet_trades_info()
    functions.append(get_bet_trades_info)

    trade_select_by_index = global_functions.get_fun__trade_select_by_index()
    functions.append(trade_select_by_index)

    history_trade_select_by_index = global_functions.get_fun__history_trade_select_by_index()
    functions.append(history_trade_select_by_index)

    filter_general = global_functions.get_fun__filter_general()
    functions.append(filter_general)

    symbol_digits = global_functions.get_fun__symbol_digits()
    functions.append(symbol_digits)

    is_order_type_sell = global_functions.get_fun__is_order_type_sell()
    functions.append(is_order_type_sell)

    dynamic_lots = global_functions.get_fun__dynamic_lots()
    functions.append(dynamic_lots)

    pip_value = global_functions.get_fun__pip_value()
    functions.append(pip_value)

    custom_point = global_functions.get_fun__custom_point()
    functions.append(custom_point)

    string_explode = global_functions.get_fun__string_explode()
    functions.append(string_explode)

    to_digits = global_functions.get_fun__to_digits()
    functions.append(to_digits)

    string_trim = global_functions.get_fun__string_trim()
    functions.append(string_trim)

    format_value_for_printing_all = global_functions.get_fun__format_value_for_printing_all()
    functions.append(format_value_for_printing_all)

    window_find_visible = global_functions.get_fun__window_find_visible()
    functions.append(window_find_visible)

    symbol_ask = global_functions.get_fun__symbol_ask()
    functions.append(symbol_ask)

    symbol_bid = global_functions.get_fun__symbol_bid()
    functions.append(symbol_bid)

    is_order_type_buy = global_functions.get_fun__is_order_type_buy()
    functions.append(is_order_type_buy)

    is_order_type_stop = global_functions.get_fun__is_order_type_stop()
    functions.append(is_order_type_stop)

    get_symbol = global_functions.get_fun__get_symbol()
    functions.append(get_symbol)

    get_timeframe = global_functions.get_fun__get_timeframe()
    functions.append(get_timeframe)

    is_symbol_accepted = global_functions.get_fun__is_symbol_accepted()
    functions.append(is_symbol_accepted)

    seconds_from_components = global_functions.get_fun__seconds_from_components()
    functions.append(seconds_from_components)

    load_object = global_functions.get_fun__load_object()
    functions.append(load_object)

    loaded_object_chart_id = global_functions.get_fun__loaded_object_chart_id()
    functions.append(loaded_object_chart_id)

    loaded_object_name = global_functions.get_fun__loaded_object_name()
    functions.append(loaded_object_name)

    loaded_object_subwindow = global_functions.get_fun__loaded_object_subwindow()
    functions.append(loaded_object_subwindow)

    loaded_object_type = global_functions.get_fun__loaded_object_type()
    functions.append(loaded_object_type)

    array_ensure_value = global_functions.get_fun__array_ensure_value()
    functions.append(array_ensure_value)

    in_array = global_functions.get_fun__in_array()
    functions.append(in_array)

    object_get_value_by_shift = global_functions.get_fun__object_get_value_by_shift()
    functions.append(object_get_value_by_shift)


def add_global_structs():
    structs_data = market_properties_class_constructor.get_structs()
    structs.append(structs_data)


def build():
    expert = ""
    expert += header
    for prop in properties:
        expert += prop
    for const in consts_system:
        expert += const
    for const in consts_user:
        expert += const
    for var in vars_user:
        expert += var
    for struct in structs:
        expert += struct
    for cls in classes:
        expert += cls
    for var in vars_system:
        expert += var
    for fun in functions:
        expert += fun

    expert += get_on_init_items()
    expert += get_on_timer_items()
    expert += get_on_tick_items()
    expert += get_on_trade_items()
    expert += get_on_chart_items()
    expert += get_on_deinit_items()

    return expert


def get_on_init_items():
    result = "int init(){\n"
    for item in on_init:
        result += item
    result += "\n}\n"
    return result


def get_on_timer_items():
    result = "void OnTimer(){\n"
    for item in on_timer:
        result += item
    result += "\n}\n"
    return result


def get_on_tick_items():
    result = "void OnTick(){\n"
    for item in on_tick:
        result += item
    result += "\n}\n"
    return result


def get_on_trade_items():
    result = "void OnTrade(){\n"
    for item in on_trade:
        result += item
    result += "\n}\n"
    return result


def get_on_chart_items():
    result = "void OnChartEvent(const int id,         // Event identifier\nconst long& lparam,   // Event parameter of long type\nconst double& dparam, // Event parameter of double type\nconst string& sparam  // Event parameter of string type\n){\n"
    for item in on_chart:
        result += item
    result += "\n}\n"
    return result


def get_on_deinit_items():
    result = "void deinit(const int reason){\n"
    for item in on_deinit:
        result += item
    result += "\n}\n"
    return result


def get_task_child(node):
    return task_dynamic_constructor.get_task_child(node)


def get_block_child(input_dic, id_block):
    return block_constructor.get_block_child(input_dic, id_block)


def get_entries_sorted(nodes, edges):
    entries = []
    for node in nodes:
        id_node = node.get("id")
        if is_entry(id_node, edges):
            entries.append(id_node)
    entries.sort()
    return entries


# node is entry if is not target and has target
def is_entry(id_node, edges):
    is_target = False
    for edge in edges:
        if id_node == edge.get("target"):
            is_target = True
            break
    if is_target:
        return False
    has_target = False
    for edge in edges:
        if id_node == edge.get("source"):
            has_target = True
            break
    return has_target


# Elements that are assigned to multiple
# tasks of same type or to multiple task types
def add_task_elements_common(nodes):
    if not hasattr(add_task_elements_common, "pass_n_times_done"):
        add_task_elements_common.pass_n_times_done = False
    if not hasattr(add_task_elements_common, "and_done"):
        add_task_elements_common.and_done = False
    if not hasattr(add_task_elements_common, "spread_filter_done"):
        add_task_elements_common.spread_filter_done = False
    if not hasattr(add_task_elements_common, "close_partially_done"):
        add_task_elements_common.close_partially_done = False

    for node in nodes:
        task_name = node.get("blockName")
        match task_name:
            case "pass_n_times":
                if add_task_elements_common.pass_n_times_done:
                    continue
                var_data = task_constructor.get_var_data(task_name)
                vars_system.append(var_data)
                add_task_elements_common.pass_n_times_done = True
            case "spread_filter":
                if add_task_elements_common.spread_filter_done:
                    continue
                structs_data = spread_filter_struct_constructor.get_structs()
                structs.append(structs_data)
                add_task_elements_common.spread_filter_done = True
            case "close_partially":
                if add_task_elements_common.close_partially_done:
                    continue
                structs_data = close_partially_items.get_structs()
                structs.append(structs_data)
                vars_data = close_partially_items.get_vars()
                vars_system.append(vars_data)
                add_task_elements_common.close_partially_done = True


def foo():
    if not hasattr(foo, "has_run"):
        foo.has_run = False

    if not foo.has_run:
        # This code will only run once
        print("This is the first time foo() is called")
        foo.has_run = True

    # This code will run every time foo() is called
    print("foo() is called")


# Call foo() multiple times
foo.has_run = False


# Elements that are assigned to a specific instance of a specific task type
def add_task_elements_specific(nodes):
    for node in nodes:
        task_name = node.get("blockName")
        if task_name == "condition_1_normal" or task_name == "formula":  # formula also use the same function as condition 1 normal
            condition_1_normal_elements(node)
        elif task_name == "condition_1_cross":
            condition_1_cross_elements(node)
        elif task_name == "modify_variables":
            modify_variables(node)
        elif task_name == "trailing_stop_each_trade":
            trailing_stop_each_trade(node)
        elif task_name == "comment":
            comment(node)
        elif task_name == "buy_sell":
            buy_sell(node)
        elif task_name == "trailing_pending_orders":
            trailing_pending_orders(node)
        elif task_name == "modify_stops_of_trades":
            modify_stops_of_trades(node)
        elif task_name == "draw_arrow":
            draw_arrow(node)
        elif task_name == "draw_button":
            draw_button(node)
        elif task_name == "draw_shape":
            draw_shape(node)
        elif task_name == "draw_line":
            draw_line(node)
        elif task_name == "draw_editfield":
            draw_editfield(node)
        elif task_name == "check_trendline_price_level":
            check_trendline_price_level(node)


def check_trendline_price_level(node):
    value_fetch = node.get("params").get("price_level")
    row1 = value_fetch.get("row1")
    row2 = value_fetch.get("row2")
    params = value_fetch.get("params")
    id_val = str(node.get("id")) + "_price_level"
    classes.append(value_fetch_class(row1, row2, params, id_val))


def draw_editfield(node):
    value_fetch = node.get("params").get("text")
    row1 = value_fetch.get("row1")
    row2 = value_fetch.get("row2")
    params = value_fetch.get("params")
    id_val = str(node.get("id")) + "_text"
    classes.append(value_fetch_class(row1, row2, params, id_val))


def draw_line(node):
    object_type = node.get("params").get("object_type")
    if "time_1" in object_type:
        value_fetch_time_1 = object_type.get("time_1")
        row1_time_1 = value_fetch_time_1.get("row1")
        row2_time_1 = value_fetch_time_1.get("row2")
        params_time_1 = value_fetch_time_1.get("params")
        id_val_time_1 = str(node.get("id")) + "_time_1"
        classes.append(value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))
    if "time_2" in object_type:
        value_fetch_time_2 = object_type.get("time_2")
        row1_time_2 = value_fetch_time_2.get("row1")
        row2_time_2 = value_fetch_time_2.get("row2")
        params_time_2 = value_fetch_time_2.get("params")
        id_val_time_2 = str(node.get("id")) + "_time_2"
        classes.append(value_fetch_class(row1_time_2, row2_time_2, params_time_2, id_val_time_2))

    if "price_1" in object_type:
        value_fetch_price_1 = object_type.get("price_1")
        row1_price_1 = value_fetch_price_1.get("row1")
        row2_price_1 = value_fetch_price_1.get("row2")
        params_price_1 = value_fetch_price_1.get("params")
        id_val_price_1 = str(node.get("id")) + "_price_1"
        classes.append(value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))
    if "price_2" in object_type:
        value_fetch_price_2 = object_type.get("price_2")
        row1_price_2 = value_fetch_price_2.get("row1")
        row2_price_2 = value_fetch_price_2.get("row2")
        params_price_2 = value_fetch_price_2.get("params")
        id_val_price_2 = str(node.get("id")) + "_price_2"
        classes.append(value_fetch_class(row1_price_2, row2_price_2, params_price_2, id_val_price_2))


def draw_shape(node):
    if "time_1" in node.get("params"):
        value_fetch_time_1 = node.get("params").get("time_1")
        row1_time_1 = value_fetch_time_1.get("row1")
        row2_time_1 = value_fetch_time_1.get("row2")
        params_time_1 = value_fetch_time_1.get("params")
        id_val_time_1 = str(node.get("id")) + "_time_1"
        classes.append(value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))
    if "time_2" in node.get("params"):
        value_fetch_time_2 = node.get("params").get("time_2")
        row1_time_2 = value_fetch_time_2.get("row1")
        row2_time_2 = value_fetch_time_2.get("row2")
        params_time_2 = value_fetch_time_2.get("params")
        id_val_time_2 = str(node.get("id")) + "_time_2"
        classes.append(value_fetch_class(row1_time_2, row2_time_2, params_time_2, id_val_time_2))
    if "time_3" in node.get("params"):
        value_fetch_time_3 = node.get("params").get("time_3")
        row1_time_3 = value_fetch_time_3.get("row1")
        row2_time_3 = value_fetch_time_3.get("row2")
        params_time_3 = value_fetch_time_3.get("params")
        id_val_time_3 = str(node.get("id")) + "_time_3"
        classes.append(value_fetch_class(row1_time_3, row2_time_3, params_time_3, id_val_time_3))

    if "price_1" in node.get("params"):
        value_fetch_price_1 = node.get("params").get("price_1")
        row1_price_1 = value_fetch_price_1.get("row1")
        row2_price_1 = value_fetch_price_1.get("row2")
        params_price_1 = value_fetch_price_1.get("params")
        id_val_price_1 = str(node.get("id")) + "_price_1"
        classes.append(value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))
    if "price_2" in node.get("params"):
        value_fetch_price_2 = node.get("params").get("price_2")
        row1_price_2 = value_fetch_price_2.get("row1")
        row2_price_2 = value_fetch_price_2.get("row2")
        params_price_2 = value_fetch_price_2.get("params")
        id_val_price_2 = str(node.get("id")) + "_price_2"
        classes.append(value_fetch_class(row1_price_2, row2_price_2, params_price_2, id_val_price_2))
    if "price_3" in node.get("params"):
        value_fetch_price_3 = node.get("params").get("price_3")
        row1_price_3 = value_fetch_price_3.get("row1")
        row2_price_3 = value_fetch_price_3.get("row2")
        params_price_3 = value_fetch_price_3.get("params")
        id_val_price_3 = str(node.get("id")) + "_price_3"
        classes.append(value_fetch_class(row1_price_3, row2_price_3, params_price_3, id_val_price_3))


def draw_button(node):
    value_fetch = node.get("params").get("text")
    row1 = value_fetch.get("row1")
    row2 = value_fetch.get("row2")
    params = value_fetch.get("params")
    id_val = str(node.get("id")) + "_obj_text"
    classes.append(value_fetch_class(row1, row2, params, id_val))


def draw_arrow(node):
    value_fetch_time_1 = node.get("params").get("time_1")
    row1_time_1 = value_fetch_time_1.get("row1")
    row2_time_1 = value_fetch_time_1.get("row2")
    params_time_1 = value_fetch_time_1.get("params")
    id_val_time_1 = str(node.get("id")) + "_time_1"
    classes.append(value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))

    value_fetch_price_1 = node.get("params").get("price_1")
    row1_price_1 = value_fetch_price_1.get("row1")
    row2_price_1 = value_fetch_price_1.get("row2")
    params_price_1 = value_fetch_price_1.get("params")
    id_val_price_1 = str(node.get("id")) + "_price_1"
    classes.append(value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))


def modify_stops_of_trades(node):
    relative_to_data = node.get("params").get("relative_to")
    if relative_to_data.get("value") == "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL":
        value_fetch = relative_to_data.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "_rt"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    new_tpsl_mode_data = node.get("params").get("new_tpsl_mode")
    if new_tpsl_mode_data.get("value") == "NEW_STOPS_CUSTOM_PRICE_LEVEL":
        value_fetch_tp = new_tpsl_mode_data.get("new_take_profit_level")
        row1_tp = value_fetch_tp.get("row1")
        row2_tp = value_fetch_tp.get("row2")
        params_tp = value_fetch_tp.get("params_tp")
        id_val_tp = str(node.get("id")) + "_ntm_tp"

        value_fetch_sl = new_tpsl_mode_data.get("new_stop_loss_level")
        row1_sl = value_fetch_sl.get("row1")
        row2_sl = value_fetch_sl.get("row2")
        params_sl = value_fetch_sl.get("params_sl")
        id_val_sl = str(node.get("id")) + "_ntm_sl"

        classes.append(value_fetch_class(row1_tp, row2_tp, params_tp, id_val_tp))
        classes.append(value_fetch_class(row1_sl, row2_sl, params_sl, id_val_sl))


def trailing_pending_orders(node):
    trailing_distance_mode_data = node.get("params").get("trailing_distance_mode")
    trailing_distance_mode = trailing_distance_mode_data.get("value")
    if trailing_distance_mode != "TRAILING_DISTANCE_MODE_FIXED":
        key = ""
        if trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC":
            key = "dynamic_level"
        elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_PIPS":
            key = "dynamic_size_pips_input"
        elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS":
            key = "dynamic_size_digits_only"
        value_fetch = trailing_distance_mode_data.get(key)
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "_tdmd"
        classes.append(value_fetch_class(row1, row2, params, id_val))


def buy_sell(node):
    open_at_price_data = node.get("params").get("open_at_price")
    open_at_price = open_at_price_data.get("value")
    if open_at_price == "OPEN_AT_CUSTOM_PRICE":
        value_fetch = open_at_price_data.get("price_to_open_dynamic_level")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "oacp"
        classes.append(value_fetch_class(row1, row2, params, id_val))


def comment(node):
    mrow1 = node.get("params").get("row1")
    if mrow1.get("Label").get("value") != "" and "value_fetch" in mrow1:
        value_fetch = mrow1.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r1"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow2 = node.get("params").get("row2")
    if mrow2.get("Label").get("value") != "" and "value_fetch" in mrow2:
        value_fetch = mrow2.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r2"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow3 = node.get("params").get("row3")
    if mrow3.get("Label").get("value") != "" and "value_fetch" in mrow3:
        value_fetch = mrow3.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r3"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow4 = node.get("params").get("row4")
    if mrow4.get("Label").get("value") != "" and "value_fetch" in mrow4:
        value_fetch = mrow4.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r4"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow5 = node.get("params").get("row5")
    if mrow5.get("Label").get("value") != "" and "value_fetch" in mrow5:
        value_fetch = mrow5.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r5"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow6 = node.get("params").get("row6")
    if mrow6.get("Label").get("value") != "" and "value_fetch" in mrow6:
        value_fetch = mrow6.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r6"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow7 = node.get("params").get("row7")
    if mrow7.get("Label").get("value") != "" and "value_fetch" in mrow7:
        value_fetch = mrow7.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r7"
        classes.append(value_fetch_class(row1, row2, params, id_val))

    mrow8 = node.get("params").get("row8")
    if mrow8.get("Label").get("value") != "" and "value_fetch" in mrow8:
        value_fetch = mrow8.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "cm_r8"
        classes.append(value_fetch_class(row1, row2, params, id_val))


def trailing_stop_each_trade(node):
    trailing_stop_mode_data = node.get("params").get("TrailingStopMode")
    trailing_stop_mode = trailing_stop_mode_data.get("value")
    if trailing_stop_mode == "TRAILING_STOP_MODE_CUSTOM_LEVEL":
        value_fetch = trailing_stop_mode_data.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id")) + "tsm_cl"
        classes.append(value_fetch_class(row1, row2, params, id_val))


def modify_variables(node):
    for item in node.get("params"):
        value_fetch = item.get("value_fetch")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params = value_fetch.get("params")
        id_val = str(node.get("id"))
        classes.append(value_fetch_class(row1, row2, params, id_val))


def condition_1_normal_elements(node):
    params = node.get("params")
    # left data
    row1_left = params.get("left").get("row1")
    row2_left = params.get("left").get("row1")
    id_val_left = str(node.get("id")) + "_" + "left"
    params_left = params.get("left").get("params")
    classes.append(value_fetch_class(row1_left, row2_left, params_left, id_val_left))
    # right data
    row1_right = params.get("right").get("row1")
    row2_right = params.get("right").get("row1")
    id_val_right = str(node.get("id")) + "_" + "right"
    params_right = params.get("right").get("params")
    classes.append(value_fetch_class(row1_right, row2_right, params_right, id_val_right))


def condition_1_cross_elements(node):
    params = node.get("params")
    # left data
    row1_left = params.get("left").get("row1")
    row2_left = params.get("left").get("row2")
    id_val_left_1 = str(node.get("id")) + "_" + "left1"
    id_val_left_2 = str(node.get("id")) + "_" + "left2"
    params_left_1 = params.get("left").get("params")
    params_left_2 = params_left_1.copy()
    if "shift" in params_left_2:
        params_left_2["shift"] = int(params_left_2["shift"]) + params.get("operator").get("cross_width")
    classes.append(value_fetch_class(row1_left, row2_left, params_left_1, id_val_left_1))
    classes.append(value_fetch_class(row1_left, row2_left, params_left_2, id_val_left_2))
    # right data
    row1_right = params.get("right").get("row1")
    row2_right = params.get("right").get("row2")
    id_val_right_1 = str(node.get("id")) + "_" + "right1"
    id_val_right_2 = str(node.get("id")) + "_" + "right2"
    params_right_1 = params.get("right").get("params")
    params_right_2 = params_right_1.copy()
    if "shift" in params_right_2:
        params_right_2["shift"] = int(params_right_2["shift"]) + params.get("operator").get("cross_width")
    classes.append(value_fetch_class(row1_right, row2_right, params_right_1, id_val_right_1))
    classes.append(value_fetch_class(row1_right, row2_right, params_right_2, id_val_right_2))


def value_fetch_class(row1, row2, params, id_val):
    if row1 == "Indicator":
        return indicator_class_constructor.get_class(row2, params, id_val)
    elif row1 == "Candle":
        return candle_class_constructor.get_class(params, id_val)
    elif row1 == "Market Properties":
        return market_properties_class_constructor.get_class(params, id_val)
    elif row1 == "Value":
        return value_class_constructor.get_class(params, id_val)
