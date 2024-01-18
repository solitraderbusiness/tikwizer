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
            case "condition_1_normal":
                condition_1_normal(node)
            case "condition_1_cross":
                condition_1_cross(node)
            case "Buy now":
                buy_sell(node)
            case "Sell now":
                buy_sell(node)
            case "check_trades_orders_count":
                check_trades_orders_count(node)
            case "check_trades_orders_nearby":
                check_trades_orders_nearby(node)
            case "close_trades":
                close_trades(node)
            case "check_profit_unrealized":
                check_profit_unrealized(node)
            case "for_each_trade":
                for_each_trade(node)
            case "delay":
                delay(node)
            case "modify_variable":
                modify_variable(node)
            case _:
                default(node)


def modify_variable(node):
    items = node.get("items")
    # input_dic = {}
    # for item in items:
    #     row1 = item.get("value").get("row1")
    #     match row1:
    #         case "Indicator":





    input_dic["sleep_seconds"] = more.get("sleep_seconds").get("value")
    input_dic["sleep_tester_normal"] = more.get("sleep_tester_normal").get("value")
    input_dic["sleep_tester_visual"] = more.get("sleep_tester_visual").get("value")
    node["input_dic_task"] = input_dic


def delay(node):
    more = node.get("more")
    input_dic = {}
    input_dic["sleep_seconds"] = more.get("sleep_seconds").get("value")
    input_dic["sleep_tester_normal"] = more.get("sleep_tester_normal").get("value")
    input_dic["sleep_tester_visual"] = more.get("sleep_tester_visual").get("value")
    node["input_dic_task"] = input_dic


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
    if task_name == "Buy now":
        input_dic["cmd"] = "OP_BUY"
        input_dic["price"] = "Ask"
    elif task_name == "Sell now":
        input_dic["cmd"] = "OP_SELL"
        input_dic["price"] = "Bid"
    input_dic["volume"] = more.get("howMuch").get("value")
    input_dic["slippage"] = more.get("slippage").get("value")
    input_dic["stoploss"] = more.get("inPipStop").get("value")
    input_dic["takeprofit"] = more.get("inPipTake").get("value")
    input_dic["comment"] = more.get("comment").get("value")
    input_dic["magic"] = 10203015  # STest
    input_dic["expiration"] = 0  # STest
    input_dic["arrow_color"] = more.get("arrowColor").get("label")

    node["input_dic_task"] = input_dic
    node.get("data")["blockName"] = "buy_sell"


def condition_1_normal(node):
    node["input_dic_task"] = {}
    more = node.get("more")
    # left data
    left = more.get("left1").get("label")
    if left == "Indicator":
        indicator_name_left = more.get("left2").get("name").lower()
        input_dic_left = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, remove if statement below when no need
        if indicator_name_left == "rsi":
            input_dic_left["period"] = input_dic_left.get("rsi_period")
            input_dic_left.pop("rsi_period")
        # STest, below input item should be placed in input_item
        input_dic_left["shift"] = more.get("candleIDLeft").get("value")
        # STest, remove when no need
        input_dic_left = expert_helper.correct_input_indicator(indicator_name_left, input_dic_left)
        node["input_dic_left"] = input_dic_left
    elif left == "Candle":
        input_dic_left = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_left["shift"] = more.get("candleIDLeft").get("value")
        node["input_dic_left"] = input_dic_left
    elif left == "Market Properties":
        input_dic_left = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_left["shift"] = more.get("candleIDLeft").get("value")
        node["input_dic_left"] = input_dic_left
    elif left == "Value":
        input_dic_left = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        input_dic_left = expert_helper.correct_input_value(input_dic_left)
        node["input_dic_left"] = input_dic_left

    # right data
    right = more.get("right1").get("label")
    if right == "Indicator":
        indicator_name_right = more.get("right2").get("name").lower()
        input_dic_right = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, remove if statement below when no need
        if indicator_name_right == "rsi":
            input_dic_right["period"] = input_dic_right.get("rsi_period")
            input_dic_right.pop("rsi_period")
        # STest, below input item should be placed in input_item
        input_dic_right["shift"] = more.get("candleIDRight").get("value")
        # STest, remove when no need
        input_dic_right = expert_helper.correct_input_indicator(indicator_name_right, input_dic_right)
        node["input_dic_right"] = input_dic_right
    elif right == "Candle":
        input_dic_right = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_right["shift"] = more.get("candleIDRight").get("value")
        node["input_dic_right"] = input_dic_right
    elif right == "Market Properties":
        input_dic_right = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_right["shift"] = more.get("candleIDRight").get("value")
        node["input_dic_right"] = input_dic_right
    elif right == "Value":
        input_dic_right = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        input_dic_right = expert_helper.correct_input_value(input_dic_right)
        node["input_dic_right"] = input_dic_right


# A question is: what happens to cross if user adds say value at left?
# In my opinion cross appies to each side that supports candle id
# So if both sides support candle id, then cross applies to both sides.
# In the end, user is responsible for correctly using cross feature.
def condition_1_cross(node):
    node["input_dic_task"] = {}
    more = node.get("more")

    # STest, remove later when added by backend
    if not "cross_width" in more:
        more["cross_width"] = {"value": 1}

    # left data
    left = more.get("left1").get("label")
    if left == "Indicator":
        indicator_name_left = more.get("left2").get("name").lower()
        input_dic_left_1 = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, remove if statement below when no need
        if indicator_name_left == "rsi":
            input_dic_left_1["period"] = input_dic_left_1.get("rsi_period")
            input_dic_left_1.pop("rsi_period")
        # STest, below input item should be placed in input_item
        input_dic_left_1["shift"] = more.get("candleIDLeft").get("value")
        # STest, remove when no need
        input_dic_left_1 = expert_helper.correct_input_indicator(indicator_name_left, input_dic_left_1)
        input_dic_left_2 = input_dic_left_1.copy()
        input_dic_left_2["shift"] = str(int(input_dic_left_2["shift"]) + more.get("cross_width").get("value"))
        # Assign the input dic
        node["input_dic_left_1"] = input_dic_left_1
        node["input_dic_left_2"] = input_dic_left_2
    elif left == "Candle":
        input_dic_left_1 = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_left_1["shift"] = more.get("candleIDLeft").get("value")
        input_dic_left_2 = input_dic_left_1.copy()
        input_dic_left_2["shift"] = str(int(input_dic_left_2["shift"]) + more.get("cross_width").get("value"))
        # Assign the input dic
        node["input_dic_left_1"] = input_dic_left_1
        node["input_dic_left_2"] = input_dic_left_2
    elif left == "Market Properties":
        input_dic_left_1 = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_left_1["shift"] = more.get("candleIDLeft").get("value")
        input_dic_left_2 = input_dic_left_1.copy()
        node["input_dic_left_1"] = input_dic_left_1
        node["input_dic_left_2"] = input_dic_left_2
    elif left == "Value":
        input_dic_left_1 = {}
        input_items_left = more.get("left")
        for item in input_items_left:
            input_dic_left_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        input_dic_left_1 = expert_helper.correct_input_value(input_dic_left_1)
        input_dic_left_2 = input_dic_left_1.copy()
        node["input_dic_left_1"] = input_dic_left_1
        node["input_dic_left_2"] = input_dic_left_2

    # right data
    right = more.get("right1").get("label")
    if right == "Indicator":
        indicator_name_right = more.get("right2").get("name").lower()
        input_dic_right_1 = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, remove if statement below when no need
        if indicator_name_right == "rsi":
            input_dic_right_1["period"] = input_dic_right_1.get("rsi_period")
            input_dic_right_1.pop("rsi_period")
        # STest, below input item should be placed in input_item
        input_dic_right_1["shift"] = more.get("candleIDRight").get("value")
        # STest, remove when no need
        input_dic_right_1 = expert_helper.correct_input_indicator(indicator_name_right, input_dic_right_1)
        input_dic_right_2 = input_dic_right_1.copy()
        input_dic_right_2["shift"] = str(int(input_dic_right_2["shift"]) + more.get("cross_width").get("value"))
        # Assign the input dic
        node["input_dic_right_1"] = input_dic_right_1
        node["input_dic_right_2"] = input_dic_right_2
    elif right == "Candle":
        input_dic_right_1 = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_right_1["shift"] = more.get("candleIDRight").get("value")
        input_dic_right_2 = input_dic_right_1.copy()
        input_dic_right_2["shift"] = str(int(input_dic_right_2["shift"]) + more.get("cross_width").get("value"))
        # Assign the input dic
        node["input_dic_right_1"] = input_dic_right_1
        node["input_dic_right_2"] = input_dic_right_2
    elif right == "Market Properties":
        input_dic_right_1 = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        # STest, below input item should be placed in input_item
        input_dic_right_1["shift"] = more.get("candleIDRight").get("value")
        input_dic_right_2 = input_dic_right_1.copy()
        node["input_dic_right_1"] = input_dic_right_1
        node["input_dic_right_2"] = input_dic_right_2
    elif right == "Value":
        input_dic_right_1 = {}
        input_items_right = more.get("right")
        for item in input_items_right:
            input_dic_right_1[item.get("optionName").lower().replace(" ", "_")] = item.get("value").get(
                "value")  # STest, should be lowercase
        input_dic_right_1 = expert_helper.correct_input_value(input_dic_right_1)
        input_dic_right_2 = input_dic_right_1.copy()
        node["input_dic_right_1"] = input_dic_right_1
        node["input_dic_right_2"] = input_dic_right_2


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
