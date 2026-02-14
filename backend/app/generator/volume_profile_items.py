import json
from . import path_root
from . import adjust

path = path_root.get()
path_sub = "/contents/tasks/various_signals/volume_profile/"


def get_enums():
    mpath = path + path_sub
    with open(mpath + "enum_data.json") as enum_file:
        if enum_file:
            enum_str = enum_file.read()
            enum_dic = json.loads(enum_str)
            enums = enum_dic.get("enum_data")
            return enums
