import json
from . import path_root
from . import adjust

path = path_root.get()
path_sub = "/contents/value/"


def get_class(value_type, input_dic, class_id, constants, variables):
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

    if value_type == "Text" and input_dic.get("value") == "":
        input_dic["value"] = "\"\""
    else:
        mvalue = input_dic.get("value")
        if value_type == "Text" and not input_dic.get("value").startswith('"') and is_not_const_var(
                input_dic.get("value"), constants, variables):
            mvalue = "\"" + mvalue
        if value_type == "Text" and not input_dic.get("value").endswith('"') and is_not_const_var(
                input_dic.get("value"), constants, variables):
            mvalue = mvalue + "\""
        input_dic["value"] = mvalue

    for key in input_dic:
        init_body_dic["init_body"] = init_body_dic.get("init_body").replace(key + "_val",
                                                                            get_proper_value(input_dic.get(key),
                                                                                             constants, variables), 1)

    mql4_body = class_template_dic.get("class_template") \
        .replace("_id", str(class_id), 1) \
        .replace("field_body", field_body_dic.get("field_body")) \
        .replace("init_body", init_body_dic.get("init_body")) \
        .replace("value_type_val", '\"' + value_type + '\"') \
        .replace("type_return", get_return_type(value_type)) \
        .replace("return_default", get_return_default(get_return_type(value_type)))

    if "adjust" in input_dic:
        var_name = "result"
        # if value_type in ["Numeric", "Color", "Pips"]:
        #     var_name = "(double)" + var_name

        adjustment = adjust.get(var_name, input_dic.get("adjust"), "msymbol")
        mql4_body = mql4_body.replace("return result;", "return " + adjustment + ";")
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
            print(variable.get("name"), value)
            return False
    return True


def get_initializer(value_type, var_id):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)

            mtype = get_return_type(value_type)

            initializer_body = initializer_dic.get("initializer") \
                .replace("_id", str(var_id)) \
                .replace("type", mtype, 1) \
                .replace("type_return", mtype)
            return initializer_body


def get_return_default(return_type):
    match return_type:
        case "double":
            return "0"
        case "bool":
            return "false"
        case "color":
            return "clrNONE"
        case "string":
            return "\"\""
        case "datetime":
            return "0"


def get_return_type(value_type):
    match value_type:
        case "Numeric":
            return "double"
        case "Boolean":
            return "bool"
        case "Color":
            return "color"
        case "Pips":
            return "double"
        case "Text":
            return "string"
        case "Text_code_input":
            return "string"
        case "Time":
            return "datetime"


def get_initializer_split(var_id):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_list = initializer_dic.get("initializer_split")
            for i in range(len(initializer_list)):
                initializer_list[i] = initializer_list[i].replace("_id", str(var_id))
            return initializer_list


def get_var_name(var_id):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            var_name = initializer_dic.get("variable_name").replace("_id", str(var_id))
            return var_name

# Test
# input = {
#     "type": "VALUE_TYPE_PIPS",
#     "value": 10,
#     "adjust": "20",
#     "pips_type": "CANDLE_LOW",
#     "symbol": "NULL"
# }
# print(get_class(input, 1040))
# print(get_initializer(1040))
# print(get_var_name(1040))
