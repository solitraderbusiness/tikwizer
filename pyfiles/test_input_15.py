# test custom indicator 1
input_data_1 = {
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
                                "label": "-"
                            },
                            "left": {
                                "row1": "my_indicators",
                                "row2": "test_indicator",
                                "params": {
                                    "input": [
                                        {
                                            "type": "string",
                                            "name": "state",
                                            "value": "test_value"
                                        },
                                        {
                                            "type": "Sample1",
                                            "name": "count",
                                            "value": "hello"
                                        }
                                    ],
                                    "enums": [
                                        "enum Sample1 {hello};",
                                        "enum Sample2 {goodbye};"
                                    ],
                                    "buffer": 1,
                                    "adjust": "-20%",
                                    "Symbol": "EURUSD",
                                    "Period": "PERIOD_M15",
                                    "ModeOutput": "id",
                                    "TimeStamp": "00:00",
                                    "VisibleID": 0,
                                    "VisibleShift": 0,
                                    "VisibleLimit": 100,
                                    "RangeCandleStart": 5,
                                    "RangeCandleEnd": 15,
                                    "RangeTimeSource": "gmt",
                                    "RangeTimeStart": "01:00",
                                    "RangeTimeEnd": "08:00",
                                    "RangeDayOffset": 0,
                                    "RangeValue": "min",
                                    "shift": "0"
                                }

                            },
                            "right": {
                                "row1": "my_indicators",
                                "row2": "Awesome - Copy",
                                "params": {
                                    "input": [
                                        {
                                            "type": "bool",
                                            "name": "state",
                                            "value": True
                                        },
                                        {
                                            "type": "int",
                                            "name": "count",
                                            "value": 0
                                        }
                                    ],
                                    "enums": [
                                        "enum Sample1 {hello};",
                                        "enum Sample2 {goodbye};"
                                    ],
                                    "buffer": 3,
                                    "adjust": "",
                                    "Symbol": "",
                                    "Period": "PERIOD_CURRENT",
                                    "ModeOutput": "id",
                                    "TimeStamp": "00:00",
                                    "VisibleID": 0,
                                    "VisibleShift": 0,
                                    "VisibleLimit": 100,
                                    "RangeCandleStart": 0,
                                    "RangeCandleEnd": 10,
                                    "RangeTimeSource": "server",
                                    "RangeTimeStart": "01:00",
                                    "RangeTimeEnd": "08:00",
                                    "RangeDayOffset": 0,
                                    "RangeValue": "max",
                                    "shift": "0"
                                }

                            },
                            "adjust": "y",
                            "variable": ""
                        },
                        "id": "a85d21b1-30c4-4130-b015-37fd4733da5e",
                        "id_by_user": 15,
                        "blockName": "Formula",
                        "category": "condition_formula",
                        "block_name_mql": "formula"
                    },
                    {
                        "params": {},
                        "id": "1c5a7352-59e2-4b9b-a65b-04a39af36934",
                        "id_by_user": 16,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                            "takeprofit": "20",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "stoploss": "20",
                            "symbol": "",
                            "group": "",
                            "volume_upper_limit": "0",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "how_much_volume": "0.1"
                        },
                        "id": "30b5af29-7a93-4614-81e3-1a66b9bba636",
                        "id_by_user": 17,
                        "category": "buy_sell",
                        "block_name_mql": "buy_now",
                        "blockName": "Buy now"
                    }
                ],
                "edges": [
                    {
                        "source": "1c5a7352-59e2-4b9b-a65b-04a39af36934",
                        "sourceHandle": "blue",
                        "target": "a85d21b1-30c4-4130-b015-37fd4733da5e",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "22139be1-51fa-4ca5-818d-67b56f998fff"
                    },
                    {
                        "source": "1c5a7352-59e2-4b9b-a65b-04a39af36934",
                        "sourceHandle": "blue",
                        "target": "30b5af29-7a93-4614-81e3-1a66b9bba636",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "a79b4f64-6354-4a65-808e-d0a0064d101a"
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
                "id": "a0f89806-f45d-4bf0-81b8-6749a95e7337",
                "type": "double",
                "name": "y",
                "value": "",
                "description": ""
            },
            {
                "id": "8cef6f63-f5a2-4ff4-a90d-ba22789e1cf4",
                "type": "double",
                "name": "z",
                "value": "",
                "description": ""
            }
        ],
        "constants": [
            {
                "id": "8d0afdbd-b1d2-44d1-b530-7a9833dd9c65",
                "type": "double",
                "name": "x",
                "value": "",
                "description": ""
            }
        ],
        "project_options": {
            "magic_and_other": {
                "magic_number": "55225",
                "expiration_date": " ",
                "on_timer_period": "600"
            },
            "pip_size": {
                "rules": "0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001 \n"
            },
            "description_and_version_number": {
                "copy_right": "test copyright",
                "description": "test description",
                "website_address": "mysite.com  ",
                "version_number": "fsdfsad 125.45"
            },
            "virtual_stops": {
                "virtual_stops": "true",
                "virtual_stops_time_out": 0,
                "emergency_stops": "always",
                "relative_size": 0,
                "add_pips": "100"
            },
            "visual": {
                "display_spread_meter": "true",
                "display_status_messages": "false",
                "display_indicators_after_test": "false"
            }
        }
    },
    "selected_name": "c3af9c3c-6ca3-4317-afd2-81e0e293b7f0",
    "name_by_user": "test",
    "highestIndex": "18"
}

# test generator stability 1
input_data_2 = {
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
            "id": "6a6b0347-309b-4748-8f04-0b7c514fa634",
            "id_by_user": 1,
            "category": "condition_formula",
            "block_name_mql": "condition",
            "blockName": "Condition"
          },
          {
            "params": {
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_ALL",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "order_age_mins": "0",
              "level_color": "clrDeepPink",
              "relative_to": "PRICE_RELATIVE_TO_OPEN_PRICE",
              "new_tpsl_mode": "NEW_STOPS_FIXED",
              "new_stoploss": "50",
              "new_takeprofit": "50"
            },
            "id": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
            "id_by_user": 2,
            "category": "trading_actions",
            "block_name_mql": "modify_stops_of_trades",
            "blockName": "Modify stops of trades"
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
            "id": "cbfe57fc-4bb3-4253-b1ed-6274fbd7aa6c",
            "id_by_user": 3,
            "category": "condition_formula",
            "block_name_mql": "condition",
            "blockName": "Condition"
          },
          {
            "params": {
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrMaroon",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "takeprofit": "20",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "stoploss": "20",
              "symbol": "",
              "group": "",
              "volume_upper_limit": "0",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "how_much_volume": "0.1"
            },
            "id": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
            "id_by_user": 4,
            "category": "buy_sell",
            "block_name_mql": "buy_now",
            "blockName": "Buy now"
          }
        ],
        "edges": [
          {
            "source": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
            "sourceHandle": "blue",
            "target": "6a6b0347-309b-4748-8f04-0b7c514fa634",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "d8c8ccfe-6469-490f-b18c-1a137a1d0ee5"
          },
          {
            "source": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
            "sourceHandle": "blue",
            "target": "cbfe57fc-4bb3-4253-b1ed-6274fbd7aa6c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "593cd5c1-9abe-4dbc-8e32-3de6be2689f4"
          },
          {
            "source": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
            "sourceHandle": "blue",
            "target": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ee804605-8f08-4457-91e2-a6b609836cbe"
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
    "constants": [],
    "project_options": {
      "magic_and_other": {
        "magic_number": 8580,
        "expiration_date": "",
        "on_timer_period": 60
      },
      "pip_size": {
        "rules": "0.001 = 0.01\n0.00001 = 0.0001\n0.000001 = 0.0001 \n"
      },
      "description_and_version_number": {
        "copy_right": "",
        "description": "",
        "website_address": "",
        "version_number": ""
      },
      "virtual_stops": {
        "virtual_stops": False,
        "virtual_stops_time_out": 0,
        "emergency_stops": "no",
        "relative_size": 0,
        "add_pips": 0
      },
      "visual": {
        "display_spread_meter": False,
        "display_status_messages": False,
        "display_indicators_after_test": True
      }
    }
  },
  "selected_name": "2dda19ff-50a6-4e98-801b-67601bab1201",
  "name_by_user": "unnamed",
  "highestIndex": "5"
}
