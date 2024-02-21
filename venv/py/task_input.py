import expert_helper


def set_task_input_dic(nodes):
    for node in nodes:
        match node.get("data").get("blockName"):
            case "pass_n_times":
                pass_n_times(node)
            case "once_every_n_bars":
                once_every_n_bars(node)
            case "once_per_seconds":
                once_per_seconds(node)
            case "every_n_ticks":
                every_n_ticks(node)
            case "in_hour_min_sec":
                in_hour_min_sec(node)
            case "months_filter":
                months_filter(node)
            case "weekday_filter":
                weekday_filter(node)
            case "spread_filter":
                spread_filter(node)
            case "condition_1_normal":
                condition_1_normal(node)
            case "condition_1_cross":
                condition_1_cross(node)
            case "formula":
                formula(node)
            case "buy_sell":
                buy_sell(node)
            case "check_trades_orders_count":
                check_trades_orders_count(node)
            case "check_trades_orders_nearby":
                check_trades_orders_nearby(node)
            case "close_trades":
                close_trades(node)
            case "delete_pending_orders":
                delete_pending_orders(node)
            case "check_profit_unrealized":
                check_profit_unrealized(node)
            case "for_each_trade":
                for_each_trade(node)
            case "delay":
                delay(node)
            case "pass":
                pass_task(node)
            case "modify_variables":
                modify_variables(node)
            case "blocks_on_off":
                blocks_on_off(node)
            case "break_even":
                break_even(node)
            case "trailing_stop_each_trade":
                trailing_stop_each_trade(node)
            case "trailing_pending_orders":
                trailing_pending_orders(node)
            case "comment":
                comment(node)
            case "close_partially":
                close_partially(node)
            case "close":
                close(node)
            case "check_profit":
                check_profit(node)
            case "check_loss":
                check_loss(node)
            case "time_filter":
                time_filter(node)
            case "modify_stops_of_trades":
                modify_stops_of_trades(node)
            case "terminate":
                terminate(node)
            case "set_current_market_for_next_blocks":
                set_current_market_for_next_blocks(node)
            case "set_current_timeframe_for_next_blocks":
                set_current_timeframe_for_next_blocks(node)
            case _:
                default(node)


def set_current_timeframe_for_next_blocks(node):
    more = node.get("more")
    input_dic = {}
    input_dic["timeframes"] = more.get("timeframes").get("value")
    node["input_dic_task"] = input_dic

def set_current_market_for_next_blocks(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbols_str"] = more.get("symbols_str").get("value")
    node["input_dic_task"] = input_dic


def terminate(node):
    more = node.get("more")
    input_dic = {}
    input_dic["message"] = more.get("message").get("value")
    node["input_dic_task"] = input_dic


def modify_stops_of_trades(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")

    input_dic["order_age_mins"] = more.get("order_age_mins").get("value")
    input_dic["relative_to"] = more.get("relative_to").get("value")
    input_dic["new_tpsl_mode"] = more.get("new_tpsl_mode").get("value")
    input_dic["new_stoploss"] = more.get("new_stoploss").get("value")
    input_dic["new_stoploss_percent"] = more.get("new_stoploss_percent").get("value")
    input_dic["new_takeprofit"] = more.get("new_takeprofit").get("value")
    input_dic["new_takeprofit_percent"] = more.get("new_takeprofit_percent").get("value")
    input_dic["level_color"] = more.get("level_color").get("value")

    node["input_dic_task"] = input_dic

    # Now fill input dic for value fetch if any
    relative_to_data = node.get("more").get("relative_to")
    relative_to = relative_to_data.get("value")
    if relative_to == "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL":
        value = relative_to_data.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        relative_to_data["input_dic"] = input_dic

    new_tpsl_mode_data = node.get("more").get("new_tpsl_mode")
    new_tpsl_mode = new_tpsl_mode_data.get("value")
    if new_tpsl_mode == "NEW_STOPS_CUSTOM_PRICE_LEVEL":
        value_tp = new_tpsl_mode_data.get("value_fetch_tp")
        params_tp = value_tp.get("params")
        input_dic_tp = value_fetch(node, params_tp, value_tp.get("row1").get("label"), value_tp.get("row2").get("name"))

        value_sl = new_tpsl_mode_data.get("value_fetch_sl")
        params_sl = value_sl.get("params")
        input_dic_sl = value_fetch(node, params_sl, value_sl.get("row1").get("label"), value_sl.get("row2").get("name"))

        new_tpsl_mode_data["input_dic_tp"] = input_dic_tp
        new_tpsl_mode_data["input_dic_sl"] = input_dic_sl


def trailing_pending_orders(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")

    input_dic["trailing_distance_mode"] = more.get("trailing_distance_mode").get("value")
    input_dic["t_distance_pips"] = more.get("t_distance_pips").get("value")
    input_dic["t_step_pips"] = more.get("t_step_pips").get("value")

    node["input_dic_task"] = input_dic

    # Now fill input dic for value fetch if any
    trailing_distance_mode_data = node.get("more").get("trailing_distance_mode")
    trailing_distance_mode = trailing_distance_mode_data.get("value")
    if trailing_distance_mode != "TRAILING_DISTANCE_MODE_FIXED":
        value = trailing_distance_mode_data.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        trailing_distance_mode_data["input_dic"] = input_dic


def time_filter(node):
    more = node.get("more")
    input_dic = {}
    input_dic["server_or_local_time"] = more.get("server_or_local_time").get("value")
    input_dic["time_start_mode"] = more.get("time_start_mode").get("value")
    input_dic["time_start"] = more.get("time_start").get("value")
    input_dic["time_start_year"] = more.get("time_start_year").get("value")
    input_dic["time_start_month"] = more.get("time_start_month").get("value")
    input_dic["time_start_day"] = more.get("time_start_day").get("value")
    input_dic["time_start_hour"] = more.get("time_start_hour").get("value")
    input_dic["time_start_minute"] = more.get("time_start_minute").get("value")
    input_dic["time_start_second"] = more.get("time_start_second").get("value")
    input_dic["time_end_mode"] = more.get("time_end_mode").get("value")
    input_dic["time_end"] = more.get("time_end").get("value")
    input_dic["time_end_year"] = more.get("time_end_year").get("value")
    input_dic["time_end_month"] = more.get("time_end_month").get("value")
    input_dic["time_end_day"] = more.get("time_end_day").get("value")
    input_dic["time_end_hour"] = more.get("time_end_hour").get("value")
    input_dic["time_end_minute"] = more.get("time_end_minute").get("value")
    input_dic["time_end_second"] = more.get("time_end_second").get("value")
    input_dic["time_end_rel_years"] = more.get("time_end_rel_years").get("value")
    input_dic["time_end_rel_months"] = more.get("time_end_rel_months").get("value")
    input_dic["time_end_rel_days"] = more.get("time_end_rel_days").get("value")
    input_dic["time_end_rel_hours"] = more.get("time_end_rel_hours").get("value")
    input_dic["time_end_rel_minutes"] = more.get("time_end_rel_minutes").get("value")
    input_dic["time_end_rel_seconds"] = more.get("time_end_rel_seconds").get("value")
    node["input_dic_task"] = input_dic


def check_loss(node):
    more = node.get("more")
    input_dic = {}
    input_dic["check_mode"] = more.get("check_mode").get("value")
    input_dic["check_value"] = more.get("check_value").get("value")
    input_dic["operator"] = more.get("operator").get("value")
    node["input_dic_task"] = input_dic


def check_profit(node):
    more = node.get("more")
    input_dic = {}
    input_dic["check_mode"] = more.get("check_mode").get("value")
    input_dic["check_value"] = more.get("check_value").get("value")
    input_dic["operator"] = more.get("operator").get("value")
    node["input_dic_task"] = input_dic


def close(node):
    more = node.get("more")
    input_dic = {}
    input_dic["slippage"] = more.get("slippage").get("value")
    input_dic["arrow_color"] = more.get("arrow_color").get("value")
    node["input_dic_task"] = input_dic


def close_partially(node):
    more = node.get("more")
    input_dic = {}
    input_dic["part_vol_mode"] = more.get("part_vol_mode").get("value")
    input_dic["part_vol_value"] = more.get("part_vol_value").get("value")
    input_dic["slippage"] = more.get("slippage").get("value")
    input_dic["arrow_color"] = more.get("arrow_color").get("value")
    node["input_dic_task"] = input_dic


def comment(node):
    more = node.get("more")
    input_dic = {}
    input_dic["Title"] = more.get("Title").get("value")
    input_dic["ObjChartSubWindow"] = more.get("ObjChartSubWindow").get("value")
    input_dic["ObjCorner"] = more.get("ObjCorner").get("value")
    input_dic["ObjX"] = more.get("ObjX").get("value")
    input_dic["ObjY"] = more.get("ObjY").get("value")
    input_dic["ObjTitleFont"] = more.get("ObjTitleFont").get("value")
    input_dic["ObjTitleFontColor"] = more.get("ObjTitleFontColor").get("value")
    input_dic["ObjTitleFontSize"] = more.get("ObjTitleFontSize").get("value")
    input_dic["ObjLabelsFont"] = more.get("ObjLabelsFont").get("value")
    input_dic["ObjLabelsFontColor"] = more.get("ObjLabelsFontColor").get("value")
    input_dic["ObjLabelsFontSize"] = more.get("ObjLabelsFontSize").get("value")
    input_dic["ObjFont"] = more.get("ObjFont").get("value")
    input_dic["ObjFontColor"] = more.get("ObjFontColor").get("value")
    input_dic["ObjFontSize"] = more.get("ObjFontSize").get("value")

    row1 = more.get("row1")
    input_dic["Label1"] = row1.get("Label").get("value")
    input_dic["FormatNumber1"] = row1.get("FormatNumber").get("value")
    input_dic["FormatTime1"] = row1.get("FormatTime").get("value")

    row2 = more.get("row2")
    input_dic["Label2"] = row2.get("Label").get("value")
    input_dic["FormatNumber2"] = row2.get("FormatNumber").get("value")
    input_dic["FormatTime2"] = row2.get("FormatTime").get("value")

    row3 = more.get("row3")
    input_dic["Label3"] = row3.get("Label").get("value")
    input_dic["FormatNumber3"] = row3.get("FormatNumber").get("value")
    input_dic["FormatTime3"] = row3.get("FormatTime").get("value")

    row4 = more.get("row4")
    input_dic["Label4"] = row4.get("Label").get("value")
    input_dic["FormatNumber4"] = row4.get("FormatNumber").get("value")
    input_dic["FormatTime4"] = row4.get("FormatTime").get("value")

    row5 = more.get("row5")
    input_dic["Label5"] = row5.get("Label").get("value")
    input_dic["FormatNumber5"] = row5.get("FormatNumber").get("value")
    input_dic["FormatTime5"] = row5.get("FormatTime").get("value")

    row6 = more.get("row6")
    input_dic["Label6"] = row6.get("Label").get("value")
    input_dic["FormatNumber6"] = row6.get("FormatNumber").get("value")
    input_dic["FormatTime6"] = row6.get("FormatTime").get("value")

    row7 = more.get("row7")
    input_dic["Label7"] = row7.get("Label").get("value")
    input_dic["FormatNumber7"] = row7.get("FormatNumber").get("value")
    input_dic["FormatTime7"] = row7.get("FormatTime").get("value")

    row8 = more.get("row8")
    input_dic["Label8"] = row8.get("Label").get("value")
    input_dic["FormatNumber8"] = row8.get("FormatNumber").get("value")
    input_dic["FormatTime8"] = row8.get("FormatTime").get("value")

    node["input_dic_task"] = input_dic

    # Now fill input task for value fetch if any
    if row1.get("Label").get("value") != "" and "value_fetch" in row1:
        value = row1.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row1["input_dic"] = input_dic

    if row2.get("Label").get("value") != "" and "value_fetch" in row2:
        value = row2.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row2["input_dic"] = input_dic

    if row3.get("Label").get("value") != "" and "value_fetch" in row3:
        value = row3.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row3["input_dic"] = input_dic

    if row4.get("Label").get("value") != "" and "value_fetch" in row4:
        value = row4.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row4["input_dic"] = input_dic

    if row5.get("Label").get("value") != "" and "value_fetch" in row5:
        value = row5.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row5["input_dic"] = input_dic

    if row6.get("Label").get("value") != "" and "value_fetch" in row6:
        value = row6.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row6["input_dic"] = input_dic

    if row7.get("Label").get("value") != "" and "value_fetch" in row7:
        value = row7.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row7["input_dic"] = input_dic

    if row8.get("Label").get("value") != "" and "value_fetch" in row8:
        value = row8.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        row8["input_dic"] = input_dic


def trailing_stop_each_trade(node):
    more = node.get("more")
    input_dic = {}
    # Filter params
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    # Trailing params
    input_dic["TrailWhat"] = more.get("TrailWhat").get("value")
    input_dic["TrailingReferencePrice"] = more.get("TrailingReferencePrice").get("value")
    input_dic["TrailingStopMode"] = more.get("TrailingStopMode").get("value")
    input_dic["tStopPips"] = more.get("tStopPips").get("value")
    input_dic["tStopMoney"] = more.get("tStopMoney").get("value")
    input_dic["tStopMultiple"] = more.get("tStopMultiple").get("value")
    input_dic["tStopPercentTP"] = more.get("tStopPercentTP").get("value")
    input_dic["tStopPercentProfit"] = more.get("tStopPercentProfit").get("value")
    input_dic["TrailingStepMode"] = more.get("TrailingStepMode").get("value")
    input_dic["tStepPips"] = more.get("tStepPips").get("value")
    input_dic["tStepPercentTS"] = more.get("tStepPercentTS").get("value")
    input_dic["TrailingStartMode"] = more.get("TrailingStartMode").get("value")
    input_dic["tStartPips"] = more.get("tStartPips").get("value")
    input_dic["tStartPercentTS"] = more.get("tStartPercentTS").get("value")
    input_dic["tStartPercentSL"] = more.get("tStartPercentSL").get("value")
    input_dic["tStartPercentTP"] = more.get("tStartPercentTP").get("value")
    input_dic["TrailingTPmode"] = more.get("TrailingTPmode").get("value")
    input_dic["tTPpips"] = more.get("tTPpips").get("value")
    input_dic["tTPpercentTS"] = more.get("tTPpercentTS").get("value")
    input_dic["LevelColor"] = more.get("LevelColor").get("value")

    node["input_dic_task"] = input_dic

    # Now fill input task for value fetch if any
    trailing_stop_mode_data = node.get("more").get("TrailingStopMode")
    trailing_stop_mode = trailing_stop_mode_data.get("value")
    if trailing_stop_mode == "TRAILING_STOP_MODE_CUSTOM_LEVEL":
        value = trailing_stop_mode_data.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        trailing_stop_mode_data["input_dic"] = input_dic


def break_even(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["on_profit_mode"] = more.get("on_profit_mode").get("value")
    input_dic["pips_on_profit"] = more.get("pips_on_profit").get("value")
    input_dic["bep_offset_mode"] = more.get("bep_offset_mode").get("value")
    input_dic["bep_offset"] = more.get("bep_offset").get("value")
    node["input_dic_task"] = input_dic


def spread_filter(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["spread_mode"] = more.get("spread_mode").get("value")
    input_dic["spread_benchmark_fix_value"] = more.get("spread_benchmark_fix_value").get("value")
    input_dic["average_spread_time_period"] = more.get("average_spread_time_period").get("value")
    input_dic["average_spread_adjust"] = more.get("average_spread_adjust").get("value")
    input_dic["operator"] = more.get("operator").get("value")
    node["input_dic_task"] = input_dic


def blocks_on_off(node):
    more = node.get("more")
    input_dic = {}
    input_dic["block_ids"] = more.get("block_ids").get("value")
    input_dic["what"] = more.get("what").get("value")
    node["input_dic_task"] = input_dic


def delay(node):
    more = node.get("more")
    input_dic = {}
    input_dic["sleep_seconds"] = more.get("sleep_seconds").get("value")
    input_dic["sleep_tester_normal"] = more.get("sleep_tester_normal").get("value")
    input_dic["sleep_tester_visual"] = more.get("sleep_tester_visual").get("value")
    node["input_dic_task"] = input_dic


def pass_task(node):
    node["input_dic_task"] = {}


def for_each_trade(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["loop_direction"] = more.get("loop_direction").get("value")
    input_dic["skip_n"] = more.get("skip_n").get("value")
    input_dic["not_more_than_n"] = more.get("not_more_than_n").get("value")
    input_dic["every_n"] = more.get("every_n").get("value")
    node["input_dic_task"] = input_dic


def check_profit_unrealized(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["profit_mode"] = more.get("profit_mode").get("value")
    input_dic["profit_benchmark_filter"] = more.get("profit_benchmark_filter").get("value")
    input_dic["profit_benchmark_comparison"] = more.get("profit_benchmark_comparison").get("value")
    input_dic["profit_filter_operator"] = more.get("profit_filter_operator").get("value")
    input_dic["profit_comparison_operator"] = more.get("profit_comparison_operator").get("value")
    node["input_dic_task"] = input_dic


def close_trades(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["older_than"] = more.get("older_than").get("value")
    input_dic["slippage"] = more.get("slippage").get("value")
    input_dic["arrow_color"] = more.get("arrow_color").get("value")
    node["input_dic_task"] = input_dic


def delete_pending_orders(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["arrow_color"] = more.get("arrow_color").get("value")

    node["input_dic_task"] = input_dic


def check_trades_orders_count(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["count_limit"] = more.get("count_limit").get("value")
    input_dic["operator"] = more.get("operator").get("value")
    node["input_dic_task"] = input_dic


def check_trades_orders_nearby(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group_mode"] = more.get("group_mode").get("value")
    input_dic["group_number"] = more.get("group_number").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["count_limit"] = more.get("count_limit").get("value")
    input_dic["operator"] = more.get("operator").get("value")

    input_dic["price_mode"] = more.get("price_mode").get("value")
    input_dic["range_mode"] = more.get("range_mode").get("value")
    input_dic["range_position"] = more.get("range_position").get("value")
    input_dic["range_value"] = more.get("range_value").get("value")

    node["input_dic_task"] = input_dic


def months_filter(node):
    more = node.get("more")
    input_dic = {}
    input_dic["months"] = more.get("months").get("value")
    node["input_dic_task"] = input_dic


def weekday_filter(node):
    more = node.get("more")
    input_dic = {}
    input_dic["time_mode"] = more.get("time_mode").get("value")
    input_dic["weekdays"] = more.get("weekdays").get("value")
    node["input_dic_task"] = input_dic


def in_hour_min_sec(node):
    more = node.get("more")
    input_dic = {}
    input_dic["time_mode"] = more.get("time_mode").get("value")
    input_dic["start_hour_1"] = more.get("start_hour_1").get("value")
    input_dic["end_hour_1"] = more.get("end_hour_1").get("value")
    input_dic["start_hour_2"] = more.get("start_hour_2").get("value")
    input_dic["end_hour_2"] = more.get("end_hour_2").get("value")
    input_dic["start_hour_3"] = more.get("start_hour_3").get("value")
    input_dic["end_hour_3"] = more.get("end_hour_3").get("value")
    input_dic["start_hour_4"] = more.get("start_hour_4").get("value")
    input_dic["end_hour_4"] = more.get("end_hour_4").get("value")
    node["input_dic_task"] = input_dic


def once_per_seconds(node):
    more = node.get("more")
    input_dic = {}
    input_dic["n"] = more.get("n").get("value")
    node["input_dic_task"] = input_dic


def every_n_ticks(node):
    more = node.get("more")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["n"] = more.get("n").get("value")
    node["input_dic_task"] = input_dic


def buy_sell(node):
    more = node.get("more")
    task_name = node.get("data").get("blockName")
    input_dic = {}
    input_dic["symbol"] = more.get("symbol").get("value")
    input_dic["group"] = more.get("group").get("value")
    input_dic["order_type"] = more.get("order_type").get("value")
    input_dic["money_management"] = more.get("money_management").get("value")
    input_dic["how_much_volume"] = more.get("how_much_volume").get("value")
    input_dic["volume_upper_limit"] = more.get("volume_upper_limit").get("value")
    input_dic["open_at_price"] = more.get("open_at_price").get("value")
    input_dic["price_offset"] = more.get("price_offset").get("value")
    input_dic["price_offset_as_pip"] = more.get("price_offset_as_pip").get("value")
    input_dic["slippage"] = more.get("slippage").get("value")
    input_dic["stoploss"] = more.get("stoploss").get("value")
    input_dic["takeprofit"] = more.get("takeprofit").get("value")
    input_dic["take_profit_mode"] = more.get("take_profit_mode").get("value")
    input_dic["stop_loss_mode"] = more.get("stop_loss_mode").get("value")
    input_dic["comment"] = more.get("comment").get("value")
    input_dic["expiration"] = more.get("expiration").get("value")
    input_dic["arrow_color"] = more.get("arrow_color").get("value")

    input_dic["look_up_on"] = more.get("look_up_on").get("value")
    input_dic["type"] = more.get("type").get("value")
    input_dic["martingale_init_vol"] = more.get("martingale_init_vol").get("value")
    input_dic["martingale_multiply_on_loss"] = more.get("martingale_multiply_on_loss").get("value")
    input_dic["martingale_multiply_on_profit"] = more.get("martingale_multiply_on_profit").get("value")
    input_dic["martingale_addlots_on_loss"] = more.get("martingale_addlots_on_loss").get("value")
    input_dic["martingale_addlots_on_profit"] = more.get("martingale_addlots_on_profit").get("value")
    input_dic["martingale_reset_on_n_losses"] = more.get("martingale_reset_on_n_losses").get("value")
    input_dic["martingale_reset_on_n_profits"] = more.get("martingale_reset_on_n_profits").get("value")

    node["input_dic_task"] = input_dic

    # Now fill input task for value fetch if any
    open_at_price_data = node.get("more").get("open_at_price")
    open_at_price = open_at_price_data.get("value")
    if open_at_price == "OPEN_AT_CUSTOM_PRICE":
        value = open_at_price_data.get("value_fetch")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        open_at_price_data["input_dic"] = input_dic


def modify_variables(node):
    node["input_dic_task"] = {}
    for item in node.get("items"):
        value = item.get("value")
        params = value.get("params")
        input_dic = value_fetch(node, params, value.get("row1").get("label"), value.get("row2").get("name"))
        item["input_dic"] = input_dic


def formula(node):
    node["input_dic_task"] = {}
    more = node.get("more")
    node["input_dic_left"] = value_fetch(node, more.get("left"), more.get("left1").get("label"),
                                         more.get("left2").get("name"))
    node["input_dic_right"] = value_fetch(node, more.get("right"), more.get("right1").get("label"),
                                          more.get("right2").get("name"))


def condition_1_normal(node):
    node["input_dic_task"] = {}
    more = node.get("more")
    node["input_dic_left"] = value_fetch(node, more.get("left"), more.get("left1").get("label"),
                                         more.get("left2").get("name"))
    node["input_dic_right"] = value_fetch(node, more.get("right"), more.get("right1").get("label"),
                                          more.get("right2").get("name"))


def condition_1_cross(node):
    node["input_dic_task"] = {}
    more = node.get("more")
    node["input_dic_left_1"] = value_fetch(node, more.get("left"), more.get("left1").get("label"),
                                           more.get("left2").get("name"))
    node["input_dic_left_2"] = input_cross(node, node.get("input_dic_left_1"))
    node["input_dic_right_1"] = value_fetch(node, more.get("right"), more.get("right1").get("label"),
                                            more.get("right2").get("name"))
    node["input_dic_right_2"] = input_cross(node, node.get("input_dic_right_1"))


def value_fetch(node, input_items, row1, row2):
    input_dic = {}
    for item in input_items:
        input_dic[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
            "value")  # STest, should be lowercase

    # handle this fucking candle id thing!
    # for condition
    if "more" in node and "candleIDLeft" in node.get("more"):
        input_dic["shift"] = node.get("more").get("candleIDLeft").get("value")
    # for modify variable
    if "items" in node:
        for item in node.get("items"):
            value = item.get("value")
            if "candleId" in value:
                input_dic["shift"] = item.get("value").get("candleId").get("value")

    if row1 == "Indicator":
        indicator_name = row2
        # STest, remove if statement below when no need
        if indicator_name == "rsi":
            input_dic["period"] = input_dic.get("rsi_period")
            input_dic.pop("rsi_period")
        # STest, remove when no need
        input_dic = expert_helper.correct_input_indicator(indicator_name, input_dic)
    elif row1 == "Value":
        input_dic = expert_helper.correct_input_value(input_dic)
    return input_dic


# A question is: what happens to cross if user adds say value at left?
# In my opinion cross appies to each side that supports candle id
# So if both sides support candle id, then cross applies to both sides.
# In the end, user is responsible for correctly using cross feature.
def input_cross(node, input_dic):
    # STest, remove later when added by backend
    if ("more" in node) and not ("cross_width" in node.get("more")):
        node.get("more")["cross_width"] = {"value": 1}

    input_dic_cross = input_dic.copy()
    if "shift" in input_dic_cross:
        input_dic_cross["shift"] = int(input_dic_cross["shift"]) + node.get("more").get("cross_width").get("value")

    return input_dic_cross


def pass_n_times(node):
    input_dic = {}
    input_dic["n"] = node.get("more").get("n").get("value")
    # set input dic
    node["input_dic_task"] = input_dic


def once_every_n_bars(node):
    input_dic = {}
    input_dic["symbol"] = "NULL"  # node.get("more").get("symbol").get("value")
    input_dic["timeframe"] = 0  # node.get("more").get("timeframe").get("value")
    input_dic["n"] = 1  # node.get("more").get("n").get("value")
    # set input dic
    node["input_dic_task"] = input_dic
    node.get("data")["blockName"] = "once_every_n_bars"


def default(node):
    node["input_dic_task"] = {}
