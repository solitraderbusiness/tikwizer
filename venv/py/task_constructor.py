import json
import path_root
import collections.abc
import indicator_class_constructor
import candle_class_constructor
import market_properties_class_constructor

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
    class_template = ""
    with open(path_task_id_template + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template = json.loads(class_txt).get("class_template")

    field_data = ""
    with open(path_task_id + "field_data.json") as field_file:
        if field_file:
            field_txt = field_file.read()
            field_data = json.loads(field_txt).get("field_data")

    constructor_data = ""
    with open(path_task_id + "constructor_data.json") as constructor_file:
        if constructor_file:
            constructor_text = constructor_file.read()
            constructor_data = json.loads(constructor_text).get("constructor_data")

    run_data = ""
    with open(path_task_id + "run_data.json") as run_file:
        if run_file:
            run_txt = run_file.read()
            run_data = json.loads(run_txt).get("run_data")

    reset_data = ""
    with open(path_task_id + "reset_data.json") as reset_file:
        if reset_file:
            reset_txt = reset_file.read()
            reset_data = json.loads(reset_txt).get("reset_data")

    function_data = ""
    with open(path_task_id + "function_data.json") as function_file:
        if function_file:
            function_txt = function_file.read()
            function_data = json.loads(function_txt).get("function_data")

    # Once on constructor data (for field variables)
    for key in input_dic:
        if isinstance(input_dic.get(key), collections.abc.Sequence) and not isinstance(input_dic.get(key), str):
            items = str(set(input_dic.get(key))) if set(input_dic.get(key)) else "{}"
            constructor_data = constructor_data.replace(key + "_val", items)
        else:
            constructor_data = constructor_data.replace(key + "_val", str(input_dic.get(key)))

    # Once on run data (for local variables)
    for key in input_dic:
        if isinstance(input_dic.get(key), collections.abc.Sequence) and not isinstance(input_dic.get(key), str):
            items = str(set(input_dic.get(key))) if set(input_dic.get(key)) else "{}"
            run_data = run_data.replace(key + "_val", items)
        else:
            run_data = run_data.replace(key + "_val", str(input_dic.get(key)))

    run_data = fill_run_if_any(node, run_data)

    task = class_template \
        .replace("_id", str(class_id), 2) \
        .replace("field_data", field_data) \
        .replace("constructor_data", constructor_data) \
        .replace("run_data", run_data) \
        .replace("run_data", run_data)\
        .replace("reset_data", reset_data)\
        .replace("function_data", function_data)

    return task

def fill_run_if_any (node, run_data):
     task_name = node.get("data").get("blockName")
     if task_name == "condition_1_normal":
         run_data = condition_1_run_data_normal(node, run_data)
     elif task_name == "condition_1_cross":
         run_data = condition_1_run_data_cross(node, run_data)

     return run_data


def condition_1_run_data_normal(node , run_data):
    more = node.get("more")
    #left data
    left_name = more.get("left1").get("label")
    id_val_left = str(node.get("id")) + "_" + "left"
    init_left = ""
    val_left  = ""
    if left_name == "Indicator":
        indicator_name = more.get("left2").get("name")
        init_left = indicator_class_constructor.get_initializer(indicator_name, id_val_left)
        val_left = indicator_class_constructor.get_var_name(indicator_name, id_val_left)
    elif left_name == "Candle":
        init_left = candle_class_constructor.get_initializer(id_val_left)
        val_left = candle_class_constructor.get_var_name(id_val_left)
    elif left_name == "Market Properties":
        init_left = market_properties_class_constructor.get_initializer(id_val_left)
        val_left = market_properties_class_constructor.get_var_name(id_val_left)
    elif left_name == "Value":
        init_left = ""
        val_left = more.get("left")[0].get("value").get("value")
    #right data
    right_name = more.get("right1").get("label")
    id_val_right = str(node.get("id")) + "_" + "right"
    init_right = ""
    val_right = ""
    if right_name == "Indicator":
        indicator_name = more.get("right2").get("name")
        init_right = indicator_class_constructor.get_initializer(indicator_name, id_val_right)
        val_right = indicator_class_constructor.get_var_name(indicator_name, id_val_right)
    elif right_name == "Candle":
        init_right = candle_class_constructor.get_initializer(id_val_right)
        val_right = candle_class_constructor.get_var_name(id_val_right)
    elif right_name == "Market Properties":
        init_right = market_properties_class_constructor.get_initializer(id_val_right)
        val_right = market_properties_class_constructor.get_var_name(id_val_right)
    elif right_name == "Value":
        init_right = ""
        val_right = more.get("right")[0].get("value").get("value")

    run_data = run_data.replace("initializer_1", init_left)\
                        .replace("initializer_2", init_right)\
                        .replace("var_name_1", str(val_left))\
                        .replace("var_name_2", str(val_right))\
                        .replace("operator", more.get("operator").get("label"))
    return run_data

def condition_1_run_data_cross(node , run_data):
    more = node.get("more")
    #Left data
    left = more.get("left1").get("label")
    id_val_11 = str(node.get("id")) + "_" + "left" + "1"
    id_val_12 = str(node.get("id")) + "_" + "left" + "2"
    init11 = ""
    init11 = ""
    var_name_12 = ""
    var_name_12 = ""
    if left == "Indicator":
        indicator_name = more.get("left2").get("name")
        init11 = indicator_class_constructor.get_initializer(indicator_name, id_val_11)
        init12 = indicator_class_constructor.get_initializer(indicator_name, id_val_12)
        val_11 = indicator_class_constructor.get_var_name(indicator_name, id_val_11)
        val_12 = indicator_class_constructor.get_var_name(indicator_name, id_val_12)
    elif left == "Candle":
        init11 = candle_class_constructor.get_initializer(id_val_11)
        init12 = candle_class_constructor.get_initializer(id_val_12)
        val_11 = candle_class_constructor.get_var_name(id_val_11)
        val_12 = candle_class_constructor.get_var_name(id_val_12)
    elif left == "Market Properties":
        init11 = market_properties_class_constructor.get_initializer(id_val_11)
        init12 = market_properties_class_constructor.get_initializer(id_val_12)
        val_11 = market_properties_class_constructor.get_var_name(id_val_11)
        val_12 = market_properties_class_constructor.get_var_name(id_val_12)
    elif left == "Value":
        init11 = ""
        init12 = ""
        val_11 = more.get("left")[0].get("value").get("value")
        val_12 = more.get("left")[0].get("value").get("value")
    #Right data
    right = more.get("right1").get("label")
    id_val_21 = str(node.get("id")) + "_" + "right" + "1"
    id_val_22 = str(node.get("id")) + "_" + "right" + "2"
    init21 = ""
    init22 = ""
    var_name_21 = ""
    var_name_22 = ""
    if right == "Indicator":
        indicator_name = more.get("right2").get("name")
        init21 = indicator_class_constructor.get_initializer(indicator_name, id_val_21)
        init22 = indicator_class_constructor.get_initializer(indicator_name, id_val_22)
        val_21 = indicator_class_constructor.get_var_name(indicator_name, id_val_21)
        val_22 = indicator_class_constructor.get_var_name(indicator_name, id_val_22)
    elif right == "Candle":
        init21 = candle_class_constructor.get_initializer(id_val_21)
        init22 = candle_class_constructor.get_initializer(id_val_22)
        val_21 = candle_class_constructor.get_var_name(id_val_21)
        val_22 = candle_class_constructor.get_var_name(id_val_22)
    elif right == "Market Properties":
        init21 = market_properties_class_constructor.get_initializer(id_val_21)
        init22 = market_properties_class_constructor.get_initializer(id_val_22)
        val_21 = market_properties_class_constructor.get_var_name(id_val_21)
        val_22 = market_properties_class_constructor.get_var_name(id_val_22)
    elif right == "Value":
        init21 = ""
        init22 = ""
        val_21 = more.get("right")[0].get("value").get("value")
        val_22 = more.get("right")[0].get("value").get("value")

    operator_1 = ""
    operator_2 = ""
    operator = node.get("more").get("operator").get("label")
    if operator == "×>":
        operator_1 = ">"
        operator_2 = "<"
    elif operator == "×<":
        operator_1 = "<"
        operator_2 = ">"

    run_data = run_data\
                        .replace("initializer_11", init11)\
                        .replace("initializer_12", init12)\
                        .replace("initializer_21", init21)\
                        .replace("initializer_22", init22)\
                        .replace("var_name_11", str(val_11))\
                        .replace("var_name_12", str(val_12))\
                        .replace("var_name_21", str(val_21))\
                        .replace("var_name_22", str(val_22))\
                        .replace("operator_1", operator_1)\
                        .replace("operator_2", operator_2)

    return run_data

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
