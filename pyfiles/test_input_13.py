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

# test market properties new
input_data_26 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "7fc8e3bd-6157-42d2-a702-c64c68857497",
                        "sourceHandle": "blue",
                        "target": "8e94f376-f0e1-4f7b-acaa-f0a0c2989a28",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-7fc8e3bd-6157-42d2-a702-c64c68857497blue-8e94f376-f0e1-4f7b-acaa-f0a0c2989a28c"
                    }
                ],
                "nodes": [
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
                            "label_1": "",
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
                                "row1": "market-properties",
                                "row2": "highest_price_candles_period",
                                "params": {
                                    "range_start": "20",
                                    "range_end": "30",
                                    "what_to_get": "GET_CANDLE_ID",
                                    "symbol": "EURUSD",
                                    "timeframe": "PERIOD_M5",
                                    "adjust": "*10"
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
                        "id": "8e94f376-f0e1-4f7b-acaa-f0a0c2989a28",
                        "id_by_user": 1,
                        "blockName": "Comment",
                        "category": "output_communication",
                        "block_name_mql": "comment"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "7fc8e3bd-6157-42d2-a702-c64c68857497",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "3"
}

# test market properties new 2
input_data_27 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "7fc8e3bd-6157-42d2-a702-c64c68857497",
                        "sourceHandle": "blue",
                        "target": "8e94f376-f0e1-4f7b-acaa-f0a0c2989a28",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-7fc8e3bd-6157-42d2-a702-c64c68857497blue-8e94f376-f0e1-4f7b-acaa-f0a0c2989a28c"
                    }
                ],
                "nodes": [
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
                            "label_1": "",
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
                                "row1": "market-properties",
                                "row2": "lowest_price_time_period",
                                "params": {
                                    "server_or_local_time": "TIME_LOCAL",
                                    "timestr_start": "08:00",
                                    "timestr_end": "13:00",
                                    "day_offset": "5",
                                    "what_to_get": "GET_PRICE",
                                    "symbol": "EURUSD",
                                    "timeframe": "PERIOD_M5",
                                    "adjust": "*10"
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
                        "id": "8e94f376-f0e1-4f7b-acaa-f0a0c2989a28",
                        "id_by_user": 1,
                        "blockName": "Comment",
                        "category": "output_communication",
                        "block_name_mql": "comment"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "7fc8e3bd-6157-42d2-a702-c64c68857497",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "3"
}

# test market properties new 3
input_data_28 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "7fc8e3bd-6157-42d2-a702-c64c68857497",
                        "sourceHandle": "blue",
                        "target": "8e94f376-f0e1-4f7b-acaa-f0a0c2989a28",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-7fc8e3bd-6157-42d2-a702-c64c68857497blue-8e94f376-f0e1-4f7b-acaa-f0a0c2989a28c"
                    }
                ],
                "nodes": [
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
                            "label_1": "",
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
                                "row1": "market-properties",
                                "row2": "highest_price_time_period",
                                "params": {
                                    "server_or_local_time": "TIME_LOCAL",
                                    "timestr_start": "12:30",
                                    "timestr_end": "13:00",
                                    "day_offset": "5",
                                    "what_to_get": "GET_TIME",
                                    "symbol": "EURUSD",
                                    "timeframe": "PERIOD_M5",
                                    "adjust": "-10pips"
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
                        "id": "8e94f376-f0e1-4f7b-acaa-f0a0c2989a28",
                        "id_by_user": 1,
                        "blockName": "Comment",
                        "category": "output_communication",
                        "block_name_mql": "comment"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "7fc8e3bd-6157-42d2-a702-c64c68857497",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "3"
}

# test market properties new 4
input_data_29 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
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
                                "row1": "market-properties",
                                "row2": "highest_price_candles_period",
                                "params": {
                                    "range_start": "4",
                                    "range_end": "8",
                                    "what_to_get": "GET_CANDLE_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test market properties: ask bid mid
input_data_30 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "ask_bid_mid",
                                "params": {
                                    "Price": "BID",
                                    "TickID": 25,
                                    "symbol": "XAUUSD",
                                    "adjust": "+14%"
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test market properties: name symbol market
input_data_31 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "name_symbol_market",
                                "params": {
                                    "adjust": "+14"
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test market properties: timeframe
input_data_32 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "timeframe",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test check profit last closed
input_data_33 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "timeframe",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "symbols_str": "EURUSD",
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "group_number": 18,
                            "type": "{1}",
                            "ProfitAmount": 20.0,
                            "OncePerTrade": True,
                            "compare": "!="
                        },
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "id_by_user": 3,
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_profit_last_closed",
                        "blockName": "Check profit (last closed)"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test check consecutive losses
input_data_34 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "timeframe",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "symbols_str": "GBPUSD",
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "group_number": 18,
                            "type": "{0}",

                            "ConsecutiveCount": 5,
                            "compare": "<="
                        },
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "id_by_user": 3,
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_consecutive_losses",
                        "blockName": "Check consecutive losses"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test check consecutive profits
input_data_35 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "timeframe",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "symbols_str": "GBPUSD",
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "group_number": 25,
                            "type": "{1}",

                            "ConsecutiveCount": 4,
                            "compare": "=="
                        },
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "id_by_user": 3,
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_consecutive_profits",
                        "blockName": "Check consecutive profits"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test value > text fix
input_data_36 = {
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
                        "params": {},
                        "id": "3357a0da-d060-4ed5-8d1c-aac7a6bf0d34",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
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
                            "label_1": "my label:",
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
                                    "value": "str",
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
                        "id": "22af07d5-bbff-4bc0-b8fd-3b37479b9f51",
                        "id_by_user": 2,
                        "blockName": "Comment",
                        "category": "output_communication",
                        "block_name_mql": "comment"
                    }
                ],
                "edges": [
                    {
                        "source": "3357a0da-d060-4ed5-8d1c-aac7a6bf0d34",
                        "sourceHandle": "blue",
                        "target": "22af07d5-bbff-4bc0-b8fd-3b37479b9f51",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "841233d7-7a4a-402e-80ad-5185069a0277"
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
        "variables": [
            {
                "type": "string",
                "name": "str",
                "value": "hello world",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "9e1fd44d-c2fe-4a7c-ba98-c0087a57425a",
    "name_by_user": "test 1357",
    "highestIndex": "3"
}

# test check type last closed
input_data_37 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "timeframe",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "symbols_str": "EURUSD",
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "group_number": 18,
                            "LastOrderType": 0,
                            "OncePerTrade": False
                        },
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "id_by_user": 3,
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_type_last_closed",
                        "blockName": "Check type (last closed)"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test check distance
input_data_38 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "sourceHandle": "blue",
                        "target": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-90754c0d-f01e-4aa1-bb06-a2bb630c0451blue-e7ae7deb-3baf-44fa-b296-d05bbee73745c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "operator": {
                                "label": "×>",
                                "cross_width": 10
                            },
                            "left": {
                                "row1": "market-properties",
                                "row2": "timeframe",
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
                        "id": "e7ae7deb-3baf-44fa-b296-d05bbee73745",
                        "id_by_user": 2,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "DistanceIsAbsolute": False,
                            "compare": ">=",
                            "upper_level": {
                                "row1": "market-properties",
                                "row2": "timeframe",
                                "params": {
                                }
                            },
                            "lower_level": {
                                "row1": "market-properties",
                                "row2": "timeframe",
                                "params": {
                                }
                            },
                            "checking_distance": {
                                "row1": "market-properties",
                                "row2": "timeframe",
                                "params": {
                                }
                            }
                        },
                        "id": "90754c0d-f01e-4aa1-bb06-a2bb630c0451",
                        "id_by_user": 3,
                        "category": "check_trading_conditions",
                        "block_name_mql": "check_distance",
                        "blockName": "Check distance"
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
    "selected_name": "dd2bd08d-06fe-4bd8-828d-dd65cae56e5e",
    "name_by_user": "test 2254",
    "highestIndex": "4"
}

# test for each pending order
input_data_39 = {
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
                            "type": "{2,4}",
                            "type_pending": "{2,3}",
                            "skip_n": "0",
                            "every_n": "1",
                            "not_more_than_n": "0",
                            "loop_direction": "newest_first",
                            "second_output": "always"
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "for_each_pending_order",
                        "blockName": "For each Pending Order"
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

# test for each closed trade
input_data_40 = {
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
                        "block_name_mql": "for_each_closed_trade",
                        "blockName": "For each Closed Trade"
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

# test once per trade order
input_data_41 = {
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
                        "params": {
                            "AllowOldOrders": True
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "once_per_trade_order",
                        "blockName": "Once per Trade/Order"
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
                        "block_name_mql": "for_each_closed_trade",
                        "blockName": "For each Closed Trade"
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

# test pips away from open price
input_data_42 = {
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
                        "params": {
                            "AllowOldOrders": True
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "once_per_trade_order",
                        "blockName": "Once per Trade/Order"
                    },
                    {
                        "params": {
                            "DirectionMode": "trading",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "function",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "pips_away_input_in_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test pips away from open price 2
input_data_43 = {
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
                        "params": {
                            "AllowOldOrders": True
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "once_per_trade_order",
                        "blockName": "Once per Trade/Order"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test single candle template
input_data_44 = {
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
                        "params": {
                            "SignalType": "continuous",
                            "CandleType": "both",
                            "CandleID": 1,
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "UpperWickMode": "between",
                            "UpWickFrom": 10.0,
                            "UpWickTo": 20.0,
                            "LowerWickMode": "between",
                            "LoWickFrom": 10.0,
                            "LoWickTo": 20.0,
                            "CandleMinSize": 0.0,
                            "CandleMaxSize": 0.0
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "various_signals",
                        "block_name_mql": "single_candle_template",
                        "blockName": "Single candle template"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test single candle template 2
input_data_45 = {
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
                        "params": {
                            "SignalType": "continuous",
                            "CandleType": "bear",
                            "CandleID": 12,
                            "symbol": "",
                            "timeframe": "PERIOD_M5",
                            "UpperWickMode": "between",
                            "UpWickFrom": 10.0,
                            "UpWickTo": 20.0,
                            "LowerWickMode": "from",
                            "LoWickFrom": 10.0,
                            "LoWickTo": 20.0,
                            "CandleMinSize": 0.0,
                            "CandleMaxSize": 0.0
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "various_signals",
                        "block_name_mql": "single_candle_template",
                        "blockName": "Single candle template"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test check age
input_data_46 = {
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
                        "params": {
                            "AgeRelativeTo": "open-time",
                            "AgeCompare": ">:",
                            "AgeDays": 60,
                            "AgeHours": 66.0,
                            "AgeMinutes": 666.0,
                            "AgeSeconds": 6666.0,
                            "compare": "=="
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "check_age",
                        "blockName": "check age"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test modify stops
input_data_47 = {
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
                        "params": {
                            "RelativeTo": "openprice",
                            "NewSLmode": "fixed",
                            "NewStopLoss": 50.0,
                            "NewStopLossPercentPrice": 0.55,
                            "NewStopLossPercent": 50.0,
                            "NewStopLossPercentTP": 50.0,
                            "NewTPmode": "fixed",
                            "NewTakeProfit": 50.0,
                            "NewTakeProfitPercentPrice": 0.55,
                            "NewTakeProfitPercent": 50.0,
                            "NewTakeProfitPercentSL": 50.0,
                            "LevelColor": "clrDeepPink",
                            "relative_to_dynamic": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_sl_mode_function": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_sl_mode_dynamicPips": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_sl_mode_dynamicDigits": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_tp_mode_function": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_tp_mode_dynamicPips": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_tp_mode_dynamicDigits": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "modify_stops",
                        "blockName": "Modify stops"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test modify stops 2
input_data_48 = {
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
                        "params": {
                            "RelativeTo": "openprice",
                            "NewSLmode": "fixed",
                            "NewStopLoss": 50.0,
                            "NewStopLossPercentPrice": 0.55,
                            "NewStopLossPercent": 50.0,
                            "NewStopLossPercentTP": 50.0,
                            "NewTPmode": "fixed",
                            "NewTakeProfit": 50.0,
                            "NewTakeProfitPercentPrice": 0.55,
                            "NewTakeProfitPercent": 50.0,
                            "NewTakeProfitPercentSL": 50.0,
                            "LevelColor": "clrDeepPink",
                            "relative_to_dynamic": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "new_sl_mode_function": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "modify_stops",
                        "blockName": "Modify stops"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test alert message
input_data_49 = {
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
                        "params": {
                            "AlertTitle": "Alert Message",
                            "AlertLabel1": "aaa",
                            "AlertLabel2": "bbb",
                            "AlertLabel3": "",
                            "AlertLabel4": "",
                            "AlertLabel5": "",
                            "AlertLabel6": "ccc",
                            "AlertLabel7": "",
                            "AlertLabel8": "",
                            "AlertLabel9": "",
                            "AlertLabel10": "ddd",
                            "AlsoSendNotification": False,
                            "value_1": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_2": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_6": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_10": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "output_communication",
                        "block_name_mql": "alert_message",
                        "blockName": "Alert message"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test phone notification
input_data_50 = {
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
                        "params": {
                            "Title": "Hello dear",
                            "Label1": "aaa",
                            "Label2": "bbb",
                            "Label3": "",
                            "Label4": "",
                            "Label5": "",
                            "Label6": "ccc",
                            "Label7": "",
                            "Label8": "",
                            "Label9": "",
                            "Label10": "ddd",
                            "value_2": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_3": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "value_7": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "output_communication",
                        "block_name_mql": "phone_notification",
                        "blockName": "Phone Notification"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test play sound
input_data_51 = {
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
                        "params": {
                            "MTsound": "ok",
                            "MYsound": "myfile.wav"
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "output_communication",
                        "block_name_mql": "play_sound",
                        "blockName": "Play sound"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test prompt
input_data_52 = {
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
                        "params": {
                            "PromptCaption": "test",
                            "PromptText": "yasss",
                            "PromptButtons": 2
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "output_communication",
                        "block_name_mql": "prompt",
                        "blockName": "Prompt"

                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test bull candle
input_data_53 = {
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
                        "params": {
                            "SignalType": "continuous",
                            "CandleID": 1,
                            "MinBodySize": 5.0,
                            "MaxBodySize": 0.0,
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "various_signals",
                        "block_name_mql": "bull_candle",
                        "blockName": "Bull candle"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test bear candle
input_data_54 = {
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
                        "params": {
                            "SignalType": "continuous",
                            "CandleID": 1,
                            "MinBodySize": 5.0,
                            "MaxBodySize": 0.0,
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "various_signals",
                        "block_name_mql": "bear_candle",
                        "blockName": "Bear candle"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test draw arrow
input_data_55 = {
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
                        "params": {},
                        "id": "25c652ff-4ab4-467d-8cf8-c89fabecf9a3",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_type": "OBJ_ARROW_UP",
                            "obj_anchor": "ANCHOR_TOP",
                            "obj_width": "1",
                            "obj_z_order": "0",
                            "obj_chart_subwindow": "",
                            "obj_style": "STYLE_SOLID",
                            "obj_back": "false",
                            "obj_selected": "false",
                            "obj_hidden": "false",
                            "obj_selectable": "false",
                            "obj_color": "clrDeepPink",
                            "obj_name": "my_arrow",
                            "object_update": "true",
                            "object_per_bar": "false",
                            "time_1": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "Shift in Time": "0",
                                    "Time Mode": "MODE_TIME_NOW"
                                }
                            }
                        },
                        "id": "d5a902cf-567d-4e43-9ec1-c8e39b504089",
                        "id_by_user": 2,
                        "category": "chart_objects",
                        "block_name_mql": "draw_arrow",
                        "blockName": "Draw Arrow"
                    }
                ],
                "edges": [
                    {
                        "source": "25c652ff-4ab4-467d-8cf8-c89fabecf9a3",
                        "sourceHandle": "blue",
                        "target": "d5a902cf-567d-4e43-9ec1-c8e39b504089",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "477cef77-ba3e-4994-8808-1f3084b830c6"
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
    "selected_name": "1bbefb4c-7277-49b7-80be-91b2c2a728f1",
    "name_by_user": "test 5896",
    "highestIndex": "3"
}

# test modify color
input_data_56 = {
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
                        "params": {
                            "SetObjColor": "clrRed"
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "modify_color",
                        "blockName": "Modify color"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test check button state
input_data_57 = {
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
                        "params": {
                            "ObjState": "false"
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "check_button_state",
                        "blockName": "Check button state"
                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test move
input_data_58 = {
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
                        "params": {
                            "SetObjTime1": "true",
                            "SetObjPrice1": "false",
                            "SetObjTime2": "false",
                            "SetObjPrice2": "false",
                            "SetObjTime3": "false",
                            "SetObjPrice3": "false",
                            "time_1": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "time_2": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "price_1": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            },
                            "price_3": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "move",
                        "blockName": "move"

                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test modify text description
input_data_59 = {
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
                        "params": {
                            "text": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "modify_text_description",
                        "blockName": "modify text (description)"

                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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

# test check type
input_data_60 = {
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
                        "params": {
                            "CheckBuyOrSell": "buy",
                            "CheckLimitOrStop": "both"
                        },
                        "id": "4e76504d-1adf-4e20-9cb8-0911863ef991",
                        "id_by_user": 1,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "check_type",
                        "blockName": "check type"

                    },
                    {
                        "params": {
                            "DirectionMode": "double",
                            "PipsAwayReferencePrice": 0,
                            "OpenPriceMode": 0,
                            "PipsAwayMode": "functionFraction",
                            "PipsAway": 50.0,
                            "PipsAwayPercent": 150.0,
                            "custom_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 25.8,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "a423ac9c-fe6c-4af3-86d6-97290a7c6ebc",
                        "id_by_user": 4,
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "pips_away_from_open_price",
                        "blockName": "Pips away from open price"
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
