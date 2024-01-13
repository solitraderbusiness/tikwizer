# pass n times > pass n times
input_data_1 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "pass_n_times"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 3,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "pass_n_times"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# pass n times > and
input_data_2 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "pass_n_times"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 3,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# pass n times > and > or
input_data_3 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "pass_n_times"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 3,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "or"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# pass n times > and > break
input_data_4 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "pass_n_times"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 3,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "break"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# pass n times > and > once every n bars
input_data_5 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "pass_n_times"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 3,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "once_every_n_bars"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "symbol": {
                        "id": 2,
                        "value": "NULL"
                    },
                    "timeframe": {
                        "id": 2,
                        "value": "PERIOD_M15"
                    },
                    "n": {
                        "id": 2,
                        "value": "3"
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# condition_1 (rsi>70) > and > once every n bars
input_data_6 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "condition1"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 444,
                    "y": 123
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
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
                        "value": 7,
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
                        }
                    ],
                    "right": [
                        {
                            "optionName": "leftNumber",
                            "value": {
                                "optionName": "leftNumber",
                                "value": "70"
                            }
                        }
                    ],
                    "candleIDLeft": {
                        "value": 0,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 0,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "once_every_n_bars"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "symbol": {
                        "id": 2,
                        "value": "NULL"
                    },
                    "timeframe": {
                        "id": 2,
                        "value": "PERIOD_M15"
                    },
                    "n": {
                        "id": 2,
                        "value": "3"
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# condition_1 (70<RSI) > and > once every n bars
input_data_7 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "condition1"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 291.7931794363558,
                    "y": 73.21032020826408
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "positionAbsolute": {
                    "x": 291.7931794363558,
                    "y": 73.21032020826408
                },
                "dragging": False,
                "enabled": True,
                "more": {
                    "left1": {
                        "id": 3,
                        "label": "Value"
                    },
                    "left2": {
                        "id": 2,
                        "name": "RSI",
                        "description": "this is RSI indicator"
                    },
                    "operator": {
                        "value": 7,
                        "label": ">"
                    },
                    "right1": {
                        "id": 3,
                        "label": "Indicator"
                    },
                    "right2": {
                        "id": 2,
                        "name": "RSI",
                        "description": "this is RSI indicator"
                    },
                    "changeStatus": False,
                    "changeStatusDesc": "",
                    "left": [
                        {
                            "optionName": "rsi Period",
                            "value": {
                                "id": 0,
                                "type": "int",
                                "name": "rsilong",
                                "value": 21,
                                "description": ""
                            }
                        }
                    ],
                    "right": [
                        {
                            "optionName": "rsi Period",
                            "value": {
                                "id": 1,
                                "type": "int",
                                "name": "rsishort",
                                "value": "7",
                                "description": ""
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
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "once_every_n_bars"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "symbol": {
                        "id": 2,
                        "value": "NULL"
                    },
                    "timeframe": {
                        "id": 2,
                        "value": "PERIOD_M15"
                    },
                    "n": {
                        "id": 2,
                        "value": "3"
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# condition_1 (rsi cross over 70) > and > once every n bars
input_data_8 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "condition1"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 444,
                    "y": 123
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
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
                        "value": 7,
                        "label": "\u00d7>"
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
                        }
                    ],
                    "right": [
                        {
                            "optionName": "leftNumber",
                            "value": {
                                "optionName": "leftNumber",
                                "value": "70"
                            }
                        }
                    ],
                    "candleIDLeft": {
                        "value": 0,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 0,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "once_every_n_bars"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "symbol": {
                        "id": 2,
                        "value": "NULL"
                    },
                    "timeframe": {
                        "id": 2,
                        "value": "PERIOD_M15"
                    },
                    "n": {
                        "id": 2,
                        "value": "3"
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# condition_1 (30 cross under rsi) > and > once every n bars
input_data_9 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "condition1"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 444,
                    "y": 123
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
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
                        "value": 7,
                        "label": "\u00d7>"
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
                        }
                    ],
                    "right": [
                        {
                            "optionName": "leftNumber",
                            "value": {
                                "optionName": "leftNumber",
                                "value": "70"
                            }
                        }
                    ],
                    "candleIDLeft": {
                        "value": 0,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 0,
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "once_every_n_bars"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "symbol": {
                        "id": 2,
                        "value": "NULL"
                    },
                    "timeframe": {
                        "id": 2,
                        "value": "PERIOD_M15"
                    },
                    "n": {
                        "id": 2,
                        "value": "3"
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# condition_1 (macd cross macd) > and > once every n bars
input_data_10 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "condition1"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 690,
                    "y": 73
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "positionAbsolute": {
                    "x": 690,
                    "y": 73
                },
                "dragging": False,
                "enabled": True,
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
                        "value": "0",
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": "0",
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 3,
                    "blockName": "once_every_n_bars"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "symbol": {
                        "id": 2,
                        "value": "NULL"
                    },
                    "timeframe": {
                        "id": 2,
                        "value": "PERIOD_M15"
                    },
                    "n": {
                        "id": 2,
                        "value": "3"
                    }
                }
            }
        ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}

# condition_1 (macd cross macd) > and > sell
input_data_11 = {
    "events": {
        "on_tick": {"nodes": [
            {
                "id": "aa",
                "data": {
                    "blockId": 1,
                    "blockName": "condition1"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 690,
                    "y": 73
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "positionAbsolute": {
                    "x": 690,
                    "y": 73
                },
                "dragging": False,
                "enabled": True,
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
                        "value": "0",
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": "0",
                        "checked": False
                    }
                }
            },

            {
                "id": "bb",
                "data": {
                    "blockId": 2,
                    "blockName": "and"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 644,
                    "y": 278
                },
                "width": 82,
                "height": 32,
                "selected": False,
                "dragging": False,
                "enabled": True,
                "more": {
                    "n": {
                        "id": 2,
                        "value": "3"
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
                        "label": "Candle"
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
                        }
                    ],
                    "candleIDLeft": {
                        "value": 1,
                        "checked": False
                    },
                    "candleIDRight": {
                        "value": 10,
                        "checked": False
                    }
                }
            },

            {
                "id": "cc",
                "data": {
                    "blockId": 53,
                    "blockName": "Sell now"
                },
                "type": "testMojtaba",
                "position": {
                    "x": 627,
                    "y": 323
                },
                "width": 70,
                "height": 32,
                "selected": False,
                "positionAbsolute": {
                    "x": 627,
                    "y": 323
                },
                "dragging": False,
                "enabled": True,
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
                        "value": 50,
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
                        "label": "Red"
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
                    "source": "aa",
                    "sourceHandle": "blue",
                    "target": "bb",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "bb",
                    "sourceHandle": "red",
                    "target": "cc",
                    "targetHandle": "black",
                    "id": "edge-aa-bb"
                }
            ]}
    },
    "constants": [
        {
            "id": 0,
            "type": "double",
            "name": "new",
            "value": "13",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "second",
            "value": "16",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "asdfd",
            "value": "45",
            "description": ""
        }
    ]
}
