import json
from . import path_root

path = path_root.get()
path_sub = "/contents/miscellaneous/on_trade_event_detector/"


def get_class():
    mpath = path + path_sub
    class_str = ""
    with open(mpath + "class.json") as class_file:
        if class_file:
            class_txt = class_file.read()
            class_dic = json.loads(class_txt)
            class_str = class_dic.get("class")
    return class_str


def get_var():
    mpath = path + path_sub
    var_str = ""
    with open(mpath + "var.json") as var_file:
        if var_file:
            var_str = var_file.read()
            var_dic = json.loads(var_str)
            var_str = var_dic.get("var")
    return var_str
