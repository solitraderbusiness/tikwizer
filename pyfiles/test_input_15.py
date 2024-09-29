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
                "virtual_stops": "True",
                "virtual_stops_time_out": 0,
                "emergency_stops": "always",
                "relative_size": 0,
                "add_pips": "100"
            },
            "visual": {
                "display_spread_meter": "True",
                "display_status_messages": "False",
                "display_indicators_after_test": "False"
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

# test pending open at fix
input_data_3 = {
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
          },
          {
            "params": {
              "symbol": "",
              "group": "",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
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
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              }
            },
            "id": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
            "id_by_user": 5,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
          }
        ],
        "nodesData": [
          {
            "id": "6a6b0347-309b-4748-8f04-0b7c514fa634",
            "type": "customNode",
            "position": {
              "x": -219.5,
              "y": -2.999999999999986
            },
            "data": {
              "id": "6a6b0347-309b-4748-8f04-0b7c514fa634",
              "child_name": "Condition",
              "color_bg": "rgb(255, 220, 169)",
              "color_font": "#222",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": True,
              "slug": "condition",
              "url_to_fetch": "NULL",
              "parent_name": 8,
              "title": "Condition",
              "bgcolor": "rgb(255, 220, 169)",
              "color": "#222",
              "category": "condition_formula",
              "index": 1,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 84,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
            "type": "customNode",
            "position": {
              "x": -255,
              "y": -150
            },
            "data": {
              "id": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
              "child_name": "Modify stops of trades",
              "color_bg": "blue",
              "color_font": "white",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": False,
              "slug": "modify-stops-of-trades",
              "url_to_fetch": "NULL",
              "parent_name": 23,
              "title": "Modify stops of trades",
              "bgcolor": "blue",
              "color": "white",
              "category": "trading_actions",
              "index": 2,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 156,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "cbfe57fc-4bb3-4253-b1ed-6274fbd7aa6c",
            "type": "customNode",
            "position": {
              "x": -78,
              "y": -79
            },
            "data": {
              "id": "cbfe57fc-4bb3-4253-b1ed-6274fbd7aa6c",
              "child_name": "Condition",
              "color_bg": "rgb(255, 220, 169)",
              "color_font": "#222",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": True,
              "slug": "condition",
              "url_to_fetch": "NULL",
              "parent_name": 8,
              "title": "Condition",
              "bgcolor": "rgb(255, 220, 169)",
              "color": "#222",
              "category": "condition_formula",
              "index": 3,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 84,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
            "type": "customNode",
            "position": {
              "x": -373,
              "y": 37
            },
            "data": {
              "id": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
              "child_name": "Buy now",
              "color_bg": "rgb(0, 128, 0)",
              "color_font": "rgb(255, 255, 255)",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": True,
              "slug": "buy-now",
              "url_to_fetch": "NULL",
              "parent_name": 1,
              "title": "Buy now",
              "bgcolor": "rgb(0, 128, 0)",
              "color": "rgb(255, 255, 255)",
              "category": "buy_sell",
              "index": 4,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 76,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
            "type": "customNode",
            "position": {
              "x": -156.67275943419781,
              "y": 141.32407748642126
            },
            "data": {
              "id": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
              "child_name": "Buy pending order",
              "color_bg": "#008000",
              "color_font": "#ccc",
              "id_sent": "2",
              "is_shown": True,
              "is_triple": True,
              "slug": "buy-pending-order",
              "url_to_fetch": "NULL",
              "parent_name": 1,
              "title": "Buy pending order",
              "bgcolor": "#008000",
              "color": "#ccc",
              "category": "buy_sell",
              "index": 5,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 134,
              "height": 24
            },
            "dragging": False
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
          },
          {
            "source": "6a6b0347-309b-4748-8f04-0b7c514fa634",
            "sourceHandle": "blue",
            "target": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "cac05a02-bc13-4bc7-ad6f-b0119cad7301"
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
        "display_spread_meter": True,
        "display_status_messages": True,
        "display_indicators_after_test": True
      }
    }
  },
  "selected_name": "2dda19ff-50a6-4e98-801b-67601bab1201",
  "name_by_user": "unnamed",
  "highestIndex": "6"
}

# test volume profile xindex
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
          },
          {
            "params": {
              "symbol": "",
              "group": "",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
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
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              }
            },
            "id": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
            "id_by_user": 5,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
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
              "Id_user": "+vpr",
              "ShowHorizon": "True",
              "TimeFromColor": "clrDarkGreen",
              "TimeFromStyle": "STYLE_DASH",
              "TimeToColor": "clrDarkGreen",
              "TimeToStyle": "STYLE_DASH",
              "HgWidthPercent": "15",
              "timeFrom_str": "01:00",
              "timeTo_str": "10:00",
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
              "mtp_part_5": "",
              "redraw_each_time": "True"
            },
            "id": "aa7d98c3-dc58-4137-8dd4-359357f398df",
            "id_by_user": 6,
            "blockName": "Volume Profile",
            "category": "various_signals",
            "block_name_mql": "volume_profile"
          }
        ],
        "nodesData": [
          {
            "id": "6a6b0347-309b-4748-8f04-0b7c514fa634",
            "type": "customNode",
            "position": {
              "x": -219.5,
              "y": -2.999999999999986
            },
            "data": {
              "id": "6a6b0347-309b-4748-8f04-0b7c514fa634",
              "child_name": "Condition",
              "color_bg": "rgb(255, 220, 169)",
              "color_font": "#222",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": True,
              "slug": "condition",
              "url_to_fetch": "NULL",
              "parent_name": 8,
              "title": "Condition",
              "bgcolor": "rgb(255, 220, 169)",
              "color": "#222",
              "category": "condition_formula",
              "index": 1,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 84,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
            "type": "customNode",
            "position": {
              "x": -255,
              "y": -150
            },
            "data": {
              "id": "3f6ad442-2c27-4b34-a654-a1ce88ea72ad",
              "child_name": "Modify stops of trades",
              "color_bg": "blue",
              "color_font": "white",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": False,
              "slug": "modify-stops-of-trades",
              "url_to_fetch": "NULL",
              "parent_name": 23,
              "title": "Modify stops of trades",
              "bgcolor": "blue",
              "color": "white",
              "category": "trading_actions",
              "index": 2,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 156,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "cbfe57fc-4bb3-4253-b1ed-6274fbd7aa6c",
            "type": "customNode",
            "position": {
              "x": -78,
              "y": -79
            },
            "data": {
              "id": "cbfe57fc-4bb3-4253-b1ed-6274fbd7aa6c",
              "child_name": "Condition",
              "color_bg": "rgb(255, 220, 169)",
              "color_font": "#222",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": True,
              "slug": "condition",
              "url_to_fetch": "NULL",
              "parent_name": 8,
              "title": "Condition",
              "bgcolor": "rgb(255, 220, 169)",
              "color": "#222",
              "category": "condition_formula",
              "index": 3,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 84,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
            "type": "customNode",
            "position": {
              "x": -373,
              "y": 37
            },
            "data": {
              "id": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
              "child_name": "Buy now",
              "color_bg": "rgb(0, 128, 0)",
              "color_font": "rgb(255, 255, 255)",
              "id_sent": "1",
              "is_shown": True,
              "is_triple": True,
              "slug": "buy-now",
              "url_to_fetch": "NULL",
              "parent_name": 1,
              "title": "Buy now",
              "bgcolor": "rgb(0, 128, 0)",
              "color": "rgb(255, 255, 255)",
              "category": "buy_sell",
              "index": 4,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 76,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
            "type": "customNode",
            "position": {
              "x": -156.67275943419781,
              "y": 141.32407748642126
            },
            "data": {
              "id": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
              "child_name": "Buy pending order",
              "color_bg": "#008000",
              "color_font": "#ccc",
              "id_sent": "2",
              "is_shown": True,
              "is_triple": True,
              "slug": "buy-pending-order",
              "url_to_fetch": "NULL",
              "parent_name": 1,
              "title": "Buy pending order",
              "bgcolor": "#008000",
              "color": "#ccc",
              "category": "buy_sell",
              "index": 5,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 134,
              "height": 24
            },
            "dragging": False
          },
          {
            "id": "aa7d98c3-dc58-4137-8dd4-359357f398df",
            "type": "customNode",
            "position": {
              "x": -375,
              "y": 210
            },
            "data": {
              "id": "aa7d98c3-dc58-4137-8dd4-359357f398df",
              "child_name": "Volume Profile",
              "color_bg": "yellow",
              "color_font": "black",
              "id_sent": "4",
              "is_shown": True,
              "is_triple": False,
              "slug": "volume-profile",
              "url_to_fetch": "NULL",
              "parent_name": 29,
              "title": "Volume Profile",
              "bgcolor": "yellow",
              "color": "black",
              "category": "various_signals",
              "index": 6,
              "loading": False
            },
            "selected": False,
            "measured": {
              "width": 111,
              "height": 24
            },
            "dragging": False
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
          },
          {
            "source": "6a6b0347-309b-4748-8f04-0b7c514fa634",
            "sourceHandle": "blue",
            "target": "c5ba7e7f-4ebe-424c-8807-4a76e1c4bd1e",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "cac05a02-bc13-4bc7-ad6f-b0119cad7301"
          },
          {
            "source": "e0856e95-43d9-4fde-8cf4-dccc3380ce6d",
            "sourceHandle": "blue",
            "target": "aa7d98c3-dc58-4137-8dd4-359357f398df",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "12ba9fe4-0623-42b0-b116-c2f50023c0ae"
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
        "display_spread_meter": True,
        "display_status_messages": True,
        "display_indicators_after_test": True
      }
    }
  },
  "selected_name": "2dda19ff-50a6-4e98-801b-67601bab1201",
  "name_by_user": "unnamed",
  "highestIndex": "7"
}
