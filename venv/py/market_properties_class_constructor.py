import json
import path_root

path = path_root.get()
path_sub = "/contents/market_properties/"


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
        init_body_dic["init_body"] = init_body_dic.get("init_body").replace(key + "_val", str(input_dic.get(key)))

    mql4_body = class_template_dic.get("class_template") \
        .replace("_id", str(class_id), 1) \
        .replace("field_body", field_body_dic.get("field_body")) \
        .replace("init_body", init_body_dic.get("init_body"))

    return mql4_body


def get_initializer(var_id):
    mpath = path + path_sub
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_body = initializer_dic.get("initializer").replace("_id", str(var_id))
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

def get_structs():
    mpath = path + path_sub
    with open(mpath + "structs.json") as structs_file:
        if structs_file:
            structs_str = structs_file.read()
            structs_dic = json.loads(structs_str)
            structs = structs_dic.get("structs")
            return structs


# Test
# input = {
#     "symbol": "NULL",
#     "timeframe": 0,
#     "find_method": "CANDLE_PERIOD",
#     "price_mode": "LOWEST_PRICE",
#     "what_to_get": "GET_PRICE",
#     "timestr_start": "\"2023.11.23 7:30:30\"",
#     "timestr_end": "\"2023.11.23 5:30:00\"",
#     "day_offset": 2,
#     "range_start": 50,
#     "range_end": 100
# }
# print(get_class(input, 1040))
# print(get_initializer(1040))
# print(get_var_name(1040))
