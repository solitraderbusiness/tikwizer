import json
import path_root

path = path_root.get()
path_sub = "/contents/tasks/time_filters/spread_filter/"



def get_structs():
    mpath = path + path_sub
    with open(mpath + "struct_data.json") as structs_file:
        if structs_file:
            structs_str = structs_file.read()
            structs_dic = json.loads(structs_str)
            structs = structs_dic.get("struct_data")
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
