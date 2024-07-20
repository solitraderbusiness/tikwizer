# This module adapts client data to mql generator

from . import path_root
import json


def refactor(data_raw):
    data = data_raw.get("data")
    data = sort_data(data)  # STest, this sorts the whole data which can consume more time, I just want to sort params
    correct_enabled(data)
    events = data["events"]
    for key in events:
        # Add indexes (overwrite ids) for later access
        event = events[key]
        overwrite_ids(event["nodes"], event["edges"])
        correct_block_names_mql(event["nodes"])
        create_specific_input(event["nodes"])
        # Block input_dic
        set_blocks_input_dic(key, event["nodes"], event["edges"])
        # Set input items that are not present in user input form front end
        params_fill(event.get("nodes"))
        # Correct double quotation issue with string values
        manage_extra_double_quotation(event.get("nodes"), data.get("constants"), data.get("variables"))
        handle_order_type_issue(event)
    add_extra_double_quotation_vars_consts(data.get("constants"), data.get("variables"))
    return data


# This sort fixes the issue with replacing items like shift,
# ma_shift where shorter one also replaces the longer one
def sort_data(d):
    if isinstance(d, dict):
        return {k: sort_data(v) for k, v in sorted(d.items(), key=lambda item: len(item[0]), reverse=True)}
    elif isinstance(d, list):
        return [sort_data(v) for v in d]
    else:
        return d


# This function creates generator specific input like order_type in buy_sell
def create_specific_input(nodes):
    for node in nodes:
        block_name = node.get("blockName")
        params = node.get("params")
        if block_name == "Buy now":
            params["order_type"] = "ORDER_BUY"
        elif block_name == "Sell now":
            params["order_type"] = "ORDER_SELL"
        elif block_name == "Buy pending order":
            params["order_type"] = "ORDER_BUY_PENDING"
        elif block_name == "Sell pending order":
            params["order_type"] = "ORDER_SELL_PENDING"
        elif block_name == "Volume profile":
            params["Id"] = params.get("Id") + "_" + str(node.get("id_by_user"))
        elif block_name in ["If trade", "If trade/order", "If pending order"]:
            params["count_limit"] = 0
            params["operator"] = ">"
        elif block_name in ["No trade", "No trade/order", "No pending order"]:
            params["count_limit"] = 0
            params["operator"] = "=="
        elif block_name == "Formula":
            if not params.get("variable").strip():
                params["variable"] = "string undefined_var_" + str(node.get("id"))


def add_extra_double_quotation_vars_consts(constants, variables):
    for const in constants:
        if const.get("type").lower().strip() == "string":
            const["value"] = '\"' + const.get("value") + '\"'
    for variable in variables:
        if variable.get("type").lower().strip() == "string":
            variable["value"] = '\"' + variable.get("value") + '\"'


# Correct string values that are expected with extra double quotations: "\"\""
def manage_extra_double_quotation(nodes, constants, variables):
    for node in nodes:
        add_extra_double_quotation_if_any(node.get("params"), constants, variables)


def add_extra_double_quotation_if_any(dic, constants, variables):
    # Keys that need a double quote
    keys = ["timestr_start", "timestr_end", "time_stamp", "timestr", "comment", "obj_name",
            "name_filter_mode", "symbols_str", "close_mode", "mode_range", "mode_base_price",
            "obj_chart_subwindow", "title", "obj_title_font", "obj_label_font", "obj_font",
            "label_1", "label_2", "label_3", "label_4", "label_5", "label_6", "label_7", "label_8",
            "stops_mode", "sl_only", "tp_only", "Id", "message", "block_ids", "obj_name_contains",
            "obj_name_prefix", "loop_direction", "sort_mode", "skip_objects", "max_objects",
            "name_contains", "name_starts_with", "time_start", "time_end", "FirstStartHour", "FirstEndHour",
            "SecondStartHour", "SecondEndHour", "ThirdStartHour", "ThirdEndHour", "FourthStartHour",
            "FourthEndHour", "second_output", "ObjSource", "Name", "ModeTakeProfit", "ModeStopLoss",
            "symbol", "Price", "PipsAwayMode", "DirectionMode", "SignalType", "CandleType", "UpperWickMode",
            "LowerWickMode", "AgeRelativeTo", "RelativeTo", "NewTPmode", "NewSLmode", "AlertTitle", "AlertLabel1",
            "AlertLabel2", "AlertLabel3", "AlertLabel4", "AlertLabel5", "AlertLabel6", "AlertLabel7", "AlertLabel8",
            "AlertLabel9", "AlertLabel10", "Title", "Label1", "Label2", "Label3", "Label4", "Label5", "Label6",
            "Label7", "Label8", "MYsound", "MTsound", "PromptCaption", "PromptText", "CheckBuyOrSell",
            "CheckLimitOrStop"]

    for key, value in dic.items():
        if isinstance(value, dict):
            add_extra_double_quotation_if_any(value, constants, variables)
        else:
            con1 = key in keys and is_not_const_var(value, constants, variables)
            # con2 commented as apparently value as key is only used in value_fetch > value and I have to take care of it in constructor class
            # con2 = key == "value" and isinstance(value, str) and is_not_const_var(value, constants, variables)
            con3 = (key == "symbol" or key == "time_market") and value != "NULL" and is_not_const_var(value, constants,
                                                                                                      variables)
            if con1 or con3:
                dic[key] = '\"' + value + '\"'


def is_not_const_var(value, constants, variables):
    for constant in constants:
        if constant.get("name") == value:
            return False
    for variable in variables:
        if variable.get("name") == value:
            return False
    return True


# This function handles the situation where there are both type
# and pending type in trade/order filters section. I decided to handle this in Python cuz in MQL
# I had to change the code in multiple places
def handle_order_type_issue(event):
    nodes = event.get("nodes")
    for node in nodes:
        params = node.get("params")
        if "type" in params and "type_pending" in params:
            types = params.get("type").replace(' ', '')[1:-1].split(',')
            types_pending = params.get("type_pending").replace(' ', '')[1:-1].split(',')

            set_types = set(types)
            set_types_pending = set(types_pending)

            # Get the intersection
            intersection = set_types & set_types_pending

            # Convert the intersection set to a string
            result = "{" + ','.join(intersection) + "}"

            # Replace in type
            params["type"] = result


# Adds the input that are not passed by front end
def params_fill(nodes):
    for node in nodes:
        # First fill value fetch if any (supports condition and formula)
        value_fetch_fill(node.get("params"))
        # Now skip condition and formula
        if node.get("block_name_mql") in ["condition_1_normal", "condition_1_cross", "formula"]:
            continue
        path = path_root.get()
        path_sub = "/contents/"
        category = node.get("category")
        task_name = node.get("block_name_mql")
        params = node.get("params")
        path_task_id = path + path_sub + "tasks" + "/" + category + "/" + task_name + "/"  # used to get data and fill template
        with open(path_task_id + "input.json") as input_file:
            if input_file:
                input_text = input_file.read()
                input_saved = json.loads(input_text)
                replace_params(input_saved, params)


# This function fills value fetch items in case there is a lack of input.
# For example in Value, if type is Numeric, all the other input are skipped
# by front. As I need them in my MQL4, I have to add them using my default input.
def value_fetch_fill(params):
    for key, value in params.items():
        if isinstance(value, dict):
            if "row1" in value and "row2" in value and "params" in value:
                check_value_fetch_params(value)
            else:
                value_fetch_fill(value)


def check_value_fetch_params(side):  # Side means left or right
    path = path_root.get()
    path_sub = "/contents/"
    path_module = ""
    params = side.get("params")
    match side.get("row1"):
        case "indicator":
            path_module = "indicators" + "/" + side.get("row2").lower() + "/"
        case "market-properties":
            path_module = "value_fetch/market_properties" + "/" + side.get("row2") + "/"
        case "value":
            path_module = "value" + "/"
        case "candle":
            path_module = "candle" + "/"
        case "object-on-the-chart":
            path_module = "object_on_the_chart" + "/" + side.get("row2").lower() + "/"
        case "trade-order-in-loop":
            path_module = "value_fetch/trade_order_in_loop/"
        case "account":
            path_module = "value_fetch/account/"
    with open(path + path_sub + path_module + "input.json") as input_file:
        if input_file:
            input_text = input_file.read()
            input_saved = json.loads(input_text)
            replace_params(input_saved, params)


def replace_params(input_saved, params):
    keys_lost = set(params.keys()) - set(input_saved.keys())
    print("keys_lost: " + str(keys_lost))  # STest, remove later
    for key, value in input_saved.items():
        if key not in params:
            params[key] = value


def correct_enabled(data):
    events = data["events"]
    for key in events:
        for node in events[key]["nodes"]:
            if "enabled" not in node:
                node["enabled"] = True


def overwrite_ids(nodes, edges):
    for i in range(len(nodes)):
        node = nodes[i]
        for edge in edges:
            if edge.get("source") == node.get("id"):
                edge["source"] = i
            if edge.get("target") == node.get("id"):
                edge["target"] = i
        node["id"] = i


def set_blocks_input_dic(key, nodes, edges):
    for node in nodes:
        input_dic = {}
        input_dic["id"] = node.get("id")
        input_dic["id_by_user"] = node.get("id_by_user")
        input_dic["name"] = "\"" + node.get("block_name_mql") + "\""
        input_dic["enabled"] = node.get("enabled")
        input_dic["event"] = get_proper_event_name(key)
        input_dic["nexts_true"] = get_nexts_true(node, edges)
        input_dic["nexts_false"] = get_nexts_false(node, edges)
        input_dic["prevs_true"] = get_prevs_true(node, edges)
        input_dic["prevs_false"] = get_prevs_false(node, edges)
        node["input_dic_block"] = input_dic


def get_proper_event_name(key):
    events = {
        "on_init": "EVENT_ON_INIT",
        "on_timer": "EVENT_ON_TIMER",
        "on_tick": "EVENT_ON_TICK",
        "on_trade": "EVENT_ON_TRADE",
        "on_chart": "EVENT_ON_CHART",
        "on_deinit": "EVENT_ON_DEINIT",
    }
    return events.get(key)


def correct_block_names_mql(nodes):
    for node in nodes:
        block_name = node.get("blockName")
        if block_name == "Condition":
            operator = node.get("params").get("operator").get("label")
            if operator == "×>" or operator == "×<":
                node["block_name_mql"] = "condition_1_cross"
            else:
                node["block_name_mql"] = "condition_1_normal"
        elif block_name in ["Buy now", "Sell now", "Buy pending order", "Sell pending order"]:
            node["block_name_mql"] = "buy_sell"
        elif block_name in ["Check trades count", "Check pending orders count", "If trade", "If trade/order",
                            "If pending order", "No trade", "No trade/order", "No pending order"]:
            node["block_name_mql"] = "check_trades_orders_count"
        elif block_name in ["No trade nearby", "No pending order nearby"]:
            node["block_name_mql"] = "no_trade_order_nearby"
        elif block_name == "Turn ON blocks":
            node["block_name_mql"] = "blocks_on_off"
            node.get("params")["what"] = "BLOCK_STATE_ENABLE"
        elif block_name == "Turn OFF blocks":
            node["block_name_mql"] = "blocks_on_off"
            node.get("params")["what"] = "BLOCK_STATE_DISABLE"
        elif block_name == "Toggle blocks":
            node["block_name_mql"] = "blocks_on_off"
            node.get("params")["what"] = "BLOCK_STATE_TOGGLE"


def get_nexts_true(node, edges):
    result = []
    for edge in edges:
        if edge.get("source") == node.get("id"):
            if edge.get("sourceHandle") == "blue":
                result.append(edge.get("target"))
    return result


def get_nexts_false(node, edges):
    result = []
    for edge in edges:
        if edge.get("source") == node.get("id"):
            if edge.get("sourceHandle") == "red":
                result.append(edge.get("target"))
    return result


def get_prevs_true(node, edges):
    result = []
    for edge in edges:
        if edge.get("target") == node.get("id"):
            if edge.get("sourceHandle") == "blue":
                result.append(edge.get("source"))
    return result


def get_prevs_false(node, edges):
    result = []
    for edge in edges:
        if edge.get("target") == node.get("id"):
            if edge.get("sourceHandle") == "red":
                result.append(edge.get("source"))
    return result
