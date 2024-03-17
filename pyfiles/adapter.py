# This module adapts client data to mql generator

from . import path_root
import json


def refactor(data):
    correct_enabled(data)
    events = data["events"]
    for key in events:
        # Add indexes (overwrite ids) for later access
        event = events[key]
        overwrite_ids(event["nodes"], event["edges"])
        add_category(event["nodes"])
        create_specific_input(event["nodes"])
        overwrite_task_names(event["nodes"])
        # Block input_dic
        set_blocks_input_dic(event["nodes"], event["edges"])
        # Set input items that are not present in user input form front end
        add_not_present_input(event)
        # Correct double quotation issue with string values
        correct_double_quotation_strings(event, data.get("constants"), data.get("variables"))
    add_extra_double_quotation_vars_consts(data.get("constants"), data.get("variables"))
    return data


# This function creates generator specific input like order_type in buy_sell or type in value
def create_specific_input(nodes):
    for node in nodes:
        block_name = node.get("blockName")
        params = node.get("params")
        if block_name == "condition":
            left = params.get("left")
            right = params.get("right")
            if left.get("row1") == "Value":
                left.get("params")["type"] = get_value_type(left.get("row2"))
            if right.get("row1") == "Value":
                right.get("params")["type"] = get_value_type(right.get("row2"))
        elif block_name == "Buy now":
            node.get("params")["order_type"] = "ORDER_BUY"
        elif block_name == "Sell now":
            node.get("params")["order_type"] = "ORDER_SELL"
        elif block_name == "Buy pending order":
            node.get("params")["order_type"] = "ORDER_BUY_PENDING"
        elif block_name == "Sell pending order":
            node.get("params")["order_type"] = "ORDER_SELL_PENDING"


def get_value_type(row2):
    match row2:
        case "Numeric":
            return "VALUE_TYPE_NUMERIC"
        case "Boolean":
            return "VALUE_TYPE_BOOLEAN"
        case "Color":
            return "VALUE_TYPE_COLOR"
        case "Pips":
            return "VALUE_TYPE_PIPS"
        case "Text":
            return "VALUE_TYPE_TEXT"
        case "Text(code input)":
            return "VALUE_TYPE_TEXT_CODE_INPUT"
        case "Time":
            return "VALUE_TYPE_TIME"


# Correct string values that are expected with extra double quotations: "\"\""
def correct_double_quotation_strings(event, constants, variables):
    nodes = event.get("nodes")
    for node in nodes:
        if node.get("blockName") == "condition_1_normal" or node.get("blockName") == "condition_1_cross" or node.get(
                "blockName") == "Formula":
            add_extra_double_quotation_if_any(node.get("params").get("left").get("params"), constants, variables)
            add_extra_double_quotation_if_any(node.get("params").get("right").get("params"), constants, variables)
        else:
            add_extra_double_quotation_if_any(node.get("params"), constants, variables)


def add_extra_double_quotation_if_any(params, constants, variables):
    for key, value in params.items():
        match key:
            case "timestr_start" | "timestr_end" | "time_stamp" | "time_market" \
                 | "timestr" | "comment" | "obj_name" | "name_filter_mode" | "symbols_str":
                for constant in constants:
                    if constant.get("name") is value:
                        continue
                for variable in variables:
                    if variable.get("name") is value:
                        continue
                params[key] = '\"' + value + '\"'
            case "value":  # STest, in future this may make trouble. This supports Value class, text types
                if isinstance(value, str):
                    for constant in constants:
                        if constant.get("name") is value:
                            continue
                    for variable in variables:
                        if variable.get("name") is value:
                            continue
                    params[key] = '\"' + value + '\"'


def add_extra_double_quotation_vars_consts(constants, variables):
    for const in constants:
        if const.get("type").lower().strip() == "string":
            const["value"] = '\"' + const.get("value") + '\"'
    for variable in variables:
        if variable.get("type").lower().strip() == "string":
            variable["value"] = '\"' + variable.get("value") + '\"'


# Adds the input that are not passed by front end
def add_not_present_input(event):
    nodes = event.get("nodes")
    for node in nodes:
        if node.get("blockName") == "condition_1_normal" or node.get("blockName") == "condition_1_cross" or node.get(
                "blockName") == "Formula":
            params_main = node.get("params")
            left = params_main.get("left")
            right = params_main.get("right")
            check_condition_params(left)
            check_condition_params(right)
        else:
            path = path_root.get()
            path_sub = "/contents/"
            category = node.get("category")
            task_name = node.get("blockName")
            params = node.get("params")
            path_task_id = path + path_sub + "tasks" + "/" + category + "/" + task_name + "/"  # used to get data and fill template
            with open(path_task_id + "input.json") as input_file:
                if input_file:
                    input_text = input_file.read()
                    input_saved = json.loads(input_text)
                    replace_params(input_saved, params)


def check_condition_params(side):  # Side means left or right
    path = path_root.get()
    path_sub = "/contents/"
    path_module = ""
    params = side.get("params")
    match side.get("row1"):
        case "Indicator":
            path_module = "indicators" + "/" + side.get("row2").lower() + "/"
        case "Market Properties":
            path_module = "market_properties" + "/"
        case "Value":
            path_module = "value" + "/"
        case "Candle":
            path_module = "candle" + "/"
    with open(path + path_sub + path_module + "input.json") as input_file:
        if input_file:
            input_text = input_file.read()
            input_saved = json.loads(input_text)
            replace_params(input_saved, params)


def replace_params(input_saved, params):
    for key, value in input_saved.items():
        if key not in params:
            params[key] = value


def correct_enabled(data):
    events = data["events"]
    for key in events:
        for node in events[key]["nodes"]:
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


def set_blocks_input_dic(nodes, edges):
    for node in nodes:
        input_dic = {}
        input_dic["id"] = node.get("id")
        input_dic["id_by_user"] = node.get("id_by_user")
        input_dic["name"] = "\"" + node.get("blockName") + "\""
        input_dic["enabled"] = node.get("enabled")
        input_dic["nexts_true"] = get_nexts_true(node, edges)
        input_dic["nexts_false"] = get_nexts_false(node, edges)
        input_dic["prevs_true"] = get_prevs_true(node, edges)
        input_dic["prevs_false"] = get_prevs_false(node, edges)
        node["input_dic_block"] = input_dic


def overwrite_task_names(nodes):
    for node in nodes:
        block_name = node.get("blockName")
        if block_name == "condition":
            operator = node.get("params").get("operator").get("label")
            if operator == "×>" or operator == "×<":
                node["blockName"] = "condition_1_cross"
            else:
                node["blockName"] = "condition_1_normal"
        elif block_name == "Once per bar":
            node["blockName"] = "once_every_n_bars"
        elif block_name == "No trade nearby" or block_name == "No pending order nearby":
            node["blockName"] = "check_trades_orders_nearby"
        elif block_name == "turn_on_blocks" or block_name == "turn_off_blocks" or block_name == "toggle_blocks":
            node["blockName"] = "blocks_on_off"
        elif block_name == "Buy now":
            node["blockName"] = "buy_sell"
            node.get("params")["order_type"] = "ORDER_BUY"
        elif block_name == "Sell now":
            node["blockName"] = "buy_sell"
            node.get("params")["order_type"] = "ORDER_SELL"
        elif block_name == "Buy pending order":
            node["blockName"] = "buy_sell"
            node.get("params")["order_type"] = "ORDER_BUY_PENDING"
        elif block_name == "Sell pending order":
            node["blockName"] = "buy_sell"
            node.get("params")["order_type"] = "ORDER_SELL_PENDING"


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


def add_category(nodes):
    for node in nodes:
        match node.get("blockName"):
            case "condition":
                node["category"] = "condition_formula"
            case "formula":
                node["category"] = "condition_formula"
            case "time_filter":
                node["category"] = "time_filters"
            case "Once per bar":
                node["category"] = "time_filters"
            case "once_every_n_bars":
                node["category"] = "time_filters"
            case "once_per_seconds":
                node["category"] = "time_filters"
            case "every_n_ticks":
                node["category"] = "time_filters"
            case "in_hour_min_sec":
                node["category"] = "time_filters"
            case "months_filter":
                node["category"] = "time_filters"
            case "weekday_filter":
                node["category"] = "time_filters"
            case "spread_filter":
                node["category"] = "time_filters"
            case "and":
                node["category"] = "controlling_blocks"
            case "or":
                node["category"] = "controlling_blocks"
            case "turn_on_blocks":
                node["category"] = "controlling_blocks"
            case "turn_off_blocks":
                node["category"] = "controlling_blocks"
            case "toggle_blocks":
                node["category"] = "controlling_blocks"
            case "set_current_market_for_next_blocks":
                node["category"] = "controlling_blocks"
            case "set_current_timeframe_for_next_blocks":
                node["category"] = "controlling_blocks"
            case "pass_n_times":
                node["category"] = "counters"
            case "for_each_trade":
                node["category"] = "loop_for_trades_orders"
            case "close_partially":
                node["category"] = "loop_for_trades_orders"
            case "close":
                node["category"] = "loop_for_trades_orders"
            case "break":
                node["category"] = "loop_for_trades_orders"
            case "check_profit":
                node["category"] = "loop_for_trades_orders"
            case "check_loss":
                node["category"] = "loop_for_trades_orders"
            case "Buy now" | "Sell now" | "Buy pending order" | "Sell pending order":
                node["category"] = ""
            case "check_trades_orders_count" | "check_trades_orders_nearby":
                node["category"] = "check_trades_orders_count"
            case "close_trades":
                node["category"] = "trading_actions"
            case "delete_pending_orders":
                node["category"] = "trading_actions"
            case "modify_stops_of_trades":
                node["category"] = "trading_actions"
            case "check_profit_unrealized":
                node["category"] = "check_trading_conditions"
            case "delay":
                node["category"] = "more"
            case "pass":
                node["category"] = "more"
            case "modify_variables":
                node["category"] = "variables"
            case "break_even":
                node["category"] = "trailing_stop_break_even"
            case "trailing_stop_each_trade":
                node["category"] = "trailing_stop_break_even"
            case "trailing_pending_orders":
                node["category"] = "trailing_stop_break_even"
            case "comment":
                node["category"] = "output_and_communication"
            case "terminate":
                node["category"] = "more"
            case "draw_arrow":
                node["category"] = "chart_and_objects"
            case "draw_button":
                node["category"] = "chart_and_objects"
            case "draw_shape":
                node["category"] = "chart_and_objects"
            case "draw_line":
                node["category"] = "chart_and_objects"
            case "draw_editfield":
                node["category"] = "chart_and_objects"
            case "delete_objects":
                node["category"] = "chart_and_objects"
            case "delete_objects_by_type":
                node["category"] = "chart_and_objects"
            case "for_each_object":
                node["category"] = "loop_for_chart_objects"
            case "select_object_by_name":
                node["category"] = "loop_for_chart_objects"
            case "delete":
                node["category"] = "loop_for_chart_objects"
            case "once_per_object":
                node["category"] = "loop_for_chart_objects"
            case "check_color":
                node["category"] = "loop_for_chart_objects"
            case "check_trendline_price_level":
                node["category"] = "loop_for_chart_objects"
            case "editfield_modified":
                node["category"] = "on_chart_filter_specific_event"
            case "object_modified":
                node["category"] = "on_chart_filter_specific_event"
            case "mouse_clicked_on_object":
                node["category"] = "on_chart_filter_specific_event"
            case "object_dragged":
                node["category"] = "on_chart_filter_specific_event"
            case _:
                node["category"] = "not_specified"
