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
                        },
                        "price": {
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
                        "type": "{1}",
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

# test alireza error
input_data_15 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "operator": {
                            "label": "×>",
                            "cross_width": 1
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "rsi",
                            "params": {
                                "period": "rsi_period",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "1",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "rsi_buy"
                            }
                        }
                    },
                    "id": "f6251dc5-c776-40d8-b1d8-8463c9b46bbd",
                    "id_by_user": 1,
                    "blockName": "condition"
                },
                {
                    "id": "6fdfd6fb-e4dd-4b41-8f20-0828f8fdb869",
                    "id_by_user": 2,
                    "blockName": "Once per bar",
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_M1"
                    }
                },
                {
                    "params": {
                        "group": "0",
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "ExpMode": "None",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "volume_upper_limit": "0",
                        "how_much_volume": "lot",
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
                        "stoploss": "sl_pips",
                        "takeprofit": "50"
                    },
                    "id": "9832311a-d9bb-4ccb-a41c-c3bfb9c59a93",
                    "id_by_user": 3,
                    "blockName": "Sell now"
                },
                {
                    "params": {
                        "group": "0",
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "ExpMode": "None",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "volume_upper_limit": "0",
                        "how_much_volume": "lot",
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
                        "stoploss": "sl_pips",
                        "takeprofit": "50"
                    },
                    "id": "4f74f1e5-3c09-43a2-a528-5f1ba0906cb0",
                    "id_by_user": 4,
                    "blockName": "Buy now"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "symbols_str": ""
                    },
                    "id": "0885306c-0bfc-4f62-b692-da1c6a31e86a",
                    "id_by_user": 5,
                    "blockName": "If trade"
                },
                {
                    "id": "499d85e8-9e50-46c4-becd-bed73e66d96c",
                    "id_by_user": 6,
                    "blockName": "No trade nearby",
                    "params": {}
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "money",
                        "compare": ">=",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "profit_dollar"
                    },
                    "id": "4b6eceb7-17fc-46f2-b0a6-2bf3a65a6637",
                    "id_by_user": 7,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "id": "fecc7fd8-b72f-480e-b3a9-84ad8b7cac1e",
                    "id_by_user": 8,
                    "blockName": "Modify Variables",
                    "params": {}
                },
                {
                    "id": "56c5c668-576a-42d1-abe0-64bb5c5cfb37",
                    "id_by_user": 9,
                    "blockName": "Comment",
                    "params": {}
                },
                {
                    "id": "e0959ab8-2089-4d42-8553-fd602fd86b35",
                    "id_by_user": 10,
                    "blockName": "Loop(pass \"n\" times)",
                    "params": {}
                },
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_M1"
                    },
                    "id": "16eca8e8-f7bd-4798-83ec-0e16fbe9d1ae",
                    "id_by_user": 11,
                    "blockName": "Once per bar"
                },
                {
                    "id": "481ec014-1488-45ae-83e1-bf9eff095b75",
                    "id_by_user": 12,
                    "blockName": "Delay",
                    "params": {}
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "older_than": "0",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "symbols_str": ""
                    },
                    "id": "08609195-a67e-493b-b864-d949994ee4b6",
                    "id_by_user": 13,
                    "blockName": "Close trades"
                },
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
                                "period": "rsi_period",
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
                                "value": "rsi_sell"
                            }
                        }
                    },
                    "id": "96c2746b-3313-4bf2-bb2e-2c28e2426978",
                    "id_by_user": 14,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{1}",
                        "symbols_str": ""
                    },
                    "id": "8cf9bd40-7f64-4908-a3cd-05026c9ebc18",
                    "id_by_user": 15,
                    "blockName": "If trade"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{1}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "money",
                        "compare": ">=",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "profit_dollar"
                    },
                    "id": "dedd7ce4-0cb2-4bbd-9f62-213d3e0ae7b5",
                    "id_by_user": 16,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{1}",
                        "older_than": "0",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "symbols_str": ""
                    },
                    "id": "a67a6f33-7346-40d8-bd7c-9777a1b39753",
                    "id_by_user": 17,
                    "blockName": "Close trades"
                }
            ],
            "edges": [
                {
                    "source": "16eca8e8-f7bd-4798-83ec-0e16fbe9d1ae",
                    "sourceHandle": "blue",
                    "target": "f6251dc5-c776-40d8-b1d8-8463c9b46bbd",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-16eca8e8-f7bd-4798-83ec-0e16fbe9d1aeblue-f6251dc5-c776-40d8-b1d8-8463c9b46bbdc"
                },
                {
                    "source": "f6251dc5-c776-40d8-b1d8-8463c9b46bbd",
                    "sourceHandle": "blue",
                    "target": "4f74f1e5-3c09-43a2-a528-5f1ba0906cb0",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-f6251dc5-c776-40d8-b1d8-8463c9b46bbdblue-4f74f1e5-3c09-43a2-a528-5f1ba0906cb0c"
                },
                {
                    "source": "16eca8e8-f7bd-4798-83ec-0e16fbe9d1ae",
                    "sourceHandle": "blue",
                    "target": "96c2746b-3313-4bf2-bb2e-2c28e2426978",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-16eca8e8-f7bd-4798-83ec-0e16fbe9d1aeblue-96c2746b-3313-4bf2-bb2e-2c28e2426978c"
                },
                {
                    "source": "96c2746b-3313-4bf2-bb2e-2c28e2426978",
                    "sourceHandle": "blue",
                    "target": "9832311a-d9bb-4ccb-a41c-c3bfb9c59a93",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-96c2746b-3313-4bf2-bb2e-2c28e2426978blue-9832311a-d9bb-4ccb-a41c-c3bfb9c59a93c"
                },
                {
                    "source": "0885306c-0bfc-4f62-b692-da1c6a31e86a",
                    "sourceHandle": "blue",
                    "target": "4b6eceb7-17fc-46f2-b0a6-2bf3a65a6637",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-0885306c-0bfc-4f62-b692-da1c6a31e86ablue-4b6eceb7-17fc-46f2-b0a6-2bf3a65a6637c"
                },
                {
                    "source": "4b6eceb7-17fc-46f2-b0a6-2bf3a65a6637",
                    "sourceHandle": "blue",
                    "target": "08609195-a67e-493b-b864-d949994ee4b6",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-4b6eceb7-17fc-46f2-b0a6-2bf3a65a6637blue-08609195-a67e-493b-b864-d949994ee4b6c"
                },
                {
                    "source": "8cf9bd40-7f64-4908-a3cd-05026c9ebc18",
                    "sourceHandle": "blue",
                    "target": "dedd7ce4-0cb2-4bbd-9f62-213d3e0ae7b5",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-8cf9bd40-7f64-4908-a3cd-05026c9ebc18blue-dedd7ce4-0cb2-4bbd-9f62-213d3e0ae7b5c"
                },
                {
                    "source": "dedd7ce4-0cb2-4bbd-9f62-213d3e0ae7b5",
                    "sourceHandle": "blue",
                    "target": "a67a6f33-7346-40d8-bd7c-9777a1b39753",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-dedd7ce4-0cb2-4bbd-9f62-213d3e0ae7b5blue-a67a6f33-7346-40d8-bd7c-9777a1b39753c"
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
            "name": "rsi_period",
            "value": "14",
            "description": ""
        },
        {
            "type": "double",
            "name": "rsi_buy",
            "value": "20",
            "description": ""
        },
        {
            "type": "double",
            "name": "rsi_sell",
            "value": "75",
            "description": ""
        },
        {
            "type": "double",
            "name": "lot",
            "value": "1",
            "description": ""
        },
        {
            "type": "double",
            "name": "profit_dollar",
            "value": "50",
            "description": ""
        },
        {
            "type": "double",
            "name": "sl_dollar",
            "value": "100",
            "description": ""
        },
        {
            "type": "double",
            "name": "sl_pips",
            "value": "10",
            "description": ""
        }
    ]
}

input_data_16 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "operator": {
                            "label": "×>",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "rsi",
                            "row1": "Indicator",
                            "params": {
                                "period": "rsi_period",
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
                                "value": "rsi_buy"
                            }
                        }
                    },
                    "id": "c15d81bc-1609-4a05-bfa6-ea0bf4adb1d4",
                    "id_by_user": 6,
                    "blockName": "condition"
                },
                {
                    "id": "5e454b31-41a3-4005-9bf8-136cae256373",
                    "id_by_user": 7,
                    "blockName": "Once per bar",
                    "params": {}
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "older_than": "0",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "symbols_str": ""
                    },
                    "id": "7fcb4dd5-c416-4217-ac0e-cdb7f23b22cf",
                    "id_by_user": 8,
                    "blockName": "Close trades"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "profit_mode_each": "no_matter",
                        "profit_mode": "money",
                        "compare": ">=",
                        "symbols_str": "",
                        "profit_amount_each": "10",
                        "compare_each": ">",
                        "profit_amount": "tp_money"
                    },
                    "id": "6659854f-e8b2-4c60-a947-c9a9ff32161c",
                    "id_by_user": 10,
                    "blockName": "Check profit (unrealized)"
                },
                {
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "symbols_str": ""
                    },
                    "id": "db1847e9-43d5-4fe9-a8d0-f3929e0d65b0",
                    "id_by_user": 11,
                    "blockName": "If trade"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "triger_1",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Boolean",
                                "params": {
                                    "value": "true"
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
                    "id": "60572059-7885-450f-85c2-75cb34c5d790",
                    "id_by_user": 12,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "operator": {
                            "label": "==",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "Boolean",
                            "row1": "Value",
                            "params": {
                                "value": "triger_1"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "true"
                            }
                        }
                    },
                    "id": "d57b9808-613f-46b1-88f3-ea36bafbc2fd",
                    "id_by_user": 13,
                    "blockName": "condition"
                },
                {
                    "id": "f2cdd165-ad26-4254-a5c8-32fc6c6f48f7",
                    "id_by_user": 14,
                    "blockName": "Once per bar",
                    "params": {}
                },
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
                                "applied_price": "PRICE_CLOSE",
                                "shift": "candle_id",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT",
                                "period": 14
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
                    "id": "faa3f76c-0aa4-4237-bb4c-72cf91194887",
                    "id_by_user": 15,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "triger_1",
                            "value_fetch": {
                                "row2": "Boolean",
                                "row1": "Value",
                                "params": {
                                    "value": "false"
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
                    "id": "0b02283e-f0bf-4378-837e-5cff0f8ef56a",
                    "id_by_user": 16,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "operator": {
                            "label": "×>",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "macd",
                            "row1": "Indicator",
                            "params": {
                                "fast_ema_period": "26",
                                "slow_ema_period": "12",
                                "signal_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": "candle_id",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT"
                            }
                        },
                        "right": {
                            "row2": "macd",
                            "row1": "Indicator",
                            "params": {
                                "fast_ema_period": "26",
                                "slow_ema_period": "13",
                                "signal_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": "candle_id",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT"
                            }
                        }
                    },
                    "id": "cdc5e9e9-6f36-417f-8975-acd5f0143e12",
                    "id_by_user": 17,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "trigger_2",
                            "value_fetch": {
                                "row2": "Boolean",
                                "row1": "Value",
                                "params": {
                                    "value": "true"
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
                    "id": "c78e62be-6da9-4e2e-97c1-9ba86201177d",
                    "id_by_user": 19,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "sleep_seconds": 5,
                        "sleep_tester_normal": "false",
                        "sleep_tester_visual": "true"
                    },
                    "id": "b7ac1ac3-01b2-4a16-b861-711b9a61a3e7",
                    "id_by_user": 20,
                    "blockName": "Delay"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "triger_1",
                            "value_fetch": {
                                "row2": "Boolean",
                                "row1": "Value",
                                "params": {
                                    "value": "false"
                                }
                            }
                        },
                        "variable2": {
                            "variable_name": "trigger_2",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Boolean",
                                "params": {
                                    "value": "false"
                                }
                            }
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
                    "id": "6dfee015-4610-409a-9e85-d4079e9dc0a3",
                    "id_by_user": 22,
                    "blockName": "Modify Variables"
                }
            ],
            "edges": [
                {
                    "source": "db1847e9-43d5-4fe9-a8d0-f3929e0d65b0",
                    "sourceHandle": "blue",
                    "target": "6659854f-e8b2-4c60-a947-c9a9ff32161c",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-db1847e9-43d5-4fe9-a8d0-f3929e0d65b0blue-6659854f-e8b2-4c60-a947-c9a9ff32161cc"
                },
                {
                    "source": "6659854f-e8b2-4c60-a947-c9a9ff32161c",
                    "sourceHandle": "blue",
                    "target": "7fcb4dd5-c416-4217-ac0e-cdb7f23b22cf",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-6659854f-e8b2-4c60-a947-c9a9ff32161cblue-7fcb4dd5-c416-4217-ac0e-cdb7f23b22cfc"
                },
                {
                    "source": "c15d81bc-1609-4a05-bfa6-ea0bf4adb1d4",
                    "sourceHandle": "blue",
                    "target": "60572059-7885-450f-85c2-75cb34c5d790",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-c15d81bc-1609-4a05-bfa6-ea0bf4adb1d4blue-60572059-7885-450f-85c2-75cb34c5d790c"
                },
                {
                    "source": "5e454b31-41a3-4005-9bf8-136cae256373",
                    "sourceHandle": "blue",
                    "target": "c15d81bc-1609-4a05-bfa6-ea0bf4adb1d4",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5e454b31-41a3-4005-9bf8-136cae256373blue-c15d81bc-1609-4a05-bfa6-ea0bf4adb1d4c"
                },
                {
                    "source": "f2cdd165-ad26-4254-a5c8-32fc6c6f48f7",
                    "sourceHandle": "blue",
                    "target": "d57b9808-613f-46b1-88f3-ea36bafbc2fd",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-f2cdd165-ad26-4254-a5c8-32fc6c6f48f7blue-d57b9808-613f-46b1-88f3-ea36bafbc2fdc"
                },
                {
                    "source": "5e454b31-41a3-4005-9bf8-136cae256373",
                    "sourceHandle": "blue",
                    "target": "faa3f76c-0aa4-4237-bb4c-72cf91194887",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5e454b31-41a3-4005-9bf8-136cae256373blue-faa3f76c-0aa4-4237-bb4c-72cf91194887c"
                },
                {
                    "source": "faa3f76c-0aa4-4237-bb4c-72cf91194887",
                    "sourceHandle": "blue",
                    "target": "0b02283e-f0bf-4378-837e-5cff0f8ef56a",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-faa3f76c-0aa4-4237-bb4c-72cf91194887blue-0b02283e-f0bf-4378-837e-5cff0f8ef56ac"
                },
                {
                    "source": "d57b9808-613f-46b1-88f3-ea36bafbc2fd",
                    "sourceHandle": "blue",
                    "target": "cdc5e9e9-6f36-417f-8975-acd5f0143e12",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-d57b9808-613f-46b1-88f3-ea36bafbc2fdblue-cdc5e9e9-6f36-417f-8975-acd5f0143e12c"
                },
                {
                    "source": "cdc5e9e9-6f36-417f-8975-acd5f0143e12",
                    "sourceHandle": "blue",
                    "target": "c78e62be-6da9-4e2e-97c1-9ba86201177d",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-cdc5e9e9-6f36-417f-8975-acd5f0143e12blue-c78e62be-6da9-4e2e-97c1-9ba86201177dc"
                },
                {
                    "source": "c78e62be-6da9-4e2e-97c1-9ba86201177d",
                    "sourceHandle": "blue",
                    "target": "b7ac1ac3-01b2-4a16-b861-711b9a61a3e7",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-c78e62be-6da9-4e2e-97c1-9ba86201177dblue-b7ac1ac3-01b2-4a16-b861-711b9a61a3e7c"
                },
                {
                    "source": "b7ac1ac3-01b2-4a16-b861-711b9a61a3e7",
                    "sourceHandle": "blue",
                    "target": "6dfee015-4610-409a-9e85-d4079e9dc0a3",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-b7ac1ac3-01b2-4a16-b861-711b9a61a3e7blue-6dfee015-4610-409a-9e85-d4079e9dc0a3c"
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
            "type": "bool",
            "name": "triger_1",
            "value": "false",
            "description": ""
        },
        {
            "type": "bool",
            "name": "trigger_2",
            "value": "false",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "int",
            "name": "rsi_period",
            "value": "14",
            "description": ""
        },
        {
            "type": "double",
            "name": "rsi_buy",
            "value": "20",
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
            "name": "lot",
            "value": "1",
            "description": ""
        },
        {
            "type": "double",
            "name": "sl_pips",
            "value": "100",
            "description": ""
        },
        {
            "type": "double",
            "name": "tp_money",
            "value": "30",
            "description": ""
        }
    ]
}

input_data_17 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "left": {
                            "row1": "Market Properties",
                            "row2": "HIGHEST_PRICE_CANDLE_PERIOD",
                            "params": {
                                "range_start": "0",
                                "range_end": "150",
                                "what_to_get": "GET_PRICE"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "0"
                            }
                        },
                        "operator": {
                            "label": "+"
                        },
                        "ajdust": "",
                        "variable": "xxx"
                    },
                    "id": "4a04d07e-ca3c-45b7-826c-afcd474e0fed",
                    "id_by_user": 2,
                    "blockName": "formula"
                },
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "7bb7f0e8-4b02-42dc-b4f6-1826993f4c1f",
                    "id_by_user": 3,
                    "blockName": "Once per bar"
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
                        "label_1": "Candle High [20] is:",
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
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "xxx"
                            }
                        }
                    },
                    "id": "e5cf2aeb-7627-4182-926a-3e12194135f7",
                    "id_by_user": 4,
                    "blockName": "Comment"
                }
            ],
            "edges": [
                {
                    "source": "7bb7f0e8-4b02-42dc-b4f6-1826993f4c1f",
                    "sourceHandle": "blue",
                    "target": "4a04d07e-ca3c-45b7-826c-afcd474e0fed",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-7bb7f0e8-4b02-42dc-b4f6-1826993f4c1fblue-4a04d07e-ca3c-45b7-826c-afcd474e0fedc"
                },
                {
                    "source": "4a04d07e-ca3c-45b7-826c-afcd474e0fed",
                    "sourceHandle": "blue",
                    "target": "e5cf2aeb-7627-4182-926a-3e12194135f7",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-4a04d07e-ca3c-45b7-826c-afcd474e0fedblue-e5cf2aeb-7627-4182-926a-3e12194135f7c"
                }
            ]
        },
        "on_trade": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_timer": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_init": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_deinit": {
            "nodes": [

            ],
            "edges": [

            ]
        }
    },
    "variables": [
        {
            "type": "double",
            "name": "xxx",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [

    ]
}

input_data_18 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "071d4995-44af-4f75-a5c3-7a127dc9e8d7",
                    "id_by_user": 2,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "title": "Comment Message",
                        "obj_chart_subwindow": "",
                        "obj_corner": "CORNER_LEFT_UPPER",
                        "obj_x": "5",
                        "obj_y": "5",
                        "label_1": "low price:",
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
                            "row2": "Numeric",
                            "params": {
                                "value": "min_price"
                            }
                        },
                        "value_fetch_2": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "max_price"
                            }
                        },
                        "value_fetch_3": {
                            "row1": "Value",
                            "row2": "Text",
                            "params": {
                                "value": "sample text"
                            }
                        }
                    },
                    "id": "3cdd6a1d-4f69-447e-a7fa-ef9afb97bae1",
                    "id_by_user": 3,
                    "blockName": "Comment"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "max_price",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "0"
                                }
                            }
                        },
                        "variable2": {
                            "variable_name": "min_price",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "9999999"
                                }
                            }
                        },
                        "variable3": {
                            "variable_name": "loop_counter",
                            "value_fetch": {
                                "row1": "Value",
                                "row2": "Numeric",
                                "params": {
                                    "value": "0"
                                }
                            }
                        },
                        "variable4": {
                            "variable_name": ""
                        },
                        "variable5": {
                            "variable_name": ""
                        }
                    },
                    "id": "10aa7065-7481-4016-965f-b5b7f0ad497d",
                    "id_by_user": 4,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "n": "loop_count"
                    },
                    "id": "f002ebcc-e73a-4e00-b1a4-3c6dee511caf",
                    "id_by_user": 5,
                    "blockName": "Loop(pass \"n\" times)"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "params": {
                                "price_mode": "CANDLE_HIGH",
                                "find_method": "FIND_BY_ID",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT",
                                "shift": "loop_counter"
                            },
                            "row1": "Candle",
                            "row2": "Candle"
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "max_price"
                            }
                        }
                    },
                    "id": "20fe764c-2251-4907-aacf-9b121d3fceda",
                    "id_by_user": 6,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "operator": {
                            "label": "<",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "Candle",
                            "row1": "Candle",
                            "params": {
                                "price_mode": "CANDLE_LOW",
                                "find_method": "FIND_BY_ID",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_CURRENT",
                                "shift": "loop_counter"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "min_price"
                            }
                        }
                    },
                    "id": "9999b102-dfaf-405a-b321-40571ebbcd36",
                    "id_by_user": 7,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "max_price",
                            "value_fetch": {
                                "row1": "Candle",
                                "row2": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_HIGH",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "NULL",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "loop_counter"
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
                    "id": "cc3e090a-3916-4a9e-a5c8-3c613b24c8fb",
                    "id_by_user": 8,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "variable1": {
                            "variable_name": "min_price",
                            "value_fetch": {
                                "row2": "Candle",
                                "row1": "Candle",
                                "params": {
                                    "price_mode": "CANDLE_LOW",
                                    "find_method": "FIND_BY_ID",
                                    "symbol": "NULL",
                                    "timeframe": "PERIOD_CURRENT",
                                    "shift": "loop_counter"
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
                    "id": "1c0bab59-f267-4d4a-b573-4a46ec4b826c",
                    "id_by_user": 9,
                    "blockName": "Modify Variables"
                },
                {
                    "params": {
                        "left": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "loop_counter"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "1"
                            }
                        },
                        "operator": {
                            "label": "+"
                        },
                        "ajdust": "loop_counter",
                        "variable": ""
                    },
                    "id": "b97d7fc0-0cbd-45ce-9374-2beb4092a024",
                    "id_by_user": 10,
                    "blockName": "formula"
                },
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 12,
                    "blockName": "Once per bar"
                }
            ],
            "edges": [
                {
                    "source": "071d4995-44af-4f75-a5c3-7a127dc9e8d7",
                    "sourceHandle": "blue",
                    "target": "3cdd6a1d-4f69-447e-a7fa-ef9afb97bae1",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-071d4995-44af-4f75-a5c3-7a127dc9e8d7blue-3cdd6a1d-4f69-447e-a7fa-ef9afb97bae1c"
                },
                {
                    "source": "10aa7065-7481-4016-965f-b5b7f0ad497d",
                    "sourceHandle": "blue",
                    "target": "f002ebcc-e73a-4e00-b1a4-3c6dee511caf",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-10aa7065-7481-4016-965f-b5b7f0ad497dblue-f002ebcc-e73a-4e00-b1a4-3c6dee511cafc"
                },
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "10aa7065-7481-4016-965f-b5b7f0ad497d",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-10aa7065-7481-4016-965f-b5b7f0ad497dc"
                },
                {
                    "source": "9999b102-dfaf-405a-b321-40571ebbcd36",
                    "sourceHandle": "blue",
                    "target": "1c0bab59-f267-4d4a-b573-4a46ec4b826c",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-9999b102-dfaf-405a-b321-40571ebbcd36blue-1c0bab59-f267-4d4a-b573-4a46ec4b826cc"
                },
                {
                    "source": "20fe764c-2251-4907-aacf-9b121d3fceda",
                    "sourceHandle": "blue",
                    "target": "cc3e090a-3916-4a9e-a5c8-3c613b24c8fb",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-20fe764c-2251-4907-aacf-9b121d3fcedablue-cc3e090a-3916-4a9e-a5c8-3c613b24c8fbc"
                },
                {
                    "source": "f002ebcc-e73a-4e00-b1a4-3c6dee511caf",
                    "sourceHandle": "blue",
                    "target": "b97d7fc0-0cbd-45ce-9374-2beb4092a024",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-f002ebcc-e73a-4e00-b1a4-3c6dee511cafblue-b97d7fc0-0cbd-45ce-9374-2beb4092a024c"
                },
                {
                    "source": "b97d7fc0-0cbd-45ce-9374-2beb4092a024",
                    "sourceHandle": "blue",
                    "target": "9999b102-dfaf-405a-b321-40571ebbcd36",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-b97d7fc0-0cbd-45ce-9374-2beb4092a024blue-9999b102-dfaf-405a-b321-40571ebbcd36c"
                },
                {
                    "source": "b97d7fc0-0cbd-45ce-9374-2beb4092a024",
                    "sourceHandle": "blue",
                    "target": "20fe764c-2251-4907-aacf-9b121d3fceda",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-b97d7fc0-0cbd-45ce-9374-2beb4092a024blue-20fe764c-2251-4907-aacf-9b121d3fcedac"
                }
            ]
        },
        "on_trade": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_timer": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_init": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_deinit": {
            "nodes": [

            ],
            "edges": [

            ]
        }
    },
    "variables": [
        {
            "type": "double",
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

input_data_19 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 12,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "sleep_seconds": "0.05",
                        "sleep_tester_normal": "true",
                        "sleep_tester_visual": "true"
                    },
                    "id": "6dd9f98b-6fd3-4914-9921-57f9df0ce7b7",
                    "id_by_user": 13,
                    "blockName": "Delay"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "6dd9f98b-6fd3-4914-9921-57f9df0ce7b7",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-6dd9f98b-6fd3-4914-9921-57f9df0ce7b7c"
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
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# test market properties after change
input_data_20 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 12,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "sleep_seconds": "0.05",
                        "sleep_tester_normal": "true",
                        "sleep_tester_visual": "true"
                    },
                    "id": "6dd9f98b-6fd3-4914-9921-57f9df0ce7b7",
                    "id_by_user": 13,
                    "blockName": "Delay"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row1": "Market Properties",
                            "row2": "HIGHEST_PRICE_CANDLE_PERIOD",
                            "params": {
                                "range_start": "0",
                                "range_end": "10",
                                "what_to_get": "what_to_get"
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
                                "shift": "shift",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        }
                    },
                    "id": "d3172b9b-4e60-4280-83c4-af9ef1c39e0b",
                    "id_by_user": 14,
                    "blockName": "condition"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "6dd9f98b-6fd3-4914-9921-57f9df0ce7b7",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-6dd9f98b-6fd3-4914-9921-57f9df0ce7b7c"
                },
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "d3172b9b-4e60-4280-83c4-af9ef1c39e0b",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-d3172b9b-4e60-4280-83c4-af9ef1c39e0bc"
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
            "name": "shift",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "string",
            "name": "what_to_get",
            "value": "5",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# test value > time
input_data_21 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 12,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "Time",
                            "row1": "Value",
                            "params": {
                                "mode_time": "MODE_TIME_NOW",
                                "mode_time_shift": "0",
                                "time_source": "TIME_SERVER",
                                "time_shift_years": "0",
                                "time_shift_months": "0",
                                "time_shift_weeks": "0",
                                "time_shift_days": "period"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "0"
                            }
                        }
                    },
                    "id": "76062001-1361-4923-b1cc-ace9f274cf46",
                    "id_by_user": 13,
                    "blockName": "condition"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "76062001-1361-4923-b1cc-ace9f274cf46",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-76062001-1361-4923-b1cc-ace9f274cf46c"
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
            "name": "period",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# test formula > adjust
input_data_22 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 12,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "Time",
                            "row1": "Value",
                            "params": {
                                "mode_time": "MODE_TIME_CANDLE_TIME",
                                "mode_time_shift": "loop_counter",
                                "time_candle_id": "min_price",
                                "time_market": "NULL",
                                "time_candle_timeframe": "PERIOD_M5"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "loop_count"
                            }
                        }
                    },
                    "id": "76062001-1361-4923-b1cc-ace9f274cf46",
                    "id_by_user": 13,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "left": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "1"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "1"
                            }
                        },
                        "operator": {
                            "label": "+"
                        },
                        "adjust": "+10%",
                        "variable": "loop_count"
                    },
                    "id": "5c747bf0-20ea-4334-a23c-8dea2d75a018",
                    "id_by_user": 14,
                    "blockName": "formula"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "76062001-1361-4923-b1cc-ace9f274cf46",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-76062001-1361-4923-b1cc-ace9f274cf46c"
                },
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "5c747bf0-20ea-4334-a23c-8dea2d75a018",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-5c747bf0-20ea-4334-a23c-8dea2d75a018c"
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
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f1",
                    "id_by_user": 1,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row2": "Candle",
                            "row1": "Candle",
                            "params": {
                                "price_mode": "price_mode",
                                "find_method": "FIND_BY_ID",
                                "symbol": "my_symbol",
                                "timeframe": "PERIOD_CURRENT",
                                "shift": "loop_count"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "loop_count"
                            }
                        }
                    },
                    "id": "76062001-1361-4923-b1cc-ace9f274cf461",
                    "id_by_user": 2,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "left": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "1"
                            }
                        },
                        "right": {
                            "row2": "Numeric",
                            "row1": "Value",
                            "params": {
                                "value": "1"
                            }
                        },
                        "operator": {
                            "label": "+"
                        },
                        "adjust": "+10%",
                        "variable": "loop_count"
                    },
                    "id": "5c747bf0-20ea-4334-a23c-8dea2d75a0181",
                    "id_by_user": 3,
                    "blockName": "formula"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f1",
                    "sourceHandle": "blue",
                    "target": "76062001-1361-4923-b1cc-ace9f274cf461",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-76062001-1361-4923-b1cc-ace9f274cf46c"
                },
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f1",
                    "sourceHandle": "blue",
                    "target": "5c747bf0-20ea-4334-a23c-8dea2d75a0181",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-5c747bf0-20ea-4334-a23c-8dea2d75a018c"
                }
            ]
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
            "type": "string",
            "name": "price_mode",
            "value": "my_personal_price_mode",
            "description": ""
        },
        {
            "type": "string",
            "name": "my_symbol",
            "value": "EURUSD, NZDUSD",
            "description": ""
        },
        {
            "type": "double",
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# test buy sell pending martingale, look upon
input_data_23 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 12,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "group": "11",
                        "symbol": "NULL",
                        "price_offset": "10",
                        "open_at_price": "OPEN_AT_BID",
                        "volume_upper_limit": "10",
                        "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "ExpMode": "None",
                        "oco": "oco2",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "stoploss": "20",
                        "takeprofit": "20",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0",
                        "how_much_volume": "0.1"
                    },
                    "id": "2b8a3c74-ac06-48b9-9c22-50c6722e2b02",
                    "id_by_user": 15,
                    "blockName": "Buy pending order"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "2b8a3c74-ac06-48b9-9c22-50c6722e2b02",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-2b8a3c74-ac06-48b9-9c22-50c6722e2b02c"
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
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# trailing pending order, new data structure, testing pending order type input
input_data_24 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 20,
                    "blockName": "trailing_pending_orders",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{2, 3, 4, 5}",
                        "type_pending": "{2, 3}",
                        "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
                        "t_distance_pips": 10.0,
                        "t_step_pips": 1.0,
                        "dynamic_size_pips_input": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "30"
                            }
                        }
                    }
                },
                {
                    "params": {
                        "group": "11",
                        "symbol": "NULL",
                        "price_offset": "10",
                        "open_at_price": "OPEN_AT_BID",
                        "volume_upper_limit": "10",
                        "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "ExpMode": "None",
                        "oco": "oco2",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "stoploss": "20",
                        "takeprofit": "20",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0",
                        "how_much_volume": "0.1"
                    },
                    "id": "2b8a3c74-ac06-48b9-9c22-50c6722e2b02",
                    "id_by_user": 15,
                    "blockName": "Buy pending order"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "2b8a3c74-ac06-48b9-9c22-50c6722e2b02",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-2b8a3c74-ac06-48b9-9c22-50c6722e2b02c"
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
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# test variables constants same name as class members to see if the solution works properly
input_data_25 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "id_by_user": 20,
                    "blockName": "trailing_pending_orders",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "group_mode",
                        "group_number": 15,
                        "type": "{2, 3, 4, 5}",
                        "type_pending": "{2, 3}",
                        "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
                        "t_distance_pips": 10.0,
                        "t_step_pips": 1.0,
                        "dynamic_size_pips_input": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "30"
                            }
                        }
                    }
                },
                {
                    "params": {
                        "group": "11",
                        "symbol": "NULL",
                        "price_offset": "10",
                        "open_at_price": "OPEN_AT_BID",
                        "volume_upper_limit": "10",
                        "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "ExpMode": "None",
                        "oco": "oco2",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "Short trade",
                        "stoploss": "20",
                        "takeprofit": "20",
                        "ExpDays": "0",
                        "ExpHours": "1",
                        "ExpMinutes": "0",
                        "how_much_volume": "0.1"
                    },
                    "id": "2b8a3c74-ac06-48b9-9c22-50c6722e2b02",
                    "id_by_user": 15,
                    "blockName": "Buy pending order"
                }
            ],
            "edges": [
                {
                    "source": "a9e6ec2f-9e93-47fb-9126-ba1d37b78b7f",
                    "sourceHandle": "blue",
                    "target": "2b8a3c74-ac06-48b9-9c22-50c6722e2b02",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-a9e6ec2f-9e93-47fb-9126-ba1d37b78b7fblue-2b8a3c74-ac06-48b9-9c22-50c6722e2b02c"
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
            "name": "period",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "max_price",
            "value": "0",
            "description": ""
        },
        {
            "type": "double",
            "name": "min_price",
            "value": "999999999",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_counter",
            "value": "0",
            "description": ""
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "group_mode",
            "value": "5",
            "description": ""
        },
        {
            "type": "double",
            "name": "loop_count",
            "value": "5",
            "description": ""
        }
    ]
}

# test order moved
input_data_26 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "order_moved",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{2,4}",
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{0}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test trade created
input_data_27 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "trade_created",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{1}",
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test trade stops modified
input_data_28 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "trade_stops_modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{0}",
                        "stops_mode": "some"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test trade sl modified
input_data_29 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "trade_sl_modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{0,1}",
                        "sl_only": "no"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test trade tp modified
input_data_30 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "trade_tp_modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{1}",
                        "tp_only": "no"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test order stops modified
input_data_31 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "order_stops_modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{2,3}",
                        "stops_mode": "slortp"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test order sl modified
input_data_32 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "Order SL modified",
                    "block_name_mql": "order_sl_modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{2,4}",
                        "type_pending": "{4,5}",
                        "sl_only": "no"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test order tp modified
input_data_33 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "Order TP modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{3,5}",
                        "type_pending": "{4,5}",
                        "tp_only": "no"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}
