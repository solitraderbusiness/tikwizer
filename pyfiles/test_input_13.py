# test for each trade new
input_data_1 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4eb302a9-43d7-4c6a-9e4a-34a2b7a67cde",
                        "sourceHandle": "blue",
                        "target": "b62ec518-9b85-4ae0-ad7a-0b5054a64b88",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4eb302a9-43d7-4c6a-9e4a-34a2b7a67cdeblue-b62ec518-9b85-4ae0-ad7a-0b5054a64b88c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "4eb302a9-43d7-4c6a-9e4a-34a2b7a67cde",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "loop_direction": "newest_last",
                            "skip_n": "0",
                            "every_n": "1",
                            "not_more_than_n": "0",
                            "symbols_str": "",
                            "second_output": "if_not_empty"
                        },
                        "id": "b62ec518-9b85-4ae0-ad7a-0b5054a64b88",
                        "id_by_user": 2,
                        "blockName": "For each Trade",
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "for_each_trade"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "409f8aa1-318e-41a2-b529-607c8f727a2d",
    "name_by_user": "test 6524",
    "highestIndex": "3"
}

# test for each trade
input_data_2 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "c86ae960-00e5-48ca-8fef-065d9aac72cc",
                        "sourceHandle": "blue",
                        "target": "6ed57532-5a0a-4eda-a91b-073fde51bb24",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-c86ae960-00e5-48ca-8fef-065d9aac72ccblue-6ed57532-5a0a-4eda-a91b-073fde51bb24c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "type": "{0,1}",
                            "skip_n": "0",
                            "every_n": "1",
                            "not_more_than_n": "0",
                            "loop_direction": "LOOP_DIRECTION_NEWEST_TO_OLDEST"
                        },
                        "id": "c86ae960-00e5-48ca-8fef-065d9aac72cc",
                        "id_by_user": 3,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "for_each_trade",
                        "blockName": "For each Trade"
                    },
                    {
                        "params": {
                            "operator": ">",
                            "check_mode": "CHECK_PROFIT_LOSS_MODE_DEPOSIT_CURRENCY",
                            "check_value": "10"
                        },
                        "id": "6ed57532-5a0a-4eda-a91b-073fde51bb24",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "check_loss",
                        "blockName": "check loss"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "409f8aa1-318e-41a2-b529-607c8f727a2d",
    "name_by_user": "test 6524",
    "highestIndex": "5"
}

# test object on the chart numeric
input_data_3 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "sourceHandle": "blue",
                        "target": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4afd77dc-82a4-4656-9f0a-6f2b0bb17b9bblue-e44bb335-3d39-4c87-a8f4-7be791aabef5c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0}",
                            "TrailWhat": "0",
                            "TrailingReferencePrice": "2",
                            "TrailingStopMode": "TRAILING_STOP_MODE_CUSTOM_LEVEL",
                            "TrailingStepMode": "TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingStartMode": "TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP",
                            "LevelColor": "clrSlateGray",
                            "symbols_str": "",
                            "value_fetch_trailingstopmode_custom_level": {
                                "row1": "object-on-the-chart",
                                "row2": "attribute_set_1_numeric",
                                "params": {
                                    "ObjSource": "name",
                                    "Name": "my_object_name",
                                    "Property": "OBJPROP_PRICE1",
                                    "FiboLevelID": 0,
                                    "TLpriceLevel": 1.2,
                                    "Shift": 0
                                }
                            },
                            "tStepPercentTS": "15",
                            "tStartPercentTS": "97",
                            "tTPpercentTS": "23"
                        },
                        "id": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "id_by_user": 1,
                        "blockName": "Trailing stop (each trade)",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_stop_each_trade"
                    },
                    {
                        "params": {},
                        "id": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "12302dfb-ac61-45c1-a388-f93acc8c56cd",
    "name_by_user": "test 9541",
    "highestIndex": "3"
}

# test object on the chart string
input_data_4 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "sourceHandle": "blue",
                        "target": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4afd77dc-82a4-4656-9f0a-6f2b0bb17b9bblue-e44bb335-3d39-4c87-a8f4-7be791aabef5c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0}",
                            "TrailWhat": "0",
                            "TrailingReferencePrice": "2",
                            "TrailingStopMode": "TRAILING_STOP_MODE_CUSTOM_LEVEL",
                            "TrailingStepMode": "TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingStartMode": "TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP",
                            "LevelColor": "clrSlateGray",
                            "symbols_str": "",
                            "value_fetch_trailingstopmode_custom_level": {
                                "row1": "object-on-the-chart",
                                "row2": "attribute_set_2_text",
                                "params": {
                                    "ObjSource": "name",
                                    "Name": "my_object_name",
                                    "Property": "OBJPROP_TEXT",
                                    "adjust": "+\"hello\""
                                }
                            },
                            "tStepPercentTS": "15",
                            "tStartPercentTS": "97",
                            "tTPpercentTS": "23"
                        },
                        "id": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "id_by_user": 1,
                        "blockName": "Trailing stop (each trade)",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_stop_each_trade"
                    },
                    {
                        "params": {},
                        "id": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "12302dfb-ac61-45c1-a388-f93acc8c56cd",
    "name_by_user": "test 9541",
    "highestIndex": "3"
}

# test value > text
input_data_5 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "f86625a3-931f-436f-a8d9-7f84b09891f1",
                        "sourceHandle": "blue",
                        "target": "4402e815-fe75-4f58-8b85-331902cc366a",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f86625a3-931f-436f-a8d9-7f84b09891f1blue-4402e815-fe75-4f58-8b85-331902cc366ac"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Text_code_input",
                                "params": {
                                    "value": "test",
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "4402e815-fe75-4f58-8b85-331902cc366a",
                        "id_by_user": 1,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "f86625a3-931f-436f-a8d9-7f84b09891f1",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "4b8a6158-eaae-4594-8165-07266c19b782",
    "name_by_user": "test 563",
    "highestIndex": "3"
}

# test field referenced to global var
input_data_6 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "7538d537-ca45-4ede-b401-40c35c7c1774",
                        "sourceHandle": "blue",
                        "target": "99a78f55-6255-4687-b23c-b6afa221f6ba",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-7538d537-ca45-4ede-b401-40c35c7c1774blue-99a78f55-6255-4687-b23c-b6afa221f6bac"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "7538d537-ca45-4ede-b401-40c35c7c1774",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "test",
                            "stoploss": "20",
                            "takeprofit": "20"
                        },
                        "id": "99a78f55-6255-4687-b23c-b6afa221f6ba",
                        "id_by_user": 2,
                        "blockName": "Buy now",
                        "category": "buy_sell",
                        "block_name_mql": "buy_now"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [
            {
                "type": "double",
                "name": "test",
                "value": "",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
    "name_by_user": "test 8624",
    "highestIndex": "3"
}

# test field referenced to global var
input_data_7 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
                        "sourceHandle": "blue",
                        "target": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-ad6608c5-5627-4517-ad41-2be6d7ed938bblue-9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4c"
                    },
                    {
                        "source": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
                        "sourceHandle": "blue",
                        "target": "b5f6e916-91bc-410e-bff0-94640b249cd8",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-ad6608c5-5627-4517-ad41-2be6d7ed938bblue-b5f6e916-91bc-410e-bff0-94640b249cd8c"
                    },
                    {
                        "source": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
                        "sourceHandle": "red",
                        "target": "730acf16-7e2d-4c9f-9c99-d692ecc637b0",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-ad6608c5-5627-4517-ad41-2be6d7ed938bred-730acf16-7e2d-4c9f-9c99-d692ecc637b0c"
                    },
                    {
                        "source": "b5f6e916-91bc-410e-bff0-94640b249cd8",
                        "sourceHandle": "blue",
                        "target": "23f4a20a-3966-4cda-a926-a028218c2ba3",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b5f6e916-91bc-410e-bff0-94640b249cd8blue-23f4a20a-3966-4cda-a926-a028218c2ba3c"
                    },
                    {
                        "source": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
                        "sourceHandle": "blue",
                        "target": "5d36e995-fccd-4f36-b7c6-19f0e78fff9b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4blue-5d36e995-fccd-4f36-b7c6-19f0e78fff9bc"
                    },
                    {
                        "source": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
                        "sourceHandle": "red",
                        "target": "3455f650-9d7a-4212-982c-3050085fe535",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4red-3455f650-9d7a-4212-982c-3050085fe535c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "open_at_price": "OPEN_AT_ASK",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrDarkBlue",
                            "price_offset": "20",
                            "how_much_volume": "0.1",
                            "stoploss": "test",
                            "takeprofit": "20"
                        },
                        "id": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
                        "id_by_user": 2,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
                    },
                    {
                        "params": {
                            "server_or_local_time": "TIME_SERVER",
                            "FirstStartMinute": "5",
                            "FirstEndMinute": "test",
                            "SecondMinutesBlock": "false",
                            "ThirdMinutesBlock": "false",
                            "FourthMinutesBlock": "false"
                        },
                        "id": "730acf16-7e2d-4c9f-9c99-d692ecc637b0",
                        "id_by_user": 3,
                        "blockName": "Minutes filter",
                        "category": "time_filters",
                        "block_name_mql": "minutes_filter"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "type": "{0,1}",
                            "profit_mode_each": "PROFIT_MODE_NO_MATTER",
                            "profit_mode": "PROFIT_MODE_PIPS_SUM",
                            "compare": ">",
                            "profit_amount": "my_int"
                        },
                        "id": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
                        "id_by_user": 4,
                        "blockName": "Check Profit (unrealized)",
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_profit_unrealized"
                    },
                    {
                        "params": {
                            "title": "Comment Message",
                            "obj_chart_subwindow": "",
                            "obj_corner": "CORNER_LEFT_UPPER",
                            "obj_x": "5",
                            "obj_y": "24",
                            "obj_title_font": "Georgia",
                            "obj_title_font_color": "clrGold",
                            "obj_title_font_size": "13",
                            "obj_label_font": "Vardena",
                            "obj_label_font_color": "clrDarkGray",
                            "obj_label_font_size": "10",
                            "obj_font": "Vardena",
                            "obj_font_color": "clrWhite",
                            "obj_font_size": "10",
                            "label_1": "greetings",
                            "format_number_1": "EMPTY_VALUE",
                            "format_time_1": "EMPTY_VALUE",
                            "label_2": "",
                            "format_number_2": "EMPTY_VALUE",
                            "format_time_2": "EMPTY_VALUE",
                            "label_3": "",
                            "format_number_3": "EMPTY_VALUE",
                            "format_time_3": "EMPTY_VALUE",
                            "label_4": "",
                            "format_number_4": "EMPTY_VALUE",
                            "format_time_4": "EMPTY_VALUE",
                            "label_5": "",
                            "format_number_5": "EMPTY_VALUE",
                            "format_time_5": "EMPTY_VALUE",
                            "label_6": "",
                            "format_number_6": "EMPTY_VALUE",
                            "format_time_6": "EMPTY_VALUE",
                            "label_7": "",
                            "format_number_7": "EMPTY_VALUE",
                            "format_time_7": "EMPTY_VALUE",
                            "label_8": "",
                            "format_number_8": "EMPTY_VALUE",
                            "format_time_8": "EMPTY_VALUE",
                            "value_fetch_1": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_2": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_3": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_4": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_5": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_6": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_7": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_8": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "23f4a20a-3966-4cda-a926-a028218c2ba3",
                        "id_by_user": 5,
                        "blockName": "Comment",
                        "category": "output_communication",
                        "block_name_mql": "comment"
                    },
                    {
                        "params": {
                            "TimesToPass": "3",
                            "CounterID": "test"
                        },
                        "id": "3455f650-9d7a-4212-982c-3050085fe535",
                        "id_by_user": 6,
                        "blockName": "Counter: Pass \"n\" times",
                        "category": "counters",
                        "block_name_mql": "counter_pass_n_times"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "order_age_mins": "0",
                            "slippage": "4",
                            "arrow_color": "clrDarkGoldenrod",
                            "symbols_str": "greetings"
                        },
                        "id": "b5f6e916-91bc-410e-bff0-94640b249cd8",
                        "id_by_user": 7,
                        "blockName": "Close trades",
                        "category": "trading_actions",
                        "block_name_mql": "close_trades"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
                            "bep_offset_mode": "BEP_OFFSET_MODE_NONE",
                            "symbols_str": "",
                            "pips_on_profit": "my_int"
                        },
                        "id": "5d36e995-fccd-4f36-b7c6-19f0e78fff9b",
                        "id_by_user": 8,
                        "blockName": "Break even point (each trade)",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "break_even_point_each_trade"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [
            {
                "type": "double",
                "name": "test",
                "value": "",
                "description": ""
            },
            {
                "type": "string",
                "name": "greetings",
                "value": "hellow how are your",
                "description": ""
            },
            {
                "type": "int",
                "name": "my_int",
                "value": "20",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
    "name_by_user": "test 8624",
    "highestIndex": "9"
}

# test object on the chart numeric
input_data_8 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "00f7330c-2fbe-47e1-a302-bec9470ab009",
                        "sourceHandle": "blue",
                        "target": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-00f7330c-2fbe-47e1-a302-bec9470ab009blue-02ec7d05-12f9-4bb3-a61c-013e13eaa98fc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "00f7330c-2fbe-47e1-a302-bec9470ab009",
                        "id_by_user": 7,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "object-on-the-chart",
                                "row2": "attribute_set_1_numeric",
                                "params": {
                                    "ObjSource": "name",
                                    "Property": "OBJPROP_RAY_LEFT",
                                    "Name": "my_object_name"
                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
                        "id_by_user": 8,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [
            {
                "type": "double",
                "name": "test",
                "value": "",
                "description": ""
            },
            {
                "type": "string",
                "name": "greetings",
                "value": "hellow how are your",
                "description": ""
            },
            {
                "type": "int",
                "name": "my_int",
                "value": "20",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
    "name_by_user": "test 8624",
    "highestIndex": "9"
}

# test object on the chart numeric 2
input_data_9 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "00f7330c-2fbe-47e1-a302-bec9470ab009",
                        "sourceHandle": "blue",
                        "target": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-00f7330c-2fbe-47e1-a302-bec9470ab009blue-02ec7d05-12f9-4bb3-a61c-013e13eaa98fc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "00f7330c-2fbe-47e1-a302-bec9470ab009",
                        "id_by_user": 7,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "object-on-the-chart",
                                "row2": "attribute_set_1_numeric",
                                "params": {
                                    "ObjSource": "objloop",
                                    "Property": "OBJPROP_PERIOD"
                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
                        "id_by_user": 8,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [
            {
                "type": "double",
                "name": "test",
                "value": "",
                "description": ""
            },
            {
                "type": "string",
                "name": "greetings",
                "value": "hellow how are your",
                "description": ""
            },
            {
                "type": "int",
                "name": "my_int",
                "value": "20",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
    "name_by_user": "test 8624",
    "highestIndex": "9"
}

# test object on the chart string
input_data_10 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "00f7330c-2fbe-47e1-a302-bec9470ab009",
                        "sourceHandle": "blue",
                        "target": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-00f7330c-2fbe-47e1-a302-bec9470ab009blue-02ec7d05-12f9-4bb3-a61c-013e13eaa98fc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "00f7330c-2fbe-47e1-a302-bec9470ab009",
                        "id_by_user": 7,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "object-on-the-chart",
                                "row2": "attribute_set_2_text",
                                "params": {
                                    "ObjSource": "name",
                                    "Property": "OBJPROP_TOOLTIP",
                                    "Name": "my_test_name"
                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
                        "id_by_user": 8,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [
            {
                "type": "double",
                "name": "test",
                "value": "",
                "description": ""
            },
            {
                "type": "string",
                "name": "greetings",
                "value": "hellow how are your",
                "description": ""
            },
            {
                "type": "int",
                "name": "my_int",
                "value": "20",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
    "name_by_user": "test 8624",
    "highestIndex": "9"
}

# test bollinger bands (multiple shift in params issue)
input_data_11 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "9646400e-0790-4b14-822e-d31216fe7612",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-9646400e-0790-4b14-822e-d31216fe7612c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "indicator",
                                "row2": "bollinger_band",
                                "params": {
                                    "period": "20",
                                    "shift": "0",
                                    "bands_shift": "0",
                                    "deviation": "2",
                                    "mode": "MODE_MAIN",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT"

                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "9646400e-0790-4b14-822e-d31216fe7612",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "4"
}

# test formula when no variable is inserted
input_data_12 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test if double quotation not added
input_data_13 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-0a1a35ad-ff6d-4828-bb13-e544b3d470c3c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20"
                        },
                        "id": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "id_by_user": 4,
                        "blockName": "Buy now",
                        "category": "buy_sell",
                        "block_name_mql": "buy_now"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test formula issue with var update feature
input_data_14 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90c3cfc5-bad5-465c-bd5b-e4152d7e4a43",
                        "sourceHandle": "blue",
                        "target": "c6e6c45b-835b-4665-bb85-08e226a14794",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90c3cfc5-bad5-465c-bd5b-e4152d7e4a43blue-c6e6c45b-835b-4665-bb85-08e226a14794c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "90c3cfc5-bad5-465c-bd5b-e4152d7e4a43",
                        "id_by_user": 4,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": "variable"
                        },
                        "id": "c6e6c45b-835b-4665-bb85-08e226a14794",
                        "id_by_user": 6,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [
            {
                "type": "double",
                "name": "variable",
                "value": "10",
                "description": ""
            }
        ],
        "constants": [
            {
                "type": "string",
                "name": "test",
                "value": "",
                "description": ""
            }
        ]
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "7"
}

# test formula with no variable assigned
input_data_15 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90c3cfc5-bad5-465c-bd5b-e4152d7e4a43",
                        "sourceHandle": "blue",
                        "target": "69df2882-37a5-47b5-9a9f-ae81ebe63791",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90c3cfc5-bad5-465c-bd5b-e4152d7e4a43blue-69df2882-37a5-47b5-9a9f-ae81ebe63791c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "90c3cfc5-bad5-465c-bd5b-e4152d7e4a43",
                        "id_by_user": 4,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "69df2882-37a5-47b5-9a9f-ae81ebe63791",
                        "id_by_user": 7,
                        "category": "condition_formula",
                        "block_name_mql": "formula",
                        "blockName": "Formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": [
            {
                "type": "string",
                "name": "test",
                "value": "",
                "description": ""
            }
        ]
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "8"
}

# test value_fetch > trade order in loop 1
input_data_16 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "trade-order-in-loop",
                                "row2": "IN_LOOP_TRADE_ORDER_CANDLE_TIME",
                                "params": {
                                    "Period_candle_id": "PERIOD_CURRENT",
                                    "Period_candle_time": "PERIOD_CURRENT",
                                    "ModeProfit": 0,
                                    "ModeStopLoss": "level",
                                    "ModeTakeProfit": "level",
                                    "ModeTicket": 0,
                                    "ModeVolume": 0,
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test value_fetch > trade order in loop 2
input_data_17 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "trade-order-in-loop",
                                "row2": "IN_LOOP_TRADE_ORDER_TICKET_NUMBER",
                                "params": {
                                    "Period_candle_id": "PERIOD_CURRENT",
                                    "Period_candle_time": "PERIOD_CURRENT",
                                    "ModeProfit": 0,
                                    "ModeStopLoss": "level",
                                    "ModeTakeProfit": "level",
                                    "ModeTicket": 0,
                                    "ModeVolume": 0,
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test value_fetch > trade order in loop 3: adjust
input_data_18 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "trade-order-in-loop",
                                "row2": "IN_LOOP_TRADE_ORDER_TICKET_NUMBER",
                                "params": {
                                    "Period_candle_id": "PERIOD_CURRENT",
                                    "Period_candle_time": "PERIOD_CURRENT",
                                    "ModeProfit": 0,
                                    "ModeStopLoss": "level",
                                    "ModeTakeProfit": "level",
                                    "ModeTicket": 0,
                                    "ModeVolume": 0,
                                    "adjust": "*15pips"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test value_fetch > trade order in loop 4, real data
input_data_19 = {
    "data": {
        "events": {
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_tick": {
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "trade-order-in-loop",
                                "row2": "IN_LOOP_TRADE_ORDER_TAKE_PROFIT",
                                "params": {
                                    "ModeTakeProfit": "fraction",
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "7cf85181-0cfc-443e-8a3d-5f4ab2160c34",
                        "id_by_user": 1,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "4125d56f-c42c-4156-990e-4e7bd3739395",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "4125d56f-c42c-4156-990e-4e7bd3739395",
                        "sourceHandle": "blue",
                        "target": "7cf85181-0cfc-443e-8a3d-5f4ab2160c34",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "21a05ff9-64b7-4bce-aa65-e0915aa09506"
                    }
                ]
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "63aa429c-b475-44a4-9ee5-4b95b6968c4c",
    "name_by_user": "test 9545",
    "highestIndex": "3"
}

# test value_fetch > account
input_data_20 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "account",
                                "row2": "ACCOUNT_INFO_NAME_DEPOSIT_CURRENCY",
                                "params": {
                                    "margin_check_OP_TYPE": 0,
                                    "margin_check_VOLUME": 0.10,
                                    "symbol": "",
                                    "margin_level_WhenNoTrades": 0,
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test value_fetch > account 2
input_data_21 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "account",
                                "row2": "ACCOUNT_INFO_FREE_MARGIN_CHECK",
                                "params": {
                                    "margin_check_OP_TYPE": 1,
                                    "margin_check_VOLUME": 0.20,
                                    "symbol": "EURUSD",
                                    "margin_level_WhenNoTrades": 0,
                                    "adjust": ""
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test value_fetch > account 3: adjust
input_data_22 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-2c7551bb-c7d8-4e4c-a8cc-52d645f97187c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "+"
                            },
                            "left": {
                                "row1": "account",
                                "row2": "ACCOUNT_INFO_FREE_MARGIN_CHECK",
                                "params": {
                                    "margin_check_OP_TYPE": 1,
                                    "margin_check_VOLUME": 0.20,
                                    "symbol": "EURUSD",
                                    "margin_level_WhenNoTrades": 0,
                                    "adjust": "-15%"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            },
                            "adjust": "",
                            "variable": ""
                        },
                        "id": "2c7551bb-c7d8-4e4c-a8cc-52d645f97187",
                        "id_by_user": 4,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test trade/order in loop: comment
input_data_23 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "sourceHandle": "blue",
                        "target": "fc544226-4fbe-4fb9-85f7-b4056d3076dd",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4e76504d-1adf-4e20-9cb8-0911863ef991blue-fc544226-4fbe-4fb9-85f7-b4056d3076ddc"
                    },
                    {
                        "source": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "sourceHandle": "blue",
                        "target": "24da57e3-2946-4641-9110-aae54447a054",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4e76504d-1adf-4e20-9cb8-0911863ef991blue-24da57e3-2946-4641-9110-aae54447a054c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": ">",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "trade-order-in-loop",
                                "row2": "IN_LOOP_TRADE_ORDER_COMMENT",
                                "params": {

                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "20",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "fc544226-4fbe-4fb9-85f7-b4056d3076dd",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "type": "{0,1}",
                            "profit_mode": "PROFIT_MODE_PIPS_SUM",
                            "compare": ">",
                            "profit_amount": "0.0",
                            "profit_mode_each": "PROFIT_MODE_NO_MATTER"
                        },
                        "id": "24da57e3-2946-4641-9110-aae54447a054",
                        "id_by_user": 3,
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_profit_unrealized",
                        "blockName": "Check Profit (unrealized)"
                    }
                ]
            },
            "on_init": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_trade": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "nodesData": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    },
    "selected_name": "24c457b1-b820-493c-9977-ab60db13cf65",
    "name_by_user": "TEST 8962",
    "highestIndex": "4"
}

# test every n ticks fix
input_data_24 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "4e76504d-1adf-4e20-9cb8-0911863ef991",
            "sourceHandle": "blue",
            "target": "24da57e3-2946-4641-9110-aae54447a054",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-4e76504d-1adf-4e20-9cb8-0911863ef991blue-24da57e3-2946-4641-9110-aae54447a054c"
          },
          {
            "source": "4e76504d-1adf-4e20-9cb8-0911863ef991",
            "sourceHandle": "blue",
            "target": "69c32756-d1ec-490e-a86f-3806fbb5edb0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-4e76504d-1adf-4e20-9cb8-0911863ef991blue-69c32756-d1ec-490e-a86f-3806fbb5edb0c"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "profit_mode": "PROFIT_MODE_PIPS_SUM",
              "compare": ">",
              "profit_amount": "0.0",
              "profit_mode_each": "PROFIT_MODE_NO_MATTER"
            },
            "id": "24da57e3-2946-4641-9110-aae54447a054",
            "id_by_user": 3,
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_unrealized",
            "blockName": "Check Profit (unrealized)"
          },
          {
            "params": {
              "symbol": "",
              "n": "100"
            },
            "id": "69c32756-d1ec-490e-a86f-3806fbb5edb0",
            "id_by_user": 4,
            "blockName": "Every \"n\" ticks",
            "category": "time_filters",
            "block_name_mql": "every_n_ticks"
          }
        ]
      },
      "on_init": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_timer": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_trade": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_chart": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_deinit": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      }
    },
    "variables": [],
    "constants": []
  },
  "selected_name": "24c457b1-b820-493c-9977-ab60db13cf65",
  "name_by_user": "TEST 8962",
  "highestIndex": "5"
}

# test for each trade
input_data_25 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "4e76504d-1adf-4e20-9cb8-0911863ef991",
            "sourceHandle": "blue",
            "target": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-4e76504d-1adf-4e20-9cb8-0911863ef991blue-a423ac9c-fe6c-4af3-86d6-97290a7c6ebcc"
          },
          {
            "source": "f10a11d3-8a96-421a-8185-19fd71316267",
            "sourceHandle": "blue",
            "target": "09bfd295-2812-4e8e-8c36-d20d29d59a77",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-f10a11d3-8a96-421a-8185-19fd71316267blue-09bfd295-2812-4e8e-8c36-d20d29d59a77c"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
            "id_by_user": 4,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade",
            "blockName": "For each Trade"
          },
          {
            "params": {
              "max_times_to_pass": "1",
              "symbol": "",
              "timeframe": "PERIOD_CURRENT"
            },
            "id": "f10a11d3-8a96-421a-8185-19fd71316267",
            "id_by_user": 5,
            "category": "time_filters",
            "block_name_mql": "once_per_bar",
            "blockName": "Once per bar"
          },
          {
            "params": {
              "symbol": "",
              "group": "11",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrMaroon",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20"
            },
            "id": "09bfd295-2812-4e8e-8c36-d20d29d59a77",
            "id_by_user": 6,
            "blockName": "Buy now",
            "category": "buy_sell",
            "block_name_mql": "buy_now"
          }
        ]
      },
      "on_init": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_timer": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_trade": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_chart": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      },
      "on_deinit": {
        "nodes": [],
        "nodesData": [],
        "edges": []
      }
    },
    "variables": [],
    "constants": []
  },
  "selected_name": "24c457b1-b820-493c-9977-ab60db13cf65",
  "name_by_user": "TEST 8962",
  "highestIndex": "7"
}
