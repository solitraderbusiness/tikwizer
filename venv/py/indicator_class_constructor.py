import json
import path_root
import adjust

path = path_root.get()
path_sub = "/contents/indicators/"

def get_class(indicator_name, input_dic, class_id):
    mpath = path + path_sub + indicator_name+"/"
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

    fun_body_dic = {}
    with open(mpath + "fun_body.json") as fun_file:
        if fun_file:
            fun_txt = fun_file.read()
            fun_body_dic = json.loads(fun_txt)

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
        .replace("init_body", init_body_dic.get("init_body")) \
        .replace("fun_body", fun_body_dic.get("fun_body"))

    if "adjust" in input_dic:
        adjustment = adjust.get("result", input_dic.get("adjust"), "symbol")
        mql4_body = mql4_body.replace("return result;", "return " + adjustment + ";")

    return mql4_body



def get_initializer(indicator_name, var_id):
    mpath = path + path_sub + indicator_name + "/"
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_body = initializer_dic.get("initializer").replace("_id", str(var_id))
            return initializer_body

def get_initializer_split(indicator_name, var_id):
    mpath = path + path_sub + indicator_name + "/"
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_list = initializer_dic.get("initializer_split")
            for i in range(len(initializer_list)):
                initializer_list[i] = initializer_list[i].replace("_id", str(var_id))
            return initializer_list

def get_var_name(indicator_name, var_id):
    mpath = path + path_sub + indicator_name + "/"
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            var_name = initializer_dic.get("variable_name").replace("_id", str(var_id))
            return var_name


