import json
from . import path_root

path = path_root.get()
path_sub = "/contents/tasks/loop_for_trades_orders/close_partially/"



def get_structs():
    mpath = path + path_sub
    with open(mpath + "struct_data.json") as structs_file:
        if structs_file:
            structs_str = structs_file.read()
            structs_dic = json.loads(structs_str)
            structs = structs_dic.get("struct_data")
            return structs


def get_vars():
    mpath = path + path_sub
    with open(mpath + "var_data.json") as vars_file:
        if vars_file:
            vars_str = vars_file.read()
            vars_dic = json.loads(vars_str)
            vars = vars_dic.get("var_data")
            return vars
