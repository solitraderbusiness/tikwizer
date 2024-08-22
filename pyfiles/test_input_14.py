# test tp sl mode : customs
input_data_1 = {
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
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "take_profit_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 20,
                                    "adjust": ""
                                }
                            },
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

# test tp sl mode : customs 2
input_data_2 = {
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
                            "stop_loss_mode": "TPSL_MODE_CUSTOM_PRICE_FRACTION",
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "take_profit_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 20,
                                    "adjust": ""
                                }
                            },
                            "stop_loss_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 40,
                                    "adjust": ""
                                }
                            },
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

# test tp sl mode : customs 3
input_data_3 = {
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
                            "stop_loss_mode": "TPSL_MODE_CUSTOM_PRICE_LEVEL",
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "take_profit_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 20,
                                    "adjust": ""
                                }
                            },
                            "stop_loss_price_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 40,
                                    "adjust": ""
                                }
                            },
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

# test enum in constants fix
input_data_4 = {
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
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
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
                        "id": "7fbbd085-22c7-4296-977a-e216ad8af62e",
                        "id_by_user": 1,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {},
                        "id": "3f394871-ee41-4bda-aeef-1af9890e8458",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "stoploss": "20",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "takeprofit": "20",
                            "symbol": "",
                            "group": "11",
                            "volume_upper_limit": "0",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "how_much_volume": "0.1"
                        },
                        "id": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
                        "id_by_user": 4,
                        "category": "buy_sell",
                        "block_name_mql": "buy_now",
                        "blockName": "Buy now"
                    },
                    {
                        "params": {
                            "type": "{0,1}",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11"
                        },
                        "id": "815fcf92-7d67-4df8-8965-8f1e506db863",
                        "id_by_user": 5,
                        "category": "check_trades_orders_count",
                        "block_name_mql": "if_trade",
                        "blockName": "If trade"
                    }
                ],
                "edges": [
                    {
                        "source": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
                        "sourceHandle": "blue",
                        "target": "7fbbd085-22c7-4296-977a-e216ad8af62e",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "60d7f212-fb62-4536-9f1c-dd1074134c92"
                    },
                    {
                        "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
                        "sourceHandle": "blue",
                        "target": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "e8c7cb9f-86f4-4c3d-91ba-ec477c72be99"
                    },
                    {
                        "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
                        "sourceHandle": "blue",
                        "target": "815fcf92-7d67-4df8-8965-8f1e506db863",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "ee667621-0fb5-45ca-b2d2-d6436f7405a9"
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
        "constants": [
            {
                "type": "enum ",
                "name": "my_enum",
                "value": "{hello}",
                "description": ""
            }
        ]
    },
    "selected_name": "a79a3586-967f-4e69-89d7-dfd97031fd21",
    "name_by_user": "",
    "highestIndex": "6"
}

# test enum in constants fix 2
input_data_5 = {
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
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
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
                        "id": "7fbbd085-22c7-4296-977a-e216ad8af62e",
                        "id_by_user": 46,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {},
                        "id": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
                        "id_by_user": 41,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {},
                        "id": "3f394871-ee41-4bda-aeef-1af9890e8458",
                        "id_by_user": 37,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "stoploss": "20",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "takeprofit": "20",
                            "symbol": "",
                            "group": "11",
                            "volume_upper_limit": "0",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "how_much_volume": "0.1"
                        },
                        "id": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
                        "id_by_user": 50,
                        "category": "buy_sell",
                        "block_name_mql": "buy_now",
                        "blockName": "Buy now"
                    },
                    {
                        "params": {
                            "type": "{0,1}",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11"
                        },
                        "id": "815fcf92-7d67-4df8-8965-8f1e506db863",
                        "id_by_user": 47,
                        "category": "check_trades_orders_count",
                        "block_name_mql": "if_trade",
                        "blockName": "If trade"
                    }
                ],
                "edges": [
                    {
                        "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
                        "sourceHandle": "blue",
                        "target": "815fcf92-7d67-4df8-8965-8f1e506db863",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "ee667621-0fb5-45ca-b2d2-d6436f7405a9"
                    },
                    {
                        "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
                        "sourceHandle": "blue",
                        "target": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "e8c7cb9f-86f4-4c3d-91ba-ec477c72be99"
                    },
                    {
                        "source": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
                        "sourceHandle": "blue",
                        "target": "7fbbd085-22c7-4296-977a-e216ad8af62e",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "60d7f212-fb62-4536-9f1c-dd1074134c92"
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
                "type": "double",
                "name": "z",
                "value": "",
                "description": ""
            }
        ],
        "constants": [
            {
                "type": "enum",
                "name": "my_enum",
                "value": "{hello}",
                "description": ""
            },
            {
                "type": "my_enum",
                "name": "chetori",
                "value": "hello",
                "description": ""
            }
        ]
    },
    "selected_name": "a79a3586-967f-4e69-89d7-dfd97031fd21",
    "name_by_user": "",
    "highestIndex": "6"
}

# test buy sell custom tp sl
input_data_6 = {
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
                        "id": "6278d6d3-1684-412d-abae-83676fc8cef4",
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
                            "stop_loss_mode": "TPSL_MODE_CUSTOM_PRICE_LEVEL",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "takeprofit": "20",
                            "TPSL_MODE_CUSTOM_PRICE_LEVEL": {
                                "row1": "candle",
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_CLOSE",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "adjust": "",
                                    "shift": "20"
                                }
                            }
                        },
                        "id": "0148f1f4-86cc-4bf3-8b01-f8dad77c6aef",
                        "id_by_user": 4,
                        "blockName": "Buy now",
                        "category": "buy_sell",
                        "block_name_mql": "buy_now"
                    }
                ],
                "edges": [
                    {
                        "source": "6278d6d3-1684-412d-abae-83676fc8cef4",
                        "sourceHandle": "blue",
                        "target": "0148f1f4-86cc-4bf3-8b01-f8dad77c6aef",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "aab880d8-3373-46a3-847a-a854d5a0c935"
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
                "type": "double",
                "name": "z",
                "value": "",
                "description": ""
            }
        ],
        "constants": [
            {
                "type": "enum",
                "name": "my_enum",
                "value": "{hello}",
                "description": ""
            },
            {
                "type": "my_enum",
                "name": "chetori",
                "value": "hello",
                "description": ""
            }
        ]
    },
    "selected_name": "a79a3586-967f-4e69-89d7-dfd97031fd21",
    "name_by_user": "",
    "highestIndex": "5"
}

# test buy sell custom tp sl 2
input_data_7 = {
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
                        "id": "6278d6d3-1684-412d-abae-83676fc8cef4",
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
                            "stop_loss_mode": "TPSL_MODE_CUSTOM_PRICE_LEVEL",
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PRICE_FRACTION",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "TPSL_MODE_CUSTOM_PRICE_LEVEL": {
                                "row1": "candle",
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_CLOSE",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "adjust": "",
                                    "shift": "20"
                                }
                            },
                            "TPSL_MODE_CUSTOM_PRICE_FRACTION": {
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "0148f1f4-86cc-4bf3-8b01-f8dad77c6aef",
                        "id_by_user": 4,
                        "blockName": "Buy now",
                        "category": "buy_sell",
                        "block_name_mql": "buy_now"
                    }
                ],
                "edges": [
                    {
                        "source": "6278d6d3-1684-412d-abae-83676fc8cef4",
                        "sourceHandle": "blue",
                        "target": "0148f1f4-86cc-4bf3-8b01-f8dad77c6aef",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "aab880d8-3373-46a3-847a-a854d5a0c935"
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
                "type": "double",
                "name": "z",
                "value": "",
                "description": ""
            }
        ],
        "constants": [
            {
                "type": "enum",
                "name": "my_enum",
                "value": "{hello}",
                "description": ""
            },
            {
                "type": "my_enum",
                "name": "chetori",
                "value": "hello",
                "description": ""
            }
        ]
    },
    "selected_name": "a79a3586-967f-4e69-89d7-dfd97031fd21",
    "name_by_user": "",
    "highestIndex": "5"
}

# test volume profile stackoverflow fix
input_data_8 = {
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
                        "id": "8967b46f-4afb-4d16-8b1d-c577d70f87da",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "ModeLevelWidth": "1",
                            "ModeLineWidth": "2",
                            "VwapColor": "clrNONE",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "MedianColor": "clrNONE",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "StatLineStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "VolumeType": "VOLUME_TICK",
                            "DataSource": "VP_SOURCE_M1",
                            "HgLineWidth": "2",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "Id": "+vpr",
                            "HgWidthPercent": "15",
                            "ShowHorizon": "true",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeFromColor": "clrDarkGreen",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "timeFrom_date": "D'2024.07.12 11:30:27'",
                            "timeTo_date": "D'2024.07.12 19:30:27'",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": ""
                        },
                        "id": "5d0c183b-57b4-4aab-b425-69ed31f40c31",
                        "id_by_user": 2,
                        "category": "various_signals",
                        "block_name_mql": "volume_profile",
                        "blockName": "Volume Profile"
                    }
                ],
                "edges": [
                    {
                        "source": "8967b46f-4afb-4d16-8b1d-c577d70f87da",
                        "sourceHandle": "blue",
                        "target": "5d0c183b-57b4-4aab-b425-69ed31f40c31",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "21b9d52d-6d4a-4c39-9971-1d18a9c3653f"
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
    "selected_name": "be1765c3-6cf7-4e2f-b254-ceae698bf72d",
    "name_by_user": "fwsafcds",
    "highestIndex": "3"
}

# test volume profile
input_data_9 = {
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
                        "id": "cf2acff2-a2bb-40fb-a637-c459885d611b",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "11:30:27",
                            "timeTo_str": "19:30:27",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "c6d503d6-e7e2-45c6-9f31-bbc2afcbb187",
                        "id_by_user": 2,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "cf2acff2-a2bb-40fb-a637-c459885d611b",
                        "sourceHandle": "blue",
                        "target": "c6d503d6-e7e2-45c6-9f31-bbc2afcbb187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "19e51291-8d7b-4b1d-8327-88db0d5280dc"
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
    "selected_name": "d25b5f01-06db-4746-ac28-f4d29e64912a",
    "name_by_user": "testsdfd",
    "highestIndex": "3"
}

# test volume profile multiple instances
input_data_10 = {
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
                        "id": "cf2acff2-a2bb-40fb-a637-c459885d611b",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_date": "11:00",
                            "timeTo_date": "19:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "c6d503d6-e7e2-45c6-9f31-bbc2afcbb187",
                        "id_by_user": 2,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_date": "01:00",
                            "timeTo_date": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "43d2d415-a825-4571-8128-966502767568",
                        "id_by_user": 3,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "cf2acff2-a2bb-40fb-a637-c459885d611b",
                        "sourceHandle": "blue",
                        "target": "c6d503d6-e7e2-45c6-9f31-bbc2afcbb187",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "19e51291-8d7b-4b1d-8327-88db0d5280dc"
                    },
                    {
                        "source": "cf2acff2-a2bb-40fb-a637-c459885d611b",
                        "sourceHandle": "blue",
                        "target": "43d2d415-a825-4571-8128-966502767568",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "c2153b76-11e4-47ab-8e91-63d22367380d"
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
    "selected_name": "d25b5f01-06db-4746-ac28-f4d29e64912a",
    "name_by_user": "testsdfd",
    "highestIndex": "4"
}

# test volume profile, some fields changed
input_data_11 = {
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
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "70",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "f86fff9a-494e-430a-8977-c12ddd184a6b",
                        "id_by_user": 1,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {},
                        "id": "160ccd38-caa1-4743-84bc-28e2441aa7d5",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "160ccd38-caa1-4743-84bc-28e2441aa7d5",
                        "sourceHandle": "blue",
                        "target": "f86fff9a-494e-430a-8977-c12ddd184a6b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "4d559fe3-f380-414f-891e-2061661c912b"
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
    "selected_name": "f7af62dd-8976-43a5-a6f8-ffd8c6d79615",
    "name_by_user": "test",
    "highestIndex": "3"
}

# test volume profile real scenario: update every day on 11 to 15
input_data_12 = {
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
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "15:00",
                            "timeTo_str": "11:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "f86fff9a-494e-430a-8977-c12ddd184a6b",
                        "id_by_user": 1,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "==",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_CANDLE_TIME",
                                    "mode_time_shift": "0",
                                    "time_candle_id": "1",
                                    "time_market": "",
                                    "time_candle_timeframe": "PERIOD_CURRENT"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_TIMESTAMP",
                                    "mode_time_shift": "0",
                                    "time_stamp": "15:00"
                                }
                            }
                        },
                        "id": "43e7d535-8c26-4c55-9a41-c4b8669b1f48",
                        "id_by_user": 3,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "e62ad514-4274-442e-9166-fd985b4982bc",
                        "id_by_user": 4,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    }
                ],
                "edges": [
                    {
                        "source": "e62ad514-4274-442e-9166-fd985b4982bc",
                        "sourceHandle": "blue",
                        "target": "43e7d535-8c26-4c55-9a41-c4b8669b1f48",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "25672cdf-8ceb-413e-b077-4ad3a2b7225b"
                    },
                    {
                        "source": "43e7d535-8c26-4c55-9a41-c4b8669b1f48",
                        "sourceHandle": "blue",
                        "target": "f86fff9a-494e-430a-8977-c12ddd184a6b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "85feaab7-ff6f-4911-a3e2-76e781b08621"
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
    "selected_name": "f7af62dd-8976-43a5-a6f8-ffd8c6d79615",
    "name_by_user": "test",
    "highestIndex": "5"
}

# test volume profile real scenario: update every day on 11 to 15 NO 2
input_data_13 = {
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
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "time_from",
                            "timeTo_str": "time_to",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "f86fff9a-494e-430a-8977-c12ddd184a6b",
                        "id_by_user": 1,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "==",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_CANDLE_TIME",
                                    "mode_time_shift": "0",
                                    "time_candle_id": "1",
                                    "time_market": "",
                                    "time_candle_timeframe": "PERIOD_CURRENT"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_TIMESTAMP",
                                    "mode_time_shift": "0",
                                    "time_stamp": "15:00"
                                }
                            }
                        },
                        "id": "43e7d535-8c26-4c55-9a41-c4b8669b1f48",
                        "id_by_user": 3,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "e62ad514-4274-442e-9166-fd985b4982bc",
                        "id_by_user": 4,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    },
                    {
                        "params": {
                            "variable1": {
                                "variable_name": "time_from",
                                "value_fetch": {
                                    "row1": "value",
                                    "row2": "Time",
                                    "params": {
                                        "mode_time": "MODE_TIME_CANDLE_TIME",
                                        "mode_time_shift": "0",
                                        "time_candle_id": "16",
                                        "time_market": "",
                                        "time_candle_timeframe": "PERIOD_CURRENT"
                                    }
                                }
                            },
                            "variable2": {
                                "variable_name": "time_to",
                                "value_fetch": {
                                    "row1": "value",
                                    "row2": "Time",
                                    "params": {
                                        "mode_time": "MODE_TIME_CANDLE_TIME",
                                        "mode_time_shift": "0",
                                        "time_candle_id": "1",
                                        "time_market": "",
                                        "time_candle_timeframe": "PERIOD_CURRENT"
                                    }
                                }
                            },
                            "variable3": {
                                "variable_name": "",
                                "value_fetch": {
                                    "row2": "Numeric",
                                    "params": {
                                        "value": "1",
                                        "adjust": ""
                                    }
                                }
                            },
                            "variable4": {
                                "variable_name": "",
                                "value_fetch": {
                                    "row2": "Numeric",
                                    "params": {
                                        "value": "1",
                                        "adjust": ""
                                    }
                                }
                            },
                            "variable5": {
                                "variable_name": "",
                                "value_fetch": {
                                    "row2": "Numeric",
                                    "params": {
                                        "value": "1",
                                        "adjust": ""
                                    }
                                }
                            }
                        },
                        "variable1": {},
                        "variable2": {},
                        "variable3": {},
                        "variable4": {},
                        "variable5": {},
                        "id": "20acfc25-ac54-4242-b087-d9c6cb51aa86",
                        "id_by_user": 5,
                        "blockName": "Modify Variables",
                        "category": "variables",
                        "block_name_mql": "modify_variables"
                    }
                ],
                "edges": [
                    {
                        "source": "e62ad514-4274-442e-9166-fd985b4982bc",
                        "sourceHandle": "blue",
                        "target": "43e7d535-8c26-4c55-9a41-c4b8669b1f48",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "25672cdf-8ceb-413e-b077-4ad3a2b7225b"
                    },
                    {
                        "source": "43e7d535-8c26-4c55-9a41-c4b8669b1f48",
                        "sourceHandle": "blue",
                        "target": "20acfc25-ac54-4242-b087-d9c6cb51aa86",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "ef7e62b7-26ed-46d3-ab95-47ce7d82b923"
                    },
                    {
                        "source": "20acfc25-ac54-4242-b087-d9c6cb51aa86",
                        "sourceHandle": "blue",
                        "target": "f86fff9a-494e-430a-8977-c12ddd184a6b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "d5bb673d-76c6-4cd0-b9e4-d6b4d17e4199"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "f7af62dd-8976-43a5-a6f8-ffd8c6d79615",
    "name_by_user": "test",
    "highestIndex": "6"
}

# test volume profile
input_data_14 = {
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
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "e62ad514-4274-442e-9166-fd985b4982bc",
                        "id_by_user": 4,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "1399703d-f1f5-4b9e-ac6c-8a89d4038913",
                        "id_by_user": 5,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "e62ad514-4274-442e-9166-fd985b4982bc",
                        "sourceHandle": "blue",
                        "target": "1399703d-f1f5-4b9e-ac6c-8a89d4038913",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "eab83e4d-858f-4ad7-844e-3981ab6420d3"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "f7af62dd-8976-43a5-a6f8-ffd8c6d79615",
    "name_by_user": "test",
    "highestIndex": "6"
}

# test volume profile
input_data_15 = {
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
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "1399703d-f1f5-4b9e-ac6c-8a89d4038913",
                        "id_by_user": 5,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {},
                        "id": "5ee39709-fceb-439f-ba34-7041b2e7126f",
                        "id_by_user": 6,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "5ee39709-fceb-439f-ba34-7041b2e7126f",
                        "sourceHandle": "blue",
                        "target": "1399703d-f1f5-4b9e-ac6c-8a89d4038913",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "5567c525-3e9f-420b-8871-540d28f65302"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "f7af62dd-8976-43a5-a6f8-ffd8c6d79615",
    "name_by_user": "test",
    "highestIndex": "7"
}

# test volume profile
input_data_16 = {
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
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "cc5c1704-d553-4e14-b6e4-45a88aa58adc",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "==",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_CANDLE_TIME",
                                    "mode_time_shift": "0",
                                    "time_candle_id": "1",
                                    "time_market": "",
                                    "time_candle_timeframe": "PERIOD_CURRENT"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_TIMESTAMP",
                                    "mode_time_shift": "0",
                                    "time_stamp": "15:00"
                                }
                            }
                        },
                        "id": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "id_by_user": 3,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "11:00",
                            "timeTo_str": "15:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "cc5c1704-d553-4e14-b6e4-45a88aa58adc",
                        "sourceHandle": "blue",
                        "target": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "68b2e058-764c-435b-99a4-9b36519fc277"
                    },
                    {
                        "source": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "sourceHandle": "blue",
                        "target": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "58ae1f13-8b87-4ad9-a4f6-8be38f0cf946"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "ac5cd6a0-e6a5-477e-9ea9-f0a8b14f6aef",
    "name_by_user": "fdsfsdfds",
    "highestIndex": "5"
}

# test volume profile
input_data_17 = {
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
                        "id": "8695a82d-1763-4f34-9108-610983927ec1",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "5c8a3d94-5671-435b-9794-42895b5893cd",
                        "id_by_user": 2,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "8695a82d-1763-4f34-9108-610983927ec1",
                        "sourceHandle": "blue",
                        "target": "5c8a3d94-5671-435b-9794-42895b5893cd",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "dab131c4-3c5f-4604-a7b2-59e17e73f1a9"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "9e4f0317-9c0a-47ba-b570-af0845c32ef9",
    "name_by_user": "vp all ticks",
    "highestIndex": "3"
}

# test volume profile
input_data_18 = {
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
                            "redraw_each_time": "true",
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "5c8a3d94-5671-435b-9794-42895b5893cd",
                        "id_by_user": 2,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {
                            "server_or_local_time": "TIME_SERVER",
                            "FirstStartHour": "11:00",
                            "FirstEndHour": "23:00",
                            "SecondHoursBlock": "false",
                            "ThirdHoursBlock": "false",
                            "FourthHoursBlock": "false"
                        },
                        "id": "a1d32db3-1148-4f66-af91-5f7785c8811e",
                        "id_by_user": 3,
                        "blockName": "Hours filter",
                        "category": "time_filters",
                        "block_name_mql": "hours_filter"
                    }
                ],
                "edges": [
                    {
                        "source": "a1d32db3-1148-4f66-af91-5f7785c8811e",
                        "sourceHandle": "blue",
                        "target": "5c8a3d94-5671-435b-9794-42895b5893cd",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "3fe593bd-635f-4fc8-90b0-7b64cd9623e3"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "9e4f0317-9c0a-47ba-b570-af0845c32ef9",
    "name_by_user": "vp all ticks",
    "highestIndex": "4"
}

# test volume profile
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
                            "server_or_local_time": "TIME_SERVER",
                            "FirstStartHour": "11:00",
                            "FirstEndHour": "23:00",
                            "SecondHoursBlock": "false",
                            "ThirdHoursBlock": "false",
                            "FourthHoursBlock": "false"
                        },
                        "id": "a1d32db3-1148-4f66-af91-5f7785c8811e",
                        "id_by_user": 3,
                        "blockName": "Hours filter",
                        "category": "time_filters",
                        "block_name_mql": "hours_filter"
                    },
                    {
                        "params": {
                            "redraw_each_time": "false",
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "af66e545-5f4b-4be4-89b0-09cdb96d9961",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "a1d32db3-1148-4f66-af91-5f7785c8811e",
                        "sourceHandle": "blue",
                        "target": "af66e545-5f4b-4be4-89b0-09cdb96d9961",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "1d9240fa-125e-4c3f-b060-9e8b2e246c2a"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "9e4f0317-9c0a-47ba-b570-af0845c32ef9",
    "name_by_user": "vp all ticks",
    "highestIndex": "5"
}

# test volume profile
input_data_20 = {
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
                            "redraw_each_time": "true",
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "af66e545-5f4b-4be4-89b0-09cdb96d9961",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "6326f0f8-876c-4d7f-b40a-831268f6c7a7",
                        "id_by_user": 5,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    }
                ],
                "edges": [
                    {
                        "source": "6326f0f8-876c-4d7f-b40a-831268f6c7a7",
                        "sourceHandle": "blue",
                        "target": "af66e545-5f4b-4be4-89b0-09cdb96d9961",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "6aad4503-7d2d-4355-ba3c-f79ec4b83fbf"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "9e4f0317-9c0a-47ba-b570-af0845c32ef9",
    "name_by_user": "vp all ticks",
    "highestIndex": "6"
}

# test volume profile
input_data_21 = {
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
                            "redraw_each_time": "true",
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": ""
                        },
                        "id": "af66e545-5f4b-4be4-89b0-09cdb96d9961",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {},
                        "id": "24c3dbed-d4ef-4e31-b9bf-65f1f994b6cb",
                        "id_by_user": 5,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "24c3dbed-d4ef-4e31-b9bf-65f1f994b6cb",
                        "sourceHandle": "blue",
                        "target": "af66e545-5f4b-4be4-89b0-09cdb96d9961",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "1c83eb90-65e4-49fc-9299-03708b8e6327"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "9e4f0317-9c0a-47ba-b570-af0845c32ef9",
    "name_by_user": "vp all ticks",
    "highestIndex": "6"
}

# test volume profile
input_data_22 = {
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
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "cc5c1704-d553-4e14-b6e4-45a88aa58adc",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "==",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_CANDLE_TIME",
                                    "mode_time_shift": "0",
                                    "time_candle_id": "1",
                                    "time_market": "",
                                    "time_candle_timeframe": "PERIOD_CURRENT"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_TIMESTAMP",
                                    "mode_time_shift": "0",
                                    "time_stamp": "15:00"
                                }
                            }
                        },
                        "id": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "id_by_user": 3,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "11:00",
                            "timeTo_str": "15:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "redraw_each_time": "false"
                        },
                        "id": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "cc5c1704-d553-4e14-b6e4-45a88aa58adc",
                        "sourceHandle": "blue",
                        "target": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "68b2e058-764c-435b-99a4-9b36519fc277"
                    },
                    {
                        "source": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "sourceHandle": "blue",
                        "target": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "58ae1f13-8b87-4ad9-a4f6-8be38f0cf946"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "ac5cd6a0-e6a5-477e-9ea9-f0a8b14f6aef",
    "name_by_user": "vp once per day",
    "highestIndex": "5"
}

# test volume profile
input_data_23 = {
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
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "11:00",
                            "timeTo_str": "15:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "vp_max_1",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "redraw_each_time": "false"
                        },
                        "id": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    },
                    {
                        "params": {},
                        "id": "9c0c760a-c3c4-4f7b-80a7-4a7e68170a58",
                        "id_by_user": 5,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "9c0c760a-c3c4-4f7b-80a7-4a7e68170a58",
                        "sourceHandle": "blue",
                        "target": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "2160cf15-03a7-4697-9450-ef5f6860f595"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            },
            {
                "id": "a3c9b6d0-5f48-48ba-be4f-57556953c640",
                "type": "double",
                "name": "vp_max_1",
                "value": "0",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "ac5cd6a0-e6a5-477e-9ea9-f0a8b14f6aef",
    "name_by_user": "vp once per day",
    "highestIndex": "6"
}

# test volume profile
input_data_24 = {
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
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "cc5c1704-d553-4e14-b6e4-45a88aa58adc",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    },
                    {
                        "params": {
                            "operator": {
                                "label": "==",
                                "cross_width": 1
                            },
                            "left": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_CANDLE_TIME",
                                    "mode_time_shift": "0",
                                    "time_candle_id": "1",
                                    "time_market": "",
                                    "time_candle_timeframe": "PERIOD_CURRENT"
                                }
                            },
                            "right": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_TIMESTAMP",
                                    "mode_time_shift": "0",
                                    "time_stamp": "15:00"
                                }
                            }
                        },
                        "id": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "id_by_user": 3,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "redraw_each_time": "true"
                        },
                        "id": "8b9f9a50-e3be-4c3a-acf8-d9d0c170f6f9",
                        "id_by_user": 4,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "cc5c1704-d553-4e14-b6e4-45a88aa58adc",
                        "sourceHandle": "blue",
                        "target": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "68b2e058-764c-435b-99a4-9b36519fc277"
                    },
                    {
                        "source": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "sourceHandle": "blue",
                        "target": "3a17cc60-604d-4b21-9718-8813088cdd05",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "58ae1f13-8b87-4ad9-a4f6-8be38f0cf946"
                    },
                    {
                        "source": "8d7b9e75-f960-4abb-9fc8-5b5a0153f5a6",
                        "sourceHandle": "blue",
                        "target": "8b9f9a50-e3be-4c3a-acf8-d9d0c170f6f9",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "ff209866-2662-441c-955c-5825f911f07e"
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
                "id": "699f2042-9372-478f-ad03-26d904ac989d",
                "type": "string",
                "name": "time_from",
                "value": "2024.8.6 11:00",
                "description": ""
            },
            {
                "id": "369ad19f-7e07-4f58-97af-32280b443dde",
                "type": "string",
                "name": "time_to",
                "value": "2024.8.6 15:00",
                "description": ""
            },
            {
                "id": "a3c9b6d0-5f48-48ba-be4f-57556953c640",
                "type": "double",
                "name": "vp_max_1",
                "value": "0",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "ac5cd6a0-e6a5-477e-9ea9-f0a8b14f6aef",
    "name_by_user": "vp once per day",
    "highestIndex": "5"
}

# test volume profile
input_data_25 = {
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
                        "id": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "",
                            "min_part_1": "",
                            "mtp_part_1": "",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "redraw_each_time": "true"
                        },
                        "id": "71ad98fb-0de2-4a93-adc2-7a0b42df5832",
                        "id_by_user": 2,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "sourceHandle": "blue",
                        "target": "71ad98fb-0de2-4a93-adc2-7a0b42df5832",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "dc324cab-e22e-4d07-ab22-40ac36744842"
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
    "selected_name": "dc467dcf-acce-46bc-bcf8-afc370150ff0",
    "name_by_user": "test vp",
    "highestIndex": "3"
}

# test candle new items: time and tick volume
input_data_26 = {
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
                        "id": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
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
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_CLOSE",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "adjust": "",
                                    "shift": "0"
                                },
                                "row1": "candle"
                            },
                            "right": {
                                "row1": "candle",
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_CLOSE",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "adjust": "",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "97e2fb73-a0df-4981-be12-47c7a3a958c0",
                        "id_by_user": 3,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    }
                ],
                "edges": [
                    {
                        "source": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "sourceHandle": "blue",
                        "target": "97e2fb73-a0df-4981-be12-47c7a3a958c0",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "dc2e9b64-98ba-4416-a4ee-1c6f49fa09a2"
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
    "selected_name": "dc467dcf-acce-46bc-bcf8-afc370150ff0",
    "name_by_user": "test vp",
    "highestIndex": "4"
}

# test volume profile
input_data_27 = {
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
                        "id": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "max_1",
                            "min_part_1": "min_1",
                            "mtp_part_1": "mtp_1",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "redraw_each_time": "true"
                        },
                        "id": "a4136b48-f52d-4d19-9bcd-c313f1af8a13",
                        "id_by_user": 3,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
                    }
                ],
                "edges": [
                    {
                        "source": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "sourceHandle": "blue",
                        "target": "a4136b48-f52d-4d19-9bcd-c313f1af8a13",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "15e94bdd-d3d9-4cd7-a474-79b99b660169"
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
                "id": "7b90993b-bfee-43aa-9b15-8a739dc1d7e1",
                "type": "double",
                "name": "max_1",
                "value": "",
                "description": ""
            },
            {
                "id": "baf77aa2-de6a-4719-b763-281059682c5c",
                "type": "double",
                "name": "min_1",
                "value": "",
                "description": ""
            },
            {
                "id": "c9d0b52c-635e-46e2-b148-588e533da1c4",
                "type": "double",
                "name": "mtp_1",
                "value": "",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "dc467dcf-acce-46bc-bcf8-afc370150ff0",
    "name_by_user": "test vp",
    "highestIndex": "4"
}

# test volume profile
input_data_28 = {
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
                        "id": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "id_by_user": 1,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                            "RangeMinutes": "2440",
                            "ModeStep": "3",
                            "numberOfBars": "30",
                            "DataSource": "VP_SOURCE_M1",
                            "VolumeType": "VOLUME_TICK",
                            "HgBarStyle": "VP_BAR_STYLE_BAR",
                            "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                            "HgColor": "clrNavy",
                            "HgColor2": "clrSteelBlue",
                            "HgLineWidth": "2",
                            "ModeColor": "clrMediumBlue",
                            "MaxColor": "clrRed",
                            "MedianColor": "clrNONE",
                            "VwapColor": "clrNONE",
                            "ModeLineWidth": "2",
                            "StatLineStyle": "STYLE_SOLID",
                            "ModeLevelColor": "clrNONE",
                            "ModeLevelWidth": "1",
                            "ModeLevelStyle": "STYLE_SOLID",
                            "RegionDividerColor": "clrDarkBlue",
                            "Id_user": "+vpr",
                            "ShowHorizon": "true",
                            "TimeFromColor": "clrDarkGreen",
                            "TimeFromStyle": "STYLE_DASH",
                            "TimeToColor": "clrDarkGreen",
                            "TimeToStyle": "STYLE_DASH",
                            "HgWidthPercent": "15",
                            "timeFrom_str": "01:00",
                            "timeTo_str": "10:00",
                            "how_many_regions": "3",
                            "region_1_factor": "2",
                            "region_2_factor": "3",
                            "region_3_factor": "1",
                            "region_4_factor": "1",
                            "region_5_factor": "1",
                            "max_part_1": "max_1",
                            "min_part_1": "min_1",
                            "mtp_part_1": "mtp_1",
                            "max_part_2": "",
                            "min_part_2": "",
                            "mtp_part_2": "",
                            "max_part_3": "",
                            "min_part_3": "",
                            "mtp_part_3": "",
                            "max_part_4": "",
                            "min_part_4": "",
                            "mtp_part_4": "",
                            "max_part_5": "",
                            "min_part_5": "",
                            "mtp_part_5": "",
                            "redraw_each_time": "true"
                        },
                        "id": "a4136b48-f52d-4d19-9bcd-c313f1af8a13",
                        "id_by_user": 3,
                        "blockName": "Volume Profile",
                        "category": "various_signals",
                        "block_name_mql": "volume_profile"
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
                            "obj_font_color": "clrBlack",
                            "obj_font_size": "10",
                            "label_1": "test values: ",
                            "format_number_1": "EMPTY_VALUE",
                            "format_time_1": "EMPTY_VALUE",
                            "label_2": "test value: ",
                            "format_number_2": "EMPTY_VALUE",
                            "format_time_2": "EMPTY_VALUE",
                            "label_3": "test value: ",
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
                                "row2": "Numeric",
                                "params": {
                                    "value": "max_1",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_2": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "min_1",
                                    "adjust": ""
                                }
                            },
                            "value_fetch_3": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "mtp_1",
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
                        "id": "9c055aa3-ad13-4e4d-8f09-b9f33caf0de9",
                        "id_by_user": 4,
                        "blockName": "Comment",
                        "category": "output_communication",
                        "block_name_mql": "comment"
                    }
                ],
                "edges": [
                    {
                        "source": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "sourceHandle": "blue",
                        "target": "a4136b48-f52d-4d19-9bcd-c313f1af8a13",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "15e94bdd-d3d9-4cd7-a474-79b99b660169"
                    },
                    {
                        "source": "a4136b48-f52d-4d19-9bcd-c313f1af8a13",
                        "sourceHandle": "blue",
                        "target": "9c055aa3-ad13-4e4d-8f09-b9f33caf0de9",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "70203121-3f7f-412c-88f6-98bc7b7d3808"
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
                "id": "7b90993b-bfee-43aa-9b15-8a739dc1d7e1",
                "type": "double",
                "name": "max_1",
                "value": "",
                "description": ""
            },
            {
                "id": "baf77aa2-de6a-4719-b763-281059682c5c",
                "type": "double",
                "name": "min_1",
                "value": "",
                "description": ""
            },
            {
                "id": "c9d0b52c-635e-46e2-b148-588e533da1c4",
                "type": "double",
                "name": "mtp_1",
                "value": "",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "dc467dcf-acce-46bc-bcf8-afc370150ff0",
    "name_by_user": "test vp",
    "highestIndex": "5"
}

# test check type
input_data_29 = {
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
                        "id": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
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
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "value": "1",
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            },
                            "right": {
                                "row1": "indicator",
                                "row2": "ma",
                                "params": {
                                    "value": "1",
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
                        "id": "dc95e90a-b25f-49ab-b10e-6777fc5d2dba",
                        "id_by_user": 5,
                        "category": "condition_formula",
                        "block_name_mql": "condition",
                        "blockName": "Condition"
                    },
                    {
                        "params": {
                            "CheckBuyOrSell": "buy",
                            "CheckLimitOrStop": "both"
                        },
                        "id": "a36b05b7-ee7b-451d-8b4d-c8bac5bff988",
                        "id_by_user": 6,
                        "blockName": "check type",
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "check_type"
                    }
                ],
                "edges": [
                    {
                        "source": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "sourceHandle": "blue",
                        "target": "dc95e90a-b25f-49ab-b10e-6777fc5d2dba",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "66b71bb0-524e-4f28-a192-6b8a1a37ddc9"
                    },
                    {
                        "source": "25ceb8ad-a3fd-459e-b2b0-95256fc20484",
                        "sourceHandle": "blue",
                        "target": "a36b05b7-ee7b-451d-8b4d-c8bac5bff988",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "ecbe6178-8709-437c-bf91-6c7c1d78b781"
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
                "id": "7b90993b-bfee-43aa-9b15-8a739dc1d7e1",
                "type": "double",
                "name": "max_1",
                "value": "",
                "description": ""
            },
            {
                "id": "baf77aa2-de6a-4719-b763-281059682c5c",
                "type": "double",
                "name": "min_1",
                "value": "",
                "description": ""
            },
            {
                "id": "c9d0b52c-635e-46e2-b148-588e533da1c4",
                "type": "double",
                "name": "mtp_1",
                "value": "",
                "description": ""
            }
        ],
        "constants": []
    },
    "selected_name": "dc467dcf-acce-46bc-bcf8-afc370150ff0",
    "name_by_user": "test vp",
    "highestIndex": "7"
}

# test draw text
input_data_30 = {
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
                            "object_per_bar": "true",
                            "object_update": "true",
                            "obj_name": "my_arrow",
                            "object_type": "OBJ_ARROW_UP",
                            "obj_x": 10,
                            "obj_y": 10,
                            "obj_font": "Arial",
                            "obj_font_size": 10,
                            "obj_angle": 0,
                            "obj_corner": "CORNER_LEFT_UPPER",
                            "obj_anchor": "ANCHOR_TOP",
                            "obj_color": "clrDeepPink",
                            "obj_back": "false",
                            "obj_selectable": "true",
                            "obj_selected": "false",
                            "obj_hidden": "false",
                            "obj_z_order": 0,
                            "obj_chart_subwindow": "",
                            "price_1": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "Shift in Time": "0",
                                    "Time Mode": "MODE_TIME_NOW"
                                }
                            },
                            "time_1": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "Shift in Time": "0",
                                    "Time Mode": "MODE_TIME_NOW"
                                }
                            },
                            "text": {
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
                        "block_name_mql": "draw_text",
                        "blockName": "Draw Text"
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
