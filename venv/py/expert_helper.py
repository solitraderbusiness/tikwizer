import json
import path_root

path = path_root.get()


def get_operator_symbol(id):
    return operators[id - 1]


def get_comparator_func(id, initializer_1, initializer_2, var_name_1, var_name_2, operator, statements_for_blue,
                        statements_for_red):
    with open(path + "/contents/comparator_with_id/" + "function_template.json") as fun_file:
        if fun_file:
            fun_txt = fun_file.read()
            fun_dic = json.loads(fun_txt)
            mql4_fun = fun_dic.get("function_template") \
                .replace("_id", str(id)) \
                .replace("initializer_1", initializer_1) \
                .replace("initializer_2", initializer_2) \
                .replace("var_name_1", var_name_1) \
                .replace("var_name_2", var_name_2) \
                .replace("statements_for_blue", statements_for_blue) \
                .replace("statements_for_red", statements_for_red) \
                .replace("operator", operator)
            return mql4_fun


def get_comparator_two_con_func(id, initializer_11, initializer_12, initializer_21, initializer_22, var_name_11,
                                var_name_12, \
                                var_name_21, var_name_22, operator_1, operator_2, statements_for_blue,
                                statements_for_red):
    with open(path + "/contents/comparator_two_con/" + "function_template.json") as fun_file:
        if fun_file:
            fun_txt = fun_file.read()
            fun_dic = json.loads(fun_txt)
            mql4_fun = fun_dic.get("function_template") \
                .replace("_id", str(id)) \
                .replace("initializer_11", initializer_11) \
                .replace("initializer_12", initializer_12) \
                .replace("initializer_21", initializer_21) \
                .replace("initializer_22", initializer_22) \
                .replace("var_name_11", str(var_name_11)) \
                .replace("var_name_12", str(var_name_12)) \
                .replace("var_name_21", str(var_name_21)) \
                .replace("var_name_22", str(var_name_22)) \
                .replace("statements_for_blue", statements_for_blue) \
                .replace("statements_for_red", statements_for_red) \
                .replace("operator_1", operator_1) \
                .replace("operator_2", operator_2)
            return mql4_fun


def get_comparator_call(id):
    with open(path + "/contents/comparator_with_id/" + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_body = initializer_dic.get("initializer").replace("_id", str(id))
            return initializer_body


def correct_input_indicator(indicator_name, input_dic):
    with open(path + "/contents/indicators/" + indicator_name + "/input.json") as file:
        if file:
            mstr = file.read()
            dic = json.loads(mstr)
            for key in dic:
                if key not in input_dic:
                    input_dic[key] = dic.get(key)
            return input_dic


def correct_input_value(input_dic):
    with open(path + "/contents/value/input.json") as file:
        if file:
            mstr = file.read()
            dic = json.loads(mstr)
            for key in dic:
                if key not in input_dic:
                    input_dic[key] = dic.get(key)
            return input_dic


def string_to_digit(str):
    array = [char for char in str]
    total = 0
    for c in array:
        total += ord(c)
    return total


def correct_once_per_bar_sides(nodes, edges):
    for node in nodes:
        is_target = False
        for edge in edges:
            target_id = edge.get("target")
            if node.get("id") == target_id:
                is_target = True
                break
        if not is_target and node.get("data").get("blockName") == "Once per bar":
            for edge in edges:
                if node.get("id") == edge.get("source") and edge.get("sourceHandle") == "blue":
                    target_id = edge.get("target")
                    for mnode in nodes:
                        if mnode.get("id") == target_id and mnode.get("data").get("blockName") == "condition1":
                            if mnode.get("more").get("left1").get("label") == "Indicator":
                                if mnode.get("more").get("candleIDLeft").get("value") == 0:
                                    mnode.get("more").get("candleIDLeft").update(
                                        {"value": mnode.get("more").get("candleIDLeft").get("value") + 1})
                            if mnode.get("more").get("right1").get("label") == "Indicator":
                                if mnode.get("more").get("candleIDRight").get("value") == 0:
                                    mnode.get("more").get("candleIDRight").update(
                                        {"value": mnode.get("more").get("candleIDRight").get("value") + 1})
