import json
from . import path_root
from . import adjust

path = path_root.get()
path_sub = "/contents/value_fetch/indicators-my-indicators/"


def get_class(row2, input_dic, class_id, constants, variables):
    mpath = path + path_sub
    class_template_dic = {}
    with open(mpath + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template_dic = json.loads(class_txt)

    field_body_dic = {}
    with open(mpath + "field_body.json") as field_file:
        if field_file:
            field_txt = field_file.read()
            field_body_dic = json.loads(field_txt)

    init_body_dic = {}
    with open(mpath + "init_body.json") as init_file:
        if init_file:
            init_txt = init_file.read()
            init_body_dic = json.loads(init_txt)

    for key in input_dic:
        init_body_dic["init_body"] = init_body_dic.get("init_body").replace(key + "_val",
                                                                            get_proper_value(input_dic.get(key),
                                                                                             constants, variables), 1)

    mql4_body = class_template_dic.get("class_template") \
        .replace("_id", str(class_id), 1) \
        .replace("field_body", field_body_dic.get("field_body")) \
        .replace("init_body", init_body_dic.get("init_body")) \
        .replace("buffer_val", str(input_dic.get("buffer"))) \
        .replace("indicator_name_val", "\"" + row2 + "\"") \
        .replace("indicator_input_val", get_proper_input(input_dic))

    if "adjust" in input_dic:
        var_name = "retval"
        adjustment = adjust.get(var_name, input_dic.get("adjust"), "OrderSymbol()")
        mql4_body = mql4_body.replace("return retval;", "return " + adjustment + ";")
    return mql4_body


def get_proper_value(value, constants, variables):
    if isinstance(value, str):
        if is_not_const_var(value, constants, variables):
            return value
        else:  # The value is the name of a constant/variable, so use the global scope
            return "::" + value
    else:
        return str(value)


def is_not_const_var(value, constants, variables):
    for constant in constants:
        if constant.get("name") == value:
            return False
    for variable in variables:
        if variable.get("name") == value:
            return False
    return True


def get_proper_input(input_dic):
    indicator_input = input_dic.get("input")
    proper_input = ""
    for item in indicator_input:
        if item.get("type") == "string":
            if item.get("name") in input_dic:
                proper_input += "\"" + str(input_dic.get(item.get("name"))) + "\"" + ", "
            else:
                proper_input += "\"" + str(item.get("value")) + "\"" + ", "
        else:
            if item.get("name") in input_dic:
                proper_input += str(input_dic.get(item.get("name"))) + ", "
            else:
                proper_input += str(item.get("value")) + ", "
    proper_input = replace_last_occurrence(proper_input, ", ", "")
    return proper_input


def replace_last_occurrence(s, old, new):
    # Find the index of the last occurrence of the substring
    index = s.rfind(old)
    if index == -1:  # If the substring is not found, return the original string
        return s
    # Replace the last occurrence
    return s[:index] + new + s[index + len(old):]


def get_initializer(var_id):
    mpath = path + path_sub + "/"
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_body = initializer_dic.get("initializer").replace("_id", str(var_id))
            return initializer_body


def get_var_name(var_id):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            var_name = initializer_dic.get("variable_name").replace("_id", str(var_id))
            return var_name

# Sample input
# {
#   "input": [
#     {
#       "type": "bool",
#       "name": "state",
#       "value": true
#     },
#     {
#       "type": "int",
#       "name": "count",
#       "value": 0
#     }
#   ],
#     "enums": [
#     "enum Sample1 {hello};",
#     "enum Sample2 {goodbye};"
#   ],
#   "buffer": 3,
#   "adjust": "",
#   "Symbol": "",
#   "Period": "PERIOD_CURRENT",
#   "ModeOutput": "id",
#   "TimeStamp": "00:00",
#   "VisibleID": 0,
#   "VisibleShift": 0,
#   "VisibleLimit": 100,
#   "RangeCandleStart": 0,
#   "RangeCandleEnd": 10,
#   "RangeTimeSource": "server",
#   "RangeTimeStart": "01:00",
#   "RangeTimeEnd": "08:00",
#   "RangeDayOffset": 0,
#   "RangeValue": "max",
#   "Shift": "0"
# }
