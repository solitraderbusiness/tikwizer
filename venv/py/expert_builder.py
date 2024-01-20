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
    blocks_tick_var = global_vars.get__blocks_tick()
    vars_system.append(blocks_tick_var)

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
    for node in nodes:
        task_name = node.get("data").get("blockName")
        match task_name:
            case "pass_n_times":
                if pass_n_times_done: continue
                var_data = task_constructor.get_var_data(task_name)
                variables.append(var_data)
                pass_n_times_done = True
            case "condition_1_normal" | "condition_1_cross":
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

# Elements that are assigned to a specific instance of a specific task type
def add_task_elements_specific(nodes):
    for node in nodes:
        task_name = node.get("data").get("blockName")
        if task_name == "condition_1_normal":
            condition_1_normal_elements(node)
        elif task_name == "condition_1_cross":
            condition_1_cross_elements(node)
        elif task_name == "modify_variables":
            modify_variables(node)


def modify_variables (node):
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
