# This test file takes place in the period of 50 blocks phase

# If pending order
input_data_1 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "39dd378f-9963-48b9-a181-dded55308916",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
                    },
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "39dd378f-9963-48b9-a181-dded55308916",
                        "sourceHandle": "blue",
                        "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
                    }
                ],
                "nodes": [
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
                            "variable": "sss"
                        },
                        "id": "39dd378f-9963-48b9-a181-dded55308916",
                        "id_by_user": 2,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "id_by_user": 3,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
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
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMMA",
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
                                    "ma_method": "MODE_SMMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "id_by_user": 4,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{2,4}",
                            "type_pending": "{2,3}",
                            "symbols_str": ""
                        },
                        "id": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "id_by_user": 5,
                        "blockName": "If pending order",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "if_pending_order"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrDarkBlue",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "price_to_open_dynamic_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "67000",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "type": "double",
                "name": "sss",
                "value": "0",
                "description": ""
            }
        ]
    },
    "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# If trade/order
input_data_2 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "39dd378f-9963-48b9-a181-dded55308916",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
                    },
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "39dd378f-9963-48b9-a181-dded55308916",
                        "sourceHandle": "blue",
                        "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
                    }
                ],
                "nodes": [
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
                            "variable": "sss"
                        },
                        "id": "39dd378f-9963-48b9-a181-dded55308916",
                        "id_by_user": 2,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "id_by_user": 3,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
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
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMMA",
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
                                    "ma_method": "MODE_SMMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "id_by_user": 4,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0, 2, 4}",
                            "symbols_str": ""
                        },
                        "id": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "id_by_user": 5,
                        "blockName": "If trade/order",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "if_trade_order"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrDarkBlue",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "price_to_open_dynamic_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "67000",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "type": "double",
                "name": "sss",
                "value": "0",
                "description": ""
            }
        ]
    },
    "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No trade/order
input_data_3 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "39dd378f-9963-48b9-a181-dded55308916",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
                    },
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "39dd378f-9963-48b9-a181-dded55308916",
                        "sourceHandle": "blue",
                        "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
                    }
                ],
                "nodes": [
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
                            "variable": "sss"
                        },
                        "id": "39dd378f-9963-48b9-a181-dded55308916",
                        "id_by_user": 2,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "id_by_user": 3,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
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
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMMA",
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
                                    "ma_method": "MODE_SMMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "id_by_user": 4,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0, 2, 4}",
                            "symbols_str": ""
                        },
                        "id": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "id_by_user": 5,
                        "blockName": "No trade/order",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "no_trade_order"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrDarkBlue",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "price_to_open_dynamic_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "67000",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "type": "double",
                "name": "sss",
                "value": "0",
                "description": ""
            }
        ]
    },
    "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No trade
input_data_4 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "39dd378f-9963-48b9-a181-dded55308916",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
                    },
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "39dd378f-9963-48b9-a181-dded55308916",
                        "sourceHandle": "blue",
                        "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
                    }
                ],
                "nodes": [
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
                            "variable": "sss"
                        },
                        "id": "39dd378f-9963-48b9-a181-dded55308916",
                        "id_by_user": 2,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "id_by_user": 3,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
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
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMMA",
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
                                    "ma_method": "MODE_SMMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "id_by_user": 4,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0}",
                            "symbols_str": ""
                        },
                        "id": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "id_by_user": 5,
                        "blockName": "No trade",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "no_trade"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrDarkBlue",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "price_to_open_dynamic_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "67000",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "type": "double",
                "name": "sss",
                "value": "0",
                "description": ""
            }
        ]
    },
    "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No pending order
input_data_5 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "39dd378f-9963-48b9-a181-dded55308916",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
                    },
                    {
                        "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "sourceHandle": "blue",
                        "target": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
                    },
                    {
                        "source": "39dd378f-9963-48b9-a181-dded55308916",
                        "sourceHandle": "blue",
                        "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
                    }
                ],
                "nodes": [
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
                            "variable": "sss"
                        },
                        "id": "39dd378f-9963-48b9-a181-dded55308916",
                        "id_by_user": 2,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
                        "id_by_user": 3,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
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
                                    "ma_period": "5",
                                    "ma_shift": "0",
                                    "ma_method": "MODE_SMMA",
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
                                    "ma_method": "MODE_SMMA",
                                    "applied_price": "PRICE_CLOSE",
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "4be75049-a2ac-4603-b424-9896de7986ea",
                        "id_by_user": 4,
                        "blockName": "Condition",
                        "category": "condition_formula",
                        "block_name_mql": "condition"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{3, 5}",
                            "type_pending": "{2, 3, 4,5}",
                            "symbols_str": ""
                        },
                        "id": "df193530-239a-42aa-94e2-ae27014a4afe",
                        "id_by_user": 5,
                        "blockName": "No pending order",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "no_pending_order"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrDarkBlue",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "price_to_open_dynamic_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "67000",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "type": "double",
                "name": "sss",
                "value": "0",
                "description": ""
            }
        ]
    },
    "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No trade nearby
input_data_6 = {
    "data": {
        "events": {
            "on_tick": {
                "nodes": [
                    {
                        "params": {},
                        "id": "a114335f-8f24-4938-a439-1c4ad155162f",
                        "id_by_user": 1,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "type": "{0,1}",
                            "mode_base_price": "current",
                            "mode_range": "pips",
                            "range_position": "0",
                            "time_1": {
                                "row1": "market-properties",
                                "row2": "HIGHEST_PRICE_CANDLE_PERIOD",
                                "params": {
                                    "range_start": "0",
                                    "range_end": "10",
                                    "what_to_get": "GET_PRICE"
                                }
                            },
                            "time_2": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_NOW",
                                    "mode_time_shift": "0",
                                    "time_source": "TIME_SERVER"
                                }
                            },
                            "range_pips": "10"
                        },
                        "id": "48d377a4-a859-441f-917e-d92cc1d807f7",
                        "id_by_user": 2,
                        "blockName": "No trade nearby",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "no_trade_nearby"
                    }
                ],
                "edges": [
                    {
                        "source": "a114335f-8f24-4938-a439-1c4ad155162f",
                        "sourceHandle": "blue",
                        "target": "48d377a4-a859-441f-917e-d92cc1d807f7",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-a114335f-8f24-4938-a439-1c4ad155162fblue-48d377a4-a859-441f-917e-d92cc1d807f7c"
                    }
                ]
            },
            "on_trade": {
                "nodes": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "edges": []
            },
            "on_init": {
                "nodes": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    }
}

# No pending order nearby
input_data_7 = {
    "data": {
        "events": {
            "on_tick": {
                "nodes": [
                    {
                        "params": {},
                        "id": "a114335f-8f24-4938-a439-1c4ad155162f",
                        "id_by_user": 1,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "type": "{2,3,4,5}",
                            "type_pending": "{4,5}",
                            "mode_base_price": "current",
                            "mode_range": "pips",
                            "range_position": "0",
                            "time_1": {
                                "row1": "market-properties",
                                "row2": "HIGHEST_PRICE_CANDLE_PERIOD",
                                "params": {
                                    "range_start": "0",
                                    "range_end": "10",
                                    "what_to_get": "GET_PRICE"
                                }
                            },
                            "time_2": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_NOW",
                                    "mode_time_shift": "0",
                                    "time_source": "TIME_SERVER"
                                }
                            },
                            "range_pips": "10"
                        },
                        "id": "48d377a4-a859-441f-917e-d92cc1d807f7",
                        "id_by_user": 2,
                        "blockName": "No pending order nearby",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "no_pending_order_nearby"
                    }
                ],
                "edges": [
                    {
                        "source": "a114335f-8f24-4938-a439-1c4ad155162f",
                        "sourceHandle": "blue",
                        "target": "48d377a4-a859-441f-917e-d92cc1d807f7",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-a114335f-8f24-4938-a439-1c4ad155162fblue-48d377a4-a859-441f-917e-d92cc1d807f7c"
                    }
                ]
            },
            "on_trade": {
                "nodes": [],
                "edges": []
            },
            "on_chart": {
                "nodes": [],
                "edges": []
            },
            "on_timer": {
                "nodes": [],
                "edges": []
            },
            "on_init": {
                "nodes": [],
                "edges": []
            },
            "on_deinit": {
                "nodes": [],
                "edges": []
            }
        },
        "variables": [],
        "constants": []
    }
}

# No pending order nearby
input_data_8 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "2f6ac49f-7d00-47e0-b949-ea82d464e526",
                        "sourceHandle": "blue",
                        "target": "8d8c089c-ed13-4647-85f3-3d488d2ea7ef",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-2f6ac49f-7d00-47e0-b949-ea82d464e526blue-8d8c089c-ed13-4647-85f3-3d488d2ea7efc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "2f6ac49f-7d00-47e0-b949-ea82d464e526",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "type": "{3,5}",
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "type_pending": "{2,3}",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "mode_base_price": "current",
                            "mode_range": "pips",
                            "range_position": "0",
                            "time_1": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_NOW",
                                    "mode_time_shift": "0",
                                    "time_source": "TIME_SERVER"
                                }
                            },
                            "time_2": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_NOW",
                                    "mode_time_shift": "0",
                                    "time_source": "TIME_SERVER"
                                }
                            },
                            "range_pips": "10"
                        },
                        "id": "8d8c089c-ed13-4647-85f3-3d488d2ea7ef",
                        "id_by_user": 3,
                        "blockName": "No pending order nearby",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "no_pending_order_nearby"
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
    "selected_name": "8962631d-4ec0-4d2c-ac3e-e713bc2bb5b4",
    "name_by_user": "test",
    "highestIndex": "4"
}

# Check pending orders count
input_data_9 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "2f6ac49f-7d00-47e0-b949-ea82d464e526",
                        "sourceHandle": "blue",
                        "target": "c6d32537-139b-4d34-b48a-fbc81a13f9e8",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-2f6ac49f-7d00-47e0-b949-ea82d464e526blue-c6d32537-139b-4d34-b48a-fbc81a13f9e8c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "2f6ac49f-7d00-47e0-b949-ea82d464e526",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "operator": ">=",
                            "orders-count": "8",
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "type_pending": "{2,3}",
                            "group_number": "20",
                            "symbols_str": ""
                        },
                        "id": "c6d32537-139b-4d34-b48a-fbc81a13f9e8",
                        "id_by_user": 2,
                        "blockName": "Check pending orders count",
                        "category": "check_trades_orders_count",
                        "block_name_mql": "check_pending_orders_count"
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
    "selected_name": "8962631d-4ec0-4d2c-ac3e-e713bc2bb5b4",
    "name_by_user": "test",
    "highestIndex": "3"
}

# Trailing pending orders
input_data_10 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "04ad8b87-5f37-4dac-b55a-f9126fae3ad3",
                        "sourceHandle": "blue",
                        "target": "443b39d7-f095-4b19-b586-e1672c8fdd68",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-04ad8b87-5f37-4dac-b55a-f9126fae3ad3blue-443b39d7-f095-4b19-b586-e1672c8fdd68c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{2,3,4,5}",
                            "type_pending": "{2,3,4,5}",
                            "trailing_distance_mode": "TRAILING_DISTANCE_MODE_DYNAMIC",
                            "t_step_pips": "1",
                            "symbols_str": "",
                            "dynamic_size_pips_input": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 30,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "443b39d7-f095-4b19-b586-e1672c8fdd68",
                        "id_by_user": 1,
                        "blockName": "Trailing pending orders",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_pending_orders"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "04ad8b87-5f37-4dac-b55a-f9126fae3ad3",
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
    "selected_name": "cf9a5141-18ad-4015-80a4-2ba82df2712b",
    "name_by_user": "تست",
    "highestIndex": "3"
}

# Trailing pending orders 2
input_data_11 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "7ba964bc-825c-46b2-b846-07601cc50daf",
                        "sourceHandle": "blue",
                        "target": "e4c7bce6-2025-4bde-ae4a-a4328dce8a56",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-7ba964bc-825c-46b2-b846-07601cc50dafblue-e4c7bce6-2025-4bde-ae4a-a4328dce8a56c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{2,3,4,5}",
                            "type_pending": "{2,3,4,5}",
                            "trailing_distance_mode": "TRAILING_DISTANCE_MODE_DYNAMIC_DIGITS",
                            "t_step_pips": "1",
                            "symbols_str": "",
                            "dynamic_size_digits_input": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 0.003,
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "e4c7bce6-2025-4bde-ae4a-a4328dce8a56",
                        "id_by_user": 1,
                        "blockName": "Trailing pending orders",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_pending_orders"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "7ba964bc-825c-46b2-b846-07601cc50daf",
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
    "selected_name": "43916177-a4d5-404c-9f54-eec10c8096e8",
    "name_by_user": "test test",
    "highestIndex": "3"
}

# Sell now > Point calculations corrected
input_data_12 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "7ba964bc-825c-46b2-b846-07601cc50daf",
                        "sourceHandle": "blue",
                        "target": "f2438e05-3437-45ac-a95b-79d042ff09f9",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-7ba964bc-825c-46b2-b846-07601cc50dafblue-f2438e05-3437-45ac-a95b-79d042ff09f9c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "7ba964bc-825c-46b2-b846-07601cc50daf",
                        "id_by_user": 2,
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar",
                        "blockName": "Once per bar"
                    },
                    {
                        "params": {
                            "symbol": "EURUSD_o",
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
                        "id": "f2438e05-3437-45ac-a95b-79d042ff09f9",
                        "id_by_user": 2,
                        "blockName": "Sell now",
                        "category": "buy_sell",
                        "block_name_mql": "sell_now"
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
    "selected_name": "43916177-a4d5-404c-9f54-eec10c8096e8",
    "name_by_user": "test test",
    "highestIndex": "3"
}

# Buy now > Point / Entry price calculations corrected (Now msymbol is taken into account)
input_data_13 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "d63e4574-3252-4f73-b98d-2c517927d315",
                        "sourceHandle": "blue",
                        "target": "f0ce422a-2d60-4b03-8f51-322845c2c4fa",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-d63e4574-3252-4f73-b98d-2c517927d315blue-f0ce422a-2d60-4b03-8f51-322845c2c4fac"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "d63e4574-3252-4f73-b98d-2c517927d315",
                        "id_by_user": 2,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
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
                        "id": "f0ce422a-2d60-4b03-8f51-322845c2c4fa",
                        "id_by_user": 3,
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
    "selected_name": "7a20c904-ef43-4410-a1ea-e4a86661dfae",
    "name_by_user": "testx",
    "highestIndex": "4"
}

# trailing stop, break even
input_data_14 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "d63e4574-3252-4f73-b98d-2c517927d315",
                        "sourceHandle": "blue",
                        "target": "e79eedcf-645b-4820-b508-1869420899a8",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-d63e4574-3252-4f73-b98d-2c517927d315blue-e79eedcf-645b-4820-b508-1869420899a8c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT",
                            "max_times_to_pass": "1"
                        },
                        "id": "d63e4574-3252-4f73-b98d-2c517927d315",
                        "id_by_user": 2,
                        "blockName": "Once per bar",
                        "category": "time_filters",
                        "block_name_mql": "once_per_bar"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_MANUAL",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
                            "bep_offset_mode": "BEP_OFFSET_MODE_NONE",
                            "symbols_str": "GBPUSD",
                            "pips_on_profit": "18"
                        },
                        "id": "e79eedcf-645b-4820-b508-1869420899a8",
                        "id_by_user": 4,
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
        "variables": [],
        "constants": []
    },
    "selected_name": "7a20c904-ef43-4410-a1ea-e4a86661dfae",
    "name_by_user": "testx",
    "highestIndex": "undefined"
}

# for each: break
input_data_15 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4ee1b4ac-a9e6-472a-ad3b-f4cafd5f57ec",
                        "sourceHandle": "blue",
                        "target": "f20e181b-093f-4268-a9eb-19c009259a0c",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4ee1b4ac-a9e6-472a-ad3b-f4cafd5f57ecblue-f20e181b-093f-4268-a9eb-19c009259a0cc"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "loop_direction": "LOOP_DIRECTION_NEWEST_TO_OLDEST",
                            "skip_n": "1",
                            "every_n": "3",
                            "not_more_than_n": "5",
                            "symbols_str": ""
                        },
                        "id": "4ee1b4ac-a9e6-472a-ad3b-f4cafd5f57ec",
                        "id_by_user": 1,
                        "blockName": "For each Trade",
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "for_each_trade"
                    },
                    {
                        "params": {},
                        "id": "f20e181b-093f-4268-a9eb-19c009259a0c",
                        "id_by_user": 2,
                        "blockName": "(loop) break",
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "loop_break"
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
    "selected_name": "7a20c904-ef43-4410-a1ea-e4a86661dfae",
    "name_by_user": "testx",
    "highestIndex": "3"
}

# for each: break 2
input_data_16 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4ee1b4ac-a9e6-472a-ad3b-f4cafd5f57ec",
                        "sourceHandle": "blue",
                        "target": "f20e181b-093f-4268-a9eb-19c009259a0c",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4ee1b4ac-a9e6-472a-ad3b-f4cafd5f57ecblue-f20e181b-093f-4268-a9eb-19c009259a0cc"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "79",
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "type": "{1}",
                            "loop_direction": "LOOP_DIRECTION_NEWEST_TO_OLDEST",
                            "skip_n": "11",
                            "every_n": "30",
                            "not_more_than_n": "50"
                        },
                        "id": "4ee1b4ac-a9e6-472a-ad3b-f4cafd5f57ec",
                        "id_by_user": 1,
                        "blockName": "For each Trade",
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "for_each_trade"
                    },
                    {
                        "params": {},
                        "id": "f20e181b-093f-4268-a9eb-19c009259a0c",
                        "id_by_user": 2,
                        "blockName": "(loop) break",
                        "category": "loop_for_trades_orders",
                        "block_name_mql": "loop_break"
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
    "selected_name": "7a20c904-ef43-4410-a1ea-e4a86661dfae",
    "name_by_user": "testx",
    "highestIndex": "undefined"
}

# break even point each trade
input_data_17 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "eb3fc70d-f701-4026-81bc-3946f7c0e2e0",
                        "sourceHandle": "blue",
                        "target": "50dbfd11-b368-4bad-96cf-2e072fce7c6b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-eb3fc70d-f701-4026-81bc-3946f7c0e2e0blue-50dbfd11-b368-4bad-96cf-2e072fce7c6bc"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0,1}",
                            "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
                            "bep_offset_mode": "BEP_OFFSET_MODE_NONE",
                            "symbols_str": "",
                            "pips_on_profit": "15"
                        },
                        "id": "50dbfd11-b368-4bad-96cf-2e072fce7c6b",
                        "id_by_user": 4,
                        "blockName": "Break even point (each trade)",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "break_even_point_each_trade"
                    },
                    {
                        "params": {
                            "max_times_to_pass": "1",
                            "symbol": "",
                            "timeframe": "PERIOD_CURRENT"
                        },
                        "id": "eb3fc70d-f701-4026-81bc-3946f7c0e2e0",
                        "id_by_user": 5,
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
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "6"
}

# break even point each trade test 2
input_data_18 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "696149b3-38fd-4e88-833e-265b7fff6cc0",
                        "sourceHandle": "blue",
                        "target": "bce8acbd-f816-4708-b43b-3268cf3c2415",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-696149b3-38fd-4e88-833e-265b7fff6cc0blue-bce8acbd-f816-4708-b43b-3268cf3c2415c"
                    }
                ],
                "nodes": [
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
                        "id": "696149b3-38fd-4e88-833e-265b7fff6cc0",
                        "id_by_user": 1,
                        "category": "buy_sell",
                        "block_name_mql": "buy_now",
                        "blockName": "Buy now"
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
                            "pips_on_profit": "15"
                        },
                        "id": "bce8acbd-f816-4708-b43b-3268cf3c2415",
                        "id_by_user": 2,
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
        "variables": [],
        "constants": []
    },
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "3"
}

# toggle blocks
input_data_19 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "cd1344fe-ed17-4104-bce0-063bfee6499c",
                        "sourceHandle": "blue",
                        "target": "5117a00c-ca82-4948-8bba-0b8e38c55f82",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-cd1344fe-ed17-4104-bce0-063bfee6499cblue-5117a00c-ca82-4948-8bba-0b8e38c55f82c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "block_ids": "2,4,5"
                        },
                        "id": "5117a00c-ca82-4948-8bba-0b8e38c55f82",
                        "id_by_user": 1,
                        "blockName": "Toggle blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "toggle_blocks"
                    },
                    {
                        "params": {},
                        "id": "cd1344fe-ed17-4104-bce0-063bfee6499c",
                        "id_by_user": 2,
                        "blockName": "OR",
                        "category": "controlling_blocks",
                        "block_name_mql": "or"
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
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "3"
}

# turn on blocks
input_data_20 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "cd1344fe-ed17-4104-bce0-063bfee6499c",
                        "sourceHandle": "blue",
                        "target": "02e69014-4d86-4431-9b95-d735ed2cbbac",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-cd1344fe-ed17-4104-bce0-063bfee6499cblue-02e69014-4d86-4431-9b95-d735ed2cbbacc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "cd1344fe-ed17-4104-bce0-063bfee6499c",
                        "id_by_user": 2,
                        "blockName": "OR",
                        "category": "controlling_blocks",
                        "block_name_mql": "or"
                    },
                    {
                        "params": {
                            "block_ids": ""
                        },
                        "id": "02e69014-4d86-4431-9b95-d735ed2cbbac",
                        "id_by_user": 3,
                        "blockName": "Turn ON blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "turn_on_blocks"
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
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "4"
}

# turn off blocks
input_data_21 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "cd1344fe-ed17-4104-bce0-063bfee6499c",
                        "sourceHandle": "blue",
                        "target": "ff3a44f4-d32d-4c81-bef4-faddd685897b",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-cd1344fe-ed17-4104-bce0-063bfee6499cblue-ff3a44f4-d32d-4c81-bef4-faddd685897bc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "cd1344fe-ed17-4104-bce0-063bfee6499c",
                        "id_by_user": 2,
                        "blockName": "OR",
                        "category": "controlling_blocks",
                        "block_name_mql": "or"
                    },
                    {
                        "params": {
                            "block_ids": "8,9,10"
                        },
                        "id": "ff3a44f4-d32d-4c81-bef4-faddd685897b",
                        "id_by_user": 3,
                        "blockName": "Turn OFF blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "turn_off_blocks"
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
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "4"
}

# for each object: delete
input_data_22 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "1eb42bb5-a649-4196-958b-5eab7e92e551",
                        "sourceHandle": "blue",
                        "target": "28825f45-ef43-45a0-8203-ad0d5bc03391",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-1eb42bb5-a649-4196-958b-5eab7e92e551blue-28825f45-ef43-45a0-8203-ad0d5bc03391c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "obj_chart_id": "0",
                            "obj_subwindow": "-1",
                            "obj_type": "-1",
                            "is_arrow_type": "-1",
                            "obj_color": "clrNONE",
                            "obj_name_prefix": "",
                            "obj_name_contains": "",
                            "loop_direction": "z-a",
                            "loop_skip": "0",
                            "loop_limit": "0",
                            "arrow_code": "0"
                        },
                        "id": "1eb42bb5-a649-4196-958b-5eab7e92e551",
                        "id_by_user": 3,
                        "blockName": "For each Object",
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "for_each_object"
                    },
                    {
                        "params": {},
                        "id": "28825f45-ef43-45a0-8203-ad0d5bc03391",
                        "id_by_user": 4,
                        "blockName": "Delete",
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "delete"
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
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "5"
}

# for each object: delete 2
input_data_23 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "1eb42bb5-a649-4196-958b-5eab7e92e551",
                        "sourceHandle": "blue",
                        "target": "28825f45-ef43-45a0-8203-ad0d5bc03391",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-1eb42bb5-a649-4196-958b-5eab7e92e551blue-28825f45-ef43-45a0-8203-ad0d5bc03391c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "obj_chart_id": "5",
                            "obj_subwindow": "-5",
                            "obj_type": "OBJ_ARROW_THUMB_UP",
                            "is_arrow_type": "OBJ_ARROW_CHECK",
                            "obj_color": "clrNavy",
                            "obj_name_prefix": "test name",
                            "obj_name_contains": "hello test",
                            "loop_direction": "a-z",
                            "loop_skip": "5",
                            "loop_limit": "20"
                        },
                        "id": "1eb42bb5-a649-4196-958b-5eab7e92e551",
                        "id_by_user": 3,
                        "blockName": "For each Object",
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "for_each_object"
                    },
                    {
                        "params": {},
                        "id": "28825f45-ef43-45a0-8203-ad0d5bc03391",
                        "id_by_user": 4,
                        "blockName": "Delete",
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "delete"
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
    "selected_name": "8d5ca693-c96b-4b62-9a06-eebc4912d4f1",
    "name_by_user": "test",
    "highestIndex": "5"
}

# toggle blocks, turn on, turn off
input_data_24 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ce96074-bf89-421d-be50-b9b1c5b8ba1d",
                        "sourceHandle": "blue",
                        "target": "f415c096-0c3f-40e2-9440-be38108f7473",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ce96074-bf89-421d-be50-b9b1c5b8ba1dblue-f415c096-0c3f-40e2-9440-be38108f7473c"
                    },
                    {
                        "source": "9ce96074-bf89-421d-be50-b9b1c5b8ba1d",
                        "sourceHandle": "blue",
                        "target": "223ce020-f8e6-4dfb-b851-5e57106aada8",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ce96074-bf89-421d-be50-b9b1c5b8ba1dblue-223ce020-f8e6-4dfb-b851-5e57106aada8c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "block_ids": ""
                        },
                        "id": "223ce020-f8e6-4dfb-b851-5e57106aada8",
                        "id_by_user": 1,
                        "blockName": "Turn ON blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "turn_on_blocks"
                    },
                    {
                        "params": {
                            "block_ids": ""
                        },
                        "id": "f415c096-0c3f-40e2-9440-be38108f7473",
                        "id_by_user": 3,
                        "blockName": "Toggle blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "toggle_blocks"
                    },
                    {
                        "params": {
                            "block_ids": ""
                        },
                        "id": "9ce96074-bf89-421d-be50-b9b1c5b8ba1d",
                        "id_by_user": 2,
                        "blockName": "Turn OFF blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "turn_off_blocks"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "4"
}

# draw button
input_data_25 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "83d60adf-a4f5-4d62-9d7d-1d2229d22fb0",
                        "sourceHandle": "blue",
                        "target": "3f10c72a-5c9f-4e9c-b817-ad31a94ab57e",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-83d60adf-a4f5-4d62-9d7d-1d2229d22fb0blue-3f10c72a-5c9f-4e9c-b817-ad31a94ab57ec"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "obj_name": "hello test"
                        },
                        "id": "83d60adf-a4f5-4d62-9d7d-1d2229d22fb0",
                        "id_by_user": 1,
                        "blockName": "Select Object by Name",
                        "category": "loop_for_chart_objects",
                        "block_name_mql": "select_object_by_name"
                    },
                    {
                        "params": {
                            "object_per_bar": "false",
                            "object_update": "true",
                            "obj_name": "my_arrow",
                            "obj_x": "10",
                            "obj_y": "10",
                            "obj_font": "Arial",
                            "obj_font_size": "10",
                            "obj_x_size": "100",
                            "obj_y_size": "20",
                            "obj_bg_color": "clrWhite",
                            "obj_border_color": "clrNONE",
                            "obj_corner": "CORNER_LEFT_UPPER",
                            "obj_state": "false",
                            "obj_color": "clrDeepPink",
                            "obj_back": "false",
                            "obj_selectable": "true",
                            "obj_hidden": "true",
                            "obj_z_order": "0",
                            "obj_chart_subwindow": "",
                            "text": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "3f10c72a-5c9f-4e9c-b817-ad31a94ab57e",
                        "id_by_user": 1,
                        "blockName": "Draw Button",
                        "category": "chart_objects",
                        "block_name_mql": "draw_button"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "2"
}

# set current timeframe
input_data_26 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "sourceHandle": "blue",
                        "target": "1fc49f31-fcbd-42eb-8436-79a0b1c4a64f",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ec6e737-da40-4399-85ad-b9c35c4cf6f7blue-1fc49f31-fcbd-42eb-8436-79a0b1c4a64fc"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "timeframe_1": "PERIOD_M30",
                            "timeframe_2": "-1",
                            "timeframe_3": "-1",
                            "timeframe_4": "PERIOD_H12",
                            "timeframe_5": "-1",
                            "timeframe_6": "PERIOD_M4",
                            "timeframe_7": "-1",
                            "timeframe_8": "-1",
                            "timeframe_9": "PERIOD_D1",
                            "timeframe_10": "-1"
                        },
                        "id": "1fc49f31-fcbd-42eb-8436-79a0b1c4a64f",
                        "id_by_user": 5,
                        "blockName": "Set \"Current Timeframe\" for next blocks",
                        "category": "controlling_blocks",
                        "block_name_mql": "set_current_timeframe_for_next_blocks"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "6"
}

# draw button
input_data_27 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "sourceHandle": "blue",
                        "target": "1f07599f-2752-46e6-8d03-4b3c5284b087",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ec6e737-da40-4399-85ad-b9c35c4cf6f7blue-1f07599f-2752-46e6-8d03-4b3c5284b087c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_per_bar": "false",
                            "object_update": "true",
                            "obj_name": "my_arrow",
                            "obj_x": "10",
                            "obj_y": "10",
                            "obj_font": "Arial",
                            "obj_font_size": "10",
                            "obj_x_size": "100",
                            "obj_y_size": "20",
                            "obj_bg_color": "clrWhite",
                            "obj_border_color": "clrNONE",
                            "obj_corner": "CORNER_LEFT_UPPER",
                            "obj_state": "false",
                            "obj_color": "clrDeepPink",
                            "obj_back": "false",
                            "obj_selectable": "true",
                            "obj_hidden": "true",
                            "obj_z_order": "0",
                            "obj_chart_subwindow": "",
                            "text": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "1f07599f-2752-46e6-8d03-4b3c5284b087",
                        "id_by_user": 2,
                        "blockName": "Draw Button",
                        "category": "chart_objects",
                        "block_name_mql": "draw_button"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "3"
}

# draw button 2
input_data_28 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "sourceHandle": "blue",
                        "target": "1f07599f-2752-46e6-8d03-4b3c5284b087",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ec6e737-da40-4399-85ad-b9c35c4cf6f7blue-1f07599f-2752-46e6-8d03-4b3c5284b087c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_per_bar": "false",
                            "object_update": "true",
                            "obj_name": "my_button",
                            "obj_x": "11",
                            "obj_y": "12",
                            "obj_font": "Verdana",
                            "obj_font_size": "1010",
                            "obj_x_size": "101",
                            "obj_y_size": "203",
                            "obj_bg_color": "clrWhite",
                            "obj_border_color": "clrNONE",
                            "obj_corner": "CORNER_RIGHT_UPPER",
                            "obj_state": "false",
                            "obj_color": "clrDeepPink",
                            "obj_back": "false",
                            "obj_selectable": "true",
                            "obj_hidden": "true",
                            "obj_z_order": "0",
                            "obj_chart_subwindow": "",
                            "text": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "yasss",
                                    "adjust": "+\" No\""
                                }
                            }
                        },
                        "id": "1f07599f-2752-46e6-8d03-4b3c5284b087",
                        "id_by_user": 2,
                        "blockName": "Draw Button",
                        "category": "chart_objects",
                        "block_name_mql": "draw_button"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "3"
}

# draw button 3
input_data_29 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "sourceHandle": "blue",
                        "target": "96076931-913e-4682-90e9-2a16a01d9909",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ec6e737-da40-4399-85ad-b9c35c4cf6f7blue-96076931-913e-4682-90e9-2a16a01d9909c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_per_bar": "true",
                            "object_update": "false",
                            "obj_name": "my_btn",
                            "obj_x": "100",
                            "obj_y": "1010",
                            "obj_font": "Verdana",
                            "obj_font_size": "11",
                            "obj_x_size": "12",
                            "obj_y_size": "13",
                            "obj_bg_color": "clrWhite",
                            "obj_border_color": "clrNONE",
                            "obj_corner": "CORNER_RIGHT_LOWER",
                            "obj_state": "true",
                            "obj_color": "clrLime",
                            "obj_back": "true",
                            "obj_selectable": "false",
                            "obj_hidden": "false",
                            "obj_z_order": "1",
                            "obj_chart_subwindow": "x_window",
                            "text": {
                                "row1": "indicator",
                                "row2": "osma",
                                "params": {
                                    "fast_ema_period": "120",
                                    "slow_ema_period": "260",
                                    "signal_period": "90",
                                    "applied_price": "PRICE_HIGH",
                                    "adjust": "",
                                    "symbol": "XAUUSD",
                                    "timeframe": "PERIOD_M6",
                                    "shift": "50"
                                }
                            }
                        },
                        "id": "96076931-913e-4682-90e9-2a16a01d9909",
                        "id_by_user": 1,
                        "blockName": "Draw Button",
                        "category": "chart_objects",
                        "block_name_mql": "draw_button"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "2"
}

# draw editfield
input_data_30 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "sourceHandle": "blue",
                        "target": "b0bd8a56-b0a7-4ca9-b9a2-79994613db83",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ec6e737-da40-4399-85ad-b9c35c4cf6f7blue-b0bd8a56-b0a7-4ca9-b9a2-79994613db83c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_per_bar": "true",
                            "object_update": "false",
                            "obj_x": "100",
                            "obj_y": "1000",
                            "obj_font": "Tahoma",
                            "obj_font_size": "14",
                            "obj_align": "ALIGN_LEFT",
                            "obj_x_size": "80",
                            "obj_y_size": "90",
                            "obj_bg_color": "clrWhite",
                            "obj_border_color": "clrNONE",
                            "obj_corner": "CORNER_RIGHT_LOWER",
                            "obj_read_only": "true",
                            "obj_color": "clrSpringGreen",
                            "obj_back": "true",
                            "obj_selectable": "false",
                            "obj_hidden": "true",
                            "obj_z_order": "15",
                            "obj_chart_subwindow": "YASSSS",
                            "text": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "sample text",
                                    "adjust": "+ \"MyText\""
                                }
                            }
                        },
                        "id": "b0bd8a56-b0a7-4ca9-b9a2-79994613db83",
                        "id_by_user": 2,
                        "blockName": "Draw Edit Field",
                        "category": "chart_objects",
                        "block_name_mql": "draw_edit_field"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "3"
}

# draw editfield 2
input_data_31 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "sourceHandle": "blue",
                        "target": "353a7fd9-ea26-441a-8cd0-fb332daf2e92",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-9ec6e737-da40-4399-85ad-b9c35c4cf6f7blue-353a7fd9-ea26-441a-8cd0-fb332daf2e92c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "9ec6e737-da40-4399-85ad-b9c35c4cf6f7",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_per_bar": "true",
                            "object_update": "true",
                            "obj_name": "hello friend",
                            "obj_x": "100",
                            "obj_y": "120",
                            "obj_font": "Arial",
                            "obj_font_size": "101",
                            "obj_align": "ALIGN_LEFT",
                            "obj_x_size": "500",
                            "obj_y_size": "180",
                            "obj_bg_color": "clrTeal",
                            "obj_border_color": "clrSienna",
                            "obj_corner": "CORNER_RIGHT_LOWER",
                            "obj_read_only": "true",
                            "obj_color": "clrSpringGreen",
                            "obj_back": "true",
                            "obj_selectable": "false",
                            "obj_hidden": "false",
                            "obj_z_order": "56",
                            "obj_chart_subwindow": "85",
                            "text": {
                                "row1": "value",
                                "row2": "Text",
                                "params": {
                                    "value": "my text",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "353a7fd9-ea26-441a-8cd0-fb332daf2e92",
                        "id_by_user": 1,
                        "blockName": "Draw Edit Field",
                        "category": "chart_objects",
                        "block_name_mql": "draw_edit_field"
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
    "selected_name": "1dbc3b9d-98e5-4253-b9b8-ff061520f0b6",
    "name_by_user": "بسیبسی",
    "highestIndex": "2"
}

# on chart events
input_data_32 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "59e94ea2-a43d-45d0-b359-a437c6d6ae8f",
                        "sourceHandle": "blue",
                        "target": "f1f6ec30-6cb0-4054-8fc8-10301cb2df42",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-59e94ea2-a43d-45d0-b359-a437c6d6ae8fblue-f1f6ec30-6cb0-4054-8fc8-10301cb2df42c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "59e94ea2-a43d-45d0-b359-a437c6d6ae8f",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "object_per_bar": "false",
                            "object_update": "true",
                            "obj_name": "my_arrow",
                            "object_type": "OBJ_ARROW_UP",
                            "obj_anchor": "ANCHOR_TOP",
                            "obj_color": "clrDeepPink",
                            "obj_style": "STYLE_SOLID",
                            "obj_width": "1",
                            "obj_back": "false",
                            "obj_selectable": "false",
                            "obj_selected": "false",
                            "obj_hidden": "false",
                            "obj_z_order": "0",
                            "obj_chart_subwindow": "",
                            "time_1": {
                                "row1": "value",
                                "row2": "Time",
                                "params": {
                                    "mode_time": "MODE_TIME_NOW",
                                    "mode_time_shift": "0",
                                    "time_source": "TIME_SERVER"
                                }
                            },
                            "price_1": {
                                "row1": "candle",
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_OPEN",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "adjust": "",
                                    "shift": "0"
                                }
                            }
                        },
                        "id": "f1f6ec30-6cb0-4054-8fc8-10301cb2df42",
                        "id_by_user": 3,
                        "blockName": "Draw Arrow",
                        "category": "chart_objects",
                        "block_name_mql": "draw_arrow"
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
                "nodes": [
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "id_by_user": 1,
                        "blockName": "Edit Field modified",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "edit_field_modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "36468608-738f-401f-8ccb-c3ec28d470a7",
                        "id_by_user": 2,
                        "blockName": "Mouse clicked on object",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "mouse_clicked_on_object"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "5cd3b010-a30d-40f5-85fa-e403f1f05688",
                        "id_by_user": 3,
                        "blockName": "Object modified",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "c664da6e-193d-431d-b6b3-68d8ce673f73",
                        "id_by_user": 4,
                        "blockName": "Object dragged",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_dragged"
                    }
                ],
                "edges": [
                    {
                        "source": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "sourceHandle": "blue",
                        "target": "5cd3b010-a30d-40f5-85fa-e403f1f05688",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f354a367-a9ca-4dd4-a358-db15b576a704blue-5cd3b010-a30d-40f5-85fa-e403f1f05688c"
                    },
                    {
                        "source": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "sourceHandle": "red",
                        "target": "36468608-738f-401f-8ccb-c3ec28d470a7",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f354a367-a9ca-4dd4-a358-db15b576a704red-36468608-738f-401f-8ccb-c3ec28d470a7c"
                    },
                    {
                        "source": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "sourceHandle": "red",
                        "target": "c664da6e-193d-431d-b6b3-68d8ce673f73",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f354a367-a9ca-4dd4-a358-db15b576a704red-c664da6e-193d-431d-b6b3-68d8ce673f73c"
                    }
                ]
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
    "selected_name": "30789b7a-81e6-4e7c-9060-8767e04c25c0",
    "name_by_user": "test 14",
    "highestIndex": "5"
}

# on chart events 2
input_data_33 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "id_by_user": 1,
                        "blockName": "Edit Field modified",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "edit_field_modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "36468608-738f-401f-8ccb-c3ec28d470a7",
                        "id_by_user": 2,
                        "blockName": "Mouse clicked on object",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "mouse_clicked_on_object"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "5cd3b010-a30d-40f5-85fa-e403f1f05688",
                        "id_by_user": 3,
                        "blockName": "Object modified",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "c664da6e-193d-431d-b6b3-68d8ce673f73",
                        "id_by_user": 4,
                        "blockName": "Object dragged",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_dragged"
                    }
                ],
                "edges": [
                    {
                        "source": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "sourceHandle": "blue",
                        "target": "5cd3b010-a30d-40f5-85fa-e403f1f05688",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f354a367-a9ca-4dd4-a358-db15b576a704blue-5cd3b010-a30d-40f5-85fa-e403f1f05688c"
                    },
                    {
                        "source": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "sourceHandle": "red",
                        "target": "36468608-738f-401f-8ccb-c3ec28d470a7",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f354a367-a9ca-4dd4-a358-db15b576a704red-36468608-738f-401f-8ccb-c3ec28d470a7c"
                    },
                    {
                        "source": "f354a367-a9ca-4dd4-a358-db15b576a704",
                        "sourceHandle": "red",
                        "target": "c664da6e-193d-431d-b6b3-68d8ce673f73",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-f354a367-a9ca-4dd4-a358-db15b576a704red-c664da6e-193d-431d-b6b3-68d8ce673f73c"
                    }
                ]
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
    "selected_name": "30789b7a-81e6-4e7c-9060-8767e04c25c0",
    "name_by_user": "test 14",
    "highestIndex": "undefined"
}

# on chart events 3
input_data_34 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "45f05286-3146-4234-aea1-71e4919fb686",
                        "id_by_user": 1,
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "edit_field_modified",
                        "blockName": "Edit Field modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "3622b3a9-8a73-4223-bf5e-b53ea9dba51e",
                        "id_by_user": 2,
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "mouse_clicked_on_object",
                        "blockName": "Mouse clicked on object"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "1d01ccf4-ad1d-4271-92eb-d97fb0d57df6",
                        "id_by_user": 3,
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_modified",
                        "blockName": "Object modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": ""
                        },
                        "id": "926eeb0e-5dbf-4eac-9ea2-e67a1138f994",
                        "id_by_user": 4,
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_dragged",
                        "blockName": "Object dragged"
                    }
                ],
                "edges": [
                    {
                        "source": "45f05286-3146-4234-aea1-71e4919fb686",
                        "sourceHandle": "blue",
                        "target": "3622b3a9-8a73-4223-bf5e-b53ea9dba51e",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-45f05286-3146-4234-aea1-71e4919fb686blue-3622b3a9-8a73-4223-bf5e-b53ea9dba51ec"
                    },
                    {
                        "source": "45f05286-3146-4234-aea1-71e4919fb686",
                        "sourceHandle": "blue",
                        "target": "1d01ccf4-ad1d-4271-92eb-d97fb0d57df6",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-45f05286-3146-4234-aea1-71e4919fb686blue-1d01ccf4-ad1d-4271-92eb-d97fb0d57df6c"
                    },
                    {
                        "source": "1d01ccf4-ad1d-4271-92eb-d97fb0d57df6",
                        "sourceHandle": "blue",
                        "target": "926eeb0e-5dbf-4eac-9ea2-e67a1138f994",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-1d01ccf4-ad1d-4271-92eb-d97fb0d57df6blue-926eeb0e-5dbf-4eac-9ea2-e67a1138f994c"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "5"
}

# on chart events 4
input_data_35 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {
                            "name_filter_mode": "names",
                            "obj_name": "TEST"
                        },
                        "id": "45f05286-3146-4234-aea1-71e4919fb686",
                        "id_by_user": 1,
                        "blockName": "Edit Field modified",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "edit_field_modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": "names",
                            "obj_name": "TEST"
                        },
                        "id": "3622b3a9-8a73-4223-bf5e-b53ea9dba51e",
                        "id_by_user": 2,
                        "blockName": "Mouse clicked on object",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "mouse_clicked_on_object"
                    },
                    {
                        "params": {
                            "name_filter_mode": "names",
                            "obj_name": "TEST"
                        },
                        "id": "1d01ccf4-ad1d-4271-92eb-d97fb0d57df6",
                        "id_by_user": 3,
                        "blockName": "Object modified",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_modified"
                    },
                    {
                        "params": {
                            "name_filter_mode": "names",
                            "obj_name": ""
                        },
                        "id": "926eeb0e-5dbf-4eac-9ea2-e67a1138f994",
                        "id_by_user": 4,
                        "blockName": "Object dragged",
                        "category": "on_chart_filter_specific_event",
                        "block_name_mql": "object_dragged"
                    }
                ],
                "edges": [
                    {
                        "source": "45f05286-3146-4234-aea1-71e4919fb686",
                        "sourceHandle": "blue",
                        "target": "3622b3a9-8a73-4223-bf5e-b53ea9dba51e",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-45f05286-3146-4234-aea1-71e4919fb686blue-3622b3a9-8a73-4223-bf5e-b53ea9dba51ec"
                    },
                    {
                        "source": "45f05286-3146-4234-aea1-71e4919fb686",
                        "sourceHandle": "blue",
                        "target": "1d01ccf4-ad1d-4271-92eb-d97fb0d57df6",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-45f05286-3146-4234-aea1-71e4919fb686blue-1d01ccf4-ad1d-4271-92eb-d97fb0d57df6c"
                    },
                    {
                        "source": "1d01ccf4-ad1d-4271-92eb-d97fb0d57df6",
                        "sourceHandle": "blue",
                        "target": "926eeb0e-5dbf-4eac-9ea2-e67a1138f994",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-1d01ccf4-ad1d-4271-92eb-d97fb0d57df6blue-926eeb0e-5dbf-4eac-9ea2-e67a1138f994c"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "5"
}

# delete objects
input_data_36 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {
                            "name_starts_with": "",
                            "name_contains": "",
                            "obj_color": "EMPTY_VALUE",
                            "sort_mode": "z_a",
                            "max_objects": "",
                            "skip_objects": ""
                        },
                        "id": "266f4ce6-5217-4ed3-9e7f-697af8102388",
                        "id_by_user": 1,
                        "blockName": "Delete objects",
                        "category": "chart_objects",
                        "block_name_mql": "delete_objects"
                    },
                    {
                        "params": {},
                        "id": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "sourceHandle": "blue",
                        "target": "266f4ce6-5217-4ed3-9e7f-697af8102388",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b230473f-b1d7-4925-b909-11b0eb992feeblue-266f4ce6-5217-4ed3-9e7f-697af8102388c"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "3"
}

# modify stops of trades
input_data_37 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {},
                        "id": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "group_mode": "ORDER_GROUP_MODE_MANUAL",
                            "type": "{1}",
                            "older_than": "10",
                            "relative_to": "PRICE_RELATIVE_TO_CURRENT_PRICE",
                            "new_tpsl_mode": "NEW_STOPS_CUSTOM_PRICE_LEVEL",
                            "level_color": "clrGray",
                            "new_stop_loss_level": {
                                "row1": "indicator",
                                "row2": "accelerator_oscillator",
                                "params": {
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            },
                            "new_take_profit_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "1aa23a60-1bc4-407f-a7db-7ce90d4170fb",
                        "id_by_user": 3,
                        "blockName": "Modify stops of trades",
                        "category": "trading_actions",
                        "block_name_mql": "modify_stops_of_trades"
                    }
                ],
                "edges": [
                    {
                        "source": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "sourceHandle": "blue",
                        "target": "1aa23a60-1bc4-407f-a7db-7ce90d4170fb",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b230473f-b1d7-4925-b909-11b0eb992feeblue-1aa23a60-1bc4-407f-a7db-7ce90d4170fbc"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "4"
}

# modify stops of trades 2
input_data_38 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {},
                        "id": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "symbols_str": "",
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "type": "{0,1}",
                            "order_age_mins": "0",
                            "relative_to": "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL",
                            "new_tpsl_mode": "NEW_STOPS_CUSTOM_PRICE_LEVEL",
                            "level_color": "clrDeepPink",
                            "group_number": "11",
                            "value_fetch_relative_to": {
                                "row1": "candle",
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_OPEN",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "adjust": "",
                                    "shift": "0"
                                }
                            },
                            "new_stop_loss_level": {
                                "row1": "indicator",
                                "row2": "accelerator_oscillator",
                                "params": {
                                    "adjust": "",
                                    "symbol": "",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "0"
                                }
                            },
                            "new_take_profit_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1",
                                    "adjust": ""
                                }
                            }
                        },
                        "id": "ec3c43b0-96bf-435a-9b63-032823f86725",
                        "id_by_user": 1,
                        "blockName": "Modify stops of trades",
                        "category": "trading_actions",
                        "block_name_mql": "modify_stops_of_trades"
                    }
                ],
                "edges": [
                    {
                        "source": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "sourceHandle": "blue",
                        "target": "ec3c43b0-96bf-435a-9b63-032823f86725",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b230473f-b1d7-4925-b909-11b0eb992feeblue-ec3c43b0-96bf-435a-9b63-032823f86725c"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "2"
}

# modify stops of trades 3
input_data_39 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {},
                        "id": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "type": "{0}",
                            "order_age_mins": "20",
                            "relative_to": "PRICE_RELATIVE_TO_OPEN_PRICE",
                            "new_tpsl_mode": "NEW_STOPS_PERCENT_OF_CURRENT_TPSL",
                            "level_color": "clrDeepSkyBlue",
                            "group_number": "14",
                            "new_stoploss_percent": "65",
                            "new_takeprofit_percent": "35"
                        },
                        "id": "ec3c43b0-96bf-435a-9b63-032823f86725",
                        "id_by_user": 1,
                        "blockName": "Modify stops of trades",
                        "category": "trading_actions",
                        "block_name_mql": "modify_stops_of_trades"
                    }
                ],
                "edges": [
                    {
                        "source": "b230473f-b1d7-4925-b909-11b0eb992fee",
                        "sourceHandle": "blue",
                        "target": "ec3c43b0-96bf-435a-9b63-032823f86725",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b230473f-b1d7-4925-b909-11b0eb992feeblue-ec3c43b0-96bf-435a-9b63-032823f86725c"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "2"
}

# time fitler
input_data_40 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [],
                "nodesData": [],
                "nodes": []
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
                "nodes": [
                    {
                        "params": {
                            "time_mode": "TIME_SERVER",
                            "time_start_mode": "TIME_MODE_TEXT",
                            "time_end_mode": "TIME_MODE_TEXT",
                            "time_start": "00:00",
                            "time_end": "00:01"
                        },
                        "id": "5475376e-7034-4de5-978b-c51de5f71258",
                        "id_by_user": 2,
                        "blockName": "Time filter",
                        "category": "time_filters",
                        "block_name_mql": "time_filter"
                    },
                    {
                        "params": {},
                        "id": "94a372bb-248d-4b4a-bcad-5c63b218cce8",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    }
                ],
                "edges": [
                    {
                        "source": "94a372bb-248d-4b4a-bcad-5c63b218cce8",
                        "sourceHandle": "blue",
                        "target": "5475376e-7034-4de5-978b-c51de5f71258",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-94a372bb-248d-4b4a-bcad-5c63b218cce8blue-5475376e-7034-4de5-978b-c51de5f71258c"
                    }
                ]
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
    "selected_name": "e45e4fb4-0015-498b-b67f-f99dc87dbef9",
    "name_by_user": "test 89",
    "highestIndex": "4"
}

# trailing pending order after adding OnTrade()
input_data_41 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "23035cd7-ffdd-44a7-9f78-7628378d8788",
                        "sourceHandle": "blue",
                        "target": "35ab0e10-f176-4e2b-8d36-8bd1d799a740",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-23035cd7-ffdd-44a7-9f78-7628378d8788blue-35ab0e10-f176-4e2b-8d36-8bd1d799a740c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "23035cd7-ffdd-44a7-9f78-7628378d8788",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{2,3,4,5}",
                            "type_pending": "{2,3,4,5}",
                            "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
                            "t_step_pips": "1",
                            "symbols_str": "",
                            "t_distance_pips": "30"
                        },
                        "id": "35ab0e10-f176-4e2b-8d36-8bd1d799a740",
                        "id_by_user": 3,
                        "blockName": "Trailing pending orders",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_pending_orders"
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
    "selected_name": "a518d20f-7aac-4f96-aa09-6d1bb4cd0228",
    "name_by_user": "test 8978",
    "highestIndex": "4"
}

# test trade created event
input_data_42 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "38236fc3-8b1b-419d-8fa9-5001d086669b",
                        "sourceHandle": "blue",
                        "target": "611211a0-5faa-4fdc-846d-6e79b8db94b5",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-38236fc3-8b1b-419d-8fa9-5001d086669bblue-611211a0-5faa-4fdc-846d-6e79b8db94b5c"
                    }
                ],
                "nodes": [
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
                        "id": "611211a0-5faa-4fdc-846d-6e79b8db94b5",
                        "id_by_user": 2,
                        "blockName": "Buy now",
                        "category": "buy_sell",
                        "block_name_mql": "buy_now"
                    },
                    {
                        "params": {},
                        "id": "38236fc3-8b1b-419d-8fa9-5001d086669b",
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
                "nodes": [
                    {
                        "params": {},
                        "id": "dd672263-821d-4278-b74a-4ec7f715cea9",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "type": "{0,1}"
                        },
                        "id": "e24a978a-2af6-4b07-be48-1fec27181ab5",
                        "id_by_user": 5,
                        "blockName": "Trade created",
                        "category": "on_trade_filter_specific_event",
                        "block_name_mql": "trade_created"
                    }
                ],
                "edges": [
                    {
                        "source": "dd672263-821d-4278-b74a-4ec7f715cea9",
                        "sourceHandle": "blue",
                        "target": "e24a978a-2af6-4b07-be48-1fec27181ab5",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-dd672263-821d-4278-b74a-4ec7f715cea9blue-e24a978a-2af6-4b07-be48-1fec27181ab5c"
                    }
                ]
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
    "selected_name": "a518d20f-7aac-4f96-aa09-6d1bb4cd0228",
    "name_by_user": "test 8978",
    "highestIndex": "6"
}

# test pending order created event
input_data_43 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "38236fc3-8b1b-419d-8fa9-5001d086669b",
                        "sourceHandle": "blue",
                        "target": "61d8eb72-276c-4251-9639-145a46ed570a",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-38236fc3-8b1b-419d-8fa9-5001d086669bblue-61d8eb72-276c-4251-9639-145a46ed570ac"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "38236fc3-8b1b-419d-8fa9-5001d086669b",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
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
                            "stoploss": "20",
                            "takeprofit": "20"
                        },
                        "id": "61d8eb72-276c-4251-9639-145a46ed570a",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "nodes": [
                    {
                        "params": {},
                        "id": "dd672263-821d-4278-b74a-4ec7f715cea9",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "type": "{2,3,4,5}",
                            "type_pending": "{2,3,4,5}"
                        },
                        "id": "5bf9f13c-5780-425b-8c5d-e5b582e21e38",
                        "id_by_user": 5,
                        "blockName": "Order created",
                        "category": "on_trade_filter_specific_event",
                        "block_name_mql": "order_created"
                    }
                ],
                "edges": [
                    {
                        "source": "dd672263-821d-4278-b74a-4ec7f715cea9",
                        "sourceHandle": "blue",
                        "target": "5bf9f13c-5780-425b-8c5d-e5b582e21e38",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-dd672263-821d-4278-b74a-4ec7f715cea9blue-5bf9f13c-5780-425b-8c5d-e5b582e21e38c"
                    }
                ]
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
    "selected_name": "a518d20f-7aac-4f96-aa09-6d1bb4cd0228",
    "name_by_user": "test 8978",
    "highestIndex": "7"
}

# test pending order deleted event
input_data_44 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "38236fc3-8b1b-419d-8fa9-5001d086669b",
                        "sourceHandle": "blue",
                        "target": "61d8eb72-276c-4251-9639-145a46ed570a",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-38236fc3-8b1b-419d-8fa9-5001d086669bblue-61d8eb72-276c-4251-9639-145a46ed570ac"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "38236fc3-8b1b-419d-8fa9-5001d086669b",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
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
                            "stoploss": "20",
                            "takeprofit": "20"
                        },
                        "id": "61d8eb72-276c-4251-9639-145a46ed570a",
                        "id_by_user": 6,
                        "blockName": "Buy pending order",
                        "category": "buy_sell",
                        "block_name_mql": "buy_pending_order"
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
                "nodes": [
                    {
                        "params": {},
                        "id": "dd672263-821d-4278-b74a-4ec7f715cea9",
                        "id_by_user": 4,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_ALL",
                            "symbol_mode": "SYMBOL_MODE_ANY",
                            "type": "{2,3,4,5}",
                            "type_pending": "{2,3,4,5}",
                            "close_mode": ""
                        },
                        "id": "0daa4df5-7b52-47a1-9304-5be4ec2a9d2a",
                        "id_by_user": 7,
                        "blockName": "Order deleted",
                        "category": "on_trade_filter_specific_event",
                        "block_name_mql": "order_deleted"
                    }
                ],
                "edges": [
                    {
                        "source": "dd672263-821d-4278-b74a-4ec7f715cea9",
                        "sourceHandle": "blue",
                        "target": "0daa4df5-7b52-47a1-9304-5be4ec2a9d2a",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-dd672263-821d-4278-b74a-4ec7f715cea9blue-0daa4df5-7b52-47a1-9304-5be4ec2a9d2ac"
                    }
                ]
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
    "selected_name": "a518d20f-7aac-4f96-aa09-6d1bb4cd0228",
    "name_by_user": "test 8978",
    "highestIndex": "8"
}

# test: block title (as comment) removed
input_data_45 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "38236fc3-8b1b-419d-8fa9-5001d086669b",
            "sourceHandle": "blue",
            "target": "61d8eb72-276c-4251-9639-145a46ed570a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-38236fc3-8b1b-419d-8fa9-5001d086669bblue-61d8eb72-276c-4251-9639-145a46ed570ac"
          },
          {
            "source": "38236fc3-8b1b-419d-8fa9-5001d086669b",
            "sourceHandle": "blue",
            "target": "9ef5fb46-975e-4bda-8e90-31ab446b6b10",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-38236fc3-8b1b-419d-8fa9-5001d086669bblue-9ef5fb46-975e-4bda-8e90-31ab446b6b10c"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "38236fc3-8b1b-419d-8fa9-5001d086669b",
            "id_by_user": 3,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
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
              "stoploss": "20",
              "takeprofit": "20"
            },
            "id": "61d8eb72-276c-4251-9639-145a46ed570a",
            "id_by_user": 6,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_ALL",
              "symbol_mode": "SYMBOL_MODE_ANY",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "arrow_color": "clrOlive"
            },
            "id": "9ef5fb46-975e-4bda-8e90-31ab446b6b10",
            "id_by_user": 1,
            "blockName": "Delete Pending Orders",
            "category": "trading_actions",
            "block_name_mql": "delete_pending_orders"
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
        "nodes": [
          {
            "params": {},
            "id": "dd672263-821d-4278-b74a-4ec7f715cea9",
            "id_by_user": 4,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_ALL",
              "symbol_mode": "SYMBOL_MODE_ANY",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "close_mode": ""
            },
            "id": "0daa4df5-7b52-47a1-9304-5be4ec2a9d2a",
            "id_by_user": 7,
            "blockName": "Order deleted",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_deleted"
          }
        ],
        "edges": [
          {
            "source": "dd672263-821d-4278-b74a-4ec7f715cea9",
            "sourceHandle": "blue",
            "target": "0daa4df5-7b52-47a1-9304-5be4ec2a9d2a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-dd672263-821d-4278-b74a-4ec7f715cea9blue-0daa4df5-7b52-47a1-9304-5be4ec2a9d2ac"
          }
        ]
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
  "selected_name": "a518d20f-7aac-4f96-aa09-6d1bb4cd0228",
  "name_by_user": "test 8978",
  "highestIndex": "2"
}
