# This module adapts client data to mql generator
import task_input


def refactor(data):
    correct_events(data)
    correct_enabled(data)
    events = data["events"]
    for key in events:
        # Add indexes (overwrite ids) for later access
        event = events[key]
        overwrite_ids(event["nodes"], event["edges"])
        add_category(event["nodes"])
        overwrite_task_names(event["nodes"])
        # Block input_dic
        set_blocks_input_dic(event["nodes"], event["edges"])
        # Task input_dic
        task_input.set_task_input_dic(event["nodes"])
    return data

def correct_enabled(data):
    events = data["events"]
    for key in events:
        for node in events[key]["nodes"]:
            node["enabled"] = True

#STest, remove later
def correct_events (data):
    on_tick = {}
    on_tick["nodes"] = data.get("nodes")
    on_tick["edges"] = data.get("edges")
    data["events"] = {"on_tick": on_tick}
    data.pop("nodes")
    data.pop("edges")



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
        input_dic["id_by_user"] = node.get("data").get("blockId")
        input_dic["name"] = "\"" + node.get("data").get("blockName") + "\""
        input_dic["enabled"] = node.get("enabled")
        input_dic["nexts_true"] = get_nexts_true(node, nodes, edges)
        input_dic["nexts_false"] = get_nexts_false(node, nodes, edges)
        input_dic["prevs_true"] = get_prevs_true(node, nodes, edges)
        input_dic["prevs_false"] = get_prevs_false(node, nodes, edges)
        node["input_dic_block"] = input_dic

def overwrite_task_names (nodes):
    for node in nodes:
        block_name = node.get("data").get("blockName")
        if block_name == "condition1":
            operator = node.get("more").get("operator").get("label")
            if operator == "×>" or operator == "×<":
                node.get("data")["blockName"] = "condition_1_cross"
            else:
                node.get("data")["blockName"] = "condition_1_normal"
        elif block_name == "Once per bar":
            node.get("data")["blockName"] = "once_every_n_bars"
        elif block_name == "No trade nearby" or block_name=="No pending order nearby":
            node.get("data")["blockName"] = "check_trades_orders_nearby"
        elif block_name == "turn_on_blocks" or block_name=="turn_off_blocks" or block_name=="toggle_blocks":
            node.get("data")["blockName"] = "blocks_on_off"
        elif block_name == "Buy now" or block_name=="Sell now" or block_name=="Buy pending order" or block_name=="Sell pending order":
            node.get("data")["blockName"] = "buy_sell"
def get_nexts_true(node, nodes, edges):
    result = []
    for edge in edges:
        if edge.get("source") == node.get("id"):
            if edge.get("sourceHandle") == "blue":
                result.append(edge.get("target"))
    return result


def get_nexts_false(node, nodes, edges):
    result = []
    for edge in edges:
        if edge.get("source") == node.get("id"):
            if edge.get("sourceHandle") == "red":
                result.append(edge.get("target"))
    return result


def get_prevs_true(node, nodes, edges):
    result = []
    for edge in edges:
        if edge.get("target") == node.get("id"):
            if edge.get("sourceHandle") == "blue":
                result.append(edge.get("source"))
    return result


def get_prevs_false(node, nodes, edges):
    result = []
    for edge in edges:
        if edge.get("target") == node.get("id"):
            if edge.get("sourceHandle") == "red":
                result.append(edge.get("source"))
    return result

def add_category (nodes):
    for node in nodes:
        match node.get("data").get("blockName"):
            case "condition1":
                node["category"] = "condition_formula"
            case "formula":
                node["category"] = "condition_formula"
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
            case "pass_n_times":
                node["category"] = "counters"
            case "for_each_trade":
                node["category"] = "loop_for_trades_orders"
            case "break":
                node["category"] = "loop_for_trades_orders"
            case "Buy now" | "Sell now" | "Buy pending order" | "Sell pending order":
                node["category"] = ""
            case "check_trades_orders_count" | "check_trades_orders_nearby":
                node["category"] = "check_trades_orders_count"
            case "close_trades" | "delete_pending_orders":
                node["category"] = "trading_actions"
            case "check_profit_unrealized":
                node["category"] = "check_trading_conditions"
            case "delay":
                node["category"] = "more"
            case "pass":
                node["category"] = "more"
            case "modify_variables":
                node["category"] = "variables"
            case _:
                node["category"] = "not_specified"

