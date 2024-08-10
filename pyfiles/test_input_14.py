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
              "timeFrom_date": "D'2024.07.12 11:30:27'",
              "timeTo_date": "D'2024.07.12 19:30:27'",
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
