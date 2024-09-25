# node is entry if is not target and has target
from . import path_root


def is_entry(id_node, edges):
    is_target = False
    for edge in edges:
        if id_node == edge.get("target"):
            is_target = True
            break
    if is_target:
        return False
    has_target = False
    for edge in edges:
        if id_node == edge.get("source"):
            has_target = True
            break
    return has_target


def get_entries_sorted(nodes, edges):
    entries = []
    for node in nodes:
        id_node = node.get("id")
        if is_entry(id_node, edges):
            entries.append(id_node)
    entries.sort()
    return entries


def get_version():
    path = path_root.get()
    with open(path + "/.project-version") as version_file:
        if version_file:
            lines = version_file.read().split('\n')
            commented_lines = ['//' + line for line in lines]
            return "\n\n\n" + '\n'.join(commented_lines)


def handle_const_var_value(data):
    if data.get("value").strip():
        if data.get("type").strip() in ["enum", "struct"]:
            return " " + str(data.get("value"))
        else:
            return " = " + str(data.get("value"))
    return ""


class ExpertBuilder:
    from . import block_constructor
    from . import task_dynamic_constructor
    from . import global_functions
    from . import constants_constructor
    from . import global_vars
    from . import indicator_class_constructor
    from . import candle_class_constructor
    from . import value_class_constructor
    from . import market_properties_class_constructor_new
    from . import object_on_the_chart_class_constructor
    from . import trade_order_in_loop_class_constructor
    from . import account_class_constructor
    from . import spread_filter_struct_constructor
    from . import on_trade_event_detector_class_constructor
    from . import close_partially_items
    from . import volume_profile_items

    def __init__(self, data):
        self.data = data
        self.header = ""
        self.properties = []
        self.consts_system = []
        self.project_options = []
        self.consts_user = []
        self.vars_system = []
        self.vars_user = []
        self.classes_structs_enums = []
        self.block_parent_blueprint = ""
        self.task_blueprint = ""
        self.task_elements = []
        self.tasks = []
        self.block_blueprint = ""
        self.blocks = []
        self.functions = []
        self.on_init = []
        self.on_timer = []
        self.on_tick = []
        self.on_trade = []
        self.on_chart = []
        self.on_deinit = []

        self.and_done = False
        self.spread_filter_done = False
        self.close_partially_done = False
        self.volume_profile_done = False

    # Main function
    def process_input(self):
        self.add_header()
        self.add_global_functions(self.data)
        self.add_global_classes_structs()
        self.add_consts_system()
        self.add_consts_user(self.data.get("constants"))
        self.add_vars_system()
        self.add_vars_user(self.data.get("variables"))
        self.add_blueprints()
        self.process_blocks_tick(self.data.get("events").get("on_tick"))
        self.process_blocks_chart(self.data.get("events").get("on_chart"))
        self.process_blocks_trade(self.data.get("events").get("on_trade"))
        self.process_blocks_timer(self.data.get("events").get("on_timer"))
        self.process_blocks_deinit(self.data.get("events").get("on_deinit"))
        self.process_blocks_init(self.data.get("events").get("on_init"))

        return self.build()

    def add_header(self):
        self.header += "//+------------------------------------------------------------------+\n//|                                                                  |\n//|                   Copyright 2023-2024, tikwizer.com              |\n//|                                                                  |\n//+------------------------------------------------------------------+\n\n"

    def add_blueprints(self):
        # Add block_parent and task class blueprint
        self.block_parent_blueprint += self.block_constructor.get_block_parent()
        # Add task blueprint
        self.task_blueprint = self.task_dynamic_constructor.get_task()
        # Add block blueprint
        self.block_blueprint = self.block_constructor.get_block()

    def process_blocks_tick(self, data):
        if data is None:
            return

        nodes = data.get("nodes")
        edges = data.get("edges")

        # Find entries
        entries = get_entries_sorted(nodes, edges)

        self.add_task_elements_common(nodes)
        self.add_task_elements_specific(nodes)

        # Add tasks
        for node in nodes:
            task = self.get_task_child(node.get("blockName"), node)
            self.tasks.append(task)

        # Add blocks and tasks
        for node in nodes:
            block = self.get_block_child(node.get("blockName"), node.get("input_dic_block"), node.get("id_by_user"))
            self.blocks.append(block)

        # addBlocks call
        call_add_blocks = self.global_functions.get_call__add_blocks_tick()
        self.on_init.append(call_add_blocks)

        self.on_tick.append("   ticks_from_start++;\n")

        self.on_tick.append("if (DRAW_SPREAD_INFO) DrawSpreadInfo();\n")
        self.on_tick.append("	if (ENABLE_STATUS && ticks_from_start == 1) DrawStatus(\"working\");\n")

        self.on_tick.append("TicksData(""); // Collect ticks in case we need it\n")

        # resetBlocks call
        call_reset_blocks = self.global_functions.get_call__reset_blocks_tick()
        self.on_tick.append(call_reset_blocks)

        # runBlocks call
        for id_block in entries:
            call_run_block = self.global_functions.get_call__run_block_tick(-1, -1, id_block)
            self.on_tick.append(call_run_block)

        # append OnTrade call
        self.on_tick.append("   if(ArraySize(blocks_trade)>0)\n      OnTrade();")

    def process_blocks_chart(self, data):
        if data is None:
            return

        nodes = data.get("nodes")
        edges = data.get("edges")

        # Find entries
        entries = get_entries_sorted(nodes, edges)

        self.add_task_elements_common(nodes)
        self.add_task_elements_specific(nodes)

        # Add tasks
        for node in nodes:
            task = self.get_task_child(node.get("blockName"), node)
            self.tasks.append(task)

        # Add blocks and tasks
        for node in nodes:
            block = self.get_block_child(node.get("blockName"), node.get("input_dic_block"), node.get("id_by_user"))
            self.blocks.append(block)

        # addBlocks call
        call_add_blocks = self.global_functions.get_call__add_blocks_chart()
        self.on_init.append(call_add_blocks)

        hold_events = "\n//hold event params then process blocks\n   onchartEventHolder.id     = id;\n   onchartEventHolder.lparam = lparam;\n   onchartEventHolder.dparam = dparam;\n   onchartEventHolder.sparam = sparam;"
        self.on_chart.append(hold_events)

        # resetBlocks call
        call_reset_blocks = self.global_functions.get_call__reset_blocks_chart()
        self.on_chart.append(call_reset_blocks)

        # runBlocks call
        for id_block in entries:
            call_run_block = self.global_functions.get_call__run_block_chart(-1, -1, id_block)
            self.on_chart.append(call_run_block)

    def process_blocks_init(self, data):
        if data is None:
            return

        nodes = data.get("nodes")
        edges = data.get("edges")

        # Find entries
        entries = get_entries_sorted(nodes, edges)

        self.add_task_elements_common(nodes)
        self.add_task_elements_specific(nodes)

        # Add tasks
        for node in nodes:
            task = self.get_task_child(node.get("blockName"), node)
            self.tasks.append(task)

        # Add blocks and tasks
        for node in nodes:
            block = self.get_block_child(node.get("blockName"), node.get("input_dic_block"), node.get("id_by_user"))
            self.blocks.append(block)

        spread_meter_check = "\tif (ENABLE_SPREAD_METER == false) {\n\t\tDRAW_SPREAD_INFO = false;\n\t}\n\telse {\n\t\tDRAW_SPREAD_INFO = !(MQLInfoInteger(MQL_TESTER) && !MQLInfoInteger(MQL_VISUAL_MODE));\n\t}\n\tif (DRAW_SPREAD_INFO) DrawSpreadInfo();"
        self.on_init.append(spread_meter_check)

        draw_status_check = "if (ENABLE_STATUS) DrawStatus(\"waiting for tick...\");"
        self.on_init.append(draw_status_check)

        # handle show indicator after test in project options
        show_indicator_code = "	TesterHideIndicators(!ENABLE_TEST_INDICATORS);\n"
        self.on_init.append(show_indicator_code)

        # set expert start time
        self.on_init.append("\n	TimeAtStart(\"set\");\n")

        # addBlocks call
        call_add_blocks = self.global_functions.get_call__add_blocks_init()
        self.on_init.append(call_add_blocks)

        # resetBlocks call
        call_reset_blocks = self.global_functions.get_call__reset_blocks_init()
        self.on_init.append(call_reset_blocks)

        # runBlocks call
        for id_block in entries:
            call_run_block = self.global_functions.get_call__run_block_init(-1, -1, id_block)
            self.on_init.append(call_run_block)

    def process_blocks_timer(self, data):
        if data is None:
            return

        nodes = data.get("nodes")
        edges = data.get("edges")

        # Find entries
        entries = get_entries_sorted(nodes, edges)

        self.add_task_elements_common(nodes)
        self.add_task_elements_specific(nodes)

        # Add tasks
        for node in nodes:
            task = self.get_task_child(node.get("blockName"), node)
            self.tasks.append(task)

        # Add blocks and tasks
        for node in nodes:
            block = self.get_block_child(node.get("blockName"), node.get("input_dic_block"), node.get("id_by_user"))
            self.blocks.append(block)

        # addBlocks call
        call_add_blocks = self.global_functions.get_call__add_blocks_timer()
        self.on_init.append(call_add_blocks)

        self.on_timer.append(
            "   static datetime t0 = 0;\n   datetime t = 0;\n   bool ok = false;\n\n   if(ONTIMER_TAKEN)\n     {\n      if(ONTIMER_TAKEN_TIME > 0)\n        {\n         if(ONTIMER_TAKEN_IN_MILLISECONDS == true)\n           {\n            t = GetTickCount();\n           }\n         else\n           {\n            t = TimeLocal();\n           }\n         if((t - t0) >= ONTIMER_TAKEN_TIME)\n           {\n            t0 = t;\n            ok = true;\n           }\n        }\n\n      if(ok == false)\n        {\n         return;\n        }\n     }\n")

        # resetBlocks call
        call_reset_blocks = self.global_functions.get_call__reset_blocks_timer()
        self.on_timer.append(call_reset_blocks)

        # runBlocks call
        for id_block in entries:
            call_run_block = self.global_functions.get_call__run_block_timer(-1, -1, id_block)
            self.on_timer.append(call_run_block)

    def process_blocks_trade(self, data):
        if data is None:
            return

        nodes = data.get("nodes")
        edges = data.get("edges")

        # Find entries
        entries = get_entries_sorted(nodes, edges)

        self.add_task_elements_common(nodes)
        self.add_task_elements_specific(nodes)

        # Add tasks
        for node in nodes:
            task = self.get_task_child(node.get("blockName"), node)
            self.tasks.append(task)

        # Add blocks and tasks
        for node in nodes:
            block = self.get_block_child(node.get("blockName"), node.get("input_dic_block"), node.get("id_by_user"))
            self.blocks.append(block)

        # addBlocks call
        call_add_blocks = self.global_functions.get_call__add_blocks_trade()
        self.on_init.append(call_add_blocks)

        # prevent run if there are no blocks (important)
        self.on_trade.append("   if(ArraySize(blocks_trade)<=0)\n      return;\n      ")

        # resetBlocks call
        call_reset_blocks = self.global_functions.get_call__reset_blocks_trade()
        self.on_trade.append(call_reset_blocks)

        # runBlocks call
        self.on_trade.append("   while(onTradeEventDetector.Start())\n{\n")
        for id_block in entries:
            call_run_block = self.global_functions.get_call__run_block_trade(-1, -1, id_block)
            self.on_trade.append(call_run_block)
        self.on_trade.append("     }\n\n    onTradeEventDetector.End();")

    def process_blocks_deinit(self, data):
        if data is None:
            return

        nodes = data.get("nodes")
        edges = data.get("edges")

        # Find entries
        entries = get_entries_sorted(nodes, edges)

        self.add_task_elements_common(nodes)
        self.add_task_elements_specific(nodes)

        # Add tasks
        for node in nodes:
            task = self.get_task_child(node.get("blockName"), node)
            self.tasks.append(task)

        # Add blocks and tasks
        for node in nodes:
            block = self.get_block_child(node.get("blockName"), node.get("input_dic_block"), node.get("id_by_user"))
            self.blocks.append(block)

        # addBlocks call
        call_add_blocks = self.global_functions.get_call__add_blocks_deinit()
        self.on_init.append(call_add_blocks)

        self.on_deinit.append("   if(ENABLE_STATUS)\n   DrawStatus(\"stopped\");")

        self.on_deinit.append("   if(ENABLE_SPREAD_METER)\n      DrawSpreadInfo();\n")

        self.on_deinit.append("   EventKillTimer();\n")

        # resetBlocks call
        call_reset_blocks = self.global_functions.get_call__reset_blocks_deinit()
        self.on_deinit.append(call_reset_blocks)

        # runBlocks call
        for id_block in entries:
            call_run_block = self.global_functions.get_call__run_block_deinit(-1, -1, id_block)
            self.on_deinit.append(call_run_block)

    def add_vars_system(self):
        # blocks_tick var
        blocks_vars = self.global_vars.get__blocks()
        self.vars_system.append(blocks_vars)

        # overriding_symbol
        overriding_symbol = self.global_vars.get__overriding_symbol()
        self.vars_system.append(overriding_symbol)

        # overriding_timeframe
        overriding_timeframe = self.global_vars.get__overriding_timeframe()
        self.vars_system.append(overriding_timeframe)

        # onchartEventHolder
        onchart_event_holder = self.global_vars.get__onchart_event_holder()
        self.vars_system.append(onchart_event_holder)

        on_trade_event_detector_var = self.on_trade_event_detector_class_constructor.get_var()
        self.vars_system.append(on_trade_event_detector_var)

        exit_loop_var = self.global_vars.get__exit_loop()
        self.vars_system.append(exit_loop_var)

        timer_period = self.global_vars.get__timer_period()
        on_timer_period = self.data.get("project_options").get("magic_and_other").get("on_timer_period")
        timer_period = timer_period.replace("user_timer_period", str(on_timer_period))
        self.vars_system.append(timer_period)

        spread_info = "bool DRAW_SPREAD_INFO   = false;"
        self.vars_system.append(spread_info)

        ticks_from_start = "int ticks_from_start    = 0;"
        self.vars_system.append(ticks_from_start)

    def add_vars_user(self, mvars):
        for var in mvars:
            var_str = var.get("type") + " " + var.get("name") + handle_const_var_value(var) + "; // " + var.get(
                "description") + "\n"
            self.vars_user.append(var_str)

    def add_consts_system(self):
        rule = self.data.get("project_options").get("pip_size").get("rules")
        spread = self.data.get("project_options").get("visual").get("display_spread_meter")
        status = self.data.get("project_options").get("visual").get("display_status_messages")
        show_indicator = self.data.get("project_options").get("visual").get("display_indicators_after_test")
        self.consts_system.extend(self.constants_constructor.get_constants(rule, spread, status, show_indicator))

    def add_consts_user(self, const_inputs):  # Defined by user
        for my_input in const_inputs:
            input_str = "extern " + my_input.get("type") + " " + my_input.get("name") \
                        + handle_const_var_value(my_input) + "; // " + my_input.get("description") + "\n"
            self.consts_user.append(input_str)

        magic_number = self.data.get("project_options").get("magic_and_other").get("magic_number")
        user_magic = "input int user_magic = " + str(magic_number) + ";\n"
        self.consts_system.append(user_magic)

    def add_global_functions(self, data):
        # AddToArray function
        fun_add_to_array = self.global_functions.get_fun__add_to_array()
        self.functions.append(fun_add_to_array)

        # RemoveIndexFromArray function
        fun_remove_index_from_array = self.global_functions.get_fun__remove_index_from_array()
        self.functions.append(fun_remove_index_from_array)

        # joinArrays function
        fun_join_arrays = self.global_functions.get_fun__join_arrays()
        self.functions.append(fun_join_arrays)

        # areAllItemsPresent function
        are_all_items_present = self.global_functions.get_fun__are_all_items_present()
        self.functions.append(are_all_items_present)

        # runBlock function tick ##############################
        fun_run_block_tick = self.global_functions.get_fun__run_block_tick()
        self.functions.append(fun_run_block_tick)

        # addBlocks function tick
        fun_add_blocks_tick = self.global_functions.get_fun__add_blocks_tick(
            data.get("events").get("on_tick").get("nodes"))
        self.functions.append(fun_add_blocks_tick)

        # resetBlocks function tick
        fun_reset_blocks_tick = self.global_functions.get_fun__reset_blocks_tick()
        self.functions.append(fun_reset_blocks_tick)

        # runBlock function chart ##############################
        fun_run_block_chart = self.global_functions.get_fun__run_block_chart()
        self.functions.append(fun_run_block_chart)

        # addBlocks function chart
        fun_add_blocks_chart = self.global_functions.get_fun__add_blocks_chart(
            data.get("events").get("on_chart").get("nodes"))
        self.functions.append(fun_add_blocks_chart)

        # resetBlocks function chart
        fun_reset_blocks_chart = self.global_functions.get_fun__reset_blocks_chart()
        self.functions.append(fun_reset_blocks_chart)

        # runBlock function trade ##############################
        fun_run_block_trade = self.global_functions.get_fun__run_block_trade()
        self.functions.append(fun_run_block_trade)

        # addBlocks function trade
        fun_add_blocks_trade = self.global_functions.get_fun__add_blocks_trade(
            data.get("events").get("on_trade").get("nodes"))
        self.functions.append(fun_add_blocks_trade)

        # resetBlocks function trade
        fun_reset_blocks_trade = self.global_functions.get_fun__reset_blocks_trade()
        self.functions.append(fun_reset_blocks_trade)

        # runBlock function timer ##############################
        fun_run_block_timer = self.global_functions.get_fun__run_block_timer()
        self.functions.append(fun_run_block_timer)

        # addBlocks function timer
        fun_add_blocks_timer = self.global_functions.get_fun__add_blocks_timer(
            data.get("events").get("on_timer").get("nodes"))
        self.functions.append(fun_add_blocks_timer)

        # resetBlocks function timer
        fun_reset_blocks_timer = self.global_functions.get_fun__reset_blocks_timer()
        self.functions.append(fun_reset_blocks_timer)

        # runBlock function init ##############################
        fun_run_block_init = self.global_functions.get_fun__run_block_init()
        self.functions.append(fun_run_block_init)

        # addBlocks function init
        fun_add_blocks_init = self.global_functions.get_fun__add_blocks_init(
            data.get("events").get("on_init").get("nodes"))
        self.functions.append(fun_add_blocks_init)

        # resetBlocks function init
        fun_reset_blocks_init = self.global_functions.get_fun__reset_blocks_init()
        self.functions.append(fun_reset_blocks_init)

        # runBlock function deinit ##############################
        fun_run_block_deinit = self.global_functions.get_fun__run_block_deinit()
        self.functions.append(fun_run_block_deinit)

        # addBlocks function deinit
        fun_add_blocks_deinit = self.global_functions.get_fun__add_blocks_deinit(
            data.get("events").get("on_deinit").get("nodes"))
        self.functions.append(fun_add_blocks_deinit)

        # resetBlocks function deinit
        fun_reset_blocks_deinit = self.global_functions.get_fun__reset_blocks_deinit()
        self.functions.append(fun_reset_blocks_deinit)

        # syncSymbolOverriding function
        fun_sync_symbol_overriding = self.global_functions.get_fun__sync_symbol_overriding()
        self.functions.append(fun_sync_symbol_overriding)

        # syncTimeframeOverriding function
        fun_sync_timeframe_overriding = self.global_functions.get_fun__sync_timeframe_overriding()
        self.functions.append(fun_sync_timeframe_overriding)

        # TimeFromString function
        fun_time_from_string = self.global_functions.get_fun__time_from_string()
        self.functions.append(fun_time_from_string)

        # TimeFromComponent function
        fun_time_from_components = self.global_functions.get_fun__time_from_components()
        self.functions.append(fun_time_from_components)

        # getGroupNumber function
        fun_get_group_number = self.global_functions.get_fun__get_group_number()
        self.functions.append(fun_get_group_number)

        # sameOrderType function
        fun_same_order_type = self.global_functions.get_fun__same_order_type()
        self.functions.append(fun_same_order_type)

        # isAutomated function
        fun_is_automated = self.global_functions.get_fun__is_automated()
        self.functions.append(fun_is_automated)

        # ReverseList function
        fun_reverse_list = self.global_functions.get_fun__reverse_list()
        self.functions.append(fun_reverse_list)

        # sleepex function
        fun_sleepex = self.global_functions.get_fun__sleepex()
        self.functions.append(fun_sleepex)

        # delete order function
        delete_order = self.global_functions.get_fun__delete_order()
        self.functions.append(delete_order)

        # wait trade context if busy function
        wait_trade_context_if_busy = self.global_functions.get_fun__wait_trade_context_if_busy()
        self.functions.append(wait_trade_context_if_busy)

        # check for trading error function
        check_for_trading_error = self.global_functions.get_fun__check_for_trading_error()
        self.functions.append(check_for_trading_error)

        # error message function
        error_message = self.global_functions.get_fun__error_message()
        self.functions.append(error_message)

        # Buy Sell + Pending + Money Management functions

        bet_martingale = self.global_functions.get_fun__bet_martingale()
        self.functions.append(bet_martingale)

        get_bet_trades_info = self.global_functions.get_fun__get_bet_trades_info()
        self.functions.append(get_bet_trades_info)

        trade_select_by_index = self.global_functions.get_fun__trade_select_by_index()
        self.functions.append(trade_select_by_index)

        history_trade_select_by_index = self.global_functions.get_fun__history_trade_select_by_index()
        self.functions.append(history_trade_select_by_index)

        filter_general = self.global_functions.get_fun__filter_general()
        self.functions.append(filter_general)

        symbol_digits = self.global_functions.get_fun__symbol_digits()
        self.functions.append(symbol_digits)

        is_order_type_sell = self.global_functions.get_fun__is_order_type_sell()
        self.functions.append(is_order_type_sell)

        dynamic_lots = self.global_functions.get_fun__dynamic_lots()
        self.functions.append(dynamic_lots)

        pip_value = self.global_functions.get_fun__pip_value()
        self.functions.append(pip_value)

        custom_point = self.global_functions.get_fun__custom_point()
        self.functions.append(custom_point)

        string_explode = self.global_functions.get_fun__string_explode()
        self.functions.append(string_explode)

        to_digits = self.global_functions.get_fun__to_digits()
        self.functions.append(to_digits)

        string_trim = self.global_functions.get_fun__string_trim()
        self.functions.append(string_trim)

        format_value_for_printing_all = self.global_functions.get_fun__format_value_for_printing_all()
        self.functions.append(format_value_for_printing_all)

        window_find_visible = self.global_functions.get_fun__window_find_visible()
        self.functions.append(window_find_visible)

        symbol_ask = self.global_functions.get_fun__symbol_ask()
        self.functions.append(symbol_ask)

        symbol_bid = self.global_functions.get_fun__symbol_bid()
        self.functions.append(symbol_bid)

        is_order_type_buy = self.global_functions.get_fun__is_order_type_buy()
        self.functions.append(is_order_type_buy)

        is_order_type_stop = self.global_functions.get_fun__is_order_type_stop()
        self.functions.append(is_order_type_stop)

        is_order_type_limit = self.global_functions.get_fun__is_order_type_limit()
        self.functions.append(is_order_type_limit)

        get_symbol = self.global_functions.get_fun__get_symbol()
        self.functions.append(get_symbol)

        get_timeframe = self.global_functions.get_fun__get_timeframe()
        self.functions.append(get_timeframe)

        is_symbol_accepted = self.global_functions.get_fun__is_symbol_accepted()
        self.functions.append(is_symbol_accepted)

        is_symbol_accepted_on_trade = self.global_functions.get_fun__is_symbol_accepted_on_trade()
        self.functions.append(is_symbol_accepted_on_trade)

        seconds_from_components = self.global_functions.get_fun__seconds_from_components()
        self.functions.append(seconds_from_components)

        load_object = self.global_functions.get_fun__load_object()
        self.functions.append(load_object)

        loaded_object_chart_id = self.global_functions.get_fun__loaded_object_chart_id()
        self.functions.append(loaded_object_chart_id)

        loaded_object_name = self.global_functions.get_fun__loaded_object_name()
        self.functions.append(loaded_object_name)

        loaded_object_subwindow = self.global_functions.get_fun__loaded_object_subwindow()
        self.functions.append(loaded_object_subwindow)

        loaded_object_type = self.global_functions.get_fun__loaded_object_type()
        self.functions.append(loaded_object_type)

        array_ensure_value = self.global_functions.get_fun__array_ensure_value()
        self.functions.append(array_ensure_value)

        in_array = self.global_functions.get_fun__in_array()
        self.functions.append(in_array)

        object_get_value_by_shift = self.global_functions.get_fun__object_get_value_by_shift()
        self.functions.append(object_get_value_by_shift)

        array_strip_key = self.global_functions.get_fun__array_strip_key()
        self.functions.append(array_strip_key)

        attr_ticket_parent = self.global_functions.get_fun__attr_ticket_parent()
        self.functions.append(attr_ticket_parent)

        e_functions = self.global_functions.get_fun__e_functions()
        self.functions.append(e_functions)

        to_pips = self.global_functions.get_fun__to_pips()
        self.functions.append(to_pips)

        ticks_data = self.global_functions.get_fun__ticks_data()
        self.functions.append(ticks_data)

        time_at_start = self.global_functions.get_fun__time_at_start()
        self.functions.append(time_at_start)

        attr_ticket_previous_sibling = self.global_functions.get_fun__attr_ticket_previous_sibling()
        self.functions.append(attr_ticket_previous_sibling)

        order_open_price_as_child = self.global_functions.get_fun__order_open_price_as_child()
        self.functions.append(order_open_price_as_child)

        on_timer_set = self.global_functions.get_fun__on_timer_set()
        self.functions.append(on_timer_set)

        izigzag = self.global_functions.get_fun__izigzag()
        self.functions.append(izigzag)

        draw_spread_info = self.global_functions.get_fun__draw_spread_info()
        self.functions.append(draw_spread_info)

        draw_status = self.global_functions.get_fun__draw_status()
        self.functions.append(draw_status)

    def add_global_classes_structs(self):
        structs_data_chart_event = "//This is used to hold onchart event for onchart blocks process\nstruct OnChartEventHolder\n  {\n   int               id;\n   long              lparam;\n   double            dparam;\n   string            sparam;\n  };"
        self.classes_structs_enums.append(structs_data_chart_event)

        on_trade_event_detector_class = self.on_trade_event_detector_class_constructor.get_class()
        self.classes_structs_enums.append(on_trade_event_detector_class)

    def build(self):
        expert = ""
        expert += self.header
        expert += self.description_and_version_number()
        for prop in self.properties:
            expert += prop
        for const in self.consts_system:
            expert += const
        for var in self.vars_user:
            expert += var
        for const in self.consts_user:
            expert += const
        for struct in self.classes_structs_enums:
            expert += struct
        expert += self.block_parent_blueprint
        expert += self.task_blueprint
        for cls in self.task_elements:
            expert += cls
        for cls in self.tasks:
            expert += cls
        expert += self.block_blueprint
        for cls in self.blocks:
            expert += cls
        for var in self.vars_system:
            expert += var
        for fun in self.functions:
            expert += fun
        expert += self.get_on_init_items()
        expert += self.get_on_timer_items()
        expert += self.get_on_tick_items()
        expert += self.get_on_trade_items()
        expert += self.get_on_chart_items()
        expert += self.get_on_deinit_items()

        expert += get_version()
        return expert

    def get_on_init_items(self):
        result = "int OnInit(){\n"
        result += self.expert_expiration()
        for item in self.on_init:
            result += item
        result += "\n       if (ArraySize(blocks_timer)>0)\n           EventSetTimer(timer_period);"
        result += "\n    	return(INIT_SUCCEEDED);"
        result += "\n}\n"
        return result

    def get_on_timer_items(self):
        result = "void OnTimer(){\n"
        for item in self.on_timer:
            result += item
        result += "\n}\n"
        return result

    def get_on_tick_items(self):
        result = "void OnTick(){\n"
        for item in self.on_tick:
            result += item
        result += "\n}\n"
        return result

    def get_on_trade_items(self):
        result = "void OnTrade(){\n"
        for item in self.on_trade:
            result += item
        result += "\n}\n"
        return result

    def get_on_chart_items(self):
        result = "void OnChartEvent(const int id,         // Event identifier\nconst long& lparam,   // Event parameter of long type\nconst double& dparam, // Event parameter of double type\nconst string& sparam  // Event parameter of string type\n){\n"
        for item in self.on_chart:
            result += item
        result += "\n}\n"
        return result

    def get_on_deinit_items(self):
        result = "void OnDeinit(const int reason){\n"
        for item in self.on_deinit:
            result += item
        result += "\n}\n"
        return result

    def get_task_child(self, block_name, node):
        task_comment = "\n//" + block_name + "\n"
        task = self.task_dynamic_constructor.get_task_child(node, self.data.get("constants"),
                                                            self.data.get("variables"))
        return task_comment + task

    def get_block_child(self, block_name, input_dic, id_block):
        # block_comment = "\n//" + block_name + "\n"
        block = self.block_constructor.get_block_child(input_dic, id_block)
        return block

    def expert_expiration(self):
        expiration_code_snippet = "   string exp_date_str = \"user_expiration\";\n   exp_date_str = StringTrimLeft(StringTrimRight(exp_date_str));\n   if(exp_date_str!=\"\" && (TimeCurrent() > D'user_expiration' || TimeLocal() > D'user_expiration'))\n     {\n      Alert(\"The trial version has expired at \"+TimeToString(D'user_expiration', TIME_DATE)+\"\");\n      ExpertRemove();\n     }"
        expiration_date = self.data.get("project_options").get("magic_and_other").get("expiration_date")
        expiration_code_snippet = expiration_code_snippet.replace("user_expiration", str(expiration_date))
        return expiration_code_snippet

    def description_and_version_number(self):
        text = "#property copyright   \"copy_right_val\"\n#property link        \"website_address_val\"\n#property description \"description_val\"\n#property version     \"version_number_val\"\n\n"
        info = self.data.get("project_options").get("description_and_version_number")
        text = text.replace("copy_right_val", info.get("copy_right"))
        text = text.replace("website_address_val", info.get("website_address"))
        text = text.replace("description_val", info.get("description"))
        text = text.replace("version_number_val", info.get("version_number"))
        return text

    # Elements that are assigned to multiple
    # tasks of same type or to multiple task types
    def add_task_elements_common(self, nodes):
        for node in nodes:
            task_name = node.get("block_name_mql")
            match task_name:
                case "spread_filter":
                    if self.spread_filter_done:
                        continue
                    structs_data = self.spread_filter_struct_constructor.get_structs()
                    self.classes_structs_enums.append(structs_data)
                    self.spread_filter_done = True
                case "close_partially":
                    if self.close_partially_done:
                        continue
                    structs_data = self.close_partially_items.get_structs()
                    self.classes_structs_enums.append(structs_data)
                    vars_data = self.close_partially_items.get_vars()
                    self.vars_system.append(vars_data)
                    self.close_partially_done = True
                case "volume_profile":
                    if self.volume_profile_done:
                        continue
                    enums_data = self.volume_profile_items.get_enums()
                    self.classes_structs_enums.append(enums_data)
                    self.volume_profile_done = True

    # Elements that are assigned to a specific instance of a specific task type
    def add_task_elements_specific(self, nodes):
        for node in nodes:
            task_name = node.get("block_name_mql")
            if task_name == "condition_1_normal":
                self.condition_1_normal_elements(node)
            elif task_name == "condition_1_cross":
                self.condition_1_cross_elements(node)
            elif task_name == "formula":
                self.formula_elements(node)
            elif task_name == "modify_variables":
                self.modify_variables(node)
            elif task_name == "trailing_stop_each_trade":
                self.trailing_stop_each_trade(node)
            elif task_name == "comment":
                self.comment(node)
            elif task_name == "buy_sell":
                self.buy_sell(node)
            elif task_name == "trailing_pending_orders":
                self.trailing_pending_orders(node)
            elif task_name == "modify_stops_of_trades":
                self.modify_stops_of_trades(node)
            elif task_name == "draw_arrow":
                self.draw_arrow(node)
            elif task_name == "draw_button":
                self.draw_button(node)
            elif task_name == "draw_shape":
                self.draw_shape(node)
            elif task_name == "draw_line":
                self.draw_line(node)
            elif task_name == "draw_edit_field":
                self.draw_editfield(node)
            elif task_name == "draw_text":
                self.draw_text(node)
            elif task_name == "check_trendline_price_level":
                self.check_trendline_price_level(node)
            elif task_name == "no_trade_order_nearby":
                self.no_trade_order_nearby_run_data(node)
            elif task_name == "check_distance":
                self.check_distance(node)
            elif task_name == "pips_away_from_open_price":
                self.pips_away_from_open_price(node)
            elif task_name == "modify_stops":
                self.modify_stops(node)
            elif task_name == "alert_message":
                self.alert_message(node)
            elif task_name == "phone_notification":
                self.phone_notification(node)
            elif task_name == "move":
                self.move(node)
            elif task_name == "modify_text_description":
                self.modify_text_description(node)

    def modify_text_description(self, node):
        value_fetch = node.get("params").get("text")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params_price_level = value_fetch.get("params")
        id_val = str(node.get("id_by_user")) + "_text"
        self.task_elements.append(self.value_fetch_class(row1, row2, params_price_level, id_val))

    def move(self, node):
        params = node.get("params")
        if "time_1" in params:
            value_fetch_time_1 = params.get("time_1")
            row1_time_1 = value_fetch_time_1.get("row1")
            row2_time_1 = value_fetch_time_1.get("row2")
            params_time_1 = value_fetch_time_1.get("params")
            id_val_time_1 = str(node.get("id_by_user")) + "_time_1"
            self.task_elements.append(self.value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))
        if "time_2" in params:
            value_fetch_time_2 = params.get("time_2")
            row1_time_2 = value_fetch_time_2.get("row1")
            row2_time_2 = value_fetch_time_2.get("row2")
            id_val_time_2 = str(node.get("id_by_user")) + "_time_2"
            params_time_2 = value_fetch_time_2.get("params")
            self.task_elements.append(self.value_fetch_class(row1_time_2, row2_time_2, params_time_2, id_val_time_2))
        if "time_3" in params:
            value_fetch_time_3 = params.get("time_3")
            row1_time_3 = value_fetch_time_3.get("row1")
            row2_time_3 = value_fetch_time_3.get("row2")
            id_val_time_3 = str(node.get("id_by_user")) + "_time_3"
            params_time_3 = value_fetch_time_3.get("params")
            self.task_elements.append(self.value_fetch_class(row1_time_3, row2_time_3, params_time_3, id_val_time_3))
        if "price_1" in params:
            value_fetch_price_1 = params.get("price_1")
            row1_price_1 = value_fetch_price_1.get("row1")
            row2_price_1 = value_fetch_price_1.get("row2")
            id_val_price_1 = str(node.get("id_by_user")) + "_price_1"
            params_price_1 = value_fetch_price_1.get("params")
            self.task_elements.append(
                self.value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))
        if "price_2" in params:
            value_fetch_price_2 = params.get("price_2")
            row1_price_2 = value_fetch_price_2.get("row1")
            row2_price_2 = value_fetch_price_2.get("row2")
            id_val_price_2 = str(node.get("id_by_user")) + "_price_2"
            params_price_2 = value_fetch_price_2.get("params")
            self.task_elements.append(
                self.value_fetch_class(row1_price_2, row2_price_2, params_price_2, id_val_price_2))
        if "price_3" in params:
            value_fetch_price_3 = params.get("price_3")
            row1_price_3 = value_fetch_price_3.get("row1")
            row2_price_3 = value_fetch_price_3.get("row2")
            id_val_price_3 = str(node.get("id_by_user")) + "_price_3"
            params_price_3 = value_fetch_price_3.get("params")
            self.task_elements.append(
                self.value_fetch_class(row1_price_3, row2_price_3, params_price_3, id_val_price_3))

    def phone_notification(self, node):
        params = node.get("params")
        if params.get("Label1") != "\"\"" and "value_1" in params:
            value_fetch_1 = params.get("value_1")
            row1_1 = value_fetch_1.get("row1")
            row2_1 = value_fetch_1.get("row2")
            params_1 = value_fetch_1.get("params")
            id_val_1 = str(node.get("id_by_user")) + "_1"
            self.task_elements.append(self.value_fetch_class(row1_1, row2_1, params_1, id_val_1))
        if params.get("Label2") != "\"\"" and "value_2" in params:
            value_fetch_2 = params.get("value_2")
            row1_2 = value_fetch_2.get("row1")
            row2_2 = value_fetch_2.get("row2")
            id_val_2 = str(node.get("id_by_user")) + "_2"
            params_2 = value_fetch_2.get("params")
            self.task_elements.append(self.value_fetch_class(row1_2, row2_2, params_2, id_val_2))
        if params.get("Label3") != "\"\"" and "value_3" in params:
            value_fetch_3 = params.get("value_3")
            row1_3 = value_fetch_3.get("row1")
            row2_3 = value_fetch_3.get("row2")
            id_val_3 = str(node.get("id_by_user")) + "_3"
            params_3 = value_fetch_3.get("params")
            self.task_elements.append(self.value_fetch_class(row1_3, row2_3, params_3, id_val_3))
        if params.get("Label4") != "\"\"" and "value_4" in params:
            value_fetch_4 = params.get("value_4")
            row1_4 = value_fetch_4.get("row1")
            row2_4 = value_fetch_4.get("row2")
            id_val_4 = str(node.get("id_by_user")) + "_4"
            params_4 = value_fetch_4.get("params")
            self.task_elements.append(self.value_fetch_class(row1_4, row2_4, params_4, id_val_4))
        if params.get("Label5") != "\"\"" and "value_5" in params:
            value_fetch_5 = params.get("value_5")
            row1_5 = value_fetch_5.get("row1")
            row2_5 = value_fetch_5.get("row2")
            id_val_5 = str(node.get("id_by_user")) + "_5"
            params_5 = value_fetch_5.get("params")
            self.task_elements.append(self.value_fetch_class(row1_5, row2_5, params_5, id_val_5))
        if params.get("Label6") != "\"\"" and "value_6" in params:
            value_fetch_6 = params.get("value_6")
            row1_6 = value_fetch_6.get("row1")
            row2_6 = value_fetch_6.get("row2")
            id_val_6 = str(node.get("id_by_user")) + "_6"
            params_6 = value_fetch_6.get("params")
            self.task_elements.append(self.value_fetch_class(row1_6, row2_6, params_6, id_val_6))
        if params.get("Label7") != "\"\"" and "value_7" in params:
            value_fetch_7 = params.get("value_7")
            row1_7 = value_fetch_7.get("row1")
            row2_7 = value_fetch_7.get("row2")
            id_val_7 = str(node.get("id_by_user")) + "_7"
            params_7 = value_fetch_7.get("params")
            self.task_elements.append(self.value_fetch_class(row1_7, row2_7, params_7, id_val_7))
        if params.get("Label8") != "\"\"" and "value_8" in params:
            value_fetch_8 = params.get("value_8")
            row1_8 = value_fetch_8.get("row1")
            row2_8 = value_fetch_8.get("row2")
            id_val_8 = str(node.get("id_by_user")) + "_8"
            params_8 = value_fetch_8.get("params")
            self.task_elements.append(self.value_fetch_class(row1_8, row2_8, params_8, id_val_8))

    def alert_message(self, node):
        params = node.get("params")
        if params.get("AlertLabel1") != "\"\"" and "value_1" in params:
            value_fetch_1 = params.get("value_1")
            row1_1 = value_fetch_1.get("row1")
            row2_1 = value_fetch_1.get("row2")
            params_1 = value_fetch_1.get("params")
            id_val_1 = str(node.get("id_by_user")) + "_1"
            self.task_elements.append(self.value_fetch_class(row1_1, row2_1, params_1, id_val_1))
        if params.get("AlertLabel2") != "\"\"" and "value_2" in params:
            value_fetch_2 = params.get("value_2")
            row1_2 = value_fetch_2.get("row1")
            row2_2 = value_fetch_2.get("row2")
            id_val_2 = str(node.get("id_by_user")) + "_2"
            params_2 = value_fetch_2.get("params")
            self.task_elements.append(self.value_fetch_class(row1_2, row2_2, params_2, id_val_2))
        if params.get("AlertLabel3") != "\"\"" and "value_3" in params:
            value_fetch_3 = params.get("value_3")
            row1_3 = value_fetch_3.get("row1")
            row2_3 = value_fetch_3.get("row2")
            id_val_3 = str(node.get("id_by_user")) + "_3"
            params_3 = value_fetch_3.get("params")
            self.task_elements.append(self.value_fetch_class(row1_3, row2_3, params_3, id_val_3))
        if params.get("AlertLabel4") != "\"\"" and "value_4" in params:
            value_fetch_4 = params.get("value_4")
            row1_4 = value_fetch_4.get("row1")
            row2_4 = value_fetch_4.get("row2")
            id_val_4 = str(node.get("id_by_user")) + "_4"
            params_4 = value_fetch_4.get("params")
            self.task_elements.append(self.value_fetch_class(row1_4, row2_4, params_4, id_val_4))
        if params.get("AlertLabel5") != "\"\"" and "value_5" in params:
            value_fetch_5 = params.get("value_5")
            row1_5 = value_fetch_5.get("row1")
            row2_5 = value_fetch_5.get("row2")
            id_val_5 = str(node.get("id_by_user")) + "_5"
            params_5 = value_fetch_5.get("params")
            self.task_elements.append(self.value_fetch_class(row1_5, row2_5, params_5, id_val_5))
        if params.get("AlertLabel6") != "\"\"" and "value_6" in params:
            value_fetch_6 = params.get("value_6")
            row1_6 = value_fetch_6.get("row1")
            row2_6 = value_fetch_6.get("row2")
            id_val_6 = str(node.get("id_by_user")) + "_6"
            params_6 = value_fetch_6.get("params")
            self.task_elements.append(self.value_fetch_class(row1_6, row2_6, params_6, id_val_6))
        if params.get("AlertLabel7") != "\"\"" and "value_7" in params:
            value_fetch_7 = params.get("value_7")
            row1_7 = value_fetch_7.get("row1")
            row2_7 = value_fetch_7.get("row2")
            id_val_7 = str(node.get("id_by_user")) + "_7"
            params_7 = value_fetch_7.get("params")
            self.task_elements.append(self.value_fetch_class(row1_7, row2_7, params_7, id_val_7))
        if params.get("AlertLabel8") != "\"\"" and "value_8" in params:
            value_fetch_8 = params.get("value_8")
            row1_8 = value_fetch_8.get("row1")
            row2_8 = value_fetch_8.get("row2")
            id_val_8 = str(node.get("id_by_user")) + "_8"
            params_8 = value_fetch_8.get("params")
            self.task_elements.append(self.value_fetch_class(row1_8, row2_8, params_8, id_val_8))
        if params.get("AlertLabel9") != "\"\"" and "value_9" in params:
            value_fetch_9 = params.get("value_9")
            row1_9 = value_fetch_9.get("row1")
            row2_9 = value_fetch_9.get("row2")
            id_val_9 = str(node.get("id_by_user")) + "_9"
            params_9 = value_fetch_9.get("params")
            self.task_elements.append(self.value_fetch_class(row1_9, row2_9, params_9, id_val_9))
        if params.get("AlertLabel10") != "\"\"" and "value_10" in params:
            value_fetch_10 = params.get("value_10")
            row1_10 = value_fetch_10.get("row1")
            row2_10 = value_fetch_10.get("row2")
            id_val_10 = str(node.get("id_by_user")) + "_10"
            params_10 = value_fetch_10.get("params")
            self.task_elements.append(self.value_fetch_class(row1_10, row2_10, params_10, id_val_10))

    def modify_stops(self, node):
        params = node.get("params")
        if "relative_to_dynamic" in params:
            value_fetch_rtd = params.get("relative_to_dynamic")
            row1_rtd = value_fetch_rtd.get("row1")
            row2_rtd = value_fetch_rtd.get("row2")
            params_rtd = value_fetch_rtd.get("params")
            id_val_rtd = str(node.get("id_by_user")) + "_rtd"
            self.task_elements.append(self.value_fetch_class(row1_rtd, row2_rtd, params_rtd, id_val_rtd))
        if "new_sl_mode_function" in params:
            value_fetch_nsmf = params.get("new_sl_mode_function")
            row1_nsf = value_fetch_nsmf.get("row1")
            row2_nsf = value_fetch_nsmf.get("row2")
            params_nsf = value_fetch_nsmf.get("params")
            id_val_nsf = str(node.get("id_by_user")) + "_nsmf"
            self.task_elements.append(self.value_fetch_class(row1_nsf, row2_nsf, params_nsf, id_val_nsf))
        if "new_sl_mode_dynamicPips" in params:
            value_fetch_nsmdp = params.get("new_sl_mode_dynamicPips")
            row1_nsmdp = value_fetch_nsmdp.get("row1")
            row2_nsmdp = value_fetch_nsmdp.get("row2")
            params_nsmdp = value_fetch_nsmdp.get("params")
            id_val_nsmdp = str(node.get("id_by_user")) + "_nsmdp"
            self.task_elements.append(self.value_fetch_class(row1_nsmdp, row2_nsmdp, params_nsmdp, id_val_nsmdp))
        if "new_sl_mode_dynamicDigits" in params:
            value_fetch_nsmdd = params.get("new_sl_mode_dynamicDigits")
            row1_nsmdd = value_fetch_nsmdd.get("row1")
            row2_nsmdd = value_fetch_nsmdd.get("row2")
            params_nsmdd = value_fetch_nsmdd.get("params")
            id_val_nsmdd = str(node.get("id_by_user")) + "_nsmdd"
            self.task_elements.append(self.value_fetch_class(row1_nsmdd, row2_nsmdd, params_nsmdd, id_val_nsmdd))
        if "new_tp_mode_function" in params:
            value_fetch_ntmf = params.get("new_tp_mode_function")
            row1_ntmf = value_fetch_ntmf.get("row1")
            row2_ntmf = value_fetch_ntmf.get("row2")
            params_ntmf = value_fetch_ntmf.get("params")
            id_val_ntmf = str(node.get("id_by_user")) + "_ntmf"
            self.task_elements.append(self.value_fetch_class(row1_ntmf, row2_ntmf, params_ntmf, id_val_ntmf))
        if "new_tp_mode_dynamicPips" in params:
            value_fetch_ntmdp = params.get("new_tp_mode_dynamicPips")
            row1_ntmdp = value_fetch_ntmdp.get("row1")
            row2_ntmdp = value_fetch_ntmdp.get("row2")
            params_ntmdp = value_fetch_ntmdp.get("params")
            id_val_ntmdp = str(node.get("id_by_user")) + "_ntmdp"
            self.task_elements.append(self.value_fetch_class(row1_ntmdp, row2_ntmdp, params_ntmdp, id_val_ntmdp))
        if "new_tp_mode_dynamicDigits" in params:
            value_fetch_ntmdd = params.get("new_tp_mode_dynamicDigits")
            row1_ntmdd = value_fetch_ntmdd.get("row1")
            row2_ntmdd = value_fetch_ntmdd.get("row2")
            params_ntmdd = value_fetch_ntmdd.get("params")
            id_val_ntmdd = str(node.get("id_by_user")) + "_ntmdd"
            self.task_elements.append(self.value_fetch_class(row1_ntmdd, row2_ntmdd, params_ntmdd, id_val_ntmdd))

    def pips_away_from_open_price(self, node):
        params = node.get("params")
        if "pips_away_input_in_pips" in params:
            value_fetch_pips = params.get("pips_away_input_in_pips")
            row1_pips = value_fetch_pips.get("row1")
            row2_pips = value_fetch_pips.get("row2")
            params_pips = value_fetch_pips.get("params")
            id_val_pips = str(node.get("id_by_user")) + "_pips"
            self.task_elements.append(self.value_fetch_class(row1_pips, row2_pips, params_pips, id_val_pips))
        if "custom_price_fraction" in params:
            value_fetch_price_fraction = params.get("custom_price_fraction")
            row1_price_fraction = value_fetch_price_fraction.get("row1")
            row2_price_fraction = value_fetch_price_fraction.get("row2")
            params_price_fraction = value_fetch_price_fraction.get("params")
            id_val_price_fraction = str(node.get("id_by_user")) + "_price_fraction"
            self.task_elements.append(
                self.value_fetch_class(row1_price_fraction, row2_price_fraction, params_price_fraction,
                                       id_val_price_fraction))

    def check_distance(self, node):
        value_fetch_upper_level = node.get("params").get("upper_level")
        row1_upper_level = value_fetch_upper_level.get("row1")
        row2_upper_level = value_fetch_upper_level.get("row2")
        params_upper_level = value_fetch_upper_level.get("params")
        id_val_upper_level = str(node.get("id_by_user")) + "_upper_level"
        self.task_elements.append(
            self.value_fetch_class(row1_upper_level, row2_upper_level, params_upper_level, id_val_upper_level))

        value_fetch_lower_level = node.get("params").get("lower_level")
        row1_lower_level = value_fetch_lower_level.get("row1")
        row2_lower_level = value_fetch_lower_level.get("row2")
        params_lower_level = value_fetch_lower_level.get("params")
        id_val_lower_level = str(node.get("id_by_user")) + "_lower_level"
        self.task_elements.append(
            self.value_fetch_class(row1_lower_level, row2_lower_level, params_lower_level, id_val_lower_level))

        value_fetch_checking_distance = node.get("params").get("checking_distance")
        row1_checking_distance = value_fetch_checking_distance.get("row1")
        row2_checking_distance = value_fetch_checking_distance.get("row2")
        params_checking_distance = value_fetch_checking_distance.get("params")
        id_val_checking_distance = str(node.get("id_by_user")) + "_checking_distance"
        self.task_elements.append(
            self.value_fetch_class(row1_checking_distance, row2_checking_distance, params_checking_distance,
                                   id_val_checking_distance))

    def check_trendline_price_level(self, node):
        value_fetch = node.get("params").get("price_level")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params_price_level = value_fetch.get("params")
        id_val = str(node.get("id_by_user")) + "_price_level"
        self.task_elements.append(self.value_fetch_class(row1, row2, params_price_level, id_val))

    def draw_editfield(self, node):
        value_fetch = node.get("params").get("text")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params_text = value_fetch.get("params")
        id_val = str(node.get("id_by_user")) + "_text"
        self.task_elements.append(self.value_fetch_class(row1, row2, params_text, id_val))

    def draw_line(self, node):
        params = node.get("params")
        if "time_1" in params:
            value_fetch_time_1 = params.get("time_1")
            row1_time_1 = value_fetch_time_1.get("row1")
            row2_time_1 = value_fetch_time_1.get("row2")
            params_time_1 = value_fetch_time_1.get("params")
            id_val_time_1 = str(node.get("id_by_user")) + "_time_1"
            self.task_elements.append(self.value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))
        if "time_2" in params:
            value_fetch_time_2 = params.get("time_2")
            row1_time_2 = value_fetch_time_2.get("row1")
            row2_time_2 = value_fetch_time_2.get("row2")
            params_time_2 = value_fetch_time_2.get("params")
            id_val_time_2 = str(node.get("id_by_user")) + "_time_2"
            self.task_elements.append(self.value_fetch_class(row1_time_2, row2_time_2, params_time_2, id_val_time_2))

        if "price_1" in params:
            value_fetch_price_1 = params.get("price_1")
            row1_price_1 = value_fetch_price_1.get("row1")
            row2_price_1 = value_fetch_price_1.get("row2")
            params_price_1 = value_fetch_price_1.get("params")
            id_val_price_1 = str(node.get("id_by_user")) + "_price_1"
            self.task_elements.append(
                self.value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))
        if "price_2" in params:
            value_fetch_price_2 = params.get("price_2")
            row1_price_2 = value_fetch_price_2.get("row1")
            row2_price_2 = value_fetch_price_2.get("row2")
            params_price_2 = value_fetch_price_2.get("params")
            id_val_price_2 = str(node.get("id_by_user")) + "_price_2"
            self.task_elements.append(
                self.value_fetch_class(row1_price_2, row2_price_2, params_price_2, id_val_price_2))

    def draw_shape(self, node):
        if "time_1" in node.get("params"):
            value_fetch_time_1 = node.get("params").get("time_1")
            row1_time_1 = value_fetch_time_1.get("row1")
            row2_time_1 = value_fetch_time_1.get("row2")
            params_time_1 = value_fetch_time_1.get("params")
            id_val_time_1 = str(node.get("id_by_user")) + "_time_1"
            self.task_elements.append(self.value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))
        if "time_2" in node.get("params"):
            value_fetch_time_2 = node.get("params").get("time_2")
            row1_time_2 = value_fetch_time_2.get("row1")
            row2_time_2 = value_fetch_time_2.get("row2")
            params_time_2 = value_fetch_time_2.get("params")
            id_val_time_2 = str(node.get("id_by_user")) + "_time_2"
            self.task_elements.append(self.value_fetch_class(row1_time_2, row2_time_2, params_time_2, id_val_time_2))
        if "time_3" in node.get("params"):
            value_fetch_time_3 = node.get("params").get("time_3")
            row1_time_3 = value_fetch_time_3.get("row1")
            row2_time_3 = value_fetch_time_3.get("row2")
            params_time_3 = value_fetch_time_3.get("params")
            id_val_time_3 = str(node.get("id_by_user")) + "_time_3"
            self.task_elements.append(self.value_fetch_class(row1_time_3, row2_time_3, params_time_3, id_val_time_3))

        if "price_1" in node.get("params"):
            value_fetch_price_1 = node.get("params").get("price_1")
            row1_price_1 = value_fetch_price_1.get("row1")
            row2_price_1 = value_fetch_price_1.get("row2")
            params_price_1 = value_fetch_price_1.get("params")
            id_val_price_1 = str(node.get("id_by_user")) + "_price_1"
            self.task_elements.append(
                self.value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))
        if "price_2" in node.get("params"):
            value_fetch_price_2 = node.get("params").get("price_2")
            row1_price_2 = value_fetch_price_2.get("row1")
            row2_price_2 = value_fetch_price_2.get("row2")
            params_price_2 = value_fetch_price_2.get("params")
            id_val_price_2 = str(node.get("id_by_user")) + "_price_2"
            self.task_elements.append(
                self.value_fetch_class(row1_price_2, row2_price_2, params_price_2, id_val_price_2))
        if "price_3" in node.get("params"):
            value_fetch_price_3 = node.get("params").get("price_3")
            row1_price_3 = value_fetch_price_3.get("row1")
            row2_price_3 = value_fetch_price_3.get("row2")
            params_price_3 = value_fetch_price_3.get("params")
            id_val_price_3 = str(node.get("id_by_user")) + "_price_3"
            self.task_elements.append(
                self.value_fetch_class(row1_price_3, row2_price_3, params_price_3, id_val_price_3))

    def draw_button(self, node):
        value_fetch = node.get("params").get("text")
        row1 = value_fetch.get("row1")
        row2 = value_fetch.get("row2")
        params_obj_text = value_fetch.get("params")
        id_val = str(node.get("id_by_user")) + "_obj_text"
        self.task_elements.append(self.value_fetch_class(row1, row2, params_obj_text, id_val))

    def draw_arrow(self, node):
        value_fetch_time_1 = node.get("params").get("time_1")
        row1_time_1 = value_fetch_time_1.get("row1")
        row2_time_1 = value_fetch_time_1.get("row2")
        params_time_1 = value_fetch_time_1.get("params")
        id_val_time_1 = str(node.get("id_by_user")) + "_time_1"
        self.task_elements.append(self.value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))

        value_fetch_price_1 = node.get("params").get("price_1")
        row1_price_1 = value_fetch_price_1.get("row1")
        row2_price_1 = value_fetch_price_1.get("row2")
        params_price_1 = value_fetch_price_1.get("params")
        id_val_price_1 = str(node.get("id_by_user")) + "_price_1"
        self.task_elements.append(self.value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))

    def draw_text(self, node):
        params = node.get("params")
        if "time_1" in params:
            value_fetch_time_1 = params.get("time_1")
            row1_time_1 = value_fetch_time_1.get("row1")
            row2_time_1 = value_fetch_time_1.get("row2")
            params_time_1 = value_fetch_time_1.get("params")
            id_val_time_1 = str(node.get("id_by_user")) + "_time_1"
            self.task_elements.append(self.value_fetch_class(row1_time_1, row2_time_1, params_time_1, id_val_time_1))
        if "price_1" in params:
            value_fetch_price_1 = params.get("price_1")
            row1_price_1 = value_fetch_price_1.get("row1")
            row2_price_1 = value_fetch_price_1.get("row2")
            params_price_1 = value_fetch_price_1.get("params")
            id_val_price_1 = str(node.get("id_by_user")) + "_price_1"
            self.task_elements.append(
                self.value_fetch_class(row1_price_1, row2_price_1, params_price_1, id_val_price_1))
        if "text" in params:
            value_fetch_text = params.get("text")
            row1_text = value_fetch_text.get("row1")
            row2_text = value_fetch_text.get("row2")
            params_text = value_fetch_text.get("params")
            id_val_text = str(node.get("id_by_user")) + "_text"
            self.task_elements.append(
                self.value_fetch_class(row1_text, row2_text, params_text, id_val_text))

    def modify_stops_of_trades(self, node):
        params = node.get("params")
        if params.get("relative_to") == "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL":
            value_fetch = params.get("value_fetch_relative_to")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_rt = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_rt"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_rt, id_val))

        if params.get("new_tpsl_mode") == "NEW_STOPS_CUSTOM_PRICE_LEVEL":
            value_fetch_tp = params.get("new_take_profit_level")
            row1_tp = value_fetch_tp.get("row1")
            row2_tp = value_fetch_tp.get("row2")
            params_tp = value_fetch_tp.get("params")
            id_val_tp = str(node.get("id_by_user")) + "_ntm_tp"

            value_fetch_sl = params.get("new_stop_loss_level")
            row1_sl = value_fetch_sl.get("row1")
            row2_sl = value_fetch_sl.get("row2")
            params_sl = value_fetch_sl.get("params")
            id_val_sl = str(node.get("id_by_user")) + "_ntm_sl"

            self.task_elements.append(self.value_fetch_class(row1_tp, row2_tp, params_tp, id_val_tp))
            self.task_elements.append(self.value_fetch_class(row1_sl, row2_sl, params_sl, id_val_sl))

    def trailing_pending_orders(self, node):
        params = node.get("params")
        trailing_distance_mode = params.get("trailing_distance_mode")
        if trailing_distance_mode != "TRAILING_DISTANCE_MODE_FIXED":
            key = ""
            if trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC":
                key = "dynamic_level"
            elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_PIPS":
                key = "dynamic_size_pips_input"
            elif trailing_distance_mode == "TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS":
                key = "dynamic_size_digits_input"
            value_fetch = params.get(key)
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_tdmd = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_tdmd"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_tdmd, id_val))

    def buy_sell(self, node):
        params = node.get("params")
        if params.get("open_at_price") == "OPEN_AT_CUSTOM_PRICE":
            value_fetch = params.get("price_to_open_dynamic_level")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_oacp = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "oacp"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_oacp, id_val))
        if params.get("take_profit_mode") == "TPSL_MODE_CUSTOM_PRICE_LEVEL":
            value_fetch = params.get("take_profit_price_level")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_tppl = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_tppl"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_tppl, id_val))
        if params.get("take_profit_mode") == "TPSL_MODE_CUSTOM_PIPS":
            value_fetch = params.get("take_profit_pips")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_tpp = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_tpp"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_tpp, id_val))
        if params.get("take_profit_mode") == "TPSL_MODE_CUSTOM_PRICE_FRACTION":
            value_fetch = params.get("take_profit_price_fraction")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_tppf = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_tppf"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_tppf, id_val))
        if params.get("stop_loss_mode") == "TPSL_MODE_CUSTOM_PRICE_LEVEL":
            value_fetch = params.get("stop_loss_price_level")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_slpl = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_slpl"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_slpl, id_val))
        if params.get("stop_loss_mode") == "TPSL_MODE_CUSTOM_PIPS":
            value_fetch = params.get("stop_loss_pips")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_slp = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_slp"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_slp, id_val))
        if params.get("stop_loss_mode") == "TPSL_MODE_CUSTOM_PRICE_FRACTION":
            value_fetch = params.get("stop_loss_price_fraction")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_slpf = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_slpf"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_slpf, id_val))

    def comment(self, node):
        params = node.get("params")
        if params.get("label_1") != "\"\"" and "value_fetch_1" in params:
            value_fetch = params.get("value_fetch_1")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r1"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_2") != "\"\"" and "value_fetch_2" in params:
            value_fetch = params.get("value_fetch_2")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r2"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_3") != "\"\"" and "value_fetch_3" in params:
            value_fetch = params.get("value_fetch_3")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r3"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_4") != "\"\"" and "value_fetch_4" in params:
            value_fetch = params.get("value_fetch_4")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r4"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_5") != "\"\"" and "value_fetch_5" in params:
            value_fetch = params.get("value_fetch_5")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r5"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_6") != "\"\"" and "value_fetch_6" in params:
            value_fetch = params.get("value_fetch_6")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r6"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_7") != "\"\"" and "value_fetch_7" in params:
            value_fetch = params.get("value_fetch_7")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r7"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

        if params.get("label_8") != "\"\"" and "value_fetch_8" in params:
            value_fetch = params.get("value_fetch_8")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_value_fetch = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "cm_r8"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_value_fetch, id_val))

    def trailing_stop_each_trade(self, node):
        params = node.get("params")
        if params.get("TrailingStopMode") == "TRAILING_STOP_MODE_CUSTOM_LEVEL":
            value_fetch = params.get("value_fetch_trailingstopmode_custom_level")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params_tsm = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "tsm_cl"
            self.task_elements.append(self.value_fetch_class(row1, row2, params_tsm, id_val))

    def no_trade_order_nearby_run_data(self, node):
        params = node.get("params")
        if params.get("mode_base_price") != "\"current\"":
            value_fetch_price = params.get("price")
            row1_price = value_fetch_price.get("row1")
            row2_price = value_fetch_price.get("row2")
            params_price = value_fetch_price.get("params")
            id_val_price = str(node.get("id_by_user")) + "_price"
            self.task_elements.append(self.value_fetch_class(row1_price, row2_price, params_price, id_val_price))

        value_fetch_t1 = params.get("time_1")
        row1_t1 = value_fetch_t1.get("row1")
        row2_t1 = value_fetch_t1.get("row2")
        params_t1 = value_fetch_t1.get("params")
        id_val_t1 = str(node.get("id_by_user")) + "_t1"
        self.task_elements.append(self.value_fetch_class(row1_t1, row2_t1, params_t1, id_val_t1))

        value_fetch_t2 = params.get("time_2")
        row1_t2 = value_fetch_t2.get("row1")
        row2_t2 = value_fetch_t2.get("row2")
        params_t2 = value_fetch_t2.get("params")
        id_val_t2 = str(node.get("id_by_user")) + "_t2"
        self.task_elements.append(self.value_fetch_class(row1_t2, row2_t2, params_t2, id_val_t2))

    def modify_variables(self, node):
        i = 0
        for key, val in node.get("params").items():
            i += 1
            if not val.get("variable_name"):
                continue
            value_fetch = val.get("value_fetch")
            row1 = value_fetch.get("row1")
            row2 = value_fetch.get("row2")
            params = value_fetch.get("params")
            id_val = str(node.get("id_by_user")) + "_var_" + str(i)
            self.task_elements.append(self.value_fetch_class(row1, row2, params, id_val))

    def formula_elements(self, node):
        params = node.get("params")
        # left data
        row1_left = params.get("left").get("row1")
        row2_left = params.get("left").get("row2")
        id_val_left = str(node.get("id_by_user")) + "_" + "left"
        params_left = params.get("left").get("params")
        self.task_elements.append(self.value_fetch_class(row1_left, row2_left, params_left, id_val_left))
        # right data
        row1_right = params.get("right").get("row1")
        row2_right = params.get("right").get("row2")
        id_val_right = str(node.get("id_by_user")) + "_" + "right"
        params_right = params.get("right").get("params")
        self.task_elements.append(self.value_fetch_class(row1_right, row2_right, params_right, id_val_right))

    def condition_1_normal_elements(self, node):
        params = node.get("params")
        # left data
        row1_left = params.get("left").get("row1")
        row2_left = params.get("left").get("row2")
        id_val_left = str(node.get("id_by_user")) + "_" + "left"
        params_left = params.get("left").get("params")
        self.task_elements.append(self.value_fetch_class(row1_left, row2_left, params_left, id_val_left))
        # right data
        row1_right = params.get("right").get("row1")
        row2_right = params.get("right").get("row2")
        id_val_right = str(node.get("id_by_user")) + "_" + "right"
        params_right = params.get("right").get("params")
        self.task_elements.append(self.value_fetch_class(row1_right, row2_right, params_right, id_val_right))

    def condition_1_cross_elements(self, node):
        params = node.get("params")
        # left data
        row1_left = params.get("left").get("row1")
        row2_left = params.get("left").get("row2")
        id_val_left_1 = str(node.get("id_by_user")) + "_" + "left1"
        id_val_left_2 = str(node.get("id_by_user")) + "_" + "left2"
        params_left_1 = params.get("left").get("params")
        params_left_2 = params_left_1.copy()
        if "shift" in params_left_2:
            params_left_2["shift"] = str(params_left_2["shift"]) + " + " + str(
                (params.get("operator").get("cross_width")))
        if "TickID" in params_left_2:
            params_left_2["TickID"] = str(params_left_2["TickID"]) + " + " + str(
                (params.get("operator").get("cross_width")))
        self.task_elements.append(self.value_fetch_class(row1_left, row2_left, params_left_1, id_val_left_1))
        self.task_elements.append(self.value_fetch_class(row1_left, row2_left, params_left_2, id_val_left_2))
        # right data
        row1_right = params.get("right").get("row1")
        row2_right = params.get("right").get("row2")
        id_val_right_1 = str(node.get("id_by_user")) + "_" + "right1"
        id_val_right_2 = str(node.get("id_by_user")) + "_" + "right2"
        params_right_1 = params.get("right").get("params")
        params_right_2 = params_right_1.copy()
        if "shift" in params_right_2:
            params_right_2["shift"] = str(params_right_2["shift"]) + "+" + str(
                params.get("operator").get("cross_width"))
        if "TickID" in params_right_2:
            params_right_2["TickID"] = str(params_right_2["TickID"]) + "+" + str(
                params.get("operator").get("cross_width"))
        self.task_elements.append(self.value_fetch_class(row1_right, row2_right, params_right_1, id_val_right_1))
        self.task_elements.append(self.value_fetch_class(row1_right, row2_right, params_right_2, id_val_right_2))

    def value_fetch_class(self, row1, row2, params, id_val):
        if row1 == "indicator":
            return self.indicator_class_constructor.get_class(row2, params, id_val,
                                                              self.data.get("constants"),
                                                              self.data.get("variables"))
        elif row1 == "candle":
            return self.candle_class_constructor.get_class(params, id_val,
                                                           self.data.get("constants"),
                                                           self.data.get("variables"))
        elif row1 == "market-properties":
            return self.market_properties_class_constructor_new.get_class(row2, params, id_val,
                                                                          self.data.get("constants"),
                                                                          self.data.get("variables"))
        elif row1 == "value":
            return self.value_class_constructor.get_class(row2, params, id_val,
                                                          self.data.get("constants"),
                                                          self.data.get("variables"))
        elif row1 == "object-on-the-chart":
            return self.object_on_the_chart_class_constructor.get_class(row2, params, id_val,
                                                                        self.data.get("constants"),
                                                                        self.data.get("variables"))
        elif row1 == "trade-order-in-loop":
            return self.trade_order_in_loop_class_constructor.get_class(row2, params, id_val,
                                                                        self.data.get("constants"),
                                                                        self.data.get("variables"))

        elif row1 == "account":
            return self.account_class_constructor.get_class(row2, params, id_val,
                                                            self.data.get("constants"),
                                                            self.data.get("variables"))
