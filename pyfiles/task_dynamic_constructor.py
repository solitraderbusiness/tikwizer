import json
from . import path_root, adjust
import collections.abc
from . import indicator_class_constructor
from . import candle_class_constructor
from . import market_properties_class_constructor_new
from . import value_class_constructor
from . import object_on_the_chart_class_constructor
from . import trade_order_in_loop_class_constructor
from . import account_class_constructor

path = path_root.get()
path_sub = "/contents/"


def get_task():
    path_task = path + path_sub + "task" + "/"
    class_template = ""
    with open(path_task + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template_dic = json.loads(class_txt)
            class_template = class_template_dic.get("class_template")
    return class_template


def get_task_child(node, constants, variables):
    category = node.get("category")
    task_name = node.get("block_name_mql")
    params = node.get("params")
    class_id = node.get("id_by_user")

    path_task_id_template = path + path_sub + "task_id" + "/"  # used to get template
    path_task_id = path + path_sub + "tasks" + "/" + category + "/" + task_name + "/"  # used to get data and fill template
    # class template
    class_template = class_template_fun(path_task_id_template)
    # class parts
    field_data_static = field_data_static_fun(path_task_id)
    field_data = field_data_dynamic_fun(field_data_static)

    constructor_data_static = constructor_data_static_fun(path_task_id, params, constants, variables)
    constructor_data = constructor_data_dynamic_fun(constructor_data_static)

    run_data_static = run_data_static_fun(path_task_id, params, constants, variables)
    run_data = run_data_dynamic_fun(node, run_data_static)

    reset_data_static = reset_data_static_fun(path_task_id)
    reset_data = reset_data_dynamic_fun(reset_data_static)

    function_data_static = function_data_static_fun(path_task_id)
    function_data = function_data_dynamic_fun(node, function_data_static)

    # class template to class final
    task = class_template \
        .replace("_id", str(class_id), 2) \
        .replace("field_data", field_data) \
        .replace("constructor_data", constructor_data) \
        .replace("run_data", run_data) \
        .replace("run_data", run_data) \
        .replace("reset_data", reset_data) \
        .replace("function_data", function_data)

    return task


def class_template_fun(path_task_id_template):
    with open(path_task_id_template + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template = json.loads(class_txt).get("class_template")
            return class_template
    return ""


def field_data_static_fun(path_task_id):
    with open(path_task_id + "field_data.json") as field_file:
        if field_file:
            field_txt = field_file.read()
            field_data = json.loads(field_txt).get("field_data")
            return field_data
    return ""


def field_data_dynamic_fun(field_data_static):
    return field_data_static


def constructor_data_static_fun(path_task_id, params, constants, variables):
    with open(path_task_id + "constructor_data.json") as constructor_file:
        if constructor_file:
            constructor_text = constructor_file.read()
            constructor_data = json.loads(constructor_text).get("constructor_data")
            constructor_data = replace_input_values(constructor_data, params, constants, variables)
            return constructor_data
    return ""


def constructor_data_dynamic_fun(constructor_data_static):
    return constructor_data_static


def run_data_static_fun(path_task_id, input_dic, constants, variables):
    with open(path_task_id + "run_data.json") as run_file:
        if run_file:
            run_txt = run_file.read()
            run_data = json.loads(run_txt).get("run_data")
            run_data = add_var_reference_if_any(run_data, input_dic, variables)
            run_data = replace_input_values(run_data, input_dic, constants, variables)
            return run_data
    return ""


def run_data_dynamic_fun(node, run_data_static):
    task_name = node.get("block_name_mql")
    run_data = run_data_static
    if task_name == "condition_1_normal":
        run_data = condition_1_run_data_normal(node, run_data_static)
    elif task_name == "condition_1_cross":
        run_data = condition_1_run_data_cross(node, run_data_static)
    elif task_name == "formula":
        run_data = formula(node, run_data_static)
    elif task_name == "modify_variables":
        run_data = modify_variable_run_data(node, run_data_static)
    elif task_name == "spread_filter":
        run_data = spread_filter_run_data(node, run_data_static)
    elif task_name == "trailing_stop_each_trade":
        run_data = trailing_stop_each_trade_run_data(node, run_data_static)
    elif task_name == "comment":
        run_data = comment_run_data(node, run_data_static)
    elif task_name == "trailing_pending_orders":
        run_data = trailing_pending_orders_run_data(node, run_data_static)
    elif task_name == "modify_stops_of_trades":
        run_data = modify_stops_of_trades_run_data(node, run_data_static)
    elif task_name == "draw_arrow":
        run_data = draw_arrow_run_data(node, run_data_static)
    elif task_name == "draw_button":
        run_data = draw_button_run_data(node, run_data_static)
    elif task_name == "draw_shape":
        run_data = draw_shape_run_data(node, run_data_static)
    elif task_name == "draw_line":
        run_data = draw_line_run_data(node, run_data_static)
    elif task_name == "draw_edit_field":
        run_data = draw_editfield_run_data(node, run_data_static)
    elif task_name == "check_trendline_price_level":
        run_data = check_trendline_price_level_run_data(node, run_data_static)
    elif task_name == "no_trade_order_nearby":
        run_data = no_trade_order_nearby_run_data(node, run_data_static)
    return run_data


def reset_data_static_fun(path_task_id):
    with open(path_task_id + "reset_data.json") as reset_file:
        if reset_file:
            reset_txt = reset_file.read()
            reset_data = json.loads(reset_txt).get("reset_data")
            return reset_data
    return ""


def reset_data_dynamic_fun(reset_data_static):
    return reset_data_static


def function_data_static_fun(path_task_id):
    with open(path_task_id + "function_data.json") as function_file:
        if function_file:
            function_txt = function_file.read()
            function_data = json.loads(function_txt).get("function_data")
            return function_data
    return ""


def function_data_dynamic_fun(node, function_data_static):
    task_name = node.get("block_name_mql")
    function_data = function_data_static
    if task_name == "buy_sell":
        function_data = buy_sell_function_data(node, function_data_static)

    return function_data


# In GoldBlox, if user references a class field to a global var,
# then it must get updated with the global var each time block runs.
# Below function adds this feature by calling field assignment each
# time block's run method is called.
def add_var_reference_if_any(data, params, variables):
    if "operator" and "variable" in params:  # This is Formula, don't do anything
        return data
    fix_star = "Task::run(block_id, block);"
    for key, value in params.items():
        if not isinstance(value, dict):  # This is a value_fetch dictionary, I have nothing to do with it here.
            if is_var(value, variables):
                data = data.replace(fix_star, fix_star + "\n" + key + " = ::" + value + ";\n")
    return data


def replace_input_values(data, params, constants, variables):
    for key, value in params.items():
        if isinstance(value, dict):  # This is a value_fetch dictionary, I have nothing to do with it here.
            pass
        else:  # So it's a string (or number or bool)
            data = data.replace(key + "_val", get_proper_value(value, constants, variables))
    return data


def get_proper_value(value, constants, variables):
    if isinstance(value, str):
        if not is_const_var(value, constants, variables):
            return value
        else:  # The value is the name of a constant/variable, so use the global scope
            return "::" + value
    else:
        return str(value)


def is_const_var(value, constants, variables):
    for constant in constants:
        if constant.get("name") == value:
            return True
    for variable in variables:
        if variable.get("name") == value:
            return True
    return False


def is_var(value, variables):
    for variable in variables:
        if variable.get("name") == value:
            return True
    return False


def check_trendline_price_level_run_data(node, function_data_static):
    value_fetch = node.get("params").get("price_level")
    row1 = value_fetch.get("row1")
    row2 = value_fetch.get("row2")
    id_val = str(node.get("id_by_user")) + "_price_level"

    init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
    val = get_value_fetch_val(row1, row2, id_val)
    function_data_static = function_data_static.replace("initializer_price_level", init)
    function_data_static = function_data_static.replace("variable_name_price_level", val)

    return function_data_static


def draw_editfield_run_data(node, function_data_static):
    value_fetch = node.get("params").get("text")
    row1 = value_fetch.get("row1")
    row2 = value_fetch.get("row2")
    id_val = str(node.get("id_by_user")) + "_text"

    init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
    val = get_value_fetch_val(row1, row2, id_val)
    function_data_static = function_data_static.replace("initializer_text", init)
    function_data_static = function_data_static.replace("variable_name_text", val)

    return function_data_static


def draw_line_run_data(node, function_data_static):
    params = node.get("params")
    if "time_1" in params:
        value_fetch_time_1 = params.get("time_1")
        row1_time_1 = value_fetch_time_1.get("row1")
        row2_time_1 = value_fetch_time_1.get("row2")
        id_val_time_1 = str(node.get("id_by_user")) + "_time_1"

        init_time_1 = get_value_fetch_init(row1_time_1, row2_time_1, value_fetch_time_1.get("params"), id_val_time_1)
        val_time_1 = get_value_fetch_val(row1_time_1, row2_time_1, id_val_time_1)
        function_data_static = function_data_static.replace("initializer_time_1", init_time_1)
        function_data_static = function_data_static.replace("variable_name_time_1", val_time_1)
    else:
        function_data_static = function_data_static.replace("initializer_time_1", "")
        function_data_static = function_data_static.replace("variable_name_time_1", "\"\"")
    if "time_2" in params:
        value_fetch_time_2 = params.get("time_2")
        row1_time_2 = value_fetch_time_2.get("row1")
        row2_time_2 = value_fetch_time_2.get("row2")
        id_val_time_2 = str(node.get("id_by_user")) + "_time_2"

        init_time_2 = get_value_fetch_init(row1_time_2, row2_time_2, value_fetch_time_2.get("params"), id_val_time_2)
        val_time_2 = get_value_fetch_val(row1_time_2, row2_time_2, id_val_time_2)
        function_data_static = function_data_static.replace("initializer_time_2", init_time_2)
        function_data_static = function_data_static.replace("variable_name_time_2", val_time_2)
    else:
        function_data_static = function_data_static.replace("initializer_time_2", "")
        function_data_static = function_data_static.replace("variable_name_time_2", "\"\"")

    if "price_1" in params:
        value_fetch_price_1 = params.get("price_1")
        row1_price_1 = value_fetch_price_1.get("row1")
        row2_price_1 = value_fetch_price_1.get("row2")
        id_val_price_1 = str(node.get("id_by_user")) + "_price_1"

        init_price_1 = get_value_fetch_init(row1_price_1, row2_price_1, value_fetch_price_1.get("params"), id_val_price_1)
        val_price_1 = get_value_fetch_val(row1_price_1, row2_price_1, id_val_price_1)
        function_data_static = function_data_static.replace("initializer_price_1", init_price_1)
        function_data_static = function_data_static.replace("variable_name_price_1", val_price_1)
    else:
        function_data_static = function_data_static.replace("initializer_price_1", "")
        function_data_static = function_data_static.replace("variable_name_price_1", "\"\"")

    if "price_2" in params:
        value_fetch_price_2 = params.get("price_2")
        row1_price_2 = value_fetch_price_2.get("row1")
        row2_price_2 = value_fetch_price_2.get("row2")
        id_val_price_2 = str(node.get("id_by_user")) + "_price_2"

        init_price_2 = get_value_fetch_init(row1_price_2, row2_price_2, value_fetch_price_2.get("params"), id_val_price_2)
        val_price_2 = get_value_fetch_val(row1_price_2, row2_price_2, id_val_price_2)
        function_data_static = function_data_static.replace("initializer_price_2", init_price_2)
        function_data_static = function_data_static.replace("variable_name_price_2", val_price_2)
    else:
        function_data_static = function_data_static.replace("initializer_price_2", "")
        function_data_static = function_data_static.replace("variable_name_price_2", "\"\"")

    return function_data_static


def draw_shape_run_data(node, function_data_static):
    if "time_1" in node.get("params"):
        value_fetch_time_1 = node.get("params").get("time_1")
        row1_time_1 = value_fetch_time_1.get("row1")
        row2_time_1 = value_fetch_time_1.get("row2")
        id_val_time_1 = str(node.get("id_by_user")) + "_time_1"

        init_time_1 = get_value_fetch_init(row1_time_1, row2_time_1, value_fetch_time_1.get("params"), id_val_time_1)
        val_time_1 = get_value_fetch_val(row1_time_1, row2_time_1, id_val_time_1)
        function_data_static = function_data_static.replace("initializer_time_1", init_time_1)
        function_data_static = function_data_static.replace("variable_name_time_1", val_time_1)
    else:
        function_data_static = function_data_static.replace("initializer_time_1", "")
        function_data_static = function_data_static.replace("variable_name_time_1", "\"\"")
    if "time_2" in node.get("params"):
        value_fetch_time_2 = node.get("params").get("time_2")
        row1_time_2 = value_fetch_time_2.get("row1")
        row2_time_2 = value_fetch_time_2.get("row2")
        id_val_time_2 = str(node.get("id_by_user")) + "_time_2"

        init_time_2 = get_value_fetch_init(row1_time_2, row2_time_2, value_fetch_time_2.get("params"), id_val_time_2)
        val_time_2 = get_value_fetch_val(row1_time_2, row2_time_2, id_val_time_2)
        function_data_static = function_data_static.replace("initializer_time_2", init_time_2)
        function_data_static = function_data_static.replace("variable_name_time_2", val_time_2)
    else:
        function_data_static = function_data_static.replace("initializer_time_2", "")
        function_data_static = function_data_static.replace("variable_name_time_2", "\"\"")
    if "time_3" in node.get("params"):
        value_fetch_time_3 = node.get("params").get("time_3")
        row1_time_3 = value_fetch_time_3.get("row1")
        row2_time_3 = value_fetch_time_3.get("row2")
        id_val_time_3 = str(node.get("id_by_user")) + "_time_3"

        init_time_3 = get_value_fetch_init(row1_time_3, row2_time_3, value_fetch_time_3.get("params"), id_val_time_3)
        val_time_3 = get_value_fetch_val(row1_time_3, row2_time_3, id_val_time_3)
        function_data_static = function_data_static.replace("initializer_time_3", init_time_3)
        function_data_static = function_data_static.replace("variable_name_time_3", val_time_3)
    else:
        function_data_static = function_data_static.replace("initializer_time_3", "")
        function_data_static = function_data_static.replace("variable_name_time_3", "\"\"")
    if "price_1" in node.get("params"):
        value_fetch_price_1 = node.get("params").get("price_1")
        row1_price_1 = value_fetch_price_1.get("row1")
        row2_price_1 = value_fetch_price_1.get("row2")
        id_val_price_1 = str(node.get("id_by_user")) + "_price_1"

        init_price_1 = get_value_fetch_init(row1_price_1, row2_price_1, value_fetch_price_1.get("params"), id_val_price_1)
        val_price_1 = get_value_fetch_val(row1_price_1, row2_price_1, id_val_price_1)
        function_data_static = function_data_static.replace("initializer_price_1", init_price_1)
        function_data_static = function_data_static.replace("variable_name_price_1", val_price_1)
    else:
        function_data_static = function_data_static.replace("initializer_price_1", "")
        function_data_static = function_data_static.replace("variable_name_price_1", "\"\"")
    if "price_2" in node.get("params"):
        value_fetch_price_2 = node.get("params").get("price_2")
        row1_price_2 = value_fetch_price_2.get("row1")
        row2_price_2 = value_fetch_price_2.get("row2")
        id_val_price_2 = str(node.get("id_by_user")) + "_price_2"

        init_price_2 = get_value_fetch_init(row1_price_2, row2_price_2, value_fetch_price_2.get("params"), id_val_price_2)
        val_price_2 = get_value_fetch_val(row1_price_2, row2_price_2, id_val_price_2)
        function_data_static = function_data_static.replace("initializer_price_2", init_price_2)
        function_data_static = function_data_static.replace("variable_name_price_2", val_price_2)
    else:
        function_data_static = function_data_static.replace("initializer_price_2", "")
        function_data_static = function_data_static.replace("variable_name_price_2", "\"\"")
    if "price_3" in node.get("params"):
        value_fetch_price_3 = node.get("params").get("price_3")
        row1_price_3 = value_fetch_price_3.get("row1")
        row2_price_3 = value_fetch_price_3.get("row2")
        id_val_price_3 = str(node.get("id_by_user")) + "_price_3"

        init_price_3 = get_value_fetch_init(row1_price_3, row2_price_3, value_fetch_price_3.get("params"), id_val_price_3)
        val_price_3 = get_value_fetch_val(row1_price_3, row2_price_3, id_val_price_3)
        function_data_static = function_data_static.replace("initializer_price_3", init_price_3)
        function_data_static = function_data_static.replace("variable_name_price_3", val_price_3)
    else:
        function_data_static = function_data_static.replace("initializer_price_3", "")
        function_data_static = function_data_static.replace("variable_name_price_3", "\"\"")

    return function_data_static


def draw_button_run_data(node, function_data_static):
    value_fetch = node.get("params").get("text")
    row1 = value_fetch.get("row1")
    row2 = value_fetch.get("row2")
    id_val = str(node.get("id_by_user")) + "_obj_text"

    init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
    val = get_value_fetch_val(row1, row2, id_val)
    function_data_static = function_data_static.replace("initializer_obj_text", init)
    function_data_static = function_data_static.replace("variable_name_obj_text", val)

    return function_data_static


def draw_arrow_run_data(node, function_data_static):
    value_fetch_time_1 = node.get("params").get("time_1")
    row1_time_1 = value_fetch_time_1.get("row1")
    row2_time_1 = value_fetch_time_1.get("row2")
    id_val_time_1 = str(node.get("id_by_user")) + "_time_1"

    init_time_1 = get_value_fetch_init(row1_time_1, row2_time_1, value_fetch_time_1.get("params"), id_val_time_1)
    val_time_1 = get_value_fetch_val(row1_time_1, row2_time_1, id_val_time_1)
    function_data_static = function_data_static.replace("initializer_time_1", init_time_1)
    function_data_static = function_data_static.replace("variable_name_time_1", val_time_1)

    value_fetch_price_1 = node.get("params").get("price_1")
    row1_price_1 = value_fetch_price_1.get("row1")
    row2_price_1 = value_fetch_price_1.get("row2")
    id_val_price_1 = str(node.get("id_by_user")) + "_price_1"

    init_price_1 = get_value_fetch_init(row1_price_1, row2_price_1, value_fetch_price_1.get("params"), id_val_price_1)
    val_price_1 = get_value_fetch_val(row1_price_1, row2_price_1, id_val_price_1)
    function_data_static = function_data_static.replace("initializer_price_1", init_price_1)
    function_data_static = function_data_static.replace("variable_name_price_1", val_price_1)

    return function_data_static


def modify_stops_of_trades_run_data(node, function_data_static):
    params = node.get("params")
    if params.get("relative_to") == "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL":
        value_fetch = params.get("value_fetch_relative_to")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "_rt"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        function_data_static = function_data_static.replace("initializer_rt", init)
        function_data_static = function_data_static.replace("variable_name_rt", val)
    else:
        function_data_static = function_data_static.replace("initializer_rt", "")
        function_data_static = function_data_static.replace("variable_name_rt", "\"\"")

    if params.get("new_tpsl_mode") == "NEW_STOPS_CUSTOM_PRICE_LEVEL":
        value_fetch_tp = params.get("new_take_profit_level")
        row1_tp = value_fetch_tp.get("row1")
        row2_tp = value_fetch_tp.get("row2")
        id_val_tp = str(node.get("id_by_user")) + "_ntm_tp"

        init_tp = get_value_fetch_init(row1_tp, row2_tp, value_fetch_tp.get("params"), id_val_tp)
        val_tp = get_value_fetch_val(row1_tp, row2_tp, id_val_tp)

        value_fetch_sl = params.get("new_stop_loss_level")
        row1_sl = value_fetch_sl.get("row1")
        row2_sl = value_fetch_sl.get("row2")
        id_val_sl = str(node.get("id_by_user")) + "_ntm_sl"

        init_sl = get_value_fetch_init(row1_sl, row2_sl, value_fetch_sl.get("params"), id_val_sl)
        val_sl = get_value_fetch_val(row1_sl, row2_sl, id_val_sl)

        function_data_static = function_data_static.replace("initializer_ntm_tp", init_tp)
        function_data_static = function_data_static.replace("variable_name_ntm_tp", val_tp)

        function_data_static = function_data_static.replace("initializer_ntm_sl", init_sl)
        function_data_static = function_data_static.replace("variable_name_ntm_sl", val_sl)
    else:
        function_data_static = function_data_static.replace("initializer_ntm_tp", "")
        function_data_static = function_data_static.replace("variable_name_ntm_tp", "\"\"")

        function_data_static = function_data_static.replace("initializer_ntm_sl", "")
        function_data_static = function_data_static.replace("variable_name_ntm_sl", "\"\"")

    return function_data_static


def buy_sell_function_data(node, function_data_static):
    params = node.get("params")
    if params.get("open_at_price") == "OPEN_AT_CUSTOM_PRICE":
        value_fetch = params.get("price_to_open_dynamic_level")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "oacp"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        function_data_static = function_data_static.replace("initializer_oacp", init)
        function_data_static = function_data_static.replace("variable_name_oacp", val)
    else:
        function_data_static = function_data_static.replace("initializer_oacp", "")
        function_data_static = function_data_static.replace("variable_name_oacp", "\"\"")

    return function_data_static


def spread_filter_run_data(node, run_data):
    run_data = run_data.replace("operator_val", node.get("params").get("operator"))
    return run_data


def comment_run_data(node, run_data):
    params = node.get("params")
    if params.get("label_1") != "\"\"" and "value_fetch_1" in params:
        value_fetch = params.get("value_fetch_1")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r1"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_1", init)
        run_data = run_data.replace("variable_name_1", val)
    else:
        run_data = run_data.replace("initializer_1", "")
        run_data = run_data.replace("variable_name_1", "\"\"")

    if params.get("label_2") != "\"\"" and "value_fetch_2" in params:
        value_fetch = params.get("value_fetch_2")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r2"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_2", init)
        run_data = run_data.replace("variable_name_2", val)
    else:
        run_data = run_data.replace("initializer_2", "")
        run_data = run_data.replace("variable_name_2", "\"\"")

    if params.get("label_3") != "\"\"" and "value_fetch_3" in params:
        value_fetch = params.get("value_fetch_3")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r3"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_3", init)
        run_data = run_data.replace("variable_name_3", val)
    else:
        run_data = run_data.replace("initializer_3", "")
        run_data = run_data.replace("variable_name_3", "\"\"")

    if params.get("label_4") != "\"\"" and "value_fetch_4" in params:
        value_fetch = params.get("value_fetch_4")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r4"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_4", init)
        run_data = run_data.replace("variable_name_4", val)
    else:
        run_data = run_data.replace("initializer_4", "")
        run_data = run_data.replace("variable_name_4", "\"\"")

    if params.get("label_5") != "\"\"" and "value_fetch_5" in params:
        value_fetch = params.get("value_fetch_5")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r5"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_5", init)
        run_data = run_data.replace("variable_name_5", val)
    else:
        run_data = run_data.replace("initializer_5", "")
        run_data = run_data.replace("variable_name_5", "\"\"")

    if params.get("label_6") != "\"\"" and "value_fetch_6" in params:
        value_fetch = params.get("value_fetch_6")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r6"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_6", init)
        run_data = run_data.replace("variable_name_6", val)
    else:
        run_data = run_data.replace("initializer_6", "")
        run_data = run_data.replace("variable_name_6", "\"\"")

    if params.get("label_7") != "\"\"" and "value_fetch_7" in params:
        value_fetch = params.get("value_fetch_7")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r7"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_7", init)
        run_data = run_data.replace("variable_name_7", val)
    else:
        run_data = run_data.replace("initializer_7", "")
        run_data = run_data.replace("variable_name_7", "\"\"")

    if params.get("label_8") != "\"\"" and "value_fetch_8" in params:
        value_fetch = params.get("value_fetch_8")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "cm_r8"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_8", init)
        run_data = run_data.replace("variable_name_8", val)
    else:
        run_data = run_data.replace("initializer_8", "")
        run_data = run_data.replace("variable_name_8", "\"\"")

    return run_data


def trailing_pending_orders_run_data(node, run_data):
    params = node.get("params")
    trailing_distance_mode = params.get("trailing_distance_mode")
    if trailing_distance_mode != "TRAILING_DISTANCE_MODE_FIXED":
        key = ""
        if trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC":
            key = "dynamic_level"
        elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_PIPS":
            key = "dynamic_size_pips_input"
        elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS":
            key = "dynamic_size_digits_input"
        value_fetch = params.get(key)
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "_tdmd"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)

        if trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC":
            run_data = run_data.replace("initializer_dynamic", init, 1)
            run_data = run_data.replace("variable_name_dynamic", val, 1)
            run_data = run_data.replace("initializer_dynamic_pips", "")
            run_data = run_data.replace("variable_name_dynamic_pips", "\"\"")
            run_data = run_data.replace("initializer_dynamic_digits", "")
            run_data = run_data.replace("variable_name_dynamic_digits", "\"\"")

        elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_PIPS":
            run_data = run_data.replace("initializer_dynamic", "", 1)
            run_data = run_data.replace("variable_name_dynamic", "0", 1)
            run_data = run_data.replace("initializer_dynamic_pips", init)
            run_data = run_data.replace("variable_name_dynamic_pips", val)
            run_data = run_data.replace("initializer_dynamic_digits", "")
            run_data = run_data.replace("variable_name_dynamic_digits", "\"\"")

        elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS":
            run_data = run_data.replace("initializer_dynamic", "", 1)
            run_data = run_data.replace("variable_name_dynamic", "0", 1)
            run_data = run_data.replace("initializer_dynamic_pips", "")
            run_data = run_data.replace("variable_name_dynamic_pips", "\"\"")
            run_data = run_data.replace("initializer_dynamic_digits", init)
            run_data = run_data.replace("variable_name_dynamic_digits", val)

    else:
        run_data = run_data.replace("initializer_dynamic", "", 1)
        run_data = run_data.replace("variable_name_dynamic", "0", 1)
        run_data = run_data.replace("initializer_dynamic_pips", "")
        run_data = run_data.replace("variable_name_dynamic_pips", "\"\"")
        run_data = run_data.replace("initializer_dynamic_digits", "")
        run_data = run_data.replace("variable_name_dynamic_digits", "\"\"")
    return run_data


def trailing_stop_each_trade_run_data(node, run_data):
    params = node.get("params")
    print(params.get("TrailingStopMode"))
    if params.get("TrailingStopMode") == "TRAILING_STOP_MODE_CUSTOM_LEVEL":
        value_fetch = params.get("value_fetch_trailingstopmode_custom_level")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        id_val = str(node.get("id_by_user")) + "tsm_cl"

        init = get_value_fetch_init(row1, row2, value_fetch.get("params"), id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_trailing_stop_mode", init)
        run_data = run_data.replace("variable_name_trailing_stop_mode", val)
    else:
        run_data = run_data.replace("initializer_trailing_stop_mode", "")
        run_data = run_data.replace("variable_name_trailing_stop_mode", "\"\"")
    return run_data


def no_trade_order_nearby_run_data(node, run_data):
    params = node.get("params")
    if params.get("mode_base_price") != "\"current\"":
        value_fetch_price = params.get("price")
        row1_price = value_fetch_price.get("row1")
        row2_price = value_fetch_price.get("row2")
        id_val_price = str(node.get("id_by_user")) + "_price"

        init_price = get_value_fetch_init(row1_price, row2_price, value_fetch_price.get("params"), id_val_price)
        val_price = get_value_fetch_val(row1_price, row2_price, id_val_price)
        run_data = run_data.replace("initializer_price", init_price)
        run_data = run_data.replace("variable_name_price", val_price)
    else:
        run_data = run_data.replace("initializer_price", "")
        run_data = run_data.replace("variable_name_price", "\"\"")

    value_fetch_t1 = params.get("time_1")
    row1_t1 = value_fetch_t1.get("row1")
    row2_t1 = value_fetch_t1.get("row2")
    id_val_t1 = str(node.get("id_by_user")) + "_t1"

    init_t1 = get_value_fetch_init(row1_t1, row2_t1, value_fetch_t1.get("params"), id_val_t1)
    val_t1 = get_value_fetch_val(row1_t1, row2_t1, id_val_t1)
    run_data = run_data.replace("initializer_t1", init_t1)
    run_data = run_data.replace("variable_name_t1", val_t1)

    value_fetch_t2 = params.get("time_2")
    row1_t2 = value_fetch_t2.get("row1")
    row2_t2 = value_fetch_t2.get("row2")
    id_val_t2 = str(node.get("id_by_user")) + "_t2"

    init_t2 = get_value_fetch_init(row1_t2, row2_t2, value_fetch_t2.get("params"), id_val_t2)
    val_t2 = get_value_fetch_val(row1_t2, row2_t2, id_val_t2)
    run_data = run_data.replace("initializer_t2", init_t2)
    run_data = run_data.replace("variable_name_t2", val_t2)

    return run_data


def modify_variable_run_data(node, run_data):
    modify_variables = ""
    i = 0
    for key, val in node.get("params").items():
        i += 1
        if not val.get("variable_name"):
            continue
        row1 = val.get("value_fetch").get("row1")
        row2 = val.get("value_fetch").get("row2")
        id_val = str(node.get("id_by_user")) + "_var_" + str(i)

        init = get_value_fetch_init(row1, row2, val.get("value_fetch").get("params"), id_val)
        mval = get_value_fetch_val(row1, row2, id_val)
        modify_variables += init + "\n"
        modify_variables += val.get("variable_name") + " = " + mval + ";\n\n"
    run_data = run_data.replace("modify_variables", modify_variables)
    return run_data


def formula(node, run_data):
    params = node.get("params")

    # Left data
    row1_left = params.get("left").get("row1")
    row2_left = params.get("left").get("row2")
    id_val_1 = str(node.get("id_by_user")) + "_" + "left"

    init_1 = get_value_fetch_init(row1_left, row2_left, params.get("left").get("params"), id_val_1)
    val_1 = get_value_fetch_val(row1_left, row2_left, id_val_1)

    # Right data
    row1_right = params.get("right").get("row1")
    row2_right = params.get("right").get("row2")
    id_val_2 = str(node.get("id_by_user")) + "_" + "right"

    init_2 = get_value_fetch_init(row1_right, row2_right, params.get("right").get("params"), id_val_2)
    val_2 = get_value_fetch_val(row1_right, row2_right, id_val_2)

    operator = params.get("operator").get("label")

    variable_name = params.get("variable")

    adjustment = adjust.get("(var_name_1 operator var_name_2)", params.get("adjust"), "getSymbol(Symbol())")
    run_data = run_data.replace("(var_name_1 operator var_name_2)", adjustment)

    run_data = run_data.replace("initializer_1", init_1) \
        .replace("initializer_2", init_2) \
        .replace("var_name_1", str(val_1)) \
        .replace("var_name_2", str(val_2)) \
        .replace("variable_name", variable_name) \
        .replace("operator", operator)
    return run_data


def condition_1_run_data_normal(node, run_data):
    params = node.get("params")

    # Left data
    row1_left = params.get("left").get("row1")
    row2_left = params.get("left").get("row2")
    id_val_1 = str(node.get("id_by_user")) + "_" + "left"

    init_1 = get_value_fetch_init(row1_left, row2_left, params.get("left").get("params"), id_val_1)
    val_1 = get_value_fetch_val(row1_left, row2_left, id_val_1)

    # Right data
    row1_right = params.get("right").get("row1")
    row2_right = params.get("right").get("row2")
    id_val_2 = str(node.get("id_by_user")) + "_" + "right"

    init_2 = get_value_fetch_init(row1_right, row2_right, params.get("right").get("params"), id_val_2)
    val_2 = get_value_fetch_val(row1_right, row2_right, id_val_2)

    operator = params.get("operator").get("label")

    run_data = run_data.replace("initializer_1", init_1) \
        .replace("initializer_2", init_2) \
        .replace("var_name_1", str(val_1)) \
        .replace("var_name_2", str(val_2)) \
        .replace("operator", operator)
    return run_data


def condition_1_run_data_cross(node, run_data):
    params = node.get("params")

    # Left data
    row1_left = params.get("left").get("row1")
    row2_left = params.get("left").get("row2")
    id_val_11 = str(node.get("id_by_user")) + "_" + "left" + "1"
    id_val_12 = str(node.get("id_by_user")) + "_" + "left" + "2"

    init11 = get_value_fetch_init(row1_left, row2_left, params.get("left").get("params"), id_val_11)
    init12 = get_value_fetch_init(row1_left, row2_left, params.get("left").get("params"), id_val_12)
    val_11 = get_value_fetch_val(row1_left, row2_left, id_val_11)
    val_12 = get_value_fetch_val(row1_left, row2_left, id_val_12)

    # Right data
    row1_right = params.get("right").get("row1")
    row2_right = params.get("right").get("row2")
    id_val_21 = str(node.get("id_by_user")) + "_" + "right" + "1"
    id_val_22 = str(node.get("id_by_user")) + "_" + "right" + "2"

    init21 = get_value_fetch_init(row1_right, row2_right, params.get("right").get("params"), id_val_21)
    init22 = get_value_fetch_init(row1_right, row2_right, params.get("right").get("params"), id_val_22)
    val_21 = get_value_fetch_val(row1_right, row2_right, id_val_21)
    val_22 = get_value_fetch_val(row1_right, row2_right, id_val_22)

    # Operator
    operator_1 = ""
    operator_2 = ""
    operator = node.get("params").get("operator").get("label")
    if operator == "×>":
        operator_1 = ">"
        operator_2 = "<"
    elif operator == "×<":
        operator_1 = "<"
        operator_2 = ">"

    run_data = run_data \
        .replace("initializer_11", init11) \
        .replace("initializer_12", init12) \
        .replace("initializer_21", init21) \
        .replace("initializer_22", init22) \
        .replace("var_name_11", str(val_11)) \
        .replace("var_name_12", str(val_12)) \
        .replace("var_name_21", str(val_21)) \
        .replace("var_name_22", str(val_22)) \
        .replace("operator_1", operator_1) \
        .replace("operator_2", operator_2)

    return run_data


def get_value_fetch_init(row1, row2, params, suffix):
    if row1 == "indicator":
        init = indicator_class_constructor.get_initializer(row2, suffix)
    elif row1 == "candle":
        init = candle_class_constructor.get_initializer(suffix)
    elif row1 == "market-properties":
        init = market_properties_class_constructor_new.get_initializer(row2, params, suffix)
    elif row1 == "value":
        init = value_class_constructor.get_initializer(row2, suffix)
    elif row1 == "object-on-the-chart":
        init = object_on_the_chart_class_constructor.get_initializer(row2, suffix)
    elif row1 == "trade-order-in-loop":
        init = trade_order_in_loop_class_constructor.get_initializer(row2, suffix)
    elif row1 == "account":
        init = account_class_constructor.get_initializer(row2, suffix)
    return init


def get_value_fetch_val(row1, row2, suffix):
    val = ""
    if row1 == "indicator":
        val = indicator_class_constructor.get_var_name(row2, suffix)
    elif row1 == "candle":
        val = candle_class_constructor.get_var_name(suffix)
    elif row1 == "market-properties":
        val = market_properties_class_constructor_new.get_var_name(row2, suffix)
    elif row1 == "value":
        val = value_class_constructor.get_var_name(suffix)
    elif row1 == "object-on-the-chart":
        val = object_on_the_chart_class_constructor.get_var_name(row2, suffix)
    elif row1 == "trade-order-in-loop":
        val = trade_order_in_loop_class_constructor.get_var_name(suffix)
    elif row1 == "account":
        val = account_class_constructor.get_var_name(suffix)
    return val


def get_initializer(var_id):
    path_task_id = path + path_sub + "task_id" + "/"
    with open(path_task_id + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_body = initializer_dic.get("initializer").replace("_id", str(var_id))
            return initializer_body


def get_var_name():
    path_task_id = path + path_sub + "task_id" + "/"
    with open(path_task_id + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            var_name = initializer_dic.get("variable_name")
            return var_name


def get_var_data(category, task_name):
    path_task_id = path + path_sub + "tasks" + "/" + category + "/" + task_name + "/"
    with open(path_task_id + "var_data.json") as var_file:
        if var_file:
            var_str = var_file.read()
            var_dic = json.loads(var_str)
            var_data = var_dic.get("var_data")
            return var_data
