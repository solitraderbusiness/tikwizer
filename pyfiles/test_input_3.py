# once per bar: macd main cross over signal : rsi>70 : buy, else if macd no cross : rsi cross under 30 : sell.
input_data_1 = {
    "nodes": [
        {
            "id": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 524,
                "y": -95
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
            "id": "6f2ef01e-3713-4071-b62a-88009881b668",
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
            "id": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 398,
                "y": 33
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
            "id": "462f5932-ec48-4617-a5c1-67104f9cfd88",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 272,
                "y": 196
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
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "ad572ddc-9b7b-4054-9389-997f150d4b12",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 687,
                "y": 29
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
                    "value": 8,
                    "label": "\u00d7<"
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
                            "value": "30"
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
            "id": "5175a656-8ea8-41c8-8e70-1cf9814802a3",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 804,
                "y": 183
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
            "source": "6f2ef01e-3713-4071-b62a-88009881b668",
            "sourceHandle": "blue",
            "target": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "targetHandle": "black",
            "id": "reactflow__edge-6f2ef01e-3713-4071-b62a-88009881b668blue-0b02a58f-b963-499e-b618-9f15838cc7a3black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "sourceHandle": "blue",
            "target": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "targetHandle": "black",
            "id": "reactflow__edge-0b02a58f-b963-499e-b618-9f15838cc7a3blue-359e5cfa-885f-422c-b530-3f6417a0b0f0black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "sourceHandle": "blue",
            "target": "462f5932-ec48-4617-a5c1-67104f9cfd88",
            "targetHandle": "black",
            "id": "reactflow__edge-359e5cfa-885f-422c-b530-3f6417a0b0f0blue-462f5932-ec48-4617-a5c1-67104f9cfd88black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "sourceHandle": "red",
            "target": "ad572ddc-9b7b-4054-9389-997f150d4b12",
            "targetHandle": "black",
            "id": "reactflow__edge-0b02a58f-b963-499e-b618-9f15838cc7a3red-ad572ddc-9b7b-4054-9389-997f150d4b12black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "ad572ddc-9b7b-4054-9389-997f150d4b12",
            "sourceHandle": "blue",
            "target": "5175a656-8ea8-41c8-8e70-1cf9814802a3",
            "targetHandle": "black",
            "id": "reactflow__edge-ad572ddc-9b7b-4054-9389-997f150d4b12blue-5175a656-8ea8-41c8-8e70-1cf9814802a3black"
        }
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# once per bar: macd main cross over signal : rsi>70 : buy, else if macd no cross : rsi cross under 30 : sell. Once per bar: rsi cross over 30 : macd main > signal : buy
input_data_2 = {
    "nodes": [
        {
            "id": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 524,
                "y": -95
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
            "id": "6f2ef01e-3713-4071-b62a-88009881b668",
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
            "id": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 398,
                "y": 33
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
            "id": "462f5932-ec48-4617-a5c1-67104f9cfd88",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 272,
                "y": 196
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
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "ad572ddc-9b7b-4054-9389-997f150d4b12",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 687,
                "y": 29
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
                    "value": 8,
                    "label": "\u00d7<"
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
                            "value": "30"
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
            "id": "5175a656-8ea8-41c8-8e70-1cf9814802a3",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 804,
                "y": 183
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
        },
        {
            "id": "f91158d1-2706-43a9-9806-5208226d2bbf",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 1006,
                "y": -64
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
                            "value": "30"
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
            "id": "df674b80-3dcd-4ef8-9ccf-6dd03c5b5113",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 1038,
                "y": 80
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
                    "value": 1,
                    "label": ">"
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
            "id": "b37536b7-ac91-4d0d-bbde-2e7dda2d9667",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 987,
                "y": 307
            },
            "width": 70,
            "height": 32,
            "selected": True,
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
            "source": "6f2ef01e-3713-4071-b62a-88009881b668",
            "sourceHandle": "blue",
            "target": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "targetHandle": "black",
            "id": "reactflow__edge-6f2ef01e-3713-4071-b62a-88009881b668blue-0b02a58f-b963-499e-b618-9f15838cc7a3black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "sourceHandle": "blue",
            "target": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "targetHandle": "black",
            "id": "reactflow__edge-0b02a58f-b963-499e-b618-9f15838cc7a3blue-359e5cfa-885f-422c-b530-3f6417a0b0f0black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "sourceHandle": "blue",
            "target": "462f5932-ec48-4617-a5c1-67104f9cfd88",
            "targetHandle": "black",
            "id": "reactflow__edge-359e5cfa-885f-422c-b530-3f6417a0b0f0blue-462f5932-ec48-4617-a5c1-67104f9cfd88black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "sourceHandle": "red",
            "target": "ad572ddc-9b7b-4054-9389-997f150d4b12",
            "targetHandle": "black",
            "id": "reactflow__edge-0b02a58f-b963-499e-b618-9f15838cc7a3red-ad572ddc-9b7b-4054-9389-997f150d4b12black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "ad572ddc-9b7b-4054-9389-997f150d4b12",
            "sourceHandle": "blue",
            "target": "5175a656-8ea8-41c8-8e70-1cf9814802a3",
            "targetHandle": "black",
            "id": "reactflow__edge-ad572ddc-9b7b-4054-9389-997f150d4b12blue-5175a656-8ea8-41c8-8e70-1cf9814802a3black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "6f2ef01e-3713-4071-b62a-88009881b668",
            "sourceHandle": "blue",
            "target": "f91158d1-2706-43a9-9806-5208226d2bbf",
            "targetHandle": "black",
            "id": "reactflow__edge-6f2ef01e-3713-4071-b62a-88009881b668blue-f91158d1-2706-43a9-9806-5208226d2bbfblack"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "f91158d1-2706-43a9-9806-5208226d2bbf",
            "sourceHandle": "blue",
            "target": "df674b80-3dcd-4ef8-9ccf-6dd03c5b5113",
            "targetHandle": "black",
            "id": "reactflow__edge-f91158d1-2706-43a9-9806-5208226d2bbfblue-df674b80-3dcd-4ef8-9ccf-6dd03c5b5113black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "df674b80-3dcd-4ef8-9ccf-6dd03c5b5113",
            "sourceHandle": "blue",
            "target": "b37536b7-ac91-4d0d-bbde-2e7dda2d9667",
            "targetHandle": "black",
            "id": "reactflow__edge-df674b80-3dcd-4ef8-9ccf-6dd03c5b5113blue-b37536b7-ac91-4d0d-bbde-2e7dda2d9667black"
        }
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Only to check if value changes are applied in output expert.
input_data_3 = {
    "nodes": [
        {
            "id": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 524,
                "y": -95
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
                            "optionName": "Signal Period",
                            "value": "13"
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "optionName": "slow EMA period",
                            "value": "30"
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "optionName": "Fast EMA Period",
                            "value": "10"
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
                            "optionName": "Signal Period",
                            "value": "14"
                        }
                    },
                    {
                        "optionName": "slow EMA period",
                        "value": {
                            "optionName": "slow EMA period",
                            "value": "31"
                        }
                    },
                    {
                        "optionName": "Fast EMA Period",
                        "value": {
                            "optionName": "Fast EMA Period",
                            "value": "11"
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
                    "value": "2",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "1",
                    "checked": False
                }
            }
        },
        {
            "id": "6f2ef01e-3713-4071-b62a-88009881b668",
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
            "id": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 398,
                "y": 33
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
                            "optionName": "rsi Period",
                            "value": "15"
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
                            "value": "71"
                        }
                    }
                ],
                "candleIDLeft": {
                    "value": "5",
                    "checked": False
                },
                "candleIDRight": {
                    "value": 0,
                    "checked": False
                }
            }
        },
        {
            "id": "462f5932-ec48-4617-a5c1-67104f9cfd88",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 272,
                "y": 196
            },
            "width": 70,
            "height": 32,
            "selected": True,
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
            "source": "6f2ef01e-3713-4071-b62a-88009881b668",
            "sourceHandle": "blue",
            "target": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "targetHandle": "black",
            "id": "reactflow__edge-6f2ef01e-3713-4071-b62a-88009881b668blue-0b02a58f-b963-499e-b618-9f15838cc7a3black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "0b02a58f-b963-499e-b618-9f15838cc7a3",
            "sourceHandle": "blue",
            "target": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "targetHandle": "black",
            "id": "reactflow__edge-0b02a58f-b963-499e-b618-9f15838cc7a3blue-359e5cfa-885f-422c-b530-3f6417a0b0f0black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "359e5cfa-885f-422c-b530-3f6417a0b0f0",
            "sourceHandle": "blue",
            "target": "462f5932-ec48-4617-a5c1-67104f9cfd88",
            "targetHandle": "black",
            "id": "reactflow__edge-359e5cfa-885f-422c-b530-3f6417a0b0f0blue-462f5932-ec48-4617-a5c1-67104f9cfd88black"
        }
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test Alireza
input_data_4 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "Once per bar"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
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
            "id": "11246ce6-1ff2-47c6-969f-cb539c2815e2",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 470,
                "y": 373
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
                    "value": 8,
                    "label": "\u00d7<"
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
                            "value": "70"
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
            "id": "fee6c47d-287f-464a-9f2c-e7af5cd91f42",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 475,
                "y": 471
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
                    "value": 10,
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
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
            "id": "c1964739-3cd1-4ada-982a-0ead9d176a8f",
            "data": {
                "blockId": 1,
                "blockName": "condition"
            },
            "type": "testMojtaba",
            "position": {
                "x": 288,
                "y": 378
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
                            "value": "30"
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
            "id": "1c3b92f1-8ffd-4a3a-9165-0ff63514b55c",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 292,
                "y": 501
            },
            "width": 70,
            "height": 32,
            "selected": True,
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
                    "value": 20,
                    "checked": False
                },
                "inPipTake": {
                    "value": 20,
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
            "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
            "sourceHandle": "blue",
            "target": "11246ce6-1ff2-47c6-969f-cb539c2815e2",
            "targetHandle": "black",
            "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-11246ce6-1ff2-47c6-969f-cb539c2815e2black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "11246ce6-1ff2-47c6-969f-cb539c2815e2",
            "sourceHandle": "blue",
            "target": "fee6c47d-287f-464a-9f2c-e7af5cd91f42",
            "targetHandle": "black",
            "id": "reactflow__edge-11246ce6-1ff2-47c6-969f-cb539c2815e2blue-fee6c47d-287f-464a-9f2c-e7af5cd91f42black"
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
            "target": "c1964739-3cd1-4ada-982a-0ead9d176a8f",
            "targetHandle": "black",
            "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-c1964739-3cd1-4ada-982a-0ead9d176a8fblack"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "c1964739-3cd1-4ada-982a-0ead9d176a8f",
            "sourceHandle": "blue",
            "target": "1c3b92f1-8ffd-4a3a-9165-0ff63514b55c",
            "targetHandle": "black",
            "id": "reactflow__edge-c1964739-3cd1-4ada-982a-0ead9d176a8fblue-1c3b92f1-8ffd-4a3a-9165-0ff63514b55cblack"
        }
    ],
    "constants": [

    ],
    "variables": [

    ]
}

# Test Alireza
input_data_5 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "Once per bar"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test once per seconds
input_data_6 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "once_per_seconds"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "n": {
                    "id": 3,
                    "value": 15
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test every n ticks
input_data_7 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "every_n_ticks"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "n": {
                    "id": 2,
                    "value": 7
                },
                "symbol": {
                    "id": 2,
                    "value": "NULL"
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test in hour min sec
input_data_8 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "in_hour_min_sec"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "time_mode": {
                    "id": 2,
                    "value": "TIME_LOCAL"
                },
                "start_hour_1": {
                    "id": 2,
                    "value": "\"9:00:00\""
                },
                "end_hour_1": {
                    "id": 2,
                    "value": "\"10:00:00\""
                },
                "start_hour_2": {
                    "id": 2,
                    "value": "\"11:30:20\""
                },
                "end_hour_2": {
                    "id": 2,
                    "value": "\"12:40:00\""
                },
                "start_hour_3": {
                    "id": 2,
                    "value": "\"13:00:50\""
                },
                "end_hour_3": {
                    "id": 2,
                    "value": "\"18:05:00\""
                },
                "start_hour_4": {
                    "id": 2,
                    "value": "\"19:05:03\""
                },
                "end_hour_4": {
                    "id": 2,
                    "value": "\"23:59:59\""
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test check trade order count
input_data_9 = {
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
                "symbol": {
                    "id": 2,
                    "value": "NULL"
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_NUMBER"
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test candle
input_data_10 = {
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
                "symbol": {
                    "id": 2,
                    "value": "NULL"
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_NUMBER"
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# once per bar: if rsi > candle buy --- if rsi > market properties sell
input_data_11 = {
    "nodes": [
        {
            "id": "832faa68-213e-46c9-8e9c-ce352a9b31a0",
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
            "id": "0100979e-c5f6-4fdf-850d-00ccdb22374b",
            "data": {
                "blockId": 1,
                "blockName": "condition"
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
                            "value": 0
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
            "id": "075001eb-9bc9-43a1-a92e-094d9d8457cb",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 587,
                "y": 413
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
                    "label": "Blue"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "dc19eb40-7707-4df6-a5bd-7e0d79014545",
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
            "id": "2c36773d-e3ba-486a-b4f4-a4b6a8146231",
            "data": {
                "blockId": 53,
                "blockName": "Sell now"
            },
            "type": "testMojtaba",
            "position": {
                "x": 1017,
                "y": 443
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
            "source": "832faa68-213e-46c9-8e9c-ce352a9b31a0",
            "sourceHandle": "blue",
            "target": "0100979e-c5f6-4fdf-850d-00ccdb22374b",
            "targetHandle": "black",
            "id": "reactflow__edge-832faa68-213e-46c9-8e9c-ce352a9b31a0blue-0100979e-c5f6-4fdf-850d-00ccdb22374bblack"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "0100979e-c5f6-4fdf-850d-00ccdb22374b",
            "sourceHandle": "blue",
            "target": "075001eb-9bc9-43a1-a92e-094d9d8457cb",
            "targetHandle": "black",
            "id": "reactflow__edge-0100979e-c5f6-4fdf-850d-00ccdb22374bblue-075001eb-9bc9-43a1-a92e-094d9d8457cbblack"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "832faa68-213e-46c9-8e9c-ce352a9b31a0",
            "sourceHandle": "blue",
            "target": "dc19eb40-7707-4df6-a5bd-7e0d79014545",
            "targetHandle": "black",
            "id": "reactflow__edge-832faa68-213e-46c9-8e9c-ce352a9b31a0blue-dc19eb40-7707-4df6-a5bd-7e0d79014545black"
        },
        {
            "type": "deleteEdgeBTN",
            "source": "dc19eb40-7707-4df6-a5bd-7e0d79014545",
            "sourceHandle": "blue",
            "target": "2c36773d-e3ba-486a-b4f4-a4b6a8146231",
            "targetHandle": "black",
            "id": "reactflow__edge-dc19eb40-7707-4df6-a5bd-7e0d79014545blue-2c36773d-e3ba-486a-b4f4-a4b6a8146231black"
        }
    ],
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

# Test check trade order nearby
input_data_12 = {
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
                "symbol": {
                    "id": 2,
                    "value": "NULL"
                },
                "group_mode": {
                    "id": 2,
                    "value": "ORDER_GROUP_MODE_NUMBER"
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test close trade
input_data_13 = {
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
                "symbol": {
                    "id": 2,
                    "value": "NULL"
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test check profit unrealized
input_data_14 = {
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
                "symbol": {
                    "value": "NULL",
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test months filter
input_data_15 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "months_filter"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "months": {
                    "value": [5, 6],
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test weekday filter
input_data_16 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "weekday_filter"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "time_mode": {
                    "value": "TIME_SERVER",
                    "checked": False
                },
                "weekdays": {
                    "value": [4, 6],
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test for each trade
input_data_17 = {
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
                "symbol": {
                    "value": "NULL",
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        }
    ]
}

# Test delay
input_data_18 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "delay"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "sleep_seconds": {
                    "value": 7,
                    "checked": False
                },
                "sleep_tester_normal": {
                    "value": True,
                    "checked": False
                },
                "sleep_tester_visual": {
                    "value": True,
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        }
    ]
}

# Test modify variables 1
input_data_19 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "modify_variables"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "params": [
                {
                    "variable_name": "aaaaaaa",
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
                                    "value": 3
                                }
                            }
                        ]
                    }
                },
                {
                    "variable_name": "aaaaaaa",
                    "value_fetch": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "MACD",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
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
                        ]
                    }
                }
            ]

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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        }
    ]
}

# Test modify variables 2
input_data_20 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "modify_variables"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "items": [
                {
                    "variable_name": "aaaaaaa",
                    "value": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
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
                                    "value": 3
                                }
                            }
                        ]
                    }
                },
                {
                    "variable_name": "aaaaaaa",
                    "value": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "MACD",
                            "description": "this is RSI indicator"
                        },
                        "params": [
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
                        ]
                    }
                },
                {
                    "variable_name": "bbbbbbb",
                    "value": {
                        "row1": {
                            "label": "Value"
                        },
                        "row2": {
                            "name": "",
                            "description": "this is RSI indicator"
                        },
                        "params": [
                            {
                                "optionName": "type",
                                "value": {
                                    "id": 1,
                                    "key": "type",
                                    "value": "VALUE_TYPE_PIPS",
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "value",
                                "value": {
                                    "id": 2,
                                    "key": "value",
                                    "value": 29,
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "adjust",
                                "value": {
                                    "id": 3,
                                    "key": "adjust",
                                    "value": 9,
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "pips_mode",
                                "value": {
                                    "id": 1,
                                    "key": "pips_mode",
                                    "value": "VALUE_PIPS_AS_IS",
                                }
                            },
                            {
                                "optionName": "symbol",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "symbol",
                                    "value": "NULL",
                                }
                            }
                        ]
                    }
                }
            ]

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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        }
    ]
}

# Test modify variables 3
input_data_21 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "modify_variables"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "items": [
                {
                    "variable_name": "aaaaaaa",
                    "value": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "RSI",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 1,
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
                                    "value": 3
                                }
                            }
                        ]
                    }
                },
                {
                    "variable_name": "aaaaaaa",
                    "value": {
                        "row1": {
                            "label": "Indicator"
                        },
                        "row2": {
                            "name": "MACD",
                            "description": "this is RSI indicator"
                        },
                        "candleId": {
                            "value": 0,
                            "description": ""
                        },
                        "params": [
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
                        ]
                    }
                },
                {
                    "variable_name": "bbbbbbb",
                    "value": {
                        "row1": {
                            "label": "Value"
                        },
                        "row2": {
                            "name": "",
                            "description": "this is RSI indicator"
                        },
                        "params": [
                            {
                                "optionName": "type",
                                "value": {
                                    "id": 1,
                                    "key": "type",
                                    "value": "VALUE_TYPE_PIPS",
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "value",
                                "value": {
                                    "id": 2,
                                    "key": "value",
                                    "value": 29,
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "adjust",
                                "value": {
                                    "id": 3,
                                    "key": "adjust",
                                    "value": 9,
                                    "indicator_name": 1
                                }
                            },
                            {
                                "optionName": "pips_mode",
                                "value": {
                                    "id": 1,
                                    "key": "pips_mode",
                                    "value": "VALUE_PIPS_AS_IS",
                                }
                            },
                            {
                                "optionName": "symbol",
                                "value": {
                                    "id": 1,
                                    "indicator_name": 1,
                                    "key": "symbol",
                                    "value": "NULL",
                                }
                            }
                        ]
                    }
                },
                {
                    "variable_name": "bbbbbbb",
                    "value": {
                        "row1": {
                            "label": "Market Properties"
                        },
                        "row2": {
                            "name": "Market Properties",
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
                            }
                        ]
                    }
                },
                {
                    "variable_name": "cccccccc",
                    "value": {
                        "row1": {
                            "label": "Candle"
                        },
                        "row2": {
                            "name": "Candle",
                            "description": ""
                        },
                        "candleId": {
                            "value": 3,
                            "description": ""
                        },
                        "params": [
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
                        ]
                    }
                }
            ]

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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        },
        {
            "id": 0,
            "type": "double",
            "name": "cccccccc",
            "value": "55",
            "description": ""
        }
    ]
}

# Test formula 1: indicator - value
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
                "symbol": {
                    "value": "NULL",
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
                "blockName": "formula"
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
                    "label": "*"
                },
                "variable": {
                    "id": 0,
                    "type": "double",
                    "name": "aaaaaaa",
                    "value": "78",
                    "description": ""
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        }
    ]
}

# Test formula 2: indicator - market properties
input_data_23 = {
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
                "symbol": {
                    "value": "NULL",
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
                "blockName": "formula"
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
                    "label": "-"
                },
                "variable": {
                    "id": 0,
                    "type": "double",
                    "name": "aaaaaaa",
                    "value": "78",
                    "description": ""
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "aaaaaaa",
            "value": "78",
            "description": ""
        }
    ]
}

# Test formula 3: indicator - candle
input_data_24 = {
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
                "symbol": {
                    "value": "NULL",
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
                "blockName": "formula"
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
                    "label": "/"
                },
                "variable": {
                    "id": 0,
                    "type": "double",
                    "name": "test_var",
                    "value": "78",
                    "description": ""
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
                    }
                ],
                "candleIDLeft": {
                    "value": "5",
                    "checked": False
                },
                "candleIDRight": {
                    "value": "6",
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
        {
            "id": 0,
            "type": "int",
            "name": "bbbbbbb",
            "value": "21",
            "description": ""
        },
        {
            "id": 1,
            "type": "int",
            "name": "rsishort",
            "value": "7",
            "description": ""
        },
        {
            "id": 2,
            "type": "double",
            "name": "lot",
            "value": "0.1",
            "description": ""
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "double",
            "name": "test_var",
            "value": "78",
            "description": ""
        }
    ]
}

# Test delete pending orders
input_data_25 = {
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
                "symbol": {
                    "id": 2,
                    "value": "NULL"
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test pass block
input_data_26 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "pass"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test blocks on off
input_data_27 = {
    "nodes": [
        {
            "id": "361e37db-e957-40fd-b072-3122dfc3e04c",
            "data": {
                "blockId": 20,
                "blockName": "toggle_blocks"
            },
            "type": "testMojtaba",
            "position": {
                "x": 397,
                "y": 114
            },
            "width": 103,
            "height": 32,
            "more": {
                "block_ids": {
                    "value": "\"5,6\"",
                    "checked": False
                },
                "what": {
                    "value": "BLOCK_STATE_TOGGLE",
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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

# Test spread filter
input_data_28 = {
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
                    "label": "Red"
                },
                "arrowColorToggle": False,
                "changeStatus": False,
                "changeStatusDesc": ""
            }
        },
        {
            "id": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
            "data": {
                "blockId": 50,
                "blockName": "Buy now"
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
