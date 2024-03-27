# Test 1 moved to test_input_3 > item 28 cuz its data is old.


# Test buy sell new
input_data_2 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "spread_filter"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "spread_mode": {
                    "value": "SPREAD_BENCHMARK_FIX",
                    "checked": False
                },
                "spread_benchmark_fix_value": {
                    "value": 14,
                    "checked": False
                },
                "average_spread_time_period": {
                    "value": 20,
                    "checked": False
                },
                "average_spread_adjust": {
                    "value": 20,
                    "checked": False
                },
                "operator": {
                    "value": "<=",
                    "checked": False
                }

            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_CUSTOM_PRICE",
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 14
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 70
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 30
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 0
                                }
                            }
                        ]
                    }
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test break even
input_data_3 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "break_even"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "value": "ORDER_GROUP_MODE_ALL",
                    "checked": False
                },
                "group_number": {
                    "value": 15,
                    "checked": False
                },
                "type": {
                    "value": [0, 1],
                    "checked": False
                },
                "on_profit_mode": {
                    "value": "ON_PROFIT_MODE_FIXED_VALUE",
                    "checked": False
                },
                "pips_on_profit": {
                    "value": 20,
                    "checked": False
                },
                "bep_offset_mode": {
                    "value": "BEP_OFFSET_MODE_PIPS_OFFSET",
                    "checked": False
                },
                "bep_offset": {
                    "value": 10,
                    "checked": False
                }

            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test trailing stop (each trade) test No 1
input_data_4 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "trailing_stop_each_trade"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "value": "ORDER_GROUP_MODE_ALL",
                    "checked": False
                },
                "group_number": {
                    "value": 15,
                    "checked": False
                },
                "type": {
                    "value": [0, 1],
                    "checked": False
                },

                "TrailWhat": {
                    "value": 1,
                },
                "TrailingReferencePrice": {
                    "value": 0,
                },
                "TrailingStopMode": {
                    "value": "TRAILING_STOP_MODE_PERCENT_OF_OPPOSITE_STOP",
                    "value_fetch_trailing_stop_mode_custom_level": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": "PERIOD_H1"
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 7
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 90
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 10
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 3
                                }
                            }
                        ]
                    }
                },
                "tStopPips": {
                    "value": 40.0,
                },
                "tStopMoney": {
                    "value": 10.0,
                },
                "tStopMultiple": {
                    "value": "\"20/5, 30/10\"",
                },
                "tStopPercentTP": {
                    "value": 100.0,
                },
                "tStopPercentProfit": {
                    "value": 50.0,
                },
                "TrailingStepMode": {
                    "value": "TRAILING_STEP_MODE_PIPS",
                },
                "tStepPips": {
                    "value": 1,
                },
                "tStepPercentTS": {
                    "value": 10.0,
                },
                "TrailingStartMode": {
                    "value": "TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP",
                },
                "tStartPips": {
                    "value": 10.0,
                },
                "tStartPercentTS": {
                    "value": 100.0,
                },
                "tStartPercentSL": {
                    "value": 10.0,
                },
                "tStartPercentTP": {
                    "value": 10.0,
                },
                "TrailingTPmode": {
                    "value": "TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE",
                },
                "tTPpips": {
                    "value": 20.0
                },
                "tTPpercentTS": {
                    "value": 200.0,
                },
                "LevelColor": {
                    "value": "clrDeepPink",
                },
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test trailing stop (each trade) test No 2
input_data_5 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "trailing_stop_each_trade"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "value": "ORDER_GROUP_MODE_ALL",
                    "checked": False
                },
                "group_number": {
                    "value": 15,
                    "checked": False
                },
                "type": {
                    "value": [0, 1],
                    "checked": False
                },

                "TrailWhat": {
                    "value": 1,
                },
                "TrailingReferencePrice": {
                    "value": 0,
                },
                "TrailingStopMode": {
                    "value": "TRAILING_STOP_MODE_CUSTOM_LEVEL",
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "\"EURUSD\""
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 21
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 80
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 20
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 1
                                }
                            }
                        ]
                    }
                },
                "tStopPips": {
                    "value": 40.0,
                },
                "tStopMoney": {
                    "value": 10.0,
                },
                "tStopMultiple": {
                    "value": "\"20/5, 30/10\"",
                },
                "tStopPercentTP": {
                    "value": 100.0,
                },
                "tStopPercentProfit": {
                    "value": 50.0,
                },
                "TrailingStepMode": {
                    "value": "TRAILING_STEP_MODE_PIPS",
                },
                "tStepPips": {
                    "value": 1,
                },
                "tStepPercentTS": {
                    "value": 10.0,
                },
                "TrailingStartMode": {
                    "value": "TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP",
                },
                "tStartPips": {
                    "value": 10.0,
                },
                "tStartPercentTS": {
                    "value": 100.0,
                },
                "tStartPercentSL": {
                    "value": 10.0,
                },
                "tStartPercentTP": {
                    "value": 10.0,
                },
                "TrailingTPmode": {
                    "value": "TRAILING_OPPOSITE_STOP_MODE_PIPS_FROM_OPEN_PRICE",
                },
                "tTPpips": {
                    "value": 20.0
                },
                "tTPpercentTS": {
                    "value": 200.0,
                },
                "LevelColor": {
                    "value": "clrDeepPink",
                },
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test comment
input_data_6 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "comment"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "Title": {
                    "value": "Comment Message",
                    "checked": False
                },
                "ObjChartSubWindow": {
                    "value": "",
                    "checked": False
                },
                "ObjCorner": {
                    "value": "CORNER_LEFT_UPPER",
                    "checked": False
                },
                "ObjX": {
                    "value": 800,
                    "checked": False
                },
                "ObjY": {
                    "value": 200,
                },
                "ObjTitleFont": {
                    "value": "Georgia",
                },
                "ObjTitleFontColor": {
                    "value": "clrBlue",
                },
                "ObjTitleFontSize": {
                    "value": 13,
                },
                "ObjLabelsFont": {
                    "value": "Verdana",
                },
                "ObjLabelsFontColor": {
                    "value": "clrDarkGray",
                },
                "ObjLabelsFontSize": {
                    "value": 10,
                },
                "ObjFont": {
                    "value": "Verdana",
                },
                "ObjFontColor": {
                    "value": "clrWhite",
                },
                "ObjFontSize": {
                    "value": 10,
                },

                "row1": {
                    "Label": {
                        "value": "label 1",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    },
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 14
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 70
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 30
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "adjust",
                                "value": {
                                    "value": "+40%"
                                }
                            }
                        ]
                    }
                },

                "row2": {
                    "Label": {
                        "value": "label 2",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    },
                    "value_fetch": {
                        "row1": {
                            "label": "Market Properties"
                        },
                        "row2": {
                            "name": "Market Properties",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "id": 1,
                                    "key": "symbol",
                                    "value": "NULL",
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "id": 2,
                                    "key": "timeframe",
                                    "value": 0,
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "find_method",
                                "value": {
                                    "id": 3,
                                    "key": "find_method",
                                    "value": "CANDLE_PERIOD",
                                    "indicator_name": 1
                                }
                            },
                            {
                                "multi": False,
                                "optionName": "price_mode",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "price_mode",
                                    "value": "LOWEST_PRICE"
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "what_to_get",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "what_to_get",
                                    "value": "GET_PRICE"
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "timestr_start",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "timestr_start",
                                    "value": "\"2023.11.23 7:30:30\""
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "timestr_end",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "timestr_end",
                                    "value": "timestr_end"
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "day_offset",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "day_offset",
                                    "value": 0
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "range_start",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "range_start",
                                    "value": 50
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "range_end",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "range_end",
                                    "value": 100
                                }
                            },
                            {
                                "multi": True,
                                "optionName": "adjust",
                                "value": {
                                    "value": "/                        a734   pips"
                                }
                            }
                        ]
                    }
                },

                "row3": {
                    "Label": {
                        "value": "",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    }
                },

                "row4": {
                    "Label": {
                        "value": "",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    }
                },

                "row5": {
                    "Label": {
                        "value": "",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    }
                },

                "row6": {
                    "Label": {
                        "value": "label 6",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    },
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 28
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 75
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 25
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 0
                                }
                            }
                        ]
                    }
                },

                "row7": {
                    "Label": {
                        "value": "",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    }
                },

                "row8": {
                    "Label": {
                        "value": "mtext",
                    },
                    "FormatNumber": {
                        "value": 50,
                    },
                    "FormatTime": {
                        "value": "EMPTY_VALUE",
                    },
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "awesome_oscillator",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": "PERIOD_M5"
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 1
                                }
                            }
                        ]
                    }
                },

                "initialized": {
                    "value": False,
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WEIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test close partially
input_data_7 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "close_partially"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "part_vol_mode": {
                    "value": "CLOSE_PARTIALLY_PERCENT_OF_INITIAL_VOLUME",
                    "checked": False
                },
                "part_vol_value": {
                    "value": 20,
                    "checked": False
                },
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "arrow_color": {
                    "value": "clrDeepPink",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": "\"hello605good\""
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test close
input_data_8 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "close"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "arrow_color": {
                    "value": "clrDeepPink",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test check profit
input_data_9 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "check_profit"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "check_mode": {
                    "value": "CHECK_PROFIT_LOSS_MODE_ACCOUNT_PROFIT",
                    "checked": False
                },
                "check_value": {
                    "value": 100.0,
                    "checked": False
                },
                "operator": {
                    "value": ">",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test check loss
input_data_10 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "check_loss"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "check_mode": {
                    "value": "CHECK_PROFIT_LOSS_MODE_BALANCE",
                    "checked": False
                },
                "check_value": {
                    "value": 120.0,
                    "checked": False
                },
                "operator": {
                    "value": "!=",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },

        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test time filter
input_data_11 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "time_filter"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "server_or_local_time": {
                    "value": "TIME_SERVER",
                    "checked": False
                },
                "time_start_mode": {
                    "value": "TIME_MODE_TEXT",
                    "checked": False
                },
                "time_start": {
                    "value": "\"00:00\"",
                    "checked": False
                },
                "time_start_year": {
                    "value": 0,
                    "checked": False
                },
                "time_start_month": {
                    "value": 0,
                    "checked": False
                },
                "time_start_day": {
                    "value": 0.0,
                    "checked": False
                },
                "time_start_hour": {
                    "value": 1.0,
                    "checked": False
                },
                "time_start_minute": {
                    "value": 0.0,
                    "checked": False
                },
                "time_start_second": {
                    "value": 0,
                    "checked": False
                },
                "time_end_mode": {
                    "value": "TIME_MODE_TEXT",
                    "checked": False
                },
                "time_end": {
                    "value": "\"00:01\"",
                    "checked": False
                },
                "time_end_year": {
                    "value": 0,
                    "checked": False
                },
                "time_end_month": {
                    "value": 0,
                    "checked": False
                },
                "time_end_day": {
                    "value": 0.0,
                    "checked": False
                },
                "time_end_hour": {
                    "value": 1.0,
                    "checked": False
                },
                "time_end_minute": {
                    "value": 1.0,
                    "checked": False
                },
                "time_end_second": {
                    "value": 0,
                    "checked": False
                },
                "time_end_rel_years": {
                    "value": 0,
                    "checked": False
                },
                "time_end_rel_months": {
                    "value": 0,
                    "checked": False
                },
                "time_end_rel_days": {
                    "value": 0.0,
                    "checked": False
                },
                "time_end_rel_hours": {
                    "value": 0.0,
                    "checked": False
                },
                "time_end_rel_minutes": {
                    "value": 1.0,
                    "checked": False
                },
                "time_end_rel_seconds": {
                    "value": 0,
                    "checked": False
                }

            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "value": "+  20   %"
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 1016,
                "y": 305
            },
            "width": 82,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Market Properties"
                },
                "right2": {
                    "id": 1,
                    "name": "Market Properties",
                    "description": "this is Market Properties"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "id": 1,
                            "key": "symbol",
                            "value": "NULL",
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "id": 2,
                            "key": "timeframe",
                            "value": 0,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "id": 3,
                            "key": "find_method",
                            "value": "CANDLE_PERIOD",
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": False,
                        "optionName": "price_mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "price_mode",
                            "value": "LOWEST_PRICE"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "what_to_get",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "what_to_get",
                            "value": "GET_PRICE"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "timestr_start",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "timestr_start",
                            "value": "\"2023.11.23 7:30:30\""
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "timestr_end",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "timestr_end",
                            "value": "timestr_end"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "day_offset",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "day_offset",
                            "value": 0
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "range_start",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "range_start",
                            "value": 50
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "range_end",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "range_end",
                            "value": 100
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": 1,
                    "checked": False
                },
                "candleIDRight": {
                    "value": 1,
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test spread filter with adjust (here adjust is built-in)
input_data_12 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "spread_filter"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "spread_mode": {
                    "value": "SPREAD_BENCHMARK_FIX",
                    "checked": False
                },
                "spread_benchmark_fix_value": {
                    "value": 14,
                    "checked": False
                },
                "average_spread_time_period": {
                    "value": 20,
                    "checked": False
                },
                "average_spread_adjust": {
                    "value": 817,
                    "checked": False
                },
                "operator": {
                    "value": "<=",
                    "checked": False
                }

            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "value": "+  20   %"
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 1016,
                "y": 305
            },
            "width": 82,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Market Properties"
                },
                "right2": {
                    "id": 1,
                    "name": "Market Properties",
                    "description": "this is Market Properties"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "id": 1,
                            "key": "symbol",
                            "value": "NULL",
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "id": 2,
                            "key": "timeframe",
                            "value": 0,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "id": 3,
                            "key": "find_method",
                            "value": "CANDLE_PERIOD",
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": False,
                        "optionName": "price_mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "price_mode",
                            "value": "LOWEST_PRICE"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "what_to_get",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "what_to_get",
                            "value": "GET_PRICE"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "timestr_start",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "timestr_start",
                            "value": "\"2023.11.23 7:30:30\""
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "timestr_end",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "timestr_end",
                            "value": "timestr_end"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "day_offset",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "day_offset",
                            "value": 0
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "range_start",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "range_start",
                            "value": 50
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "range_end",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "range_end",
                            "value": 100
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": 1,
                    "checked": False
                },
                "candleIDRight": {
                    "value": 1,
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test once per bar (further test)
input_data_13 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "Once per bar"
            },
            "type": "testMojtaba",
            "position": {
                "x": 658,
                "y": -200
            },
            "width": 103,
            "height": 32
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Text"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "value": "+  20   %"
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "60"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 1016,
                "y": 305
            },
            "width": 82,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Market Properties"
                },
                "right2": {
                    "id": 1,
                    "name": "Market Properties",
                    "description": "this is Market Properties"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "id": 1,
                            "key": "symbol",
                            "value": "NULL",
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "id": 2,
                            "key": "timeframe",
                            "value": 0,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "id": 3,
                            "key": "find_method",
                            "value": "CANDLE_PERIOD",
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": False,
                        "optionName": "price_mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "price_mode",
                            "value": "LOWEST_PRICE"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "what_to_get",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "what_to_get",
                            "value": "GET_PRICE"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "timestr_start",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "timestr_start",
                            "value": "\"2023.11.23 7:30:30\""
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "timestr_end",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "timestr_end",
                            "value": "timestr_end"
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "day_offset",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "day_offset",
                            "value": 0
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "range_start",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "range_start",
                            "value": 50
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "range_end",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "range_end",
                            "value": 100
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": 1,
                    "checked": False
                },
                "candleIDRight": {
                    "value": 1,
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 279,
                "y": 274
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 2,
                    "label": "<"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Boolean"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "leftNumber",
                        "value": {
                            "optionName": "leftNumber",
                            "value": "40"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test trailing pending orders
input_data_14 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "trailing_pending_orders"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "value": "ORDER_GROUP_MODE_ALL",
                    "checked": False
                },
                "group_number": {
                    "value": "15",
                    "checked": False
                },
                "type": {
                    "value": [2, 3, 4, 5],
                    "checked": False
                },

                "trailing_distance_mode": {
                    "value": "TRAILING_DISTANCE_MODE_FIXED",
                    "value_fetch": {
                        "row1": {
                            "label": "Value"
                        },
                        "row2": {
                            "name": "Numeric",
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "type",
                                "value": {
                                    "optionName": "type",
                                    "value": "VALUE_TYPE_NUMERIC"
                                }
                            },
                            {
                                "optionName": "value",
                                "value": {
                                    "optionName": "value",
                                    "value": 20.4
                                }
                            },
                            {
                                "optionName": "adjust",
                                "value": {
                                    "optionName": "adjust",
                                    "value": "*21%"
                                }
                            },
                            {
                                "optionName": "pips_mode",
                                "value": {
                                    "optionName": "pips_mode",
                                    "value": "VALUE_PIPS_AS_IS"
                                }
                            },
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            }
                        ]
                    }
                },
                "t_distance_pips": {
                    "value": 10.0,
                },
                "t_step_pips": {
                    "value": 1.0,
                },
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test modify stops of trades
input_data_15 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "modify_stops_of_trades"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "value": "ORDER_GROUP_MODE_ALL",
                    "checked": False
                },
                "group_number": {
                    "value": "15",
                    "checked": False
                },
                "type": {
                    "value": [0, 1],
                    "checked": False
                },

                "order_age_mins": {
                    "value": 5,
                    "checked": False
                },
                "relative_to": {
                    "value": "PRICE_RELATIVE_TO_CUSTOM_PRICE_LEVEL",
                    "checked": False,
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 45
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 70
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 30
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 0
                                }
                            }
                        ]
                    }
                },
                "new_tpsl_mode": {
                    "value": "NEW_STOPS_CUSTOM_PRICE_LEVEL",
                    "checked": False,
                    "value_fetch_sl": {
                        "row1": {
                            "label": "Value"
                        },
                        "row2": {
                            "name": "Numeric",
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "type",
                                "value": {
                                    "optionName": "type",
                                    "value": "VALUE_TYPE_NUMERIC"
                                }
                            },
                            {
                                "optionName": "value",
                                "value": {
                                    "optionName": "value",
                                    "value": 85
                                }
                            },
                            {
                                "optionName": "adjust",
                                "value": {
                                    "optionName": "adjust",
                                    "value": "*21%"
                                }
                            },
                            {
                                "optionName": "pips_mode",
                                "value": {
                                    "optionName": "pips_mode",
                                    "value": "VALUE_PIPS_AS_IS"
                                }
                            },
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            }
                        ]
                    },
                    "value_fetch_tp": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
                            {
                                "optionName": "symbol",
                                "value": {
                                    "value": "NULL"
                                }
                            },
                            {
                                "optionName": "timeframe",
                                "value": {
                                    "value": 0
                                }
                            },
                            {
                                "optionName": "period",
                                "value": {
                                    "value": 14
                                }
                            },
                            {
                                "optionName": "applied_price",
                                "value": {
                                    "value": "PRICE_CLOSE"
                                }
                            },
                            {
                                "optionName": "buy_threshold",
                                "value": {
                                    "value": 70
                                }
                            },
                            {
                                "optionName": "sell_threshold",
                                "value": {
                                    "value": 30
                                }
                            },
                            {
                                "optionName": "shift",
                                "value": {
                                    "value": 0
                                }
                            }
                        ]
                    }
                },
                "new_stoploss": {
                    "value": 30,
                    "checked": False
                },
                "new_stoploss_percent": {
                    "value": 50,
                    "checked": False
                },
                "new_takeprofit": {
                    "value": 80,
                    "checked": False
                },
                "new_takeprofit_percent": {
                    "value": 50,
                    "checked": False
                },
                "level_color": {
                    "value": "clrDeepPink",
                    "checked": False
                },
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test terminate
input_data_16 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "terminate"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "message": {
                    "value": "\"My expert terminated\"",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test set current market
input_data_17 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "set_current_market_for_next_blocks"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbols_str": {
                    "value":   "\"EURUSD,GBPUSD\"",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test set current timeframe
input_data_18 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "set_current_timeframe_for_next_blocks"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "timeframes": {
                    "value":   [15, 30],
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test check trades orders count
input_data_19 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "check_trades_orders_count"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "id": 2,
                    "value": "SYMBOL_MODE_SPECIFIED"
                },
                "symbols_str": {
                    "id": 2,
                    "value": "\",EURUSD,GBPUSD\""
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_ALL"
                },
                "group_number": {
                    "id": 2,
                    "value": 25
                },
                "type": {
                    "id": 2,
                    "value": [1, 2]
                },
                "count_limit": {
                    "id": 2,
                    "value": 0
                },
                "operator": {
                    "id": 2,
                    "value": ">"
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test check trades orders nearby
input_data_20 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "check_trades_orders_nearby"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "id": 2,
                    "value": "SYMBOL_MODE_SPECIFIED"
                },
                "symbols_str": {
                    "id": 2,
                    "value": "\",EURUSD,GBPUSD\""
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_ALL"
                },
                "group_number": {
                    "id": 2,
                    "value": 25
                },
                "type": {
                    "id": 2,
                    "value": [1, 2]
                },
                "count_limit": {
                    "id": 2,
                    "value": 0
                },
                "operator": {
                    "id": 2,
                    "value": ">"
                },

                "price_mode": {
                    "id": 2,
                    "value": "PRICE_AUTO"
                },
                "range_mode": {
                    "id": 2,
                    "value": "RANGE_MODE_PIPS"
                },
                "range_position": {
                    "id": 2,
                    "value": "RANGE_POSITION_AROUND"
                },
                "range_value": {
                    "id": 2,
                    "value": 10
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test check profit unrealized
input_data_21 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "check_profit_unrealized"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                 "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "id": 1,
                    "value": "ORDER_GROUP_MODE_ALL"
                },
                "group_number": {
                    "value": 15,
                    "checked": False
                },
                "type": {
                    "value": [0, 1],
                    "checked": False
                },
                "profit_mode": {
                    "value": "PROFIT_MODE_MONEY",
                    "checked": False
                },
                "profit_benchmark_filter": {
                    "value": 0,
                    "checked": False
                },
                "profit_benchmark_comparison": {
                    "value": 100,
                    "checked": False
                },
                "profit_filter_operator": {
                    "value": "==",
                    "checked": False
                },
                "profit_comparison_operator": {
                    "value": "<=",
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test for each trade
input_data_22 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "for_each_trade"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "EURUSD,GBPUSD",
                    "checked": False
                },
                "group_mode": {
                    "value": "ORDER_GROUP_MODE_ALL",
                    "checked": False
                },
                "group_number": {
                    "value": 15,
                    "checked": False
                },
                "type": {
                    "value": [0, 1],
                    "checked": False
                },
                "loop_direction": {
                    "value": "LOOP_DIRECTION_OLDEST_TO_NEWEST",
                    "checked": False
                },
                "skip_n": {
                    "value": 1,
                    "checked": False
                },
                "not_more_than_n": {
                    "value": 4,
                    "checked": False
                },
                "every_n": {
                    "value": 2,
                    "checked": False
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test close trades
input_data_23 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "close_trades"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",EURUSD,GBPUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_ALL"
                },
                "group_number": {
                    "id": 2,
                    "value": 25
                },
                "type": {
                    "id": 2,
                    "value": [1, 2]
                },
                "older_than": {
                    "id": 2,
                    "value": 0.3
                },
                "slippage": {
                    "id": 2,
                    "value": 3
                },
                "arrow_color": {
                    "id": 2,
                    "value": "Red"
                },
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}

# Test delete pending orders
input_data_24 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "delete_pending_orders"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "symbol_mode": {
                    "value": "SYMBOL_MODE_SPECIFIED",
                    "checked": False
                },
                "symbols_str": {
                    "value": "\",XAUUSD,BTCUSD\"",
                    "checked": False
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_ALL"
                },
                "group_number": {
                    "id": 2,
                    "value": 25
                },
                "type": {
                    "id": 2,
                    "value": [5, 6]
                },
                "arrow_color": {
                    "id": 2,
                    "value": "Red"
                }
            }
        },
        {
            "id": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": ">"
                },
                "right1": {
                    "id": 7,
                    "label": "Value"
                },
                "right2": {
                    "id": 1,
                    "name": "Numeric"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "type",
                        "value": {
                            "optionName": "type",
                            "value": "VALUE_TYPE_NUMERIC"
                        }
                    },
                    {
                        "optionName": "value",
                        "value": {
                            "optionName": "value",
                            "value": 20.4
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "optionName": "adjust",
                            "value": "*21%"
                        }
                    },
                    {
                        "optionName": "pips_mode",
                        "value": {
                            "optionName": "pips_mode",
                            "value": "VALUE_PIPS_AS_IS"
                        }
                    },
                    {
                        "optionName": "symbol",
                        "value": {
                            "value": "NULL"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 462,
                "y": 263
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 2,
                    "name": "RSI",
                    "description": "this is RSI indicator"
                },
                "operator": {
                    "value": 1,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 7,
                    "label": "Candle"
                },
                "right2": {
                    "id": 1,
                    "name": "Candle"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "rsi Period",
                        "value": {
                            "id": 7,
                            "key": "rsi Period",
                            "value": 14,
                            "indicator_name": 2
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "symbol",
                        "value": {
                            "optionName": "symbol",
                            "value": "NULL"
                        }
                    },
                    {
                        "optionName": "timeframe",
                        "value": {
                            "optionName": "timeframe",
                            "value": "0"
                        }
                    },
                    {
                        "optionName": "find_method",
                        "value": {
                            "optionName": "find_method",
                            "value": "FIND_BY_ID"
                        }
                    },
                    {
                        "optionName": "price_mode",
                        "value": {
                            "optionName": "price_mode",
                            "value": "CANDLE_HIGH"
                        }
                    },
                    {
                        "optionName": "timestr",
                        "value": {
                            "optionName": "timestr",
                            "value": "\"2023.4.26 13:40:30\""
                        }
                    },
                    {
                        "optionName": "adjust",
                        "value": {
                            "value": "58pips",
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 284,
                "y": 391
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 8,
                    "label": "\u00d7<"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "adjust",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "/20pips",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 469,
                "y": 397
            },
            "width": 82,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "left1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "left2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "operator": {
                    "value": 7,
                    "label": "\u00d7>"
                },
                "right1": {
                    "id": 3,
                    "label": "Indicator"
                },
                "right2": {
                    "id": 1,
                    "name": "Macd",
                    "description": "this is macd indicator"
                },
                "changeStatus": False,
                "changeStatusDesc": "",
                "left": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "MODE_MAIN",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "right": [
                    {
                        "optionName": "Signal Period",
                        "value": {
                            "id": 1,
                            "key": "Signal Period",
                            "value": 12,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "id": 2,
                            "key": "slow EMA period",
                            "value": 29,
                            "indicator_name": 1
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "id": 3,
                            "key": "Fast EMA Period",
                            "value": 9,
                            "indicator_name": 1
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "applied_price",
                        "value": {
                            "id": 1,
                            "indicator_name": 1,
                            "key": "apiLater",
                            "value": "PRICE_CLOSE",
                            "items": [
                                "PRICE_CLOSE",
                                "PRICE_OPEN",
                                "PRICE_HIGH",
                                "PRICE_LOW",
                                "PRICE_MIDIAN",
                                "PRICE_TYPICAL",
                                "PRICE_WIGHTED"
                            ]
                        }
                    },
                    {
                        "multi": True,
                        "optionName": "mode",
                        "value": {
                            "multi": True,
                            "optionName": "mode",
                            "value": "MODE_SIGNAL",
                            "items": [
                                "MODE_MAIN",
                                "MODE_SIGNAL"
                            ]
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "1",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 285,
                "y": 515
            },
            "width": 70,
            "height": 32,
            "selected": True,
            "dragging": False,
            "more": {
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "group": {
                    "value": 11,
                    "checked": False
                },
                "order_type": {
                    "id": 1,
                    "value": "ORDER_BUY_PENDING"
                },
                "money_management": {
                    "value": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
                    "checked": False
                },
                "how_much_volume": {
                    "value": 35,
                    "checked": False
                },
                "volume_upper_limit": {
                    "id": 0,
                    "value": 10
                },
                "open_at_price": {
                    "id": 2,
                    "value": "OPEN_AT_ASK"
                },
                "price_offset": {
                    "id": 25,
                    "value": 10
                },
                "price_offset_as_pip": {
                    "value": True
                },
                "slippage": {
                    "id": 1,
                    "value": 4
                },
                "stoploss": {
                    "value": 20,
                    "checked": False
                },
                "takeprofit": {
                    "value": 20,
                    "checked": False
                },
                "take_profit_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "stop_loss_mode": {
                    "id": 2,
                    "value": "TPSL_MODE_FIXED_PIPS"
                },
                "comment": {
                    "id": 2,
                    "value": "\"\""
                },
                "expiration": {
                    "id": 2,
                    "value": 0
                },
                "arrow_color": {
                    "id": 2,
                    "value": "clrYellow"
                },
                "look_up_on": {
                    "id": 2,
                    "value": "LOOK_UP_RUNNING_ONLY"
                },
                "type": {
                    "id": 2,
                    "value": [0, 1]
                },
                "martingale_init_vol": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_multiply_on_loss": {
                    "id": 2,
                    "value": 0
                },
                "martingale_multiply_on_profit": {
                    "id": 2,
                    "value": 0
                },
                "martingale_addlots_on_loss": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_addlots_on_profit": {
                    "id": 2,
                    "value": 0.1
                },
                "martingale_reset_on_n_losses": {
                    "id": 2,
                    "value": 5
                },
                "martingale_reset_on_n_profits": {
                    "id": 2,
                    "value": 5
                }
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 474,
                "y": 527
            },
            "width": 70,
            "height": 32,
            "selected": False,
            "dragging": False,
            "more": {
                "group": {
                    "value": 0,
                    "checked": False
                },
                "symbol": {
                    "value": "NULL",
                    "checked": False
                },
                "monyManagement": {
                    "id": 1,
                    "label": "Fixed volume"
                },
                "howMuch": {
                    "value": 0.1,
                    "checked": False
                },
                "volumeUpper": {
                    "value": 0,
                    "checked": False
                },
                "stopLoss": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "takeProfit": {
                    "id": 2,
                    "label": "Fixed pips"
                },
                "inPipStop": {
                    "value": 50,
                    "checked": False
                },
                "inPipTake": {
                    "value": 10,
                    "checked": False
                },
                "expirationMode": {
                    "id": 1,
                    "label": "No expiration"
                },
                "expirationModeToggle": False,
                "slippage": {
                    "value": 4,
                    "checked": False
                },
                "comment": {
                    "value": 0,
                    "checked": False
                },
                "arrowColor": {
                    "id": 2,
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
    ],
    "constants": [

    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "a734",
            "value": "45",
            "description": ""
        }
    ]
}
