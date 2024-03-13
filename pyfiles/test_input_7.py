# This script represents data input using new structure + support for all the events

# Test on tick + on chart event infrastructure
input_data_1 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 26,
                    "blockName": "pass",
                    "params": {

                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 30,
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
                                "time_stamp": "\"00:00\"",
                                "time_candle_id": 1,
                                "time_market": "\"\"",
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
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Market Properties",
                            "row2": "Market Properties",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "find_method": "CANDLE_PERIOD",
                                "price_mode": "LOWEST_PRICE",
                                "what_to_get": "GET_PRICE",
                                "timestr_start": "\"2023.11.23 7:30:30\"",
                                "timestr_end": "\"2023.11.23 21:30:30\"",
                                "day_offset": 0,
                                "range_start": 50,
                                "range_end": 100,
                                "adjust": "/      my_var   pips"
                            }
                        },
                        "right": {
                            "row1": "Candle",
                            "row2": "Candle",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": "0",
                                "find_method": "FIND_BY_ID",
                                "price_mode": "CANDLE_HIGH",
                                "timestr": "\"2023.4.26 13:40:30\"",
                                "shift": 5,
                                "adjust": "58pips"
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
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 1,
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
                                "time_stamp": "\"00:00\"",
                                "time_candle_id": 1,
                                "time_market": "\"\"",
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
                    "id_by_user": 20,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 51,
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
                    "id_by_user": 61,
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
                    "id_by_user": 53,
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
                        "comment": "\"\"",
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
                    "id_by_user": 50,
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
            "value": "\"test value\"",
            "description": ""
        }
    ]
}

# test profit unrealized
input_data_2 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 26,
                    "blockName": "check_profit_unrealized",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": "\",EURUSD,GBPUSD\"",
                        "group_mode": "ORDER_GROUP_MODE_NONE",
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
                    "id_by_user": 30,
                    "blockName": "check_trades_orders_count",
                    "params": {
                        "symbol_mode":  "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": "\",EURUSD,GBPUSD\"",
                        "group_mode": "ORDER_GROUP_MODE_NONE",
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
                    "blockName": "condition",
                    "params": {
                        "left": {
                            "row1": "Market Properties",
                            "row2": "Market Properties",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": 0,
                                "find_method": "CANDLE_PERIOD",
                                "price_mode": "LOWEST_PRICE",
                                "what_to_get": "GET_PRICE",
                                "timestr_start": "\"2023.11.23 7:30:30\"",
                                "timestr_end": "\"2023.11.23 21:30:30\"",
                                "day_offset": 0,
                                "range_start": 50,
                                "range_end": 100,
                                "adjust": "/      my_var   pips"
                            }
                        },
                        "right": {
                            "row1": "Candle",
                            "row2": "Candle",
                            "params": {
                                "symbol": "NULL",
                                "timeframe": "0",
                                "find_method": "FIND_BY_ID",
                                "price_mode": "CANDLE_HIGH",
                                "timestr": "\"2023.4.26 13:40:30\"",
                                "shift": 5,
                                "adjust": "58pips"
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
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "id_by_user": 1,
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
                                "time_stamp": "\"00:00\"",
                                "time_candle_id": 1,
                                "time_market": "\"\"",
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
                    "id_by_user": 20,
                    "blockName": "delete_objects_by_type",
                    "params": {
                        "window": 0,
                        "type": "OBJ_VLINE"
                    }
                },
                {
                    "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "id_by_user": 51,
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
                    "id_by_user": 61,
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
                    "id_by_user": 53,
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
                        "comment": "\"\"",
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
                    "id_by_user": 50,
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
            "value": "\"test value\"",
            "description": ""
        }
    ]
}
