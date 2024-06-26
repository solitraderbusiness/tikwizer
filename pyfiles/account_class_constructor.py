import json
from . import path_root
from . import adjust

path = path_root.get()
path_sub = "/contents/value_fetch/account/"


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

    init_body_dic["init_body"] = init_body_dic.get("init_body").replace("row2_val", row2)

    mql4_body = class_template_dic.get("class_template") \
        .replace("_id", str(class_id), 1) \
        .replace("field_body", field_body_dic.get("field_body")) \
        .replace("init_body", init_body_dic.get("init_body"))

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


def get_initializer(row2, var_id):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)

            mtype = get_return_type(row2)

            initializer_body = initializer_dic.get("initializer") \
                .replace("_id", str(var_id)) \
                .replace("type", mtype, 1) \
                .replace("type_return", mtype)
            return initializer_body


def get_return_type(row2):
    match row2:
        case "ACCOUNT_INFO_BALLANCE":
            return "double"
        case "ACCOUNT_INFO_CREDIT":
            return "double"
        case "ACCOUNT_INFO_EQUITY":
            return "double"
        case "ACCOUNT_INFO_FREE_MARGIN":
            return "double"
        case "ACCOUNT_INFO_FREE_MARGIN_CHECK":
            return "double"
        case "ACCOUNT_INFO_LEVERAGE":
            return "long"
        case "ACCOUNT_INFO_LOGIN_NUMBER":
            return "long"
        case "ACCOUNT_INFO_MARGIN":
            return "double"
        case "ACCOUNT_INFO_MARGIN_LEVEL":
            return "double"
        case "ACCOUNT_INFO_NAME_BROKER":
            return "string"
        case "ACCOUNT_INFO_NAME_CLIENT":
            return "string"
        case "ACCOUNT_INFO_NAME_DEPOSIT_CURRENCY":
            return "string"
        case "ACCOUNT_INFO_NAME_SERVER":
            return "string"
        case "ACCOUNT_INFO_PROFIT_EQUITY_BALLANCE":
            return "double"
        case "ACCOUNT_INFO_STOPOUT_LEVEL":
            return "double"
        case "ACCOUNT_INFO_MARGIN_CALL_LEVEL":
            return "double"
        case "ACCOUNT_INFO_ORDERS_TRADES_LIMIT":
            return "int"


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
