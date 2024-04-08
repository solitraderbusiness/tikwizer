input_data_1 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row2": "macd",
                            "row1": "Indicator",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        },
                        "right": {
                            "row2": "macd",
                            "row1": "Indicator",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        }
                    },
                    "id": "9c678a92-9e3d-42dd-b611-12c0e9169f53",
                    "id_by_user": 1,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "left": {
                            "row2": "macd",
                            "row1": "Indicator",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        },
                        "right": {
                            "row2": "Candle",
                            "row1": "Candle",
                            "params": {
                                "price_mode": "CANDLE_OPEN",
                                "find_method": "FIND_BY_ID",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "shift": "10"
                            }
                        },
                        "operator": {
                            "label": "+"
                        },
                        "ajdust": "",
                        "variable": ""
                    },
                    "id": "e4d5aaf1-9cfa-4104-969f-677f882f24f5",
                    "id_by_user": 2,
                    "blockName": "formula"
                },
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_M1"
                    },
                    "id": "ff32924f-edea-48e6-aa4a-cb5c8776a007",
                    "id_by_user": 3,
                    "blockName": "Once per bar"
                },
                {
                    "id": "28e470e3-db9d-472c-9aca-f038db161498",
                    "id_by_user": 4,
                    "blockName": "If trade",
                    "params": {}
                }
            ],
            "edges": [
                {
                    "source": "9c678a92-9e3d-42dd-b611-12c0e9169f53",
                    "sourceHandle": "blue",
                    "target": "e4d5aaf1-9cfa-4104-969f-677f882f24f5",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-9c678a92-9e3d-42dd-b611-12c0e9169f53blue-e4d5aaf1-9cfa-4104-969f-677f882f24f5c"
                },
                {
                    "source": "ff32924f-edea-48e6-aa4a-cb5c8776a007",
                    "sourceHandle": "blue",
                    "target": "9c678a92-9e3d-42dd-b611-12c0e9169f53",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-ff32924f-edea-48e6-aa4a-cb5c8776a007blue-9c678a92-9e3d-42dd-b611-12c0e9169f53c"
                },
                {
                    "source": "ff32924f-edea-48e6-aa4a-cb5c8776a007",
                    "sourceHandle": "blue",
                    "target": "28e470e3-db9d-472c-9aca-f038db161498",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-ff32924f-edea-48e6-aa4a-cb5c8776a007blue-28e470e3-db9d-472c-9aca-f038db161498c"
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

input_data_2 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        }
                    },
                    "id": "36d1ea60-a992-4d51-9929-b3bd50c92668",
                    "id_by_user": 1,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_NUMBER",
                        "group_number": "11",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0,1}",
                        "symbols_str": ""
                    },
                    "id": "d24a7f1e-adca-4937-b7af-d1f2772999e5",
                    "id_by_user": 2,
                    "blockName": "If trade"
                },
                {
                    "id": "e240807c-df38-4e54-92cc-de81ffe9157f",
                    "id_by_user": 4,
                    "blockName": "OR",
                    "params": {}
                },
                {
                    "params": {
                        "group": "0",
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "ExpMode": "None",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "volume_upper_limit": "0",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "1",
                        "martingale_reset_on_n_profits": "1",
                        "look_up_on": "LOOK_UP_HISTORY_ONLY",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0",
                        "stoploss": "50",
                        "takeprofit": "50"
                    },
                    "id": "55408bb6-8215-4e4f-b310-4ecd3282f7e8",
                    "id_by_user": 5,
                    "blockName": "Buy now"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_NUMBER",
                        "group_number": "11",
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "type": "{0}",
                        "older_than": "",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "symbols_str": "GBPUSD"
                    },
                    "id": "306e3448-73cb-4b79-b030-6120cbebe995",
                    "id_by_user": 6,
                    "blockName": "Close trades"
                }
            ],
            "edges": [
                {
                    "source": "d24a7f1e-adca-4937-b7af-d1f2772999e5",
                    "sourceHandle": "blue",
                    "target": "36d1ea60-a992-4d51-9929-b3bd50c92668",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-d24a7f1e-adca-4937-b7af-d1f2772999e5blue-36d1ea60-a992-4d51-9929-b3bd50c92668c"
                },
                {
                    "source": "36d1ea60-a992-4d51-9929-b3bd50c92668",
                    "sourceHandle": "blue",
                    "target": "e240807c-df38-4e54-92cc-de81ffe9157f",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-36d1ea60-a992-4d51-9929-b3bd50c92668blue-e240807c-df38-4e54-92cc-de81ffe9157fc"
                },
                {
                    "source": "e240807c-df38-4e54-92cc-de81ffe9157f",
                    "sourceHandle": "blue",
                    "target": "55408bb6-8215-4e4f-b310-4ecd3282f7e8",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-e240807c-df38-4e54-92cc-de81ffe9157fblue-55408bb6-8215-4e4f-b310-4ecd3282f7e8c"
                },
                {
                    "source": "d24a7f1e-adca-4937-b7af-d1f2772999e5",
                    "sourceHandle": "blue",
                    "target": "306e3448-73cb-4b79-b030-6120cbebe995",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-d24a7f1e-adca-4937-b7af-d1f2772999e5blue-306e3448-73cb-4b79-b030-6120cbebe995c"
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

# rsi crosses above 70 > sell
input_data_3 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "0"
                    },
                    "id": "1ee4dda0-a797-4380-9089-8c1fa11eeefe",
                    "id_by_user": 3,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "operator": {
                            "label": "×<",
                            "cross_width": "1"
                        },
                        "left": {
                            "row2": "rsi",
                            "row1": "Indicator",
                            "params": {
                                "period": 14,
                                "applied_price": "PRICE_CLOSE",
                                "shift": "1",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "30"
                            }
                        }
                    },
                    "id": "70f53285-c41c-48e9-a4c5-ab3caa3d2cad",
                    "id_by_user": 4,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "group": "11",
                        "symbol": "NULL",
                        "price_offset": "20",
                        "open_at_price": "OPEN_AT_BID",
                        "volume_upper_limit": "10",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "ExpMode": "None",
                        "oco": "oco2",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "how_much_volume": "100",
                        "martingale_multiply_on_profit": "1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "1",
                        "martingale_reset_on_n_profits": "1",
                        "stoploss": "20",
                        "takeprofit": "20",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0"
                    },
                    "id": "16815e46-7fe3-40c1-aae4-965cbba897dc",
                    "id_by_user": 5,
                    "blockName": "Sell now"
                }
            ],
            "edges": [
                {
                    "source": "1ee4dda0-a797-4380-9089-8c1fa11eeefe",
                    "sourceHandle": "blue",
                    "target": "70f53285-c41c-48e9-a4c5-ab3caa3d2cad",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-1ee4dda0-a797-4380-9089-8c1fa11eeefeblue-70f53285-c41c-48e9-a4c5-ab3caa3d2cadc"
                },
                {
                    "source": "70f53285-c41c-48e9-a4c5-ab3caa3d2cad",
                    "sourceHandle": "blue",
                    "target": "16815e46-7fe3-40c1-aae4-965cbba897dc",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-70f53285-c41c-48e9-a4c5-ab3caa3d2cadblue-16815e46-7fe3-40c1-aae4-965cbba897dcc"
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

# if no trade nearby then comment hello, else comment goodbye
input_data_4 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "title": "hello",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "cf188edb-3d32-40ce-9c4d-52033ca2161e",
                    "id_by_user": 8,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "title": "good bye",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "a1594cf2-7183-4a78-b331-61403b0de909",
                    "id_by_user": 9,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "mode_base_price": "current",
                        "mode_range": "pips",
                        "range_position": "0",
                        "group_mode": "ORDER_GROUP_MODE_NUMBER",
                        "group_number": "11",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "symbols_str": "",
                        "type": "{0}",
                        "range_pips": "10",
                        "range_fraction": "0.0010",
                        "time_1": {
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_NOW",
                                "mode_time_shift": "-1",
                                "time_source": "TIME_SERVER"
                            },
                            "row1": "Value"
                        },
                        "time_2": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_NOW",
                                "mode_time_shift": "-1",
                                "time_source": "TIME_SERVER"
                            }
                        }
                    },
                    "id": "6559c286-1291-4ba0-a584-f45acf8a38d9",
                    "id_by_user": 10,
                    "blockName": "No trade nearby"
                }
            ],
            "edges": [
                {
                    "source": "6559c286-1291-4ba0-a584-f45acf8a38d9",
                    "sourceHandle": "blue",
                    "target": "cf188edb-3d32-40ce-9c4d-52033ca2161e",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-6559c286-1291-4ba0-a584-f45acf8a38d9blue-cf188edb-3d32-40ce-9c4d-52033ca2161ec"
                },
                {
                    "source": "6559c286-1291-4ba0-a584-f45acf8a38d9",
                    "sourceHandle": "blue",
                    "target": "a1594cf2-7183-4a78-b331-61403b0de909",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-6559c286-1291-4ba0-a584-f45acf8a38d9blue-a1594cf2-7183-4a78-b331-61403b0de909c"
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

# if trade
input_data_5 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "title": "hello",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "cf188edb-3d32-40ce-9c4d-52033ca2161e",
                    "id_by_user": 8,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "title": "good bye",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "a1594cf2-7183-4a78-b331-61403b0de909",
                    "id_by_user": 9,
                    "blockName": "Comment"
                },
                {
                    "id": "527d19b3-fdd1-46da-94d9-d43cbcc773b5",
                    "id_by_user": 10,
                    "blockName": "If trade",
                    "params": {}
                }
            ],
            "edges": [
                {
                    "source": "527d19b3-fdd1-46da-94d9-d43cbcc773b5",
                    "sourceHandle": "blue",
                    "target": "cf188edb-3d32-40ce-9c4d-52033ca2161e",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-527d19b3-fdd1-46da-94d9-d43cbcc773b5blue-cf188edb-3d32-40ce-9c4d-52033ca2161ec"
                },
                {
                    "source": "527d19b3-fdd1-46da-94d9-d43cbcc773b5",
                    "sourceHandle": "blue",
                    "target": "a1594cf2-7183-4a78-b331-61403b0de909",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-527d19b3-fdd1-46da-94d9-d43cbcc773b5blue-a1594cf2-7183-4a78-b331-61403b0de909c"
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

# comment variable value, the modify variable then comment it again
input_data_6 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "title": "x",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "cf188edb-3d32-40ce-9c4d-52033ca2161e",
                    "id_by_user": 8,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "x",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "9999"
                                }
                            }
                        },
                        "variable2": {
                            "variable_name": ""
                        },
                        "variable3": {
                            "variable_name": ""
                        },
                        "variable4": {
                            "variable_name": ""
                        },
                        "variable5": {
                            "variable_name": ""
                        }
                    },
                    "id": "9bd217d2-e7ea-4e44-8c47-9e8e616886af",
                    "id_by_user": 9,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "title": "x",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_RIGHT_UPPER",
                        "obj_x": "200",
                        "obj_y": "200",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "cf6abe47-fc14-4139-a6e8-01ce176b1bca",
                    "id_by_user": 10,
                    "blockName": "Comment"
                }
            ],
            "edges": [
                {
                    "source": "cf188edb-3d32-40ce-9c4d-52033ca2161e",
                    "sourceHandle": "blue",
                    "target": "9bd217d2-e7ea-4e44-8c47-9e8e616886af",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-cf188edb-3d32-40ce-9c4d-52033ca2161eblue-9bd217d2-e7ea-4e44-8c47-9e8e616886afc"
                },
                {
                    "source": "9bd217d2-e7ea-4e44-8c47-9e8e616886af",
                    "sourceHandle": "blue",
                    "target": "cf6abe47-fc14-4139-a6e8-01ce176b1bca",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-9bd217d2-e7ea-4e44-8c47-9e8e616886afblue-cf6abe47-fc14-4139-a6e8-01ce176b1bcac"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        }
    ],
    "constants": []
}

# pass n times > modify variable
input_data_7 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "n": "5"
                    },
                    "id": "f2c8dd94-a16c-44c4-b5f6-6731050fc0a7",
                    "id_by_user": 9,
                    "blockName": "Loop(pass \"n\" times)"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "x",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "1"
                                }
                            }
                        },
                        "variable2": {
                            "variable_name": ""
                        },
                        "variable3": {
                            "variable_name": ""
                        },
                        "variable4": {
                            "variable_name": ""
                        },
                        "variable5": {
                            "variable_name": ""
                        }
                    },
                    "variable1": {},
                    "variable2": {},
                    "variable3": {},
                    "variable4": {},
                    "variable5": {},
                    "id": "948310dd-dda8-47ac-986c-58f4b0f99883",
                    "id_by_user": 10,
                    "blockName": "Modify Variables"
                }
            ],
            "edges": [
                {
                    "source": "f2c8dd94-a16c-44c4-b5f6-6731050fc0a7",
                    "sourceHandle": "blue",
                    "target": "948310dd-dda8-47ac-986c-58f4b0f99883",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-f2c8dd94-a16c-44c4-b5f6-6731050fc0a7blue-948310dd-dda8-47ac-986c-58f4b0f99883c"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        }
    ],
    "constants": []
}

# compound test
input_data_8 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "left": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "1"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "10"
                            }
                        },
                        "operator": {
                            "label": "+"
                        },
                        "ajdust": "10",
                        "variable": "x"
                    },
                    "id": "a82bc962-b41a-4edb-a7e6-e590ab1994c1",
                    "id_by_user": 6,
                    "blockName": "formula"
                },
                {
                    "params": {
                        "title": "Comment Message",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
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
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
                        "obj_font_size": "10",
                        "value_fetch_1": {
                            "row1": "Value",
                            "row2": "Text",
                            "params": {
                                "value": "x"
                            }
                        }
                    },
                    "id": "8f3549e5-e2ae-4dc0-81c8-2a42659af757",
                    "id_by_user": 7,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0,1}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "pips",
                        "compare": "!=",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "0"
                    },
                    "id": "d319cf72-3960-45e8-be92-b1a2e363f66b",
                    "id_by_user": 8,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "params": {
                        "title": "Comment Message",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                            "row2": "Text",
                            "params": {
                                "value": "there is profit"
                            },
                            "row1": "Value"
                        }
                    },
                    "id": "9efdd450-d4c3-4fdb-b9ae-f721224ce4c4",
                    "id_by_user": 9,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "title": "Comment Message",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                            "row2": "Text",
                            "params": {
                                "value": "no profit"
                            },
                            "row1": "Value"
                        }
                    },
                    "id": "c6995e16-d9c6-48c5-8b94-eaa0bb3fe46d",
                    "id_by_user": 10,
                    "blockName": "Comment"
                }
            ],
            "edges": [
                {
                    "source": "a82bc962-b41a-4edb-a7e6-e590ab1994c1",
                    "sourceHandle": "blue",
                    "target": "8f3549e5-e2ae-4dc0-81c8-2a42659af757",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a82bc962-b41a-4edb-a7e6-e590ab1994c1blue-8f3549e5-e2ae-4dc0-81c8-2a42659af757c"
                },
                {
                    "source": "d319cf72-3960-45e8-be92-b1a2e363f66b",
                    "sourceHandle": "blue",
                    "target": "9efdd450-d4c3-4fdb-b9ae-f721224ce4c4",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-d319cf72-3960-45e8-be92-b1a2e363f66bblue-9efdd450-d4c3-4fdb-b9ae-f721224ce4c4c"
                },
                {
                    "source": "d319cf72-3960-45e8-be92-b1a2e363f66b",
                    "sourceHandle": "red",
                    "target": "c6995e16-d9c6-48c5-8b94-eaa0bb3fe46d",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-d319cf72-3960-45e8-be92-b1a2e363f66bred-c6995e16-d9c6-48c5-8b94-eaa0bb3fe46dc"
                },
                {
                    "source": "a82bc962-b41a-4edb-a7e6-e590ab1994c1",
                    "sourceHandle": "blue",
                    "target": "d319cf72-3960-45e8-be92-b1a2e363f66b",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a82bc962-b41a-4edb-a7e6-e590ab1994c1blue-d319cf72-3960-45e8-be92-b1a2e363f66bc"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        }
    ],
    "constants": []
}

# test AND block
input_data_9 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "afe5e738-995e-4a4f-8f80-1e200277414d",
                    "id_by_user": 10,
                    "blockName": "AND",
                    "params": {}
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "rsi",
                            "params": {
                                "applied_price": "PRICE_CLOSE",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "period": 14
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "70"
                            }
                        }
                    },
                    "id": "c0333815-8b34-4763-8ea5-21473a4cecc3",
                    "id_by_user": 11,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "operator": {
                            "label": "<",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "rsi",
                            "row1": "Indicator",
                            "params": {
                                "applied_price": "PRICE_LOW",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "period": 14
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "30"
                            }
                        }
                    },
                    "id": "5067aeaf-e68d-45ef-86dc-a0bbc93981aa",
                    "id_by_user": 12,
                    "blockName": "condition"
                },
                {
                    "id": "aed1cf6f-af3c-466a-93fa-26efeb202336",
                    "id_by_user": 13,
                    "blockName": "Comment",
                    "params": {}
                }
            ],
            "edges": [
                {
                    "source": "c0333815-8b34-4763-8ea5-21473a4cecc3",
                    "sourceHandle": "blue",
                    "target": "afe5e738-995e-4a4f-8f80-1e200277414d",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-c0333815-8b34-4763-8ea5-21473a4cecc3blue-afe5e738-995e-4a4f-8f80-1e200277414dc"
                },
                {
                    "source": "5067aeaf-e68d-45ef-86dc-a0bbc93981aa",
                    "sourceHandle": "blue",
                    "target": "afe5e738-995e-4a4f-8f80-1e200277414d",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5067aeaf-e68d-45ef-86dc-a0bbc93981aablue-afe5e738-995e-4a4f-8f80-1e200277414dc"
                },
                {
                    "source": "afe5e738-995e-4a4f-8f80-1e200277414d",
                    "sourceHandle": "blue",
                    "target": "aed1cf6f-af3c-466a-93fa-26efeb202336",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-afe5e738-995e-4a4f-8f80-1e200277414dblue-aed1cf6f-af3c-466a-93fa-26efeb202336c"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        }
    ],
    "constants": []
}

# test if rsi > 70 then close trades
input_data_10 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0,1}",
                        "older_than": "0",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "symbols_str": ""
                    },
                    "id": "0e9455ce-b9c1-4b45-8ff7-3be3687ba25b",
                    "id_by_user": 13,
                    "blockName": "Close trades"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row2": "rsi",
                            "row1": "Indicator",
                            "params": {
                                "period": 14,
                                "applied_price": "PRICE_LOW",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "70"
                            }
                        }
                    },
                    "id": "1da8edfc-91fe-47a3-bc17-e44dd58f2533",
                    "id_by_user": 14,
                    "blockName": "condition"
                }
            ],
            "edges": [
                {
                    "source": "1da8edfc-91fe-47a3-bc17-e44dd58f2533",
                    "sourceHandle": "blue",
                    "target": "0e9455ce-b9c1-4b45-8ff7-3be3687ba25b",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-1da8edfc-91fe-47a3-bc17-e44dd58f2533blue-0e9455ce-b9c1-4b45-8ff7-3be3687ba25bc"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        }
    ],
    "constants": []
}

# test value double quotation fix
input_data_11 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "operator": {
                            "label": "×<",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "rsi",
                            "row1": "Indicator",
                            "params": {
                                "period": "yyy",
                                "applied_price": "PRICE_LOW",
                                "shift": "1",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "xxx"
                            }
                        }
                    },
                    "id": "a0f00e21-19e3-442f-bb92-f8c4078ba7e6",
                    "id_by_user": 1,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_NUMBER",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "group_number": "11",
                        "symbols_str": ""
                    },
                    "id": "a1f0a547-9c62-4b93-9bb3-156dcb5ded18",
                    "id_by_user": 2,
                    "blockName": "If trade"
                }
            ],
            "edges": [
                {
                    "source": "a0f00e21-19e3-442f-bb92-f8c4078ba7e6",
                    "sourceHandle": "blue",
                    "target": "a1f0a547-9c62-4b93-9bb3-156dcb5ded18",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a0f00e21-19e3-442f-bb92-f8c4078ba7e6blue-a1f0a547-9c62-4b93-9bb3-156dcb5ded18c"
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
    "constants": [
        {
            "type": "double",
            "name": "xxx",
            "value": "100",
            "description": ""
        },
        {
            "type": "bool",
            "name": "yyy",
            "value": "true",
            "description": ""
        }
    ]
}

input_data_12 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "rsi",
                            "row1": "Indicator",
                            "params": {
                                "period": 14,
                                "applied_price": "PRICE_LOW",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "xxx"
                            }
                        }
                    },
                    "id": "5b5f3bec-1c29-43f7-8401-808d3ee3c152",
                    "id_by_user": 1,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "group": "0",
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "ExpMode": "None",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "volume_upper_limit": "0",
                        "how_much_volume": "100",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "1",
                        "martingale_reset_on_n_profits": "1",
                        "look_up_on": "LOOK_UP_HISTORY_ONLY",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0",
                        "stoploss": "50",
                        "takeprofit": "50"
                    },
                    "id": "04ed345e-0f75-4e73-abde-fbbe854e874a",
                    "id_by_user": 2,
                    "blockName": "Sell now"
                }
            ],
            "edges": [
                {
                    "source": "5b5f3bec-1c29-43f7-8401-808d3ee3c152",
                    "sourceHandle": "blue",
                    "target": "04ed345e-0f75-4e73-abde-fbbe854e874a",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5b5f3bec-1c29-43f7-8401-808d3ee3c152blue-04ed345e-0f75-4e73-abde-fbbe854e874ac"
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
    "constants": [
        {
            "type": "double",
            "name": "xxx",
            "value": "43",
            "description": ""
        },
        {
            "type": "bool",
            "name": "yyy",
            "value": "false",
            "description": ""
        }
    ]
}

# test profit unrealized, type issue
# diagnose: issue is type_val in filter was not placed in json files in some newer blocks
input_data_13 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0,1}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "pips",
                        "compare": "<",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "0"
                    },
                    "id": "a5128410-0026-4a61-8bf4-144d96de57c6",
                    "id_by_user": 4,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "id": "3ab8dbe5-c9f7-44b5-9954-b01c313695a2",
                    "id_by_user": 5,
                    "blockName": "Once per bar",
                    "params": {}
                }
            ],
            "edges": [
                {
                    "source": "a5128410-0026-4a61-8bf4-144d96de57c6",
                    "sourceHandle": "blue",
                    "target": "3ab8dbe5-c9f7-44b5-9954-b01c313695a2",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a5128410-0026-4a61-8bf4-144d96de57c6blue-3ab8dbe5-c9f7-44b5-9954-b01c313695a2c"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        },
        {
            "type": "bool",
            "name": "xxx",
            "value": "true",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "rsi_under",
            "value": "40",
            "description": ""
        },
        {
            "type": "double",
            "name": "candle_id",
            "value": "1",
            "description": ""
        },
        {
            "type": "double",
            "name": "period",
            "value": "14",
            "description": ""
        }
    ]
}

# test complicated blocks (multiple cluster/graph)
# diagnose: issue is some blocks have empty params (front/backend issue)
input_data_14 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0,1}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "pips",
                        "compare": "<",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "0"
                    },
                    "id": "a5128410-0026-4a61-8bf4-144d96de57c6",
                    "id_by_user": 4,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "id": "3ab8dbe5-c9f7-44b5-9954-b01c313695a2",
                    "id_by_user": 5,
                    "blockName": "Once per bar",
                    "params": {}
                },
                {
                    "params": {
                        "group": "0",
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "ExpMode": "None",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "volume_upper_limit": "0",
                        "how_much_volume": "100",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "1",
                        "martingale_reset_on_n_profits": "1",
                        "look_up_on": "LOOK_UP_HISTORY_ONLY",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0",
                        "stoploss": "50",
                        "takeprofit": "50"
                    },
                    "id": "e87539b1-a36f-47d8-a7c0-3961f349af2e",
                    "id_by_user": 6,
                    "blockName": "Sell now"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": 9,
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        }
                    },
                    "id": "2199bf8d-90d6-44cd-bdd8-8ae31ff96b79",
                    "id_by_user": 7,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_NUMBER",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "pips",
                        "compare": "<",
                        "group_number": "11",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "0"
                    },
                    "id": "2a2f544b-f4e0-4e79-93d0-9154b2226307",
                    "id_by_user": 8,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "params": {
                        "title": "Comment Message",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "obj_title_font": "Georgia",
                        "obj_title_font_color": "clrRed",
                        "obj_title_font_size": "13",
                        "obj_label_font": "Verdana",
                        "obj_label_font_color": "clrRed",
                        "obj_label_font_size": "10",
                        "obj_font": "Verdana",
                        "obj_font_color": "clrRed",
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
                        "format_time_8": "EMPTY_VALUE"
                    },
                    "id": "3c7fafcf-de5e-4054-9d2f-58985439e697",
                    "id_by_user": 9,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_M1"
                    },
                    "id": "80febcec-800d-430e-9552-f3e883f461b5",
                    "id_by_user": 10,
                    "blockName": "Once per bar"
                },
                {
                    "id": "1512fdfe-991f-438f-a8ca-bd7eb1ae8265",
                    "id_by_user": 11,
                    "blockName": "Delay",
                    "params": {}
                },
                {
                    "id": "960c34a0-a4c2-4201-bb81-1e8bdc5d5f46",
                    "id_by_user": 12,
                    "blockName": "AND",
                    "params": {}
                },
                {
                    "id": "726b0487-9f69-4916-90bf-0f8f8c6e20c5",
                    "id_by_user": 13,
                    "blockName": "OR",
                    "params": {}
                },
                {
                    "id": "a9a88983-d460-4190-8ced-3faafd82bfc6",
                    "id_by_user": 14,
                    "blockName": "Modify Variables",
                    "params": {}
                },
                {
                    "id": "e8b2a8dc-ad9c-4d45-89e6-35227ab31946",
                    "id_by_user": 15,
                    "blockName": "Modify Variables",
                    "params": {}
                },
                {
                    "id": "6ef5ec5e-67bc-4f79-abcb-8008ef892c10",
                    "id_by_user": 16,
                    "blockName": "Close trades",
                    "params": {}
                },
                {
                    "id": "2fce317a-84c0-41a5-8004-69fda827c7e0",
                    "id_by_user": 17,
                    "blockName": "condition",
                    "params": {}
                },
                {
                    "id": "aa15645b-e733-43ce-9cba-6d9cb191a6a8",
                    "id_by_user": 18,
                    "blockName": "No trade nearby",
                    "params": {}
                }
            ],
            "edges": [
                {
                    "source": "a5128410-0026-4a61-8bf4-144d96de57c6",
                    "sourceHandle": "blue",
                    "target": "3ab8dbe5-c9f7-44b5-9954-b01c313695a2",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a5128410-0026-4a61-8bf4-144d96de57c6blue-3ab8dbe5-c9f7-44b5-9954-b01c313695a2c"
                },
                {
                    "source": "2199bf8d-90d6-44cd-bdd8-8ae31ff96b79",
                    "sourceHandle": "blue",
                    "target": "e87539b1-a36f-47d8-a7c0-3961f349af2e",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-2199bf8d-90d6-44cd-bdd8-8ae31ff96b79blue-e87539b1-a36f-47d8-a7c0-3961f349af2ec"
                },
                {
                    "source": "1512fdfe-991f-438f-a8ca-bd7eb1ae8265",
                    "sourceHandle": "blue",
                    "target": "e87539b1-a36f-47d8-a7c0-3961f349af2e",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-1512fdfe-991f-438f-a8ca-bd7eb1ae8265blue-e87539b1-a36f-47d8-a7c0-3961f349af2ec"
                },
                {
                    "source": "e87539b1-a36f-47d8-a7c0-3961f349af2e",
                    "sourceHandle": "blue",
                    "target": "960c34a0-a4c2-4201-bb81-1e8bdc5d5f46",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-e87539b1-a36f-47d8-a7c0-3961f349af2eblue-960c34a0-a4c2-4201-bb81-1e8bdc5d5f46c"
                },
                {
                    "source": "2fce317a-84c0-41a5-8004-69fda827c7e0",
                    "sourceHandle": "blue",
                    "target": "6ef5ec5e-67bc-4f79-abcb-8008ef892c10",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-2fce317a-84c0-41a5-8004-69fda827c7e0blue-6ef5ec5e-67bc-4f79-abcb-8008ef892c10c"
                },
                {
                    "source": "6ef5ec5e-67bc-4f79-abcb-8008ef892c10",
                    "sourceHandle": "blue",
                    "target": "aa15645b-e733-43ce-9cba-6d9cb191a6a8",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-6ef5ec5e-67bc-4f79-abcb-8008ef892c10blue-aa15645b-e733-43ce-9cba-6d9cb191a6a8c"
                },
                {
                    "source": "aa15645b-e733-43ce-9cba-6d9cb191a6a8",
                    "sourceHandle": "blue",
                    "target": "80febcec-800d-430e-9552-f3e883f461b5",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-aa15645b-e733-43ce-9cba-6d9cb191a6a8blue-80febcec-800d-430e-9552-f3e883f461b5c"
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
    "variables": [
        {
            "type": "double",
            "name": "x",
            "value": "1000",
            "description": ""
        },
        {
            "type": "bool",
            "name": "xxx",
            "value": "true",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "rsi_under",
            "value": "40",
            "description": ""
        },
        {
            "type": "double",
            "name": "candle_id",
            "value": "1",
            "description": ""
        },
        {
            "type": "double",
            "name": "period",
            "value": "14",
            "description": ""
        }
    ]
}
