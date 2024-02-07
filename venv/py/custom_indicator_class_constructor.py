import json
import path_root

path = path_root.get()
path_sub = "/contents/indicators/custom/"

def get_class(input_dic, class_id):
    mpath = path + path_sub

    #1_ load class template
    class_template_dic = {}
    with open(mpath + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template_dic = json.loads(class_txt)

    #2_ make a dic containing only specific input params
    input_custom = input_dic.copy()
    keys_common = ['symbol', 'timeframe', 'name', 'mode', 'shift']
    for key in keys_common:
        input_custom.pop(key, None)

    #3_ create a field body of specific params
    custom_field = ""
    for key in input_custom:
        value = input_custom.get(key)
        if type(value) == int:
            custom_field += "int" + " " + key + ";" + "\n"
        elif type(value) == bool:
            custom_field += "bool" + " " + key + ";" + "\n"
        elif type(value) == float:
            custom_field += "double" + " " + key + ";" + "\n"
        elif type(value) == str:
            custom_field += "string" + " " + key + ";" + "\n"


    #4_ create init body of all params (both common and specific params) and place values
    custom_init = ""
    print(input_dic)
    for key in input_dic:
        custom_init += key + " = " + str(input_dic.get(key)) + ";" + "\n"

    #5_ create custom params for function body
    custom_params = ""
    for key in input_custom:
        custom_params += key + ", "

    #6_ update class template and create output
    mql4_body = class_template_dic.get("class_template") \
        .replace("_id", str(class_id), 1) \
        .replace("custom_field", custom_field) \
        .replace("custom_init", custom_init) \
        .replace("custom_params", custom_params)

    if "adjust" in input_dic:
        adjustment = adjust.get("result", input_dic.get("adjust"), "symbol")
        mql4_body = mql4_body.replace("return result;", "return " + adjustment + ";")

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


