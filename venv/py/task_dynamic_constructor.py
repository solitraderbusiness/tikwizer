import json
import path_root
import collections.abc
import indicator_class_constructor
import candle_class_constructor
import market_properties_class_constructor
import value_class_constructor

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
    function_data = function_data_dynamic_fun(function_data_static)

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
    elif task_name == "modify_variables":
        run_data = modify_variable_run_data(node, run_data_static)
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

def function_data_dynamic_fun(function_data_static):
    return function_data_static





def replace_input_values(data, input_dic):
    for key in input_dic:
        if isinstance(input_dic.get(key), collections.abc.Sequence) and not isinstance(input_dic.get(key), str):
            items = str(set(input_dic.get(key))) if set(input_dic.get(key)) else "{}"
            data = data.replace(key + "_val", items)
        else:
            data = data.replace(key + "_val", str(input_dic.get(key)))
    return data


def modify_variable_run_data(node, run_data):
    modify_variables = ""
    for item in node.get("items"):
        row1 = item.get("row1").get("label")
        row2 = item.get("row2").get("name")
        id_val = str(node.get("id"))

        init = get_value_fetch_init(row1, row2, id_val)
        val = get_value_fetch_val(row1, row2, id_val)
        modify_variables += init + "\n"
        modify_variables += item.get("vairable_name") + " = " + val + ";\n\n"
    run_data = run_data.repace("modify_variables", modify_variables)
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

    operator = node.get("more").get("operator").get("label")

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

    #Operator
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


def get_value_fetch_init (row1, row2, suffix):
    if row1 == "Indicator":
        init = indicator_class_constructor.get_initializer(row2, suffix)
    elif row1 == "Candle":
        init = candle_class_constructor.get_initializer(suffix)
    elif row1 == "Market Properties":
        init = market_properties_class_constructor.get_initializer(suffix)
    elif row1 == "Value":
        init = value_class_constructor.get_initializer(suffix)
    return init

def get_value_fetch_val (row1, row2, suffix):
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
