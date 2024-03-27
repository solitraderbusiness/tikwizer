# test data by front
input_data_1 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "5c26a5a2-6cbb-41fb-883f-1395e42eeaad",
                    "id_by_user": 1,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": "×>",
                            "cross_width": "10"
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "rsi",
                            "params": {
                                "applied_price": "PRICE_CLOSE",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "period": "14"
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "rsi",
                            "params": {
                                "applied_price": "PRICE_CLOSE",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "period": "9"
                            }
                        }
                    }
                },
                {
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Pips",
                            "params": {
                                "value": "variable_test",
                                "pips_mode": "VALUE_PIPS_AS_PRICE_FRACTION"
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "fast_ema_period": 29,
                                "slow_ema_period": 26,
                                "signal_period": "constant_test",
                                "applied_price": "PRICE_LOW",
                                "mode": "MODE_MAIN",
                                "shift": "0",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2"
                            }
                        }
                    },
                    "id": "db3f351a-4e4f-4523-b83e-dc4fcc22e0b7",
                    "id_by_user": 2,
                    "blockName": "condition"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Candle",
                            "row2": "Candle",
                            "params": {
                                "price_mode": "CANDLE_HIGH",
                                "find_method": "FIND_BY_ID",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "shift": "constant_test"
                            }
                        },
                        "right": {
                            "row1": "Candle",
                            "row2": "Candle",
                            "params": {
                                "price_mode": "CANDLE_HIGH",
                                "find_method": "FIND_BY_DATE",
                                "symbol": "NULL",
                                "timeframe": "PERIOD_M2",
                                "time_str": "00:00"
                            }
                        }
                    },
                    "id": "1b982a17-5966-46a1-9151-66a8290ad9b9",
                    "id_by_user": 3,
                    "blockName": "condition"
                },
                {
                    "id": "96227086-b92e-426e-8beb-1b9278cff405",
                    "id_by_user": 4,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Market Properties",
                            "row2": "HIGHEST_PRICE_TIME_PERIOD",
                            "params": {
                                "what_to_get": "GET_CANDLE_ID",
                                "timestr_start": "1:00",
                                "timestr_end": "8:00",
                                "day_offset": "0",
                                "time_mode": "TIME_SERVER"
                            }
                        },
                        "right": {
                            "row1": "Market Properties",
                            "row2": "HIGHEST_PRICE_CANDLE_PERIOD",
                            "params": {
                                "range_start": "0",
                                "range_end": "10",
                                "what_to_get": "GET_CANDLE_ID"
                            }
                        }
                    }
                },
                {
                    "id": "7a7e4caa-a998-417c-a303-249fe016508a",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": "=="
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_TIME_VALUE",
                                "mode_time_shift": "-1",
                                "time_value": "NULL"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Color",
                            "params": {
                                "value": "clrRed"
                            }
                        }
                    }
                },
                {
                    "id": "3136f9d8-f83b-41b0-bf57-553de1ce95c7",
                    "id_by_user": 6,
                    "blockName": "Buy now",
                    "params": {
                        "group": 1,
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
                        "volume_upper_limit": "10",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "takeprofit": 50,
                        "how_much_volume": "3"
                    }
                },
                {
                    "id": "4fe8330a-cf36-4d81-b152-deb89527938c",
                    "id_by_user": 7,
                    "blockName": "Buy now",
                    "params": {
                        "group": 1,
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "volume_upper_limit": "10",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "look_up_on": "LOOK_UP_HISTORY_ONLY",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "0",
                        "martingale_reset_on_n_profits": "1",
                        "stoploss": "2",
                        "takeprofit": "1"
                    }
                }
            ],
            "edges": [
                {
                    "source": "5c26a5a2-6cbb-41fb-883f-1395e42eeaad",
                    "sourceHandle": "blue",
                    "target": "db3f351a-4e4f-4523-b83e-dc4fcc22e0b7",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5c26a5a2-6cbb-41fb-883f-1395e42eeaadblue-db3f351a-4e4f-4523-b83e-dc4fcc22e0b7c"
                },
                {
                    "source": "db3f351a-4e4f-4523-b83e-dc4fcc22e0b7",
                    "sourceHandle": "blue",
                    "target": "1b982a17-5966-46a1-9151-66a8290ad9b9",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-db3f351a-4e4f-4523-b83e-dc4fcc22e0b7blue-1b982a17-5966-46a1-9151-66a8290ad9b9c"
                },
                {
                    "source": "1b982a17-5966-46a1-9151-66a8290ad9b9",
                    "sourceHandle": "blue",
                    "target": "96227086-b92e-426e-8beb-1b9278cff405",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-1b982a17-5966-46a1-9151-66a8290ad9b9blue-96227086-b92e-426e-8beb-1b9278cff405c"
                },
                {
                    "source": "96227086-b92e-426e-8beb-1b9278cff405",
                    "sourceHandle": "blue",
                    "target": "7a7e4caa-a998-417c-a303-249fe016508a",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-96227086-b92e-426e-8beb-1b9278cff405blue-7a7e4caa-a998-417c-a303-249fe016508ac"
                },
                {
                    "source": "7a7e4caa-a998-417c-a303-249fe016508a",
                    "sourceHandle": "blue",
                    "target": "3136f9d8-f83b-41b0-bf57-553de1ce95c7",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-7a7e4caa-a998-417c-a303-249fe016508ablue-3136f9d8-f83b-41b0-bf57-553de1ce95c7c"
                },
                {
                    "source": "7a7e4caa-a998-417c-a303-249fe016508a",
                    "sourceHandle": "red",
                    "target": "4fe8330a-cf36-4d81-b152-deb89527938c",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-7a7e4caa-a998-417c-a303-249fe016508ared-4fe8330a-cf36-4d81-b152-deb89527938cc"
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
            "name": "variable_test",
            "value": "2",
            "description": "variable test"
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "constant_test",
            "value": "1",
            "description": "constant test"
        }
    ]
}

# test different kinds of value by front
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
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "1"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Boolean",
                            "params": {
                                "value": "true"
                            }
                        }
                    },
                    "id": "fe06f1fe-2f67-45ce-9aee-152bd554fd79",
                    "id_by_user": 1,
                    "blockName": "condition"
                },
                {
                    "id": "b62f89da-d03e-47e9-80d3-2a3e07b06a5f",
                    "id_by_user": 2,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": "=>"
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Color",
                            "params": {
                                "value": "clrDarkGreen"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Pips",
                            "params": {
                                "value": "10",
                                "pips_mode": "VALUE_PIPS_AS_IS"
                            }
                        }
                    }
                },
                {
                    "id": "516b0d19-4c10-45af-af4b-4cbcafc6566f",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Pips",
                            "params": {
                                "value": "10",
                                "pips_mode": "VALUE_PIPS_AS_PRICE_FRACTION"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_NOW",
                                "mode_time_shift": "-1",
                                "time_source": "TIME_LOCAL"
                            }
                        }
                    }
                },
                {
                    "id": "95d95056-2df6-4297-b21c-1c8580590dd1",
                    "id_by_user": 4,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_TIMESTAMP",
                                "mode_time_shift": "0",
                                "MODE_TIME_TIMESTAMP": "13:43",
                                "time_shift_years": "1",
                                "time_shift_months": "2",
                                "time_shift_weeks": "3",
                                "time_shift_days": "4"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_COMPONENTS",
                                "mode_time_shift": "1",
                                "time_source": "TIME_LOCAL",
                                "time_component_year": "1",
                                "time_component_month": "2",
                                "time_component_day": "3",
                                "time_component_hour": "4",
                                "time_component_minute": "6",
                                "time_component_second": "7",
                                "time_shift_years": "9",
                                "time_shift_months": "9",
                                "time_shift_weeks": "9",
                                "time_shift_days": "9"
                            }
                        }
                    }
                },
                {
                    "id": "0c644a16-3325-4551-a69c-b0458ed29213",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": ">"
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_CANDLE_TIME",
                                "mode_time_shift": "-1",
                                "time_candle_id": "1",
                                "time_market": "2",
                                "time_candle_timeframe": "PERIOD_M2"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Time",
                            "params": {
                                "mode_time": "MODE_TIME_TIME_VALUE",
                                "mode_time_shift": "-1",
                                "time_value": "123"
                            }
                        }
                    }
                },
                {
                    "id": "4d127d24-e561-4240-a1f9-d7f625fe6fbc",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "operator": {
                            "label": "=="
                        },
                        "left": {
                            "row1": "Value",
                            "row2": "Text",
                            "params": {
                                "text": "testiing Text"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Text(code input)",
                            "params": {
                                "value": "Testing code input"
                            }
                        }
                    }
                }
            ],
            "edges": []
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

# test mouse clicked on object
input_data_3 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "check_profit_unrealized",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": [0, 1],
                        "profit_mode": "PROFIT_MODE_MONEY",
                        "profit_benchmark_filter": 0,
                        "profit_benchmark_comparison": 100,
                        "profit_filter_operator": "==",
                        "profit_comparison_operator": "<="
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": [1, 2],
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
        "on_chart": {
            "nodes": [
                {
                    "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "id_by_user": 2,
                    "blockName": "mouse_clicked_on_object",
                    "params": {
                        "name_filter_mode": "names",
                        "obj_name": "test_name_obj_xx, test_name_obj_xxx"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "RSI",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "period": "10",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "10",
                                "buy_threshold": 70,
                                "sell_threshold": 30
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "type": "VALUE_TYPE_TIME",
                                "value": 25.1,
                                "adjust": "",
                                "pips_mode": "VALUE_PIPS_AS_IS",
                                "symbol": "NULL",

                                "mode_time": 0,
                                "time_source": 0,
                                "time_stamp": "00:00",
                                "time_candle_id": 1,
                                "time_market": "",
                                "time_candle_timeframe": 0,
                                "time_component_year": 0,
                                "time_component_month": 0,
                                "time_component_day": 0,
                                "time_component_hour": 12,
                                "time_component_minute": 0,
                                "time_component_second": 0,
                                "time_value": 0,
                                "mode_time_shift": 0,
                                "time_shift_years": 0,
                                "time_shift_months": 0,
                                "time_shift_weeks": 0,
                                "time_shift_days": 0,
                                "time_shift_hours": 0,
                                "time_shift_minutes": 0,
                                "time_shift_seconds": 0,
                                "time_skip_weekdays": False
                            },
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "id_by_user": 4,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×<",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "id_by_user": 7,
                    "blockName": "Sell now",
                    "params": {
                        "symbol": "NULL",
                        "group": 11,
                        "order_type": "ORDER_BUY_PENDING",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "how_much_volume": 35,
                        "volume_upper_limit": 10,
                        "open_at_price": {
                            "value": "OPEN_AT_CUSTOM_PRICE",
                            "price_to_open_dynamic_level": {
                                "row1": "Indicator",
                                "row2": "RSI",
                                "params": {
                                    "symbol": "NULL",
                                    "timeframe": 0,
                                    "period": "10",
                                    "applied_price": "PRICE_CLOSE",
                                    "shift": "10",
                                    "buy_threshold": 70,
                                    "sell_threshold": 30
                                }
                            }
                        },
                        "price_offset": 10,
                        "price_offset_as_pip": True,
                        "slippage": 4,
                        "stoploss": 20,
                        "takeprofit": 20,
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "comment": "",
                        "expiration": 0,
                        "arrow_color": "clrYellow",
                        "look_up_on": "LOOK_UP_RUNNING_ONLY",
                        "type": [0, 1],
                        "martingale_init_vol": 0.1,
                        "martingale_multiply_on_loss": 0,
                        "martingale_multiply_on_profit": 0,
                        "martingale_addlots_on_loss": 0.1,
                        "martingale_addlots_on_profit": 0.1,
                        "martingale_reset_on_n_losses": 5,
                        "martingale_reset_on_n_profits": 5
                    }
                },
                {
                    "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "id_by_user": 8,
                    "blockName": "pass",
                    "params": {

                    }
                }
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

# test object dragged
input_data_4 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "check_profit_unrealized",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": [0, 1],
                        "profit_mode": "PROFIT_MODE_MONEY",
                        "profit_benchmark_filter": 0,
                        "profit_benchmark_comparison": 100,
                        "profit_filter_operator": "==",
                        "profit_comparison_operator": "<="
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": [1, 2],
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
        "on_chart": {
            "nodes": [
                {
                    "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "id_by_user": 2,
                    "blockName": "object_dragged",
                    "params": {
                        "name_filter_mode": "names",
                        "obj_name": "test_name_obj_yy, test_name_obj_zz"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "RSI",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "period": "10",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "10",
                                "buy_threshold": 70,
                                "sell_threshold": 30
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "type": "VALUE_TYPE_TIME",
                                "value": 25.1,
                                "adjust": "",
                                "pips_mode": "VALUE_PIPS_AS_IS",
                                "symbol": "NULL",

                                "mode_time": 0,
                                "time_source": 0,
                                "time_stamp": "00:00",
                                "time_candle_id": 1,
                                "time_market": "",
                                "time_candle_timeframe": 0,
                                "time_component_year": 0,
                                "time_component_month": 0,
                                "time_component_day": 0,
                                "time_component_hour": 12,
                                "time_component_minute": 0,
                                "time_component_second": 0,
                                "time_value": 0,
                                "mode_time_shift": 0,
                                "time_shift_years": 0,
                                "time_shift_months": 0,
                                "time_shift_weeks": 0,
                                "time_shift_days": 0,
                                "time_shift_hours": 0,
                                "time_shift_minutes": 0,
                                "time_shift_seconds": 0,
                                "time_skip_weekdays": False
                            },
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "id_by_user": 4,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×<",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "id_by_user": 7,
                    "blockName": "Sell now",
                    "params": {
                        "symbol": "NULL",
                        "group": 11,
                        "order_type": "ORDER_BUY_PENDING",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "how_much_volume": 35,
                        "volume_upper_limit": 10,
                        "open_at_price": {
                            "value": "OPEN_AT_CUSTOM_PRICE",
                            "price_to_open_dynamic_level": {
                                "row1": "Indicator",
                                "row2": "RSI",
                                "params": {
                                    "symbol": "NULL",
                                    "timeframe": 0,
                                    "period": "10",
                                    "applied_price": "PRICE_CLOSE",
                                    "shift": "10",
                                    "buy_threshold": 70,
                                    "sell_threshold": 30
                                }
                            }
                        },
                        "price_offset": 10,
                        "price_offset_as_pip": True,
                        "slippage": 4,
                        "stoploss": 20,
                        "takeprofit": 20,
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "comment": "",
                        "expiration": 0,
                        "arrow_color": "clrYellow",
                        "look_up_on": "LOOK_UP_RUNNING_ONLY",
                        "type": [0, 1],
                        "martingale_init_vol": 0.1,
                        "martingale_multiply_on_loss": 0,
                        "martingale_multiply_on_profit": 0,
                        "martingale_addlots_on_loss": 0.1,
                        "martingale_addlots_on_profit": 0.1,
                        "martingale_reset_on_n_losses": 5,
                        "martingale_reset_on_n_profits": 5
                    }
                },
                {
                    "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "id_by_user": 8,
                    "blockName": "pass",
                    "params": {

                    }
                }
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

# test order deleted
input_data_5 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "order_deleted",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": [0, 1],
                        "close_mode": "",
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": [1, 2],
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
        "on_chart": {
            "nodes": [
                {
                    "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "id_by_user": 2,
                    "blockName": "object_dragged",
                    "params": {
                        "name_filter_mode": "names",
                        "obj_name": "test_name_obj_yy, test_name_obj_zz"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "RSI",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "period": "10",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "10",
                                "buy_threshold": 70,
                                "sell_threshold": 30
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "type": "VALUE_TYPE_TIME",
                                "value": 25.1,
                                "adjust": "",
                                "pips_mode": "VALUE_PIPS_AS_IS",
                                "symbol": "NULL",

                                "mode_time": 0,
                                "time_source": 0,
                                "time_stamp": "00:00",
                                "time_candle_id": 1,
                                "time_market": "",
                                "time_candle_timeframe": 0,
                                "time_component_year": 0,
                                "time_component_month": 0,
                                "time_component_day": 0,
                                "time_component_hour": 12,
                                "time_component_minute": 0,
                                "time_component_second": 0,
                                "time_value": 0,
                                "mode_time_shift": 0,
                                "time_shift_years": 0,
                                "time_shift_months": 0,
                                "time_shift_weeks": 0,
                                "time_shift_days": 0,
                                "time_shift_hours": 0,
                                "time_shift_minutes": 0,
                                "time_shift_seconds": 0,
                                "time_skip_weekdays": False
                            },
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "id_by_user": 4,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×<",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "id_by_user": 7,
                    "blockName": "Sell now",
                    "params": {
                        "symbol": "NULL",
                        "group": 11,
                        "order_type": "ORDER_BUY_PENDING",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "how_much_volume": 35,
                        "volume_upper_limit": 10,
                        "open_at_price": {
                            "value": "OPEN_AT_CUSTOM_PRICE",
                            "price_to_open_dynamic_level": {
                                "row1": "Indicator",
                                "row2": "RSI",
                                "params": {
                                    "symbol": "NULL",
                                    "timeframe": 0,
                                    "period": "10",
                                    "applied_price": "PRICE_CLOSE",
                                    "shift": "10",
                                    "buy_threshold": 70,
                                    "sell_threshold": 30
                                }
                            }
                        },
                        "price_offset": 10,
                        "price_offset_as_pip": True,
                        "slippage": 4,
                        "stoploss": 20,
                        "takeprofit": 20,
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "comment": "",
                        "expiration": 0,
                        "arrow_color": "clrYellow",
                        "look_up_on": "LOOK_UP_RUNNING_ONLY",
                        "type": [0, 1],
                        "martingale_init_vol": 0.1,
                        "martingale_multiply_on_loss": 0,
                        "martingale_multiply_on_profit": 0,
                        "martingale_addlots_on_loss": 0.1,
                        "martingale_addlots_on_profit": 0.1,
                        "martingale_reset_on_n_losses": 5,
                        "martingale_reset_on_n_profits": 5
                    }
                },
                {
                    "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "id_by_user": 8,
                    "blockName": "pass",
                    "params": {

                    }
                }
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

# test once per bar and sell buy by front
input_data_6 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "14e307ec-0bb1-45c5-8eac-10ca8630c149",
                    "id_by_user": 8,
                    "blockName": "Once per bar",
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_M1"
                    }
                },
                {
                    "id": "71c814ef-49fb-4272-8b21-b60dea986a32",
                    "id_by_user": 9,
                    "blockName": "Buy now",
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
                        "how_much_volume": "100",
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
                    }
                }
            ],
            "edges": [
                {
                    "source": "14e307ec-0bb1-45c5-8eac-10ca8630c149",
                    "sourceHandle": "blue",
                    "target": "71c814ef-49fb-4272-8b21-b60dea986a32",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-14e307ec-0bb1-45c5-8eac-10ca8630c149blue-71c814ef-49fb-4272-8b21-b60dea986a32c"
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
            "name": "variable_test_",
            "value": "55",
            "description": "asd"
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "constant_test_",
            "value": "12",
            "description": "test"
        }
    ]
}

# test once per bar and sell buy + consts vars placed as values by front
input_data_7 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "7124eefb-6f99-41f9-abc7-7616c20e2b3f",
                    "id_by_user": 1,
                    "blockName": "Once per bar",
                    "params": {
                        "symbol": "",
                        "max_time": "1",
                        "timeframe": "PERIOD_M1"
                    }
                },
                {
                    "id": "9f71f89f-a61e-43fa-b666-8a0664c1d53a",
                    "id_by_user": 3,
                    "blockName": "Buy now",
                    "params": {
                        "group": "0",
                        "symbol": "cosnt_2_",
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "ExpMode": "None",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "var_2_",
                        "how_much_volume": "test_var",
                        "volume_upper_limit": "const_1_",
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
                    }
                },
                {
                    "id": "0fe95f32-725f-4e96-aeba-a6e81847d9a9",
                    "id_by_user": 2,
                    "blockName": "Sell now",
                    "params": {
                        "group": "0",
                        "symbol": "NULL",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "ExpMode": "specified",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "slippage": "test_var",
                        "arrow_color": "clrBlue",
                        "comment": "Short trade",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "1",
                        "martingale_reset_on_n_profits": "1",
                        "look_up_on": "LOOK_UP_HISTORY_ONLY",
                        "stoploss": "50",
                        "takeprofit": "50",
                        "ExpDays": "0",
                        "ExpHours": "const_1_",
                        "ExpMinutes": "cosnt_2_"
                    }
                }
            ],
            "edges": [
                {
                    "source": "7124eefb-6f99-41f9-abc7-7616c20e2b3f",
                    "sourceHandle": "blue",
                    "target": "0fe95f32-725f-4e96-aeba-a6e81847d9a9",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-7124eefb-6f99-41f9-abc7-7616c20e2b3fblue-0fe95f32-725f-4e96-aeba-a6e81847d9a9c"
                },
                {
                    "source": "7124eefb-6f99-41f9-abc7-7616c20e2b3f",
                    "sourceHandle": "red",
                    "target": "9f71f89f-a61e-43fa-b666-8a0664c1d53a",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-7124eefb-6f99-41f9-abc7-7616c20e2b3fred-9f71f89f-a61e-43fa-b666-8a0664c1d53ac"
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
            "name": "test_var",
            "value": "123",
            "description": "123"
        },
        {
            "type": "double",
            "name": "var_2_",
            "value": "asd",
            "description": "asf"
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "const_1_",
            "value": "123",
            "description": "123"
        },
        {
            "type": "double",
            "name": "cosnt_2_",
            "value": "sad",
            "description": "sad"
        }
    ]
}

# test trade closed
input_data_8 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_chart": {
            "nodes": [
                {
                    "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "id_by_user": 2,
                    "blockName": "object_dragged",
                    "params": {
                        "name_filter_mode": "names",
                        "obj_name": "test_name_obj_yy, test_name_obj_zz"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "RSI",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "period": "10",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "10",
                                "buy_threshold": 70,
                                "sell_threshold": 30
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "type": "VALUE_TYPE_TIME",
                                "value": 25.1,
                                "adjust": "",
                                "pips_mode": "VALUE_PIPS_AS_IS",
                                "symbol": "NULL",

                                "mode_time": 0,
                                "time_source": 0,
                                "time_stamp": "00:00",
                                "time_candle_id": 1,
                                "time_market": "",
                                "time_candle_timeframe": 0,
                                "time_component_year": 0,
                                "time_component_month": 0,
                                "time_component_day": 0,
                                "time_component_hour": 12,
                                "time_component_minute": 0,
                                "time_component_second": 0,
                                "time_value": 0,
                                "mode_time_shift": 0,
                                "time_shift_years": 0,
                                "time_shift_months": 0,
                                "time_shift_weeks": 0,
                                "time_shift_days": 0,
                                "time_shift_hours": 0,
                                "time_shift_minutes": 0,
                                "time_shift_seconds": 0,
                                "time_skip_weekdays": False
                            },
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "id_by_user": 4,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×<",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "id_by_user": 7,
                    "blockName": "Sell now",
                    "params": {
                        "symbol": "NULL",
                        "group": 11,
                        "order_type": "ORDER_BUY_PENDING",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "how_much_volume": 35,
                        "volume_upper_limit": 10,
                        "open_at_price": {
                            "value": "OPEN_AT_CUSTOM_PRICE",
                            "price_to_open_dynamic_level": {
                                "row1": "Indicator",
                                "row2": "RSI",
                                "params": {
                                    "symbol": "NULL",
                                    "timeframe": 0,
                                    "period": "10",
                                    "applied_price": "PRICE_CLOSE",
                                    "shift": "10",
                                    "buy_threshold": 70,
                                    "sell_threshold": 30
                                }
                            }
                        },
                        "price_offset": 10,
                        "price_offset_as_pip": True,
                        "slippage": 4,
                        "stoploss": 20,
                        "takeprofit": 20,
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "comment": "",
                        "expiration": 0,
                        "arrow_color": "clrYellow",
                        "look_up_on": "LOOK_UP_RUNNING_ONLY",
                        "type": [0, 1],
                        "martingale_init_vol": 0.1,
                        "martingale_multiply_on_loss": 0,
                        "martingale_multiply_on_profit": 0,
                        "martingale_addlots_on_loss": 0.1,
                        "martingale_addlots_on_profit": 0.1,
                        "martingale_reset_on_n_losses": 5,
                        "martingale_reset_on_n_profits": 5
                    }
                },
                {
                    "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "id_by_user": 8,
                    "blockName": "pass",
                    "params": {

                    }
                }
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
                    "blockName": "trade_closed",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": [0, 1],
                        "close_mode": "",
                        "close_partial_mode": 2
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": [1, 2],
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

# test order created
input_data_9 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_chart": {
            "nodes": [
                {
                    "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "id_by_user": 2,
                    "blockName": "object_dragged",
                    "params": {
                        "name_filter_mode": "names",
                        "obj_name": "test_name_obj_yy, test_name_obj_zz"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "RSI",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "period": "10",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "10",
                                "buy_threshold": 70,
                                "sell_threshold": 30
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "type": "VALUE_TYPE_TIME",
                                "value": 25.1,
                                "adjust": "",
                                "pips_mode": "VALUE_PIPS_AS_IS",
                                "symbol": "NULL",

                                "mode_time": 0,
                                "time_source": 0,
                                "time_stamp": "00:00",
                                "time_candle_id": 1,
                                "time_market": "",
                                "time_candle_timeframe": 0,
                                "time_component_year": 0,
                                "time_component_month": 0,
                                "time_component_day": 0,
                                "time_component_hour": 12,
                                "time_component_minute": 0,
                                "time_component_second": 0,
                                "time_value": 0,
                                "mode_time_shift": 0,
                                "time_shift_years": 0,
                                "time_shift_months": 0,
                                "time_shift_weeks": 0,
                                "time_shift_days": 0,
                                "time_shift_hours": 0,
                                "time_shift_minutes": 0,
                                "time_shift_seconds": 0,
                                "time_skip_weekdays": False
                            },
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "id_by_user": 4,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×<",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "id_by_user": 7,
                    "blockName": "Sell now",
                    "params": {
                        "symbol": "NULL",
                        "group": 11,
                        "order_type": "ORDER_BUY_PENDING",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "how_much_volume": 35,
                        "volume_upper_limit": 10,
                        "open_at_price": {
                            "value": "OPEN_AT_CUSTOM_PRICE",
                            "price_to_open_dynamic_level": {
                                "row1": "Indicator",
                                "row2": "RSI",
                                "params": {
                                    "symbol": "NULL",
                                    "timeframe": 0,
                                    "period": "10",
                                    "applied_price": "PRICE_CLOSE",
                                    "shift": "10",
                                    "buy_threshold": 70,
                                    "sell_threshold": 30
                                }
                            }
                        },
                        "price_offset": 10,
                        "price_offset_as_pip": True,
                        "slippage": 4,
                        "stoploss": 20,
                        "takeprofit": 20,
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "comment": "",
                        "expiration": 0,
                        "arrow_color": "clrYellow",
                        "look_up_on": "LOOK_UP_RUNNING_ONLY",
                        "type": [0, 1],
                        "martingale_init_vol": 0.1,
                        "martingale_multiply_on_loss": 0,
                        "martingale_multiply_on_profit": 0,
                        "martingale_addlots_on_loss": 0.1,
                        "martingale_addlots_on_profit": 0.1,
                        "martingale_reset_on_n_losses": 5,
                        "martingale_reset_on_n_profits": 5
                    }
                },
                {
                    "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "id_by_user": 8,
                    "blockName": "pass",
                    "params": {

                    }
                }
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
                    "blockName": "order_created",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": [2, 3],
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": [1, 2],
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

# test formula by front
input_data_10 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "left": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "3"
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "value": "4"
                            }
                        },
                        "operator": {
                            "label": "×"
                        },
                        "adjust": "3",
                        "variable": "variable_test_"
                    },
                    "id": "a33fde25-57b2-4c49-b180-6fb0a6939eef",
                    "id_by_user": 1,
                    "blockName": "formula"
                }
            ],
            "edges": []
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
            "name": "variable_test_",
            "value": "12",
            "description": "test"
        }
    ],
    "constants": []
}

# test trade created
input_data_11 = {
    "events": {
        "on_tick": {
            "nodes": [

            ],
            "edges": [

            ]
        },
        "on_chart": {
            "nodes": [
                {
                    "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "id_by_user": 2,
                    "blockName": "object_dragged",
                    "params": {
                        "name_filter_mode": "names",
                        "obj_name": "test_name_obj_yy, test_name_obj_zz"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 3,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "RSI",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "period": "10",
                                "applied_price": "PRICE_CLOSE",
                                "shift": "10",
                                "buy_threshold": 70,
                                "sell_threshold": 30
                            }
                        },
                        "right": {
                            "row1": "Value",
                            "row2": "Numeric",
                            "params": {
                                "type": "VALUE_TYPE_TIME",
                                "value": 25.1,
                                "adjust": "",
                                "pips_mode": "VALUE_PIPS_AS_IS",
                                "symbol": "NULL",

                                "mode_time": 0,
                                "time_source": 0,
                                "time_stamp": "00:00",
                                "time_candle_id": 1,
                                "time_market": "",
                                "time_candle_timeframe": 0,
                                "time_component_year": 0,
                                "time_component_month": 0,
                                "time_component_day": 0,
                                "time_component_hour": 12,
                                "time_component_minute": 0,
                                "time_component_second": 0,
                                "time_value": 0,
                                "mode_time_shift": 0,
                                "time_shift_years": 0,
                                "time_shift_months": 0,
                                "time_shift_weeks": 0,
                                "time_shift_days": 0,
                                "time_shift_hours": 0,
                                "time_shift_minutes": 0,
                                "time_shift_seconds": 0,
                                "time_skip_weekdays": False
                            },
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "id_by_user": 4,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 5,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×>",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "id_by_user": 6,
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_MAIN",
                                "shift": 1
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "Macd",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "signal_period": 12,
                                "slow_ema_period": 29,
                                "fast_ema_period": 9,
                                "applied_price": "PRICE_CLOSE",
                                "mode": "MODE_SIGNAL",
                                "shift": 1
                            }
                        },
                        "operator": {
                            "value": 1,
                            "label": "×<",
                            "cross_width": 10
                        }
                    }
                },
                {
                    "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "id_by_user": 7,
                    "blockName": "Sell now",
                    "params": {
                        "symbol": "NULL",
                        "group": 11,
                        "order_type": "ORDER_BUY_PENDING",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "how_much_volume": 35,
                        "volume_upper_limit": 10,
                        "open_at_price": {
                            "value": "OPEN_AT_CUSTOM_PRICE",
                            "price_to_open_dynamic_level": {
                                "row1": "Indicator",
                                "row2": "RSI",
                                "params": {
                                    "symbol": "NULL",
                                    "timeframe": 0,
                                    "period": "10",
                                    "applied_price": "PRICE_CLOSE",
                                    "shift": "10",
                                    "buy_threshold": 70,
                                    "sell_threshold": 30
                                }
                            }
                        },
                        "price_offset": 10,
                        "price_offset_as_pip": True,
                        "slippage": 4,
                        "stoploss": 20,
                        "takeprofit": 20,
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "comment": "",
                        "expiration": 0,
                        "arrow_color": "clrYellow",
                        "look_up_on": "LOOK_UP_RUNNING_ONLY",
                        "type": [0, 1],
                        "martingale_init_vol": 0.1,
                        "martingale_multiply_on_loss": 0,
                        "martingale_multiply_on_profit": 0,
                        "martingale_addlots_on_loss": 0.1,
                        "martingale_addlots_on_profit": 0.1,
                        "martingale_reset_on_n_losses": 5,
                        "martingale_reset_on_n_profits": 5
                    }
                },
                {
                    "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "id_by_user": 8,
                    "blockName": "pass",
                    "params": {

                    }
                }
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
                        "type": [1, 2],
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": [1, 2],
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

# test filter data change (either buy or sell as string like "{0,1}")
input_data_12 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "14e307ec-0bb1-45c5-8eac-10ca8630c149",
                    "id_by_user": 8,
                    "blockName": "If trade",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 25,
                        "type": "{1, 2}",
                        "count_limit": 0,
                        "operator": ">"
                    }
                },
                {
                    "id": "71c814ef-49fb-4272-8b21-b60dea986a32",
                    "id_by_user": 9,
                    "blockName": "Buy now",
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
                        "how_much_volume": "100",
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
                    }
                }
            ],
            "edges": [
                {
                    "source": "14e307ec-0bb1-45c5-8eac-10ca8630c149",
                    "sourceHandle": "blue",
                    "target": "71c814ef-49fb-4272-8b21-b60dea986a32",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-14e307ec-0bb1-45c5-8eac-10ca8630c149blue-71c814ef-49fb-4272-8b21-b60dea986a32c"
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
            "name": "variable_test_",
            "value": "55",
            "description": "asd"
        }
    ],
    "constants": [
        {
            "type": "double",
            "name": "constant_test_",
            "value": "12",
            "description": "test"
        }
    ]
}

# test if trade by front
input_data_13 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "5569520f-852b-470d-b1e6-aebfedd1ceec",
                    "id_by_user": 3,
                    "blockName": "If trade",
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_NUMBER",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{0}",
                        "group_number": "11",
                        "symbols_str": ""
                    }
                },
                {
                    "id": "eb013875-b664-46cd-b932-f2dbde72ee79",
                    "id_by_user": 4,
                    "blockName": "If trade",
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_MANUAL",
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "type": "{1}",
                        "symbols_str": "XAU"
                    }
                },
                {
                    "id": "c970e08e-de1b-4dd8-a4da-39ac4f67b08a",
                    "id_by_user": 5,
                    "blockName": "If trade",
                    "params": {
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "symbol_mode": "SYMBOL_MODE_ANY",
                        "type": "{1}",
                        "symbols_str": ""
                    }
                }
            ],
            "edges": [
                {
                    "source": "5569520f-852b-470d-b1e6-aebfedd1ceec",
                    "sourceHandle": "blue",
                    "target": "c970e08e-de1b-4dd8-a4da-39ac4f67b08a",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5569520f-852b-470d-b1e6-aebfedd1ceecblue-c970e08e-de1b-4dd8-a4da-39ac4f67b08ac"
                },
                {
                    "source": "5569520f-852b-470d-b1e6-aebfedd1ceec",
                    "sourceHandle": "red",
                    "target": "eb013875-b664-46cd-b932-f2dbde72ee79",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-5569520f-852b-470d-b1e6-aebfedd1ceecred-eb013875-b664-46cd-b932-f2dbde72ee79c"
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

# test pending order by front
input_data_14 = {
    "events": {
        "on_tick": {
            "nodes": [
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
                    "id": "0cdd234e-34df-4385-88e6-5779f3585866",
                    "id_by_user": 1,
                    "blockName": "Buy pending order"
                },
                {
                    "params": {
                        "group": "0",
                        "symbol": "XAU",
                        "price_offset": "2",
                        "open_at_price": "OPEN_AT_MID",
                        "volume_upper_limit": "9",
                        "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "ExpMode": "today",
                        "oco": "oco1",
                        "slippage": "4",
                        "arrow_color": "clrBlue",
                        "comment": "Short trade",
                        "stoploss": "13",
                        "takeprofit": "13",
                        "how_much_volume": "67"
                    },
                    "id": "4e82a131-d802-4c94-9f56-33daf3d09069",
                    "id_by_user": 2,
                    "blockName": "Sell pending order"
                },
                {
                    "params": {
                        "group": "const_double",
                        "symbol": "const_string",
                        "price_offset": "variable_double",
                        "open_at_price": "OPEN_AT_ASK",
                        "volume_upper_limit": "3",
                        "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                        "stop_loss_mode": "TPSL_MODE_NO_SL",
                        "take_profit_mode": "TPSL_MODE_NO_TP",
                        "oco": "oco2",
                        "slippage": "4",
                        "arrow_color": "clrRed",
                        "comment": "variable_string",
                        "martingale_multiply_on_profit": "1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "1",
                        "martingale_reset_on_n_profits": "1",
                        "stoploss": "20",
                        "takeprofit": "20",
                        "ExpDays": "1",
                        "ExpHours": "variable_double",
                        "ExpMinutes": "const_double",
                        "ExpMode": "specified"
                    },
                    "id": "eb6c21da-b8f7-4e53-9221-420d69170d28",
                    "id_by_user": 3,
                    "blockName": "Buy pending order"
                }
            ],
            "edges": [
                {
                    "source": "0cdd234e-34df-4385-88e6-5779f3585866",
                    "sourceHandle": "blue",
                    "target": "4e82a131-d802-4c94-9f56-33daf3d09069",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-0cdd234e-34df-4385-88e6-5779f3585866blue-4e82a131-d802-4c94-9f56-33daf3d09069c"
                },
                {
                    "source": "4e82a131-d802-4c94-9f56-33daf3d09069",
                    "sourceHandle": "blue",
                    "target": "eb6c21da-b8f7-4e53-9221-420d69170d28",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-4e82a131-d802-4c94-9f56-33daf3d09069blue-eb6c21da-b8f7-4e53-9221-420d69170d28c"
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
            "type": "string",
            "name": "variable_string",
            "value": "test",
            "description": "string"
        },
        {
            "type": "double",
            "name": "variable_double",
            "value": "12",
            "description": "double"
        }
    ],
    "constants": [
        {
            "type": "string",
            "name": "const_string",
            "value": "test const ",
            "description": "string"
        },
        {
            "type": "double",
            "name": "const_double",
            "value": "13",
            "description": "double"
        }
    ]
}
