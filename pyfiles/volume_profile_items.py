import json
from . import path_root
from . import adjust

path = path_root.get()
path_sub = "/contents/tasks/volume_profile/volume_profile/"


def get_classes():
    mpath = path + path_sub
    with open(mpath + "class_data.json") as classes_file:
        if classes_file:
            classes_str = classes_file.read()
            classes_dic = json.loads(classes_str)
            classes = classes_dic.get("class_data")
            return classes


def get_vars():
    mpath = path + path_sub
    with open(mpath + "var_data.json") as var_file:
        if var_file:
            var_str = var_file.read()
            var_dic = json.loads(var_str)
            mvars = var_dic.get("var_data")
            return mvars


def get_enums():
    mpath = path + path_sub
    with open(mpath + "enum_data.json") as enum_file:
        if enum_file:
            enum_str = enum_file.read()
            enum_dic = json.loads(enum_str)
            enums = enum_dic.get("enum_data")
            return enums
