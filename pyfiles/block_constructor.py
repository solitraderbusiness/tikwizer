import json
from . import path_root
import collections

path = path_root.get()


def get_block_parent():
    path_sub = "/contents/block_parent/"
    mpath = path + path_sub + "/"
    class_template = ""
    with open(mpath + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template_dic = json.loads(class_txt)
            class_template = class_template_dic.get("class_template")
    return class_template


def get_block():
    path_sub = "/contents/block/"
    mpath = path + path_sub + "/"
    class_template = ""
    with open(mpath + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template_dic = json.loads(class_txt)
            class_template = class_template_dic.get("class_template")
    return class_template


def get_block_child(input_dic, class_id):
    path_sub = "/contents/block_i/"
    mpath = path + path_sub + "/"
    class_template = ""
    with open(mpath + "class_template.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_template_dic = json.loads(class_txt)
            class_template = class_template_dic.get("class_template")

    for key in input_dic:
        if isinstance(input_dic.get(key), collections.abc.Sequence) and not isinstance(input_dic.get(key), str):
            items = str(set(input_dic.get(key))) if set(input_dic.get(key)) else "{}"
            class_template = class_template.replace(key + "_val", items)
        else:
            class_template = class_template.replace(key + "_val", str(input_dic.get(key)))

    result = class_template.replace("_id", str(class_id))
    return result


def get_initializer(var_id):
    path_sub = "/contents/block_i/"
    mpath = path + path_sub + "/"
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            initializer_body = initializer_dic.get("initializer").replace("_id", str(var_id))
            return initializer_body


def get_var_name(var_id):
    path_sub = "/contents/block_i/"
    mpath = path + path_sub + "/"
    with open(mpath + "initializer.json") as initializer_file:
        if initializer_file:
            initializer_str = initializer_file.read()
            initializer_dic = json.loads(initializer_str)
            var_name = initializer_dic.get("variable_name").replace("_id", str(var_id))
            return var_name

# input_dic = {
#     "id": "\"fdsnsldifkdsl\"",
#     "id_by_user": 4,
#     "name": "\"Condition1\"",
#     "enabled": True,
#     "nexts_true": [8, 5],
#     "nexts_false": [10],
#     "prevs_true": [1],
#     "prevs_false": [2]
# }
#
# print(get_block_parent())
# print(get_block())
# print(get_block_child(input_dic, 4))
# print(get_initializer(4))
# print(get_var_name(4))
