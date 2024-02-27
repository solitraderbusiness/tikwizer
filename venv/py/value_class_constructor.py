import json
import path_root
import adjust

path = path_root.get()
path_sub = "/contents/value/"


def get_class(input_dic, class_id):
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
        init_body_dic["init_body"] = init_body_dic.get("init_body").replace(key + "_val", str(input_dic.get(key)), 1)

    mql4_body = class_template_dic.get("class_template") \
        .replace("_id", str(class_id), 1) \
        .replace("field_body", field_body_dic.get("field_body")) \
        .replace("init_body", init_body_dic.get("init_body"))

    if "adjust" in input_dic:
        type = input_dic.get("type")
        var_name = "result"
        match type:
            case "VALUE_TYPE_NUMERIC" | "VALUE_TYPE_BOOLEAN" | "VALUE_TYPE_COLOR" | "VALUE_TYPE_PIPS":
                var_name = "(double)" + var_name

        adjustment = adjust.get(var_name, input_dic.get("adjust"), "msymbol")
        mql4_body = mql4_body.replace("return result;", "return " + adjustment + ";")
    return mql4_body


def get_initializer(var_id, var_type):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)

            mtype = ""
            match var_type:
                case "Numeric":
                    mtype = "double"
                case "Boolean":
                    mtype = "bool"
                case "Color":
                    mtype = "color"
                case "Pips":
                    mtype = "double"
                case "Text":
                    mtype = "string"
                case "Text(code input)":
                    mtype = "string"
                case "Time":
                    mtype = "datetime"

            initializer_body = initializer_dic.get("initializer").replace("_id", str(var_id)).replace("type", mtype)
            return initializer_body


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
