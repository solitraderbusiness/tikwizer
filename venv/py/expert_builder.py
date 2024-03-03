import block_constructor
import task_constructor
import task_dynamic_constructor
import global_functions
import constants_constructor
import global_vars
import indicator_class_constructor
import candle_class_constructor
import value_class_constructor
import market_properties_class_constructor
import spread_filter_struct_constructor
import close_partially_items

header = ""
properties = []
consts_system = []
consts_user = []
vars_system = []
vars_user = []
structs = []
classes = []
functions = []
on_init = []
on_timer = []
on_tick = []
on_trade = []
on_chart = []
on_deinit = []


def process_input(data):
    # process global functions
    add_global_functions(data)

    # process system constants
    add_consts_system()

    # process user constants (inputs)
    add_consts_user(data.get("constants"))

    # process system vars
    add_vars_system()

    # process user vars
    add_vars_user(data.get("variables"))

    process_tick_blocks(data.get("events").get("on_tick"))
    # process on init blocks
    # process on trade blocks ...
    return build()


def process_tick_blocks(data):
    nodes = data.get("nodes")
    edges = data.get("edges")

    # Add block_parent and task class blueprint
    block_parent_blue_print = block_constructor.get_block_parent()
    task_blue_print = task_constructor.get_task()
    classes.append(block_parent_blue_print)
    classes.append(task_blue_print)

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
        input_str = "extern " + input.get("type") + " " + input.get("name") + " = " + input.get(
            "value") + "; // " + input.get("description") + "\n"
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
    pass_n_times_done = False
    and_done = False
    market_properties_done = False
    spread_filter_done = False
    close_partially_done = False
    for node in nodes:
        task_name = node.get("data").get("blockName")
        match task_name:
            case "pass_n_times":
                if pass_n_times_done: continue
                var_data = task_constructor.get_var_data(task_name)
                variables.append(var_data)
                pass_n_times_done = True
            case "condition_1_normal" | "condition_1_cross" | "formula":
                left_label = node.get("more").get("left1").get("label")
                right_label = node.get("more").get("right1").get("label")
                if (left_label == "Market Properties" or right_label == "Market Properties"):
                    if market_properties_done: continue
                    structs_data = market_properties_class_constructor.get_structs()
                    structs.append(structs_data)
                    market_properties_done = True
            case "modify_variables":
                for item in node.get("items"):
                    if (item.get("value").get("row1").get("label") == "Market Properties"):
                        if market_properties_done: continue
                        structs_data = market_properties_class_constructor.get_structs()
                        structs.append(structs_data)
                        market_properties_done = True
            case "comment":
                if market_properties_done: continue
                row1 = node.get("more").get("row1")
                row2 = node.get("more").get("row2")
                row3 = node.get("more").get("row3")
                row4 = node.get("more").get("row4")
                row5 = node.get("more").get("row5")
                row6 = node.get("more").get("row6")
                row7 = node.get("more").get("row7")
                row8 = node.get("more").get("row8")

                con1 = "value_fetch" in row1 and row1.get("value_fetch").get("row1").get("label") == "Market Properties"
                con2 = "value_fetch" in row2 and row2.get("value_fetch").get("row1").get("label") == "Market Properties"
                con3 = "value_fetch" in row3 and row3.get("value_fetch").get("row1").get("label") == "Market Properties"
                con4 = "value_fetch" in row4 and row4.get("value_fetch").get("row1").get("label") == "Market Properties"
                con5 = "value_fetch" in row5 and row5.get("value_fetch").get("row1").get("label") == "Market Properties"
                con6 = "value_fetch" in row6 and row6.get("value_fetch").get("row1").get("label") == "Market Properties"
                con7 = "value_fetch" in row7 and row7.get("value_fetch").get("row1").get("label") == "Market Properties"
                con8 = "value_fetch" in row8 and row8.get("value_fetch").get("row1").get("label") == "Market Properties"

                con = con1 or con2 or con3 or con4 or con5 or con6 or con7 or con8
                if (con):
                    structs_data = market_properties_class_constructor.get_structs()
                    structs.append(structs_data)
                    market_properties_done = True
            case "spread_filter":
                if spread_filter_done: continue
                structs_data = spread_filter_struct_constructor.get_structs()
                structs.append(structs_data)
                spread_filter_done = True
            case "close_partially":
                if close_partially_done: continue
                structs_data = close_partially_items.get_structs()
                structs.append(structs_data)
                vars_data = close_partially_items.get_vars()
                vars_system.append(vars_data)
                spread_filter_done = True


# Elements that are assigned to a specific instance of a specific task type
def add_task_elements_specific(nodes):
    for node in nodes:
        task_name = node.get("data").get("blockName")
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
            draw_shape(node)


def draw_line(node):
    if "obj_time_1" in node.get("more"):
        obj_time_1_data = node.get("more").get("obj_time_1")
        input_dic_time_1 = obj_time_1_data.get("input_dic")
        value_fetch_time_1 = obj_time_1_data.get("value_fetch")
        row1_time_1 = value_fetch_time_1.get("row1").get("label")
        row2_time_1 = value_fetch_time_1.get("row2").get("name")
        id_val_time_1 = str(node.get("id")) + "_time_1"
        classes.append(value_fetch_class(row1_time_1, row2_time_1, input_dic_time_1, id_val_time_1))
    if "obj_time_2" in node.get("more"):
        obj_time_2_data = node.get("more").get("obj_time_2")
        input_dic_time_2 = obj_time_2_data.get("input_dic")
        value_fetch_time_2 = obj_time_2_data.get("value_fetch")
        row1_time_2 = value_fetch_time_2.get("row1").get("label")
        row2_time_2 = value_fetch_time_2.get("row2").get("name")
        id_val_time_2 = str(node.get("id")) + "_time_2"
        classes.append(value_fetch_class(row1_time_2, row2_time_2, input_dic_time_2, id_val_time_2))

    if "obj_price_1" in node.get("more"):
        obj_price_1_data = node.get("more").get("obj_price_1")
        input_dic_price_1 = obj_price_1_data.get("input_dic")
        value_fetch_price_1 = obj_price_1_data.get("value_fetch")
        row1_price_1 = value_fetch_price_1.get("row1").get("label")
        row2_price_1 = value_fetch_price_1.get("row2").get("name")
        id_val_price_1 = str(node.get("id")) + "_price_1"
        classes.append(value_fetch_class(row1_price_1, row2_price_1, input_dic_price_1, id_val_price_1))
    if "obj_price_2" in node.get("more"):
        obj_price_2_data = node.get("more").get("obj_price_2")
        input_dic_price_2 = obj_price_2_data.get("input_dic")
        value_fetch_price_2 = obj_price_2_data.get("value_fetch")
        row1_price_2 = value_fetch_price_2.get("row1").get("label")
        row2_price_2 = value_fetch_price_2.get("row2").get("name")
        id_val_price_2 = str(node.get("id")) + "_price_2"
        classes.append(value_fetch_class(row1_price_2, row2_price_2, input_dic_price_2, id_val_price_2))

def draw_shape(node):
    if "obj_time_1" in node.get("more"):
        obj_time_1_data = node.get("more").get("obj_time_1")
        input_dic_time_1 = obj_time_1_data.get("input_dic")
        value_fetch_time_1 = obj_time_1_data.get("value_fetch")
        row1_time_1 = value_fetch_time_1.get("row1").get("label")
        row2_time_1 = value_fetch_time_1.get("row2").get("name")
        id_val_time_1 = str(node.get("id")) + "_time_1"
        classes.append(value_fetch_class(row1_time_1, row2_time_1, input_dic_time_1, id_val_time_1))
    if "obj_time_2" in node.get("more"):
        obj_time_2_data = node.get("more").get("obj_time_2")
        input_dic_time_2 = obj_time_2_data.get("input_dic")
        value_fetch_time_2 = obj_time_2_data.get("value_fetch")
        row1_time_2 = value_fetch_time_2.get("row1").get("label")
        row2_time_2 = value_fetch_time_2.get("row2").get("name")
        id_val_time_2 = str(node.get("id")) + "_time_2"
        classes.append(value_fetch_class(row1_time_2, row2_time_2, input_dic_time_2, id_val_time_2))
    if "obj_time_3" in node.get("more"):
        obj_time_3_data = node.get("more").get("obj_time_3")
        input_dic_time_3 = obj_time_3_data.get("input_dic")
        value_fetch_time_3 = obj_time_3_data.get("value_fetch")
        row1_time_3 = value_fetch_time_3.get("row1").get("label")
        row2_time_3 = value_fetch_time_3.get("row2").get("name")
        id_val_time_3 = str(node.get("id")) + "_time_3"
        classes.append(value_fetch_class(row1_time_3, row2_time_3, input_dic_time_3, id_val_time_3))

    if "obj_price_1" in node.get("more"):
        obj_price_1_data = node.get("more").get("obj_price_1")
        input_dic_price_1 = obj_price_1_data.get("input_dic")
        value_fetch_price_1 = obj_price_1_data.get("value_fetch")
        row1_price_1 = value_fetch_price_1.get("row1").get("label")
        row2_price_1 = value_fetch_price_1.get("row2").get("name")
        id_val_price_1 = str(node.get("id")) + "_price_1"
        classes.append(value_fetch_class(row1_price_1, row2_price_1, input_dic_price_1, id_val_price_1))
    if "obj_price_2" in node.get("more"):
        obj_price_2_data = node.get("more").get("obj_price_2")
        input_dic_price_2 = obj_price_2_data.get("input_dic")
        value_fetch_price_2 = obj_price_2_data.get("value_fetch")
        row1_price_2 = value_fetch_price_2.get("row1").get("label")
        row2_price_2 = value_fetch_price_2.get("row2").get("name")
        id_val_price_2 = str(node.get("id")) + "_price_2"
        classes.append(value_fetch_class(row1_price_2, row2_price_2, input_dic_price_2, id_val_price_2))
    if "obj_price_3" in node.get("more"):
        obj_price_3_data = node.get("more").get("obj_price_3")
        input_dic_price_3 = obj_price_3_data.get("input_dic")
        value_fetch_price_3 = obj_price_3_data.get("value_fetch")
        row1_price_3 = value_fetch_price_3.get("row1").get("label")
        row2_price_3 = value_fetch_price_3.get("row2").get("name")
        id_val_price_3 = str(node.get("id")) + "_price_3"
        classes.append(value_fetch_class(row1_price_3, row2_price_3, input_dic_price_3, id_val_price_3))


def draw_button(node):
    obj_text_data = node.get("more").get("obj_text")
    input_dic = obj_text_data.get("input_dic")
    value_fetch = obj_text_data.get("value_fetch")
    row1 = value_fetch.get("row1").get("label")
    row2 = value_fetch.get("row2").get("name")
    id_val = str(node.get("id")) + "_obj_text"
    classes.append(value_fetch_class(row1, row2, input_dic, id_val))


def draw_arrow(node):
    obj_time_1_data = node.get("more").get("obj_time_1")
    input_dic_time_1 = obj_time_1_data.get("input_dic")
    value_fetch_time_1 = obj_time_1_data.get("value_fetch")
    row1_time_1 = value_fetch_time_1.get("row1").get("label")
    row2_time_1 = value_fetch_time_1.get("row2").get("name")
    id_val_time_1 = str(node.get("id")) + "_time_1"
    classes.append(value_fetch_class(row1_time_1, row2_time_1, input_dic_time_1, id_val_time_1))

    obj_price_1_data = node.get("more").get("obj_price_1")
    input_dic_price_1 = obj_price_1_data.get("input_dic")
    value_fetch_price_1 = obj_price_1_data.get("value_fetch")
    row1_price_1 = value_fetch_price_1.get("row1").get("label")
    row2_price_1 = value_fetch_price_1.get("row2").get("name")
    id_val_price_1 = str(node.get("id")) + "_price_1"
    classes.append(value_fetch_class(row1_price_1, row2_price_1, input_dic_price_1, id_val_price_1))


def modify_stops_of_trades(node):
    relative_to_data = node.get("more").get("relative_to")
    if relative_to_data.get("value") == "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL":
        input_dic = relative_to_data.get("input_dic")
        value_fetch = relative_to_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "_rt"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    new_tpsl_mode_data = node.get("more").get("new_tpsl_mode")
    if new_tpsl_mode_data.get("value") == "NEW_STOPS_CUSTOM_PRICE_LEVEL":
        input_dic_tp = new_tpsl_mode_data.get("input_dic_tp")
        value_fetch_tp = new_tpsl_mode_data.get("value_fetch_tp")
        row1_tp = value_fetch_tp.get("row1").get("label")
        row2_tp = value_fetch_tp.get("row2").get("name")
        id_val_tp = str(node.get("id")) + "_ntm_tp"

        input_dic_sl = new_tpsl_mode_data.get("input_dic_sl")
        value_fetch_sl = new_tpsl_mode_data.get("value_fetch_sl")
        row1_sl = value_fetch_sl.get("row1").get("label")
        row2_sl = value_fetch_sl.get("row2").get("name")
        id_val_sl = str(node.get("id")) + "_ntm_sl"

        classes.append(value_fetch_class(row1_tp, row2_tp, input_dic_tp, id_val_tp))
        classes.append(value_fetch_class(row1_sl, row2_sl, input_dic_sl, id_val_sl))


def trailing_pending_orders(node):
    trailing_distance_mode_data = node.get("more").get("trailing_distance_mode")
    trailing_distance_mode = trailing_distance_mode_data.get("value")
    if trailing_distance_mode != "TRAILING_DISTANCE_MODE_FIXED":
        input_dic = trailing_distance_mode_data.get("input_dic")
        value_fetch = trailing_distance_mode_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "_tdmd"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))


def buy_sell(node):
    open_at_price_data = node.get("more").get("open_at_price")
    open_at_price = open_at_price_data.get("value")
    if open_at_price == "OPEN_AT_CUSTOM_PRICE":
        input_dic = open_at_price_data.get("input_dic")
        value_fetch = open_at_price_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "oacp"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))


def comment(node):
    mrow1 = node.get("more").get("row1")
    if mrow1.get("Label").get("value") != "" and "value_fetch" in mrow1:
        input_dic = mrow1.get("input_dic")
        value_fetch = mrow1.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r1"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow2 = node.get("more").get("row2")
    if mrow2.get("Label").get("value") != "" and "value_fetch" in mrow2:
        input_dic = mrow2.get("input_dic")
        value_fetch = mrow2.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r2"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow3 = node.get("more").get("row3")
    if mrow3.get("Label").get("value") != "" and "value_fetch" in mrow3:
        input_dic = mrow3.get("input_dic")
        value_fetch = mrow3.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r3"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow4 = node.get("more").get("row4")
    if mrow4.get("Label").get("value") != "" and "value_fetch" in mrow4:
        input_dic = mrow4.get("input_dic")
        value_fetch = mrow4.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r4"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow5 = node.get("more").get("row5")
    if mrow5.get("Label").get("value") != "" and "value_fetch" in mrow5:
        input_dic = mrow5.get("input_dic")
        value_fetch = mrow5.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r5"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow6 = node.get("more").get("row6")
    if mrow6.get("Label").get("value") != "" and "value_fetch" in mrow6:
        input_dic = mrow6.get("input_dic")
        value_fetch = mrow6.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r6"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow7 = node.get("more").get("row7")
    if mrow7.get("Label").get("value") != "" and "value_fetch" in mrow7:
        input_dic = mrow7.get("input_dic")
        value_fetch = mrow7.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r7"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))

    mrow8 = node.get("more").get("row8")
    if mrow8.get("Label").get("value") != "" and "value_fetch" in mrow8:
        input_dic = mrow8.get("input_dic")
        value_fetch = mrow8.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r8"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))


def trailing_stop_each_trade(node):
    trailing_stop_mode_data = node.get("more").get("TrailingStopMode")
    trailing_stop_mode = trailing_stop_mode_data.get("value")
    if trailing_stop_mode == "TRAILING_STOP_MODE_CUSTOM_LEVEL":
        input_dic = trailing_stop_mode_data.get("input_dic")
        value_fetch = trailing_stop_mode_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "tsm_cl"
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))


def modify_variables(node):
    for item in node.get("items"):
        input_dic = item.get("input_dic")
        value = item.get("value")
        row1 = value.get("row1").get("label")
        row2 = value.get("row2").get("name")
        id_val = str(node.get("id"))
        classes.append(value_fetch_class(row1, row2, input_dic, id_val))


def condition_1_normal_elements(node):
    more = node.get("more")
    # left data
    row1_left = more.get("left1").get("label")
    row2_left = more.get("left2").get("name")
    id_val_left = str(node.get("id")) + "_" + "left"
    input_dic_left = node.get("input_dic_left")
    classes.append(value_fetch_class(row1_left, row2_left, input_dic_left, id_val_left))

    # right data
    row1_right = more.get("right1").get("label")
    row2_right = more.get("right2").get("name")
    id_val_right = str(node.get("id")) + "_" + "right"
    input_dic_right = node.get("input_dic_right")
    classes.append(value_fetch_class(row1_right, row2_right, input_dic_right, id_val_right))


def condition_1_cross_elements(node):
    more = node.get("more")
    # left data
    row1_left = more.get("left1").get("label")
    row2_left = more.get("left2").get("name")
    id_val_left_1 = str(node.get("id")) + "_" + "left1"
    id_val_left_2 = str(node.get("id")) + "_" + "left2"
    input_dic_left_1 = node.get("input_dic_left_1")
    input_dic_left_2 = node.get("input_dic_left_2")
    classes.append(value_fetch_class(row1_left, row2_left, input_dic_left_1, id_val_left_1))
    classes.append(value_fetch_class(row1_left, row2_left, input_dic_left_2, id_val_left_2))

    # right data
    row1_right = more.get("right1").get("label")
    row2_right = more.get("right2").get("name")
    id_val_right_1 = str(node.get("id")) + "_" + "right1"
    id_val_right_2 = str(node.get("id")) + "_" + "right2"
    input_dic_right_1 = node.get("input_dic_right_1")
    input_dic_right_2 = node.get("input_dic_right_2")
    classes.append(value_fetch_class(row1_right, row2_right, input_dic_right_1, id_val_right_1))
    classes.append(value_fetch_class(row1_right, row2_right, input_dic_right_2, id_val_right_2))


def value_fetch_class(row1, row2, input_dic, id_val):
    mclass = ""
    if row1 == "Indicator":
        mclass = indicator_class_constructor.get_class(row2, input_dic, id_val)
    elif row1 == "Candle":
        mclass = candle_class_constructor.get_class(input_dic, id_val)
    elif row1 == "Market Properties":
        mclass = market_properties_class_constructor.get_class(input_dic, id_val)
    elif row1 == "Value":
        mclass = value_class_constructor.get_class(input_dic, id_val)
    return mclass
