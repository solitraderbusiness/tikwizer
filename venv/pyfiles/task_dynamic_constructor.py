import json
from . import path_root
import collections.abc
from . import indicator_class_constructor
from . import candle_class_constructor
from . import market_properties_class_constructor
from . import value_class_constructor

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


def get_task_child(node):
    category = node.get("category")
    task_name = node.get("data").get("blockName")
    input_dic = node.get("input_dic_task")
    class_id = node.get("id")

    path_task_id_template = path + path_sub + "task_id" + "/"  # used to get template
    path_task_id = path + path_sub + "tasks" + "/" + category + "/" + task_name + "/"  # used to get data and fill template
    # class template
    class_template = class_template_fun(path_task_id_template)
    # class parts
    field_data_static = field_data_static_fun(path_task_id)
    field_data = field_data_dynamic_fun(field_data_static)

    constructor_data_static = constructor_data_static_fun(path_task_id, input_dic)
    constructor_data = constructor_data_dynamic_fun(constructor_data_static)

    run_data_static = run_data_static_fun(path_task_id, input_dic)
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


def constructor_data_static_fun(path_task_id, input_dic):
    with open(path_task_id + "constructor_data.json") as constructor_file:
        if constructor_file:
            constructor_text = constructor_file.read()
            constructor_data = json.loads(constructor_text).get("constructor_data")
            constructor_data = replace_input_values(constructor_data, input_dic)
            return constructor_data
    return ""


def constructor_data_dynamic_fun(constructor_data_static):
    return constructor_data_static


def run_data_static_fun(path_task_id, input_dic):
    with open(path_task_id + "run_data.json") as run_file:
        if run_file:
            run_txt = run_file.read()
            run_data = json.loads(run_txt).get("run_data")
            run_data = replace_input_values(run_data, input_dic)
            return run_data
    return ""


def run_data_dynamic_fun(node, run_data_static):
    task_name = node.get("data").get("blockName")
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
    task_name = node.get("data").get("blockName")
    function_data = function_data_static
    if task_name == "buy_sell":
        function_data = buy_sell_function_data(node, function_data_static)

    return function_data


def draw_line_run_data(node, function_data_static):
    if "obj_time_1" in node.get("more"):
        obj_time_1_data = node.get("more").get("obj_time_1")
        value_fetch_time_1 = obj_time_1_data.get("value_fetch")
        row1_time_1 = value_fetch_time_1.get("row1").get("label")
        row2_time_1 = value_fetch_time_1.get("row2").get("name")
        id_val_time_1 = str(node.get("id")) + "_time_1"

        init_time_1 = get_value_fetch_init(row1_time_1, row2_time_1, id_val_time_1)
        val_time_1 = get_value_fetch_val(row1_time_1, row2_time_1, id_val_time_1)
        function_data_static = function_data_static.replace("initializer_time_1", init_time_1)
        function_data_static = function_data_static.replace("variable_name_time_1", val_time_1)
    else:
        function_data_static = function_data_static.replace("initializer_time_1", "")
        function_data_static = function_data_static.replace("variable_name_time_1", "\"\"")
    if "obj_time_2" in node.get("more"):
        obj_time_2_data = node.get("more").get("obj_time_2")
        value_fetch_time_2 = obj_time_2_data.get("value_fetch")
        row1_time_2 = value_fetch_time_2.get("row1").get("label")
        row2_time_2 = value_fetch_time_2.get("row2").get("name")
        id_val_time_2 = str(node.get("id")) + "_time_2"

        init_time_2 = get_value_fetch_init(row1_time_2, row2_time_2, id_val_time_2)
        val_time_2 = get_value_fetch_val(row1_time_2, row2_time_2, id_val_time_2)
        function_data_static = function_data_static.replace("initializer_time_2", init_time_2)
        function_data_static = function_data_static.replace("variable_name_time_2", val_time_2)
    else:
        function_data_static = function_data_static.replace("initializer_time_2", "")
        function_data_static = function_data_static.replace("variable_name_time_2", "\"\"")

    if "obj_price_1" in node.get("more"):
        obj_price_1_data = node.get("more").get("obj_price_1")
        value_fetch_price_1 = obj_price_1_data.get("value_fetch")
        row1_price_1 = value_fetch_price_1.get("row1").get("label")
        row2_price_1 = value_fetch_price_1.get("row2").get("name")
        id_val_price_1 = str(node.get("id")) + "_price_1"

        init_price_1 = get_value_fetch_init(row1_price_1, row2_price_1, id_val_price_1)
        val_price_1 = get_value_fetch_val(row1_price_1, row2_price_1, id_val_price_1)
        function_data_static = function_data_static.replace("initializer_price_1", init_price_1)
        function_data_static = function_data_static.replace("variable_name_price_1", val_price_1)
    else:
        function_data_static = function_data_static.replace("initializer_price_1", "")
        function_data_static = function_data_static.replace("variable_name_price_1", "\"\"")
    if "obj_price_2" in node.get("more"):
        obj_price_2_data = node.get("more").get("obj_price_2")
        value_fetch_price_2 = obj_price_2_data.get("value_fetch")
        row1_price_2 = value_fetch_price_2.get("row1").get("label")
        row2_price_2 = value_fetch_price_2.get("row2").get("name")
        id_val_price_2 = str(node.get("id")) + "_price_2"

        init_price_2 = get_value_fetch_init(row1_price_2, row2_price_2, id_val_price_2)
        val_price_2 = get_value_fetch_val(row1_price_2, row2_price_2, id_val_price_2)
        function_data_static = function_data_static.replace("initializer_price_2", init_price_2)
        function_data_static = function_data_static.replace("variable_name_price_2", val_price_2)
    else:
        function_data_static = function_data_static.replace("initializer_price_2", "")
        function_data_static = function_data_static.replace("variable_name_price_2", "\"\"")

    return function_data_static

def draw_shape_run_data(node, function_data_static):
    if "obj_time_1" in node.get("more"):
        obj_time_1_data = node.get("more").get("obj_time_1")
        value_fetch_time_1 = obj_time_1_data.get("value_fetch")
        row1_time_1 = value_fetch_time_1.get("row1").get("label")
        row2_time_1 = value_fetch_time_1.get("row2").get("name")
        id_val_time_1 = str(node.get("id")) + "_time_1"

        init_time_1 = get_value_fetch_init(row1_time_1, row2_time_1, id_val_time_1)
        val_time_1 = get_value_fetch_val(row1_time_1, row2_time_1, id_val_time_1)
        function_data_static = function_data_static.replace("initializer_time_1", init_time_1)
        function_data_static = function_data_static.replace("variable_name_time_1", val_time_1)
    else:
        function_data_static = function_data_static.replace("initializer_time_1", "")
        function_data_static = function_data_static.replace("variable_name_time_1", "\"\"")
    if "obj_time_2" in node.get("more"):
        obj_time_2_data = node.get("more").get("obj_time_2")
        value_fetch_time_2 = obj_time_2_data.get("value_fetch")
        row1_time_2 = value_fetch_time_2.get("row1").get("label")
        row2_time_2 = value_fetch_time_2.get("row2").get("name")
        id_val_time_2 = str(node.get("id")) + "_time_2"

        init_time_2 = get_value_fetch_init(row1_time_2, row2_time_2, id_val_time_2)
        val_time_2 = get_value_fetch_val(row1_time_2, row2_time_2, id_val_time_2)
        function_data_static = function_data_static.replace("initializer_time_2", init_time_2)
        function_data_static = function_data_static.replace("variable_name_time_2", val_time_2)
    else:
        function_data_static = function_data_static.replace("initializer_time_2", "")
        function_data_static = function_data_static.replace("variable_name_time_2", "\"\"")
    if "obj_time_3" in node.get("more"):
        obj_time_3_data = node.get("more").get("obj_time_3")
        value_fetch_time_3 = obj_time_3_data.get("value_fetch")
        row1_time_3 = value_fetch_time_3.get("row1").get("label")
        row2_time_3 = value_fetch_time_3.get("row2").get("name")
        id_val_time_3 = str(node.get("id")) + "_time_3"

        init_time_3 = get_value_fetch_init(row1_time_3, row2_time_3, id_val_time_3)
        val_time_3 = get_value_fetch_val(row1_time_3, row2_time_3, id_val_time_3)
        function_data_static = function_data_static.replace("initializer_time_3", init_time_3)
        function_data_static = function_data_static.replace("variable_name_time_3", val_time_3)
    else:
        function_data_static = function_data_static.replace("initializer_time_3", "")
        function_data_static = function_data_static.replace("variable_name_time_3", "\"\"")
    if "obj_price_1" in node.get("more"):
        obj_price_1_data = node.get("more").get("obj_price_1")
        value_fetch_price_1 = obj_price_1_data.get("value_fetch")
        row1_price_1 = value_fetch_price_1.get("row1").get("label")
        row2_price_1 = value_fetch_price_1.get("row2").get("name")
        id_val_price_1 = str(node.get("id")) + "_price_1"

        init_price_1 = get_value_fetch_init(row1_price_1, row2_price_1, id_val_price_1)
        val_price_1 = get_value_fetch_val(row1_price_1, row2_price_1, id_val_price_1)
        function_data_static = function_data_static.replace("initializer_price_1", init_price_1)
        function_data_static = function_data_static.replace("variable_name_price_1", val_price_1)
    else:
        function_data_static = function_data_static.replace("initializer_price_1", "")
        function_data_static = function_data_static.replace("variable_name_price_1", "\"\"")
    if "obj_price_2" in node.get("more"):
        obj_price_2_data = node.get("more").get("obj_price_2")
        value_fetch_price_2 = obj_price_2_data.get("value_fetch")
        row1_price_2 = value_fetch_price_2.get("row1").get("label")
        row2_price_2 = value_fetch_price_2.get("row2").get("name")
        id_val_price_2 = str(node.get("id")) + "_price_2"

        init_price_2 = get_value_fetch_init(row1_price_2, row2_price_2, id_val_price_2)
        val_price_2 = get_value_fetch_val(row1_price_2, row2_price_2, id_val_price_2)
        function_data_static = function_data_static.replace("initializer_price_2", init_price_2)
        function_data_static = function_data_static.replace("variable_name_price_2", val_price_2)
    else:
        function_data_static = function_data_static.replace("initializer_price_2", "")
        function_data_static = function_data_static.replace("variable_name_price_2", "\"\"")
    if "obj_price_3" in node.get("more"):
        obj_price_3_data = node.get("more").get("obj_price_3")
        value_fetch_price_3 = obj_price_3_data.get("value_fetch")
        row1_price_3 = value_fetch_price_3.get("row1").get("label")
        row2_price_3 = value_fetch_price_3.get("row2").get("name")
        id_val_price_3 = str(node.get("id")) + "_price_3"

        init_price_3 = get_value_fetch_init(row1_price_3, row2_price_3, id_val_price_3)
        val_price_3 = get_value_fetch_val(row1_price_3, row2_price_3, id_val_price_3)
        function_data_static = function_data_static.replace("initializer_price_3", init_price_3)
        function_data_static = function_data_static.replace("variable_name_price_3", val_price_3)
    else:
        function_data_static = function_data_static.replace("initializer_price_3", "")
        function_data_static = function_data_static.replace("variable_name_price_3", "\"\"")

    return function_data_static

def draw_button_run_data(node, function_data_static):
    obj_text_data = node.get("more").get("obj_text")
    value_fetch = obj_text_data.get("value_fetch")
    row1 = value_fetch.get("row1").get("label")
    row2 = value_fetch.get("row2").get("name")
    id_val = str(node.get("id")) + "_obj_text"

    init = get_value_fetch_init(row1, row2, id_val)
    val = get_value_fetch_val(row1, row2, id_val)
    function_data_static = function_data_static.replace("initializer_obj_text", init)
    function_data_static = function_data_static.replace("variable_name_obj_text", val)

    return function_data_static


def draw_arrow_run_data(node, function_data_static):
    obj_time_1_data = node.get("more").get("obj_time_1")
    value_fetch_time_1 = obj_time_1_data.get("value_fetch")
    row1_time_1 = value_fetch_time_1.get("row1").get("label")
    row2_time_1 = value_fetch_time_1.get("row2").get("name")
    id_val_time_1 = str(node.get("id")) + "_time_1"

    init_time_1 = get_value_fetch_init(row1_time_1, row2_time_1, id_val_time_1)
    val_time_1 = get_value_fetch_val(row1_time_1, row2_time_1, id_val_time_1)
    function_data_static = function_data_static.replace("initializer_time_1", init_time_1)
    function_data_static = function_data_static.replace("variable_name_time_1", val_time_1)

    obj_price_1_data = node.get("more").get("obj_price_1")
    value_fetch_price_1 = obj_price_1_data.get("value_fetch")
    row1_price_1 = value_fetch_price_1.get("row1").get("label")
    row2_price_1 = value_fetch_price_1.get("row2").get("name")
    id_val_price_1 = str(node.get("id")) + "_price_1"

    init_price_1 = get_value_fetch_init(row1_price_1, row2_price_1, id_val_price_1)
    val_price_1 = get_value_fetch_val(row1_price_1, row2_price_1, id_val_price_1)
    function_data_static = function_data_static.replace("initializer_price_1", init_price_1)
    function_data_static = function_data_static.replace("variable_name_price_1", val_price_1)

    return function_data_static


def modify_stops_of_trades_run_data(node, function_data_static):
    relative_to_data = node.get("more").get("relative_to")
    if relative_to_data.get("value") == "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL":
        value_fetch = relative_to_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "_rt"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        function_data_static = function_data_static.replace("initializer_rt", init)
        function_data_static = function_data_static.replace("variable_name_rt", val)
    else:
        function_data_static = function_data_static.replace("initializer_rt", "")
        function_data_static = function_data_static.replace("variable_name_rt", "\"\"")

    new_tpsl_mode_data = node.get("more").get("new_tpsl_mode")
    if new_tpsl_mode_data.get("value") == "NEW_STOPS_CUSTOM_PRICE_LEVEL":
        value_fetch_tp = new_tpsl_mode_data.get("value_fetch_tp")
        row1_tp = value_fetch_tp.get("row1").get("label")
        row2_tp = value_fetch_tp.get("row2").get("name")
        id_val_tp = str(node.get("id")) + "_ntm_tp"

        init_tp = get_value_fetch_init(row1_tp, row2_tp, id_val_tp)
        val_tp = get_value_fetch_val(row1_tp, row2_tp, id_val_tp)

        value_fetch_sl = new_tpsl_mode_data.get("value_fetch_sl")
        row1_sl = value_fetch_sl.get("row1").get("label")
        row2_sl = value_fetch_sl.get("row2").get("name")
        id_val_sl = str(node.get("id")) + "_ntm_sl"

        init_sl = get_value_fetch_init(row1_sl, row2_sl, id_val_sl)
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
    open_at_price_data = node.get("more").get("open_at_price")
    if open_at_price_data.get("value") == "OPEN_AT_CUSTOM_PRICE":
        value_fetch = open_at_price_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "oacp"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        function_data_static = function_data_static.replace("initializer_oacp", init)
        function_data_static = function_data_static.replace("variable_name_oacp", val)
    else:
        function_data_static = function_data_static.replace("initializer_oacp", "")
        function_data_static = function_data_static.replace("variable_name_oacp", "\"\"")

    return function_data_static


def replace_input_values(data, input_dic):
    for key in input_dic:
        if isinstance(input_dic.get(key), collections.abc.Sequence) and not isinstance(input_dic.get(key), str):
            items = str(set(input_dic.get(key))) if set(input_dic.get(key)) else "{}"
            data = data.replace(key + "_val", items)
        else:
            data = data.replace(key + "_val", str(input_dic.get(key)))
    return data


def spread_filter_run_data(node, run_data):
    run_data = run_data.replace("operator_val", node.get("input_dic_task").get("operator"))
    return run_data


def comment_run_data(node, run_data):
    mrow1 = node.get("more").get("row1")
    if mrow1.get("Label").get("value") != "" and "value_fetch" in mrow1:
        value_fetch = mrow1.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r1"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_1", init)
        run_data = run_data.replace("variable_name_1", val)
    else:
        run_data = run_data.replace("initializer_1", "")
        run_data = run_data.replace("variable_name_1", "\"\"")

    mrow2 = node.get("more").get("row2")
    if mrow2.get("Label").get("value") != "" and "value_fetch" in mrow2:
        value_fetch = mrow2.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r2"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_2", init)
        run_data = run_data.replace("variable_name_2", val)
    else:
        run_data = run_data.replace("initializer_2", "")
        run_data = run_data.replace("variable_name_2", "\"\"")

    mrow3 = node.get("more").get("row3")
    if mrow3.get("Label").get("value") != "" and "value_fetch" in mrow3:
        value_fetch = mrow3.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r3"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_3", init)
        run_data = run_data.replace("variable_name_3", val)
    else:
        run_data = run_data.replace("initializer_3", "")
        run_data = run_data.replace("variable_name_3", "\"\"")

    mrow4 = node.get("more").get("row4")
    if mrow4.get("Label").get("value") != "" and "value_fetch" in mrow4:
        value_fetch = mrow4.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r4"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_4", init)
        run_data = run_data.replace("variable_name_4", val)
    else:
        run_data = run_data.replace("initializer_4", "")
        run_data = run_data.replace("variable_name_4", "\"\"")

    mrow5 = node.get("more").get("row5")
    if mrow5.get("Label").get("value") != "" and "value_fetch" in mrow5:
        value_fetch = mrow5.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r5"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_5", init)
        run_data = run_data.replace("variable_name_5", val)
    else:
        run_data = run_data.replace("initializer_5", "")
        run_data = run_data.replace("variable_name_5", "\"\"")

    mrow6 = node.get("more").get("row6")
    if mrow6.get("Label").get("value") != "" and "value_fetch" in mrow6:
        value_fetch = mrow6.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r6"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_6", init)
        run_data = run_data.replace("variable_name_6", val)
    else:
        run_data = run_data.replace("initializer_6", "")
        run_data = run_data.replace("variable_name_6", "\"\"")

    mrow7 = node.get("more").get("row7")
    if mrow7.get("Label").get("value") != "" and "value_fetch" in mrow7:
        value_fetch = mrow7.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r7"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_7", init)
        run_data = run_data.replace("variable_name_7", val)
    else:
        run_data = run_data.replace("initializer_7", "")
        run_data = run_data.replace("variable_name_7", "\"\"")

    mrow8 = node.get("more").get("row8")
    if mrow8.get("Label").get("value") != "" and "value_fetch" in mrow8:
        value_fetch = mrow8.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "cm_r8"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_8", init)
        run_data = run_data.replace("variable_name_8", val)
    else:
        run_data = run_data.replace("initializer_8", "")
        run_data = run_data.replace("variable_name_8", "\"\"")

    return run_data


def trailing_pending_orders_run_data(node, run_data):
    trailing_distance_mode_data = node.get("more").get("trailing_distance_mode")
    trailing_distance_mode = trailing_distance_mode_data.get("value")
    if trailing_distance_mode != "TRAILING_DISTANCE_MODE_FIXED":
        value_fetch = trailing_distance_mode_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "_tdmd"

        init = get_value_fetch_init(row1, row2, id_val)
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
    trailing_stop_mode_data = node.get("more").get("TrailingStopMode")
    trailing_stop_mode = trailing_stop_mode_data.get("value")
    if trailing_stop_mode == "TRAILING_STOP_MODE_CUSTOM_LEVEL":
        value_fetch = trailing_stop_mode_data.get("value_fetch")
        row1 = value_fetch.get("row1").get("label")
        row2 = value_fetch.get("row2").get("name")
        id_val = str(node.get("id")) + "tsm_cl"

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        run_data = run_data.replace("initializer_trailing_stop_mode", init)
        run_data = run_data.replace("variable_name_trailing_stop_mode", val)
    else:
        run_data = run_data.replace("initializer_trailing_stop_mode", "")
        run_data = run_data.replace("variable_name_trailing_stop_mode", "\"\"")
    return run_data


def modify_variable_run_data(node, run_data):
    modify_variables = ""
    for item in node.get("items"):
        row1 = item.get("value").get("row1").get("label")
        row2 = item.get("value").get("row2").get("name")
        id_val = str(node.get("id"))

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        modify_variables += init + "\n"
        modify_variables += item.get("variable_name") + " = " + val + ";\n\n"
    run_data = run_data.replace("modify_variables", modify_variables)
    return run_data


def formula(node, run_data):
    more = node.get("more")

    # Left data
    row1_left = more.get("left1").get("label")
    row2_left = more.get("left2").get("name")
    id_val_1 = str(node.get("id")) + "_" + "left"

    init_1 = get_value_fetch_init(row1_left, row2_left, id_val_1)
    val_1 = get_value_fetch_val(row1_left, row2_left, id_val_1)

    # Right data
    row1_right = more.get("right1").get("label")
    row2_right = more.get("right2").get("name")
    id_val_2 = str(node.get("id")) + "_" + "right"

    init_2 = get_value_fetch_init(row1_right, row2_right, id_val_2)
    val_2 = get_value_fetch_val(row1_right, row2_right, id_val_2)

    operator = more.get("operator").get("label")

    variable_name = more.get("variable").get("name")

    run_data = run_data.replace("initializer_1", init_1) \
        .replace("initializer_2", init_2) \
        .replace("var_name_1", str(val_1)) \
        .replace("var_name_2", str(val_2)) \
        .replace("variable_name", variable_name) \
        .replace("operator", operator)
    return run_data


def condition_1_run_data_normal(node, run_data):
    more = node.get("more")

    # Left data
    row1_left = more.get("left1").get("label")
    row2_left = more.get("left2").get("name")
    id_val_1 = str(node.get("id")) + "_" + "left"

    init_1 = get_value_fetch_init(row1_left, row2_left, id_val_1)
    val_1 = get_value_fetch_val(row1_left, row2_left, id_val_1)

    # Right data
    row1_right = more.get("right1").get("label")
    row2_right = more.get("right2").get("name")
    id_val_2 = str(node.get("id")) + "_" + "right"

    init_2 = get_value_fetch_init(row1_right, row2_right, id_val_2)
    val_2 = get_value_fetch_val(row1_right, row2_right, id_val_2)

    operator = more.get("operator").get("label")

    run_data = run_data.replace("initializer_1", init_1) \
        .replace("initializer_2", init_2) \
        .replace("var_name_1", str(val_1)) \
        .replace("var_name_2", str(val_2)) \
        .replace("operator", operator)
    return run_data


def condition_1_run_data_cross(node, run_data):
    more = node.get("more")

    # Left data
    row1_left = more.get("left1").get("label")
    row2_left = more.get("left2").get("name")
    id_val_11 = str(node.get("id")) + "_" + "left" + "1"
    id_val_12 = str(node.get("id")) + "_" + "left" + "2"

    init11 = get_value_fetch_init(row1_left, row2_left, id_val_11)
    init12 = get_value_fetch_init(row1_left, row2_left, id_val_12)
    val_11 = get_value_fetch_val(row1_left, row2_left, id_val_11)
    val_12 = get_value_fetch_val(row1_left, row2_left, id_val_12)

    # Right data
    row1_right = more.get("right1").get("label")
    row2_right = more.get("right2").get("name")
    id_val_21 = str(node.get("id")) + "_" + "right" + "1"
    id_val_22 = str(node.get("id")) + "_" + "right" + "2"

    init21 = get_value_fetch_init(row1_right, row2_right, id_val_21)
    init22 = get_value_fetch_init(row1_right, row2_right, id_val_22)
    val_21 = get_value_fetch_val(row1_right, row2_right, id_val_21)
    val_22 = get_value_fetch_val(row1_right, row2_right, id_val_22)

    # Operator
    operator_1 = ""
    operator_2 = ""
    operator = node.get("more").get("operator").get("label")
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


def get_value_fetch_init(row1, row2, suffix):
    if row1 == "Indicator":
        init = indicator_class_constructor.get_initializer(row2, suffix)
    elif row1 == "Candle":
        init = candle_class_constructor.get_initializer(suffix)
    elif row1 == "Market Properties":
        init = market_properties_class_constructor.get_initializer(suffix)
    elif row1 == "Value":
        init = value_class_constructor.get_initializer(suffix, row2)
    return init


def get_value_fetch_val(row1, row2, suffix):
    if row1 == "Indicator":
        val = indicator_class_constructor.get_var_name(row2, suffix)
    elif row1 == "Candle":
        val = candle_class_constructor.get_var_name(suffix)
    elif row1 == "Market Properties":
        val = market_properties_class_constructor.get_var_name(suffix)
    elif row1 == "Value":
        val = value_class_constructor.get_var_name(suffix)
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


def get_var_data(task_name):
    path_task_id = path + path_sub + "tasks" + "/" + task_name + "/"
    with open(path_task_id + "var_data.json") as var_file:
        if var_file:
            var_str = var_file.read()
            var_dic = json.loads(var_str)
            var_data = var_dic.get("var_data")
            return var_data

# input_dic = {
#     "n": 3
# }
#
# print(get_task())
# print(get_task_child("pass_n_times", input_dic, 4))
# print(get_initializer(4))
# print(get_var_name())
# print(get_var_data("pass_n_times"))
