
# test tp sl mode : customs
input_data_1 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-0a1a35ad-ff6d-4828-bb13-e544b3d470c3c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "take_profit_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 20,
                                    "adjust": ""
                                }
                            },
                        },
                        "id": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "id_by_user": 4,
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
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test tp sl mode : customs 2
input_data_2 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-0a1a35ad-ff6d-4828-bb13-e544b3d470c3c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_CUSTOM_PRICE_FRACTION",
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "take_profit_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 20,
                                    "adjust": ""
                                }
                            },
                            "stop_loss_price_fraction": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 40,
                                    "adjust": ""
                                }
                            },
                        },
                        "id": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "id_by_user": 4,
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
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test tp sl mode : customs 3
input_data_3 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "b4338921-9e69-4eda-b381-ea3217676107",
                        "sourceHandle": "blue",
                        "target": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-b4338921-9e69-4eda-b381-ea3217676107blue-0a1a35ad-ff6d-4828-bb13-e544b3d470c3c"
                    }
                ],
                "nodes": [
                    {
                        "params": {},
                        "id": "b4338921-9e69-4eda-b381-ea3217676107",
                        "id_by_user": 3,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
                    },
                    {
                        "params": {
                            "symbol": "",
                            "group": "11",
                            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                            "volume_upper_limit": "0",
                            "stop_loss_mode": "TPSL_MODE_CUSTOM_PRICE_LEVEL",
                            "take_profit_mode": "TPSL_MODE_CUSTOM_PIPS",
                            "slippage": "4",
                            "comment": "",
                            "arrow_color": "clrMaroon",
                            "how_much_volume": "0.1",
                            "stoploss": "20",
                            "takeprofit": "20",
                            "take_profit_pips": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 20,
                                    "adjust": ""
                                }
                            },
                            "stop_loss_price_level": {
                                "row1": "value",
                                "row2": "Numeric",
                                "params": {
                                    "value": 40,
                                    "adjust": ""
                                }
                            },
                        },
                        "id": "0a1a35ad-ff6d-4828-bb13-e544b3d470c3",
                        "id_by_user": 4,
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
    "selected_name": "ebc2e384-235e-4b4e-ad19-08fd935321de",
    "name_by_user": "test 8915",
    "highestIndex": "5"
}

# test symbol type change
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
            "params": {},
            "id": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "count_limit": "3",
              "operator": ">",
              "type": "{0,1}"
            },
            "id": "a113bb86-a461-40ec-9d64-403cd42346df",
            "id_by_user": 2,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_trades_count",
            "blockName": "Check trades count"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "fe800d43-f6d9-45c9-af1e-bb812b543d4a",
            "id_by_user": 3,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_tradeorder",
            "blockName": "If trade/order"
          }
        ],
        "edges": [
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "a113bb86-a461-40ec-9d64-403cd42346df",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a7c3ac2e-af07-4bcd-b682-e42e671d2d49"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "fe800d43-f6d9-45c9-af1e-bb812b543d4a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "61f90468-2c79-48a2-bbc8-0a3048c84a7e"
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
    "constants": []
  },
  "selected_name": "72f59944-525b-446c-9f6f-4d3074f77117",
  "name_by_user": "tesdt 5687",
  "highestIndex": "4"
}

# test referenced in run data bug fix
input_data_5 = {
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
            "params": {},
            "id": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "count_limit": "3",
              "operator": ">",
              "type": "{0,1}"
            },
            "id": "a113bb86-a461-40ec-9d64-403cd42346df",
            "id_by_user": 2,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_trades_count",
            "blockName": "Check trades count"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{4,5}",
              "symbols_str": "my_symbols"
            },
            "id": "fe800d43-f6d9-45c9-af1e-bb812b543d4a",
            "id_by_user": 3,
            "blockName": "If trade/order",
            "category": "check_trades_orders_count",
            "block_name_mql": "if_tradeorder"
          },
          {
            "params": {
              "n": "my_number"
            },
            "id": "da0f5cdb-2dea-4ab2-b3ff-0bb089d3c2e5",
            "id_by_user": 4,
            "blockName": "Loop (pass \"n\" times)",
            "category": "counters",
            "block_name_mql": "loop_pass_n_times"
          }
        ],
        "edges": [
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "a113bb86-a461-40ec-9d64-403cd42346df",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a7c3ac2e-af07-4bcd-b682-e42e671d2d49"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "fe800d43-f6d9-45c9-af1e-bb812b543d4a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "61f90468-2c79-48a2-bbc8-0a3048c84a7e"
          },
          {
            "source": "da0f5cdb-2dea-4ab2-b3ff-0bb089d3c2e5",
            "sourceHandle": "blue",
            "target": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "59a5771d-6411-44c7-ad32-e13d118c2858"
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
        "type": "int",
        "name": "my_number",
        "value": "410",
        "description": ""
      }
    ],
    "constants": [
      {
        "type": "string",
        "name": "my_symbols",
        "value": "EURUSD",
        "description": ""
      }
    ]
  },
  "selected_name": "72f59944-525b-446c-9f6f-4d3074f77117",
  "name_by_user": "tesdt 5687",
  "highestIndex": "5"
}

# test symbol type change
input_data_6 = {
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
            "params": {},
            "id": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "count_limit": "3",
              "operator": ">",
              "type": "{0,1}"
            },
            "id": "a113bb86-a461-40ec-9d64-403cd42346df",
            "id_by_user": 2,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_trades_count",
            "blockName": "Check trades count"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,2,4}",
              "symbols_str": "my_symbols_2"
            },
            "id": "fe800d43-f6d9-45c9-af1e-bb812b543d4a",
            "id_by_user": 3,
            "blockName": "If trade/order",
            "category": "check_trades_orders_count",
            "block_name_mql": "if_tradeorder"
          },
          {
            "params": {
              "n": "my_number"
            },
            "id": "da0f5cdb-2dea-4ab2-b3ff-0bb089d3c2e5",
            "id_by_user": 4,
            "blockName": "Loop (pass \"n\" times)",
            "category": "counters",
            "block_name_mql": "loop_pass_n_times"
          }
        ],
        "edges": [
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "a113bb86-a461-40ec-9d64-403cd42346df",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a7c3ac2e-af07-4bcd-b682-e42e671d2d49"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "fe800d43-f6d9-45c9-af1e-bb812b543d4a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "61f90468-2c79-48a2-bbc8-0a3048c84a7e"
          },
          {
            "source": "da0f5cdb-2dea-4ab2-b3ff-0bb089d3c2e5",
            "sourceHandle": "blue",
            "target": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "59a5771d-6411-44c7-ad32-e13d118c2858"
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
        "type": "int",
        "name": "my_number",
        "value": "410",
        "description": ""
      },
      {
        "type": "string",
        "name": "my_symbols_2",
        "value": "XAUUSD,GBPJPY",
        "description": ""
      }
    ],
    "constants": [
      {
        "type": "string",
        "name": "my_symbols",
        "value": "EURUSD",
        "description": ""
      }
    ]
  },
  "selected_name": "72f59944-525b-446c-9f6f-4d3074f77117",
  "name_by_user": "tesdt 5687",
  "highestIndex": "5"
}

# test symbol type change in nearby
input_data_7 = {
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
            "params": {},
            "id": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "n": "my_number"
            },
            "id": "da0f5cdb-2dea-4ab2-b3ff-0bb089d3c2e5",
            "id_by_user": 4,
            "blockName": "Loop (pass \"n\" times)",
            "category": "counters",
            "block_name_mql": "loop_pass_n_times"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "cd4c8b58-fb79-4f31-ac46-1dc9ba4b56c5",
            "id_by_user": 6,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade",
            "blockName": "No trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "027f6b8f-1c1b-4076-ae15-50b293e5f165",
            "id_by_user": 7,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order",
            "blockName": "No pending order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "mode_base_price": "current",
              "mode_range": "pips",
              "range_position": "0",
              "time_1": {
                "row1": "candle",
                "row2": "Candle",
                "params": {
                  "price_mode": "CANDLE_CLOSE",
                  "find_method": "FIND_BY_ID",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "adjust": "",
                  "shift": "0"
                }
              },
              "time_2": {
                "row1": "indicator",
                "row2": "accelerator_oscillator",
                "params": {
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              },
              "range_pips": "10"
            },
            "id": "dee7db18-bb8a-4e47-8523-a5dea0199817",
            "id_by_user": 8,
            "blockName": "No pending order nearby",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order_nearby"
          }
        ],
        "edges": [
          {
            "source": "da0f5cdb-2dea-4ab2-b3ff-0bb089d3c2e5",
            "sourceHandle": "blue",
            "target": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "59a5771d-6411-44c7-ad32-e13d118c2858"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "027f6b8f-1c1b-4076-ae15-50b293e5f165",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "e709dada-4452-43ad-bec8-54011f3b587b"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "cd4c8b58-fb79-4f31-ac46-1dc9ba4b56c5",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a74886b1-98b6-4a80-98c4-238fee04d0db"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "dee7db18-bb8a-4e47-8523-a5dea0199817",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "35a64f1a-cd4b-4b6b-936a-ea35ae05bd6e"
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
        "type": "int",
        "name": "my_number",
        "value": "410",
        "description": ""
      },
      {
        "type": "string",
        "name": "my_symbols_2",
        "value": "XAUUSD,GBPJPY",
        "description": ""
      }
    ],
    "constants": [
      {
        "type": "string",
        "name": "my_symbols",
        "value": "EURUSD",
        "description": ""
      },
      {
        "type": "enum",
        "name": "testenum",
        "value": "{hello}",
        "description": ""
      },
      {
        "type": "testenum",
        "name": "my_test",
        "value": "hello",
        "description": ""
      }
    ]
  },
  "selected_name": "72f59944-525b-446c-9f6f-4d3074f77117",
  "name_by_user": "tesdt 5687",
  "highestIndex": "9"
}

# test symbol type change multiple blocks
input_data_8 = {
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
            "params": {},
            "id": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "type": "{0,1}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "fcda987a-ba21-42cb-aece-49804ba999f7",
            "id_by_user": 8,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade",
            "blockName": "If trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "2316bb25-d732-471b-864a-a77afa443bad",
            "id_by_user": 9,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_pending_order",
            "blockName": "If pending order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "263c6c97-c669-4ecb-891b-ab804cb04e4b",
            "id_by_user": 10,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order",
            "blockName": "No pending order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "mode_base_price": "current",
              "mode_range": "pips",
              "range_position": "0",
              "time_1": {
                "row1": "account",
                "row2": "ACCOUNT_INFO_BALLANCE",
                "params": {
                  "adjust": ""
                }
              },
              "time_2": {
                "row1": "trade-order-in-loop",
                "row2": "IN_LOOP_TRADE_ORDER_CANDLE_ID",
                "params": {
                  "Period_candle_id": "PERIOD_CURRENT",
                  "adjust": ""
                }
              },
              "range_pips": "10"
            },
            "id": "3af478fd-8770-468b-aa1b-c4abb070b3c0",
            "id_by_user": 11,
            "blockName": "No pending order nearby",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order_nearby"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "9b8130c6-6ebf-4525-a6ab-97dfd02a411b",
            "id_by_user": 13,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade",
            "blockName": "For each Trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "10",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "a881ccdd-8224-415a-a8d5-1863afec2da0",
            "id_by_user": 14,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_closed_trade",
            "blockName": "For each Closed Trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
              "pips_on_profit": "15",
              "bep_offset_mode": "BEP_OFFSET_MODE_NONE"
            },
            "id": "126ed278-e964-4653-bff2-9d47c0999efa",
            "id_by_user": 15,
            "category": "trailing_stop_break_even",
            "block_name_mql": "break_even_point_each_trade",
            "blockName": "Break even point (each trade)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "t_step_pips": "1",
              "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
              "t_distance_pips": "30"
            },
            "id": "89af17af-45f7-48e4-9243-7cb319264110",
            "id_by_user": 16,
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_pending_orders",
            "blockName": "Trailing pending orders"
          },
          {
            "params": {
              "symbols_str": "eurusd,gbpusd,audusd"
            },
            "id": "1838212e-3d00-41a4-af54-e8251c2da5ce",
            "id_by_user": 17,
            "blockName": "Set \"Current Market\" for next blocks",
            "category": "controlling_blocks",
            "block_name_mql": "set_current_market_for_next_blocks"
          },
          {
            "params": {
              "ConsecutiveCount": "3",
              "compare": ">=",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "b12269be-fdcb-4658-a2b3-ea3b08cfca84",
            "id_by_user": 18,
            "category": "check_trading_conditions",
            "block_name_mql": "check_consecutive_losses",
            "blockName": "Check consecutive losses"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "LastOrderType": "0",
              "OncePerTrade": "false"
            },
            "id": "d3b6f585-8e87-4f60-a652-f1e44173e181",
            "id_by_user": 19,
            "category": "check_trading_conditions",
            "block_name_mql": "check_type_last_closed",
            "blockName": "Check type (last closed)"
          },
          {
            "params": {
              "ProfitAmount": "0",
              "compare": ">",
              "OncePerTrade": "false",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": ""
            },
            "id": "81e12147-c457-41e6-88d5-460e74346483",
            "id_by_user": 20,
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_last_closed",
            "blockName": "Check profit (last closed)"
          }
        ],
        "edges": [
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "b12269be-fdcb-4658-a2b3-ea3b08cfca84",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "129ba68d-5f55-4e6a-9612-c2efc9b89834"
          },
          {
            "source": "b12269be-fdcb-4658-a2b3-ea3b08cfca84",
            "sourceHandle": "blue",
            "target": "d3b6f585-8e87-4f60-a652-f1e44173e181",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "1fa78c4e-0024-4e2a-a00c-378e39006daa"
          },
          {
            "source": "d3b6f585-8e87-4f60-a652-f1e44173e181",
            "sourceHandle": "blue",
            "target": "81e12147-c457-41e6-88d5-460e74346483",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "2811e2a4-ac22-4d38-9961-6472f6092a57"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "2316bb25-d732-471b-864a-a77afa443bad",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "d563e1e1-c3cf-4004-8661-18ed82c604a3"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "fcda987a-ba21-42cb-aece-49804ba999f7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "b9563f62-c62a-4fa2-82f4-470a279a0b14"
          },
          {
            "source": "fcda987a-ba21-42cb-aece-49804ba999f7",
            "sourceHandle": "blue",
            "target": "263c6c97-c669-4ecb-891b-ab804cb04e4b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f22c5472-5666-4503-8f8d-723a589565fb"
          },
          {
            "source": "2316bb25-d732-471b-864a-a77afa443bad",
            "sourceHandle": "blue",
            "target": "3af478fd-8770-468b-aa1b-c4abb070b3c0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "d21a8e62-3239-45e5-9327-3a87e7d0d9d8"
          },
          {
            "source": "2316bb25-d732-471b-864a-a77afa443bad",
            "sourceHandle": "blue",
            "target": "263c6c97-c669-4ecb-891b-ab804cb04e4b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "fdf15b3c-d954-4e69-89a4-7ab454be3688"
          },
          {
            "source": "fcda987a-ba21-42cb-aece-49804ba999f7",
            "sourceHandle": "blue",
            "target": "3af478fd-8770-468b-aa1b-c4abb070b3c0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "26c119a4-832a-4104-bc7b-da93ce46b112"
          },
          {
            "source": "9b8130c6-6ebf-4525-a6ab-97dfd02a411b",
            "sourceHandle": "blue",
            "target": "a881ccdd-8224-415a-a8d5-1863afec2da0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "895ad4aa-fc4f-40fd-9be6-1b03343042ff"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "9b8130c6-6ebf-4525-a6ab-97dfd02a411b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "bee6892c-f8df-4078-8e3f-fb7442b8a53e"
          },
          {
            "source": "17d87d68-57c5-4eef-93e2-65034b36961c",
            "sourceHandle": "blue",
            "target": "126ed278-e964-4653-bff2-9d47c0999efa",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "84f8a046-c5b3-4ed2-88df-85fa368859ca"
          },
          {
            "source": "126ed278-e964-4653-bff2-9d47c0999efa",
            "sourceHandle": "blue",
            "target": "89af17af-45f7-48e4-9243-7cb319264110",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "4bde0028-d207-4cb6-b96f-9de6baaefa1f"
          },
          {
            "source": "89af17af-45f7-48e4-9243-7cb319264110",
            "sourceHandle": "blue",
            "target": "1838212e-3d00-41a4-af54-e8251c2da5ce",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "efdaba1d-465d-472c-b37c-74dbe85caf10"
          }
        ]
      },
      "on_trade": {
        "nodes": [
          {
            "params": {},
            "id": "26d44f14-5566-48e8-a338-d1d1e65cf9be",
            "id_by_user": 21,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "a9fd2005-a6c4-49b0-ae01-b6bd86b3e469",
            "id_by_user": 22,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_created",
            "blockName": "Trade created"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "close_mode": "",
              "close_partial_mode": "0"
            },
            "id": "9ac1ed43-91d5-4b0f-85c6-40bf2eed8f61",
            "id_by_user": 23,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_closed",
            "blockName": "Trade closed"
          },
          {
            "params": {
              "sl_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "d3fcdd74-89bb-4c28-b764-febc985120e7",
            "id_by_user": 24,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_sl_modified",
            "blockName": "Order SL modified"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "close_mode": ""
            },
            "id": "fbffa5e8-058f-4be9-9887-49626cb93e1b",
            "id_by_user": 25,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_deleted",
            "blockName": "Order deleted"
          }
        ],
        "edges": [
          {
            "source": "26d44f14-5566-48e8-a338-d1d1e65cf9be",
            "sourceHandle": "blue",
            "target": "a9fd2005-a6c4-49b0-ae01-b6bd86b3e469",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "1f25e192-4fb1-4916-a768-965119b1a7d7"
          },
          {
            "source": "a9fd2005-a6c4-49b0-ae01-b6bd86b3e469",
            "sourceHandle": "blue",
            "target": "d3fcdd74-89bb-4c28-b764-febc985120e7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "eec05aff-0f50-4e51-aeb2-459297516198"
          },
          {
            "source": "26d44f14-5566-48e8-a338-d1d1e65cf9be",
            "sourceHandle": "blue",
            "target": "9ac1ed43-91d5-4b0f-85c6-40bf2eed8f61",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "13c8dcaf-ef88-4e80-8e65-126c05595499"
          },
          {
            "source": "9ac1ed43-91d5-4b0f-85c6-40bf2eed8f61",
            "sourceHandle": "blue",
            "target": "fbffa5e8-058f-4be9-9887-49626cb93e1b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "d8d171dc-f417-4936-83ab-7576ca45d050"
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
    "variables": [
      {
        "type": "int",
        "name": "my_number",
        "value": "410",
        "description": ""
      },
      {
        "type": "string",
        "name": "my_symbols_2",
        "value": "XAUUSD,GBPJPY",
        "description": ""
      }
    ],
    "constants": [
      {
        "type": "string",
        "name": "my_symbols",
        "value": "EURUSD",
        "description": ""
      },
      {
        "type": "enum",
        "name": "testenum",
        "value": "{hello}",
        "description": ""
      },
      {
        "type": "testenum",
        "name": "my_test",
        "value": "hello",
        "description": ""
      }
    ]
  },
  "selected_name": "72f59944-525b-446c-9f6f-4d3074f77117",
  "name_by_user": "tesdt 5687",
  "highestIndex": "26"
}

# test symbol type change multiple blocks 2
input_data_9 = {
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
            "params": {},
            "id": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "count_limit": "3",
              "operator": ">",
              "type": "{0,1}"
            },
            "id": "7bb0915d-88eb-4157-9678-cde67bb527de",
            "id_by_user": 2,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_trades_count",
            "blockName": "Check trades count"
          },
          {
            "params": {
              "count_limit": "3",
              "operator": ">",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "919ea4ec-b50a-4e7e-b86f-e0582c4e75a6",
            "id_by_user": 3,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_pending_orders_count",
            "blockName": "Check pending orders count"
          },
          {
            "params": {
              "type": "{0,1}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "4e2e2295-ae27-4aaf-a690-5893555b49c7",
            "id_by_user": 4,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade",
            "blockName": "If trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1,2,3,4,5}"
            },
            "id": "4c4f3997-30c8-4880-a480-6844ce747ac7",
            "id_by_user": 5,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_tradeorder",
            "blockName": "If trade/order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "0f2fc8bf-f57b-4829-97d9-4b809ec562b3",
            "id_by_user": 6,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_pending_order",
            "blockName": "If pending order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "be5c334f-e7e2-435c-b437-7cc87c3e1d06",
            "id_by_user": 7,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade",
            "blockName": "No trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1,2,3,4,5}"
            },
            "id": "b556553a-8e17-4fdf-a352-8cb50e6b7807",
            "id_by_user": 8,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_tradeorder",
            "blockName": "No trade/order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "0aef72c0-43bb-4fe9-9fc7-ecb214f521e0",
            "id_by_user": 9,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order",
            "blockName": "No pending order"
          },
          {
            "params": {
              "mode_range": "pips",
              "range_pips": "10",
              "range_position": "0",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "mode_base_price": "current"
            },
            "id": "5eb60b8a-a148-4b74-9f91-2d74a92037d1",
            "id_by_user": 10,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade_nearby",
            "blockName": "No trade nearby"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "mode_base_price": "current",
              "mode_range": "pips",
              "range_position": "0",
              "time_1": {
                "row1": "object-on-the-chart",
                "row2": "attribute_set_1_numeric",
                "params": {
                  "ObjSource": "name",
                  "Property": "OBJPROP_PRICE1",
                  "Name": "my_object_name"
                }
              },
              "time_2": {
                "row1": "account",
                "row2": "ACCOUNT_INFO_STOPOUT_LEVEL",
                "params": {
                  "adjust": ""
                }
              },
              "range_pips": "10"
            },
            "id": "4ddde398-17a4-4a38-ad35-85e39cbda225",
            "id_by_user": 11,
            "blockName": "No pending order nearby",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order_nearby"
          },
          {
            "params": {
              "ConsecutiveCount": "3",
              "compare": ">=",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "e77bc162-ec9b-4255-9801-16514456f3a3",
            "id_by_user": 12,
            "category": "check_trading_conditions",
            "block_name_mql": "check_consecutive_losses",
            "blockName": "Check consecutive losses"
          },
          {
            "params": {
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "ConsecutiveCount": "3",
              "compare": ">="
            },
            "id": "9576db6e-3510-4867-8ff3-96e5f894930c",
            "id_by_user": 13,
            "category": "check_trading_conditions",
            "block_name_mql": "check_consecutive_profits",
            "blockName": "Check consecutive profits"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "LastOrderType": "0",
              "OncePerTrade": "false"
            },
            "id": "a0537cf5-5374-409c-bb36-1642dccd27a3",
            "id_by_user": 14,
            "category": "check_trading_conditions",
            "block_name_mql": "check_type_last_closed",
            "blockName": "Check type (last closed)"
          },
          {
            "params": {
              "ProfitAmount": "0",
              "compare": ">",
              "OncePerTrade": "false",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": ""
            },
            "id": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "id_by_user": 15,
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_last_closed",
            "blockName": "Check profit (last closed)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "profit_mode": "PROFIT_MODE_PIPS_SUM",
              "compare": ">",
              "profit_amount": "0.0",
              "profit_mode_each": "PROFIT_MODE_NO_MATTER"
            },
            "id": "13860f4c-e4e0-4f00-97ec-a22cdf1b30bf",
            "id_by_user": 16,
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_unrealized",
            "blockName": "Check Profit (unrealized)"
          },
          {
            "params": {
              "DistanceIsAbsolute": "false",
              "compare": ">"
            },
            "id": "8ca25f3f-a591-45dc-a65d-76e8fe729219",
            "id_by_user": 17,
            "category": "check_trading_conditions",
            "block_name_mql": "check_distance",
            "blockName": "Check distance"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "7e84ef0d-3502-4627-8f62-941cea34ce6b",
            "id_by_user": 18,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade",
            "blockName": "For each Trade"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "type_pending": "{2,3,4,5}",
              "type": "{2,3,4,5}",
              "second_output": "always",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first"
            },
            "id": "49f07b50-a2cd-49e0-9a24-fbff3d56e494",
            "id_by_user": 19,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_pending_order",
            "blockName": "For each Pending Order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "10",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "02707afa-f68a-40df-9b59-9a143c0c8f25",
            "id_by_user": 20,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_closed_trade",
            "blockName": "For each Closed Trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
              "pips_on_profit": "15",
              "bep_offset_mode": "BEP_OFFSET_MODE_NONE"
            },
            "id": "13a4fe1d-c771-423a-a677-b0bf62523f8a",
            "id_by_user": 21,
            "category": "trailing_stop_break_even",
            "block_name_mql": "break_even_point_each_trade",
            "blockName": "Break even point (each trade)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "TrailWhat": "1",
              "TrailingReferencePrice": "0",
              "TrailingStopMode": "TRAILING_STOP_MODE_PIP",
              "TrailingStepMode": "TRAILING_STEP_MODE_PIPS",
              "TrailingStartMode": "TRAILING_START_MODE_OFF",
              "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE",
              "LevelColor": "clrDeepPink",
              "symbols_str": "",
              "tStopPips": "40",
              "tStepPips": "1"
            },
            "id": "3970482d-36e3-44da-a398-6e64833b83b5",
            "id_by_user": 22,
            "blockName": "Trailing stop (each trade)",
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_stop_each_trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "t_step_pips": "1",
              "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
              "t_distance_pips": "30"
            },
            "id": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "id_by_user": 23,
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_pending_orders",
            "blockName": "Trailing pending orders"
          },
          {
            "params": {
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "order_age_mins": "0",
              "level_color": "clrDeepPink",
              "relative_to": "PRICE_RELATIVE_TO_OPEN_PRICE",
              "new_tpsl_mode": "NEW_STOPS_FIXED",
              "new_stoploss": "50",
              "new_takeprofit": "50"
            },
            "id": "736fee60-19aa-4701-8e8c-eb3d5554fdbf",
            "id_by_user": 24,
            "category": "trading_actions",
            "block_name_mql": "modify_stops_of_trades",
            "blockName": "Modify stops of trades"
          },
          {
            "params": {
              "slippage": "4",
              "arrow_color": "clrDarkGoldenrod",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "older_than": "0",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "aeac1d1b-9b8a-4488-89ef-71fc42269620",
            "id_by_user": 25,
            "category": "trading_actions",
            "block_name_mql": "close_trades",
            "blockName": "Close trades"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "arrow_color": "clrOlive",
              "symbols_str": ""
            },
            "id": "11b41302-2f48-4c36-806d-e0c0f990a792",
            "id_by_user": 26,
            "blockName": "Delete Pending Orders",
            "category": "trading_actions",
            "block_name_mql": "delete_pending_orders"
          },
          {
            "params": {
              "symbols_str": "eurusd,gbpusd,audusd"
            },
            "id": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "id_by_user": 27,
            "category": "controlling_blocks",
            "block_name_mql": "set_current_market_for_next_blocks",
            "blockName": "Set \"Current Market\" for next blocks"
          }
        ],
        "edges": [
          {
            "source": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "sourceHandle": "blue",
            "target": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "5bc87cab-4f9b-4d58-8d88-09e8d93b9194"
          },
          {
            "source": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "sourceHandle": "blue",
            "target": "7e84ef0d-3502-4627-8f62-941cea34ce6b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ecc5ff10-c9a2-4f68-8794-7223b1834ce5"
          },
          {
            "source": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "sourceHandle": "blue",
            "target": "13a4fe1d-c771-423a-a677-b0bf62523f8a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "696bf2c8-2fd8-484a-bf41-d46eff59b669"
          },
          {
            "source": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "sourceHandle": "blue",
            "target": "e77bc162-ec9b-4255-9801-16514456f3a3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "dbc7490c-714e-4774-b2a3-54f31f61c291"
          },
          {
            "source": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "sourceHandle": "blue",
            "target": "9576db6e-3510-4867-8ff3-96e5f894930c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "506015ba-ecaa-4a4e-9261-272f4b4b74e8"
          },
          {
            "source": "e77bc162-ec9b-4255-9801-16514456f3a3",
            "sourceHandle": "blue",
            "target": "a0537cf5-5374-409c-bb36-1642dccd27a3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f65d871c-29e6-4070-9083-d18e1c0959ac"
          },
          {
            "source": "a0537cf5-5374-409c-bb36-1642dccd27a3",
            "sourceHandle": "blue",
            "target": "13860f4c-e4e0-4f00-97ec-a22cdf1b30bf",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "decf0fd3-5c2e-4b93-800b-664213e03f00"
          },
          {
            "source": "9576db6e-3510-4867-8ff3-96e5f894930c",
            "sourceHandle": "blue",
            "target": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "34d24a4f-40fe-448c-920e-a3af272b1c04"
          },
          {
            "source": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "sourceHandle": "blue",
            "target": "8ca25f3f-a591-45dc-a65d-76e8fe729219",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f0a6a18d-0420-40fa-b779-58dd68d20f5e"
          },
          {
            "source": "13860f4c-e4e0-4f00-97ec-a22cdf1b30bf",
            "sourceHandle": "blue",
            "target": "736fee60-19aa-4701-8e8c-eb3d5554fdbf",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "15da8037-f968-4c61-a3f8-8c82a5abaf96"
          },
          {
            "source": "8ca25f3f-a591-45dc-a65d-76e8fe729219",
            "sourceHandle": "blue",
            "target": "aeac1d1b-9b8a-4488-89ef-71fc42269620",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a83ff7d1-78d3-490b-aab9-1d3daf925bf7"
          },
          {
            "source": "8ca25f3f-a591-45dc-a65d-76e8fe729219",
            "sourceHandle": "blue",
            "target": "11b41302-2f48-4c36-806d-e0c0f990a792",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "bd378430-ce2b-4249-8560-9e2e8af0469b"
          },
          {
            "source": "7e84ef0d-3502-4627-8f62-941cea34ce6b",
            "sourceHandle": "blue",
            "target": "49f07b50-a2cd-49e0-9a24-fbff3d56e494",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "08542aa0-2e4b-4a39-88e1-860cb6f1736b"
          },
          {
            "source": "49f07b50-a2cd-49e0-9a24-fbff3d56e494",
            "sourceHandle": "blue",
            "target": "02707afa-f68a-40df-9b59-9a143c0c8f25",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "c6986f0b-03f8-4cfa-8044-410137f1c75b"
          },
          {
            "source": "13a4fe1d-c771-423a-a677-b0bf62523f8a",
            "sourceHandle": "blue",
            "target": "3970482d-36e3-44da-a398-6e64833b83b5",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "2181c1b4-552a-4c56-abe4-2f419e8f0552"
          },
          {
            "source": "3970482d-36e3-44da-a398-6e64833b83b5",
            "sourceHandle": "blue",
            "target": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "65f1cae8-a358-4d33-b019-140dd99bae3b"
          },
          {
            "source": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "sourceHandle": "blue",
            "target": "919ea4ec-b50a-4e7e-b86f-e0582c4e75a6",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "040ced91-0a1f-4d15-b1f6-96d5d6b69380"
          },
          {
            "source": "919ea4ec-b50a-4e7e-b86f-e0582c4e75a6",
            "sourceHandle": "blue",
            "target": "4c4f3997-30c8-4880-a480-6844ce747ac7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "3fb32ad5-cc8d-46a3-995f-739ffd16b6b3"
          },
          {
            "source": "4c4f3997-30c8-4880-a480-6844ce747ac7",
            "sourceHandle": "blue",
            "target": "be5c334f-e7e2-435c-b437-7cc87c3e1d06",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "74ce54db-fac3-45dc-9f07-0abe6980f655"
          },
          {
            "source": "be5c334f-e7e2-435c-b437-7cc87c3e1d06",
            "sourceHandle": "blue",
            "target": "0aef72c0-43bb-4fe9-9fc7-ecb214f521e0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "78ef36d3-ef34-40c3-b01b-93a7f370b7ff"
          },
          {
            "source": "0aef72c0-43bb-4fe9-9fc7-ecb214f521e0",
            "sourceHandle": "blue",
            "target": "4ddde398-17a4-4a38-ad35-85e39cbda225",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "61c9ddcf-0b38-4d2a-8fd8-15b48d5988ae"
          },
          {
            "source": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "sourceHandle": "blue",
            "target": "7bb0915d-88eb-4157-9678-cde67bb527de",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "b16ef988-eea4-4065-8ea5-aaa19b87b3d7"
          },
          {
            "source": "7bb0915d-88eb-4157-9678-cde67bb527de",
            "sourceHandle": "blue",
            "target": "4e2e2295-ae27-4aaf-a690-5893555b49c7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "1441071f-c6bb-490a-9414-cac6addcea9c"
          },
          {
            "source": "4e2e2295-ae27-4aaf-a690-5893555b49c7",
            "sourceHandle": "blue",
            "target": "0f2fc8bf-f57b-4829-97d9-4b809ec562b3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "39ca8490-d47a-4eba-a2c4-141d2dec64fb"
          },
          {
            "source": "0f2fc8bf-f57b-4829-97d9-4b809ec562b3",
            "sourceHandle": "blue",
            "target": "b556553a-8e17-4fdf-a352-8cb50e6b7807",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f6efaa9c-6d00-4168-9881-f8ef352ab1ec"
          },
          {
            "source": "b556553a-8e17-4fdf-a352-8cb50e6b7807",
            "sourceHandle": "blue",
            "target": "5eb60b8a-a148-4b74-9f91-2d74a92037d1",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "893ee9f9-1b74-4c38-8928-476890e478e8"
          }
        ]
      },
      "on_trade": {
        "nodes": [
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "symbols_str": ""
            },
            "id": "2562f477-c298-47a9-97ef-cb3446f0bdc1",
            "id_by_user": 28,
            "blockName": "Trade created",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_created"
          },
          {
            "params": {
              "stops_mode": "some",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "group_number": "11",
              "symbols_str": ""
            },
            "id": "780ebaec-893e-4985-b6aa-690480a51c46",
            "id_by_user": 29,
            "blockName": "Trade stops modified",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_stops_modified"
          },
          {
            "params": {
              "sl_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "88864476-a665-4c7f-8a31-ae1326c25533",
            "id_by_user": 30,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_sl_modified",
            "blockName": "Trade SL modified"
          },
          {
            "params": {
              "tp_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "e76b5f30-ba42-4c75-b9c8-a2a8f9fbf97a",
            "id_by_user": 31,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_tp_modified",
            "blockName": "Trade TP modified"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "close_mode": "",
              "close_partial_mode": "0"
            },
            "id": "f9d3b7ee-2ae9-4bf4-8871-d9f9e14f747a",
            "id_by_user": 32,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_closed",
            "blockName": "Trade closed"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "ca6ab966-bad0-40d4-b274-46e77635b66b",
            "id_by_user": 33,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_created",
            "blockName": "Order created"
          },
          {
            "params": {
              "stops_mode": "some",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "535b4360-df9b-48cf-bc97-37d76ca59dee",
            "id_by_user": 34,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_stops_modified",
            "blockName": "Order stops modified"
          },
          {
            "params": {
              "sl_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "group_number": "11",
              "symbols_str": ""
            },
            "id": "b92fed55-87ab-4864-a5c0-127fc9a79d8b",
            "id_by_user": 35,
            "blockName": "Order SL modified",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_sl_modified"
          },
          {
            "params": {
              "tp_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "group_number": "11",
              "symbols_str": ""
            },
            "id": "1cc2480b-6e51-4de3-a134-02bfe81a3cce",
            "id_by_user": 36,
            "blockName": "Order TP modified",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_tp_modified"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "close_mode": ""
            },
            "id": "373b4e5a-79f2-496d-b4ab-77d177080b6f",
            "id_by_user": 37,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_deleted",
            "blockName": "Order deleted"
          },
          {
            "params": {},
            "id": "20f6877c-a355-4dfe-a493-d69ba876432d",
            "id_by_user": 38,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          }
        ],
        "edges": [
          {
            "source": "20f6877c-a355-4dfe-a493-d69ba876432d",
            "sourceHandle": "blue",
            "target": "2562f477-c298-47a9-97ef-cb3446f0bdc1",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "2e0c5973-6334-4dc5-84f4-1ef4cc20092e"
          },
          {
            "source": "2562f477-c298-47a9-97ef-cb3446f0bdc1",
            "sourceHandle": "blue",
            "target": "88864476-a665-4c7f-8a31-ae1326c25533",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "de405bc6-bcf1-4f4e-bc2d-c7161da94191"
          },
          {
            "source": "88864476-a665-4c7f-8a31-ae1326c25533",
            "sourceHandle": "blue",
            "target": "f9d3b7ee-2ae9-4bf4-8871-d9f9e14f747a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "cac4ba09-2db3-4281-b0ec-2cb69228078b"
          },
          {
            "source": "f9d3b7ee-2ae9-4bf4-8871-d9f9e14f747a",
            "sourceHandle": "blue",
            "target": "535b4360-df9b-48cf-bc97-37d76ca59dee",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ff31ff28-11d3-4f58-a7fc-79b250d62841"
          },
          {
            "source": "535b4360-df9b-48cf-bc97-37d76ca59dee",
            "sourceHandle": "blue",
            "target": "1cc2480b-6e51-4de3-a134-02bfe81a3cce",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f954d405-2782-48a7-9ed3-c066348947c8"
          },
          {
            "source": "20f6877c-a355-4dfe-a493-d69ba876432d",
            "sourceHandle": "blue",
            "target": "780ebaec-893e-4985-b6aa-690480a51c46",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "16905f89-f818-428d-8149-1a0ac5c7439e"
          },
          {
            "source": "780ebaec-893e-4985-b6aa-690480a51c46",
            "sourceHandle": "blue",
            "target": "e76b5f30-ba42-4c75-b9c8-a2a8f9fbf97a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "b6379a62-7da8-4d97-a6af-f6c15e605552"
          },
          {
            "source": "e76b5f30-ba42-4c75-b9c8-a2a8f9fbf97a",
            "sourceHandle": "blue",
            "target": "ca6ab966-bad0-40d4-b274-46e77635b66b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "16e19c15-b86a-47de-b6ae-e6253e8ecb7d"
          },
          {
            "source": "ca6ab966-bad0-40d4-b274-46e77635b66b",
            "sourceHandle": "blue",
            "target": "b92fed55-87ab-4864-a5c0-127fc9a79d8b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "fcc68752-3195-4d8c-8095-99577ed2b0c8"
          },
          {
            "source": "b92fed55-87ab-4864-a5c0-127fc9a79d8b",
            "sourceHandle": "blue",
            "target": "373b4e5a-79f2-496d-b4ab-77d177080b6f",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a2aff953-5bed-47cb-9afc-eb4d82d8c01c"
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
  "selected_name": "486c0457-63a2-4ed1-8ea0-0a8baacf12d8",
  "name_by_user": "",
  "highestIndex": "39"
}

# test symbol type change multiple blocks 3
input_data_10 = {
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
            "params": {},
            "id": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "count_limit": "3",
              "operator": ">",
              "type": "{0,1}"
            },
            "id": "7bb0915d-88eb-4157-9678-cde67bb527de",
            "id_by_user": 2,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_trades_count",
            "blockName": "Check trades count"
          },
          {
            "params": {
              "count_limit": "3",
              "operator": ">",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "919ea4ec-b50a-4e7e-b86f-e0582c4e75a6",
            "id_by_user": 3,
            "category": "check_trades_orders_count",
            "block_name_mql": "check_pending_orders_count",
            "blockName": "Check pending orders count"
          },
          {
            "params": {
              "type": "{0,1}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "4e2e2295-ae27-4aaf-a690-5893555b49c7",
            "id_by_user": 4,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade",
            "blockName": "If trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1,2,3,4,5}"
            },
            "id": "4c4f3997-30c8-4880-a480-6844ce747ac7",
            "id_by_user": 5,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_tradeorder",
            "blockName": "If trade/order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "0f2fc8bf-f57b-4829-97d9-4b809ec562b3",
            "id_by_user": 6,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_pending_order",
            "blockName": "If pending order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "be5c334f-e7e2-435c-b437-7cc87c3e1d06",
            "id_by_user": 7,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade",
            "blockName": "No trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1,2,3,4,5}"
            },
            "id": "b556553a-8e17-4fdf-a352-8cb50e6b7807",
            "id_by_user": 8,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_tradeorder",
            "blockName": "No trade/order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "0aef72c0-43bb-4fe9-9fc7-ecb214f521e0",
            "id_by_user": 9,
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order",
            "blockName": "No pending order"
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
                "row1": "candle",
                "row2": "Candle",
                "params": {
                  "price_mode": "CANDLE_CLOSE",
                  "find_method": "FIND_BY_ID",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "adjust": "",
                  "shift": "0"
                }
              },
              "time_2": {
                "row1": "trade-order-in-loop",
                "row2": "IN_LOOP_TRADE_ORDER_CANDLE_ID",
                "params": {
                  "Period_candle_id": "PERIOD_CURRENT",
                  "adjust": ""
                }
              },
              "range_pips": "10"
            },
            "id": "5eb60b8a-a148-4b74-9f91-2d74a92037d1",
            "id_by_user": 10,
            "blockName": "No trade nearby",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade_nearby"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "mode_base_price": "current",
              "mode_range": "pips",
              "range_position": "0",
              "time_1": {
                "row1": "object-on-the-chart",
                "row2": "attribute_set_1_numeric",
                "params": {
                  "ObjSource": "name",
                  "Property": "OBJPROP_PRICE1",
                  "Name": "my_object_name"
                }
              },
              "time_2": {
                "row1": "account",
                "row2": "ACCOUNT_INFO_STOPOUT_LEVEL",
                "params": {
                  "adjust": ""
                }
              },
              "range_pips": "10"
            },
            "id": "4ddde398-17a4-4a38-ad35-85e39cbda225",
            "id_by_user": 11,
            "blockName": "No pending order nearby",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order_nearby"
          },
          {
            "params": {
              "ConsecutiveCount": "3",
              "compare": ">=",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "e77bc162-ec9b-4255-9801-16514456f3a3",
            "id_by_user": 12,
            "category": "check_trading_conditions",
            "block_name_mql": "check_consecutive_losses",
            "blockName": "Check consecutive losses"
          },
          {
            "params": {
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "ConsecutiveCount": "3",
              "compare": ">="
            },
            "id": "9576db6e-3510-4867-8ff3-96e5f894930c",
            "id_by_user": 13,
            "category": "check_trading_conditions",
            "block_name_mql": "check_consecutive_profits",
            "blockName": "Check consecutive profits"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "LastOrderType": "0",
              "OncePerTrade": "false"
            },
            "id": "a0537cf5-5374-409c-bb36-1642dccd27a3",
            "id_by_user": 14,
            "category": "check_trading_conditions",
            "block_name_mql": "check_type_last_closed",
            "blockName": "Check type (last closed)"
          },
          {
            "params": {
              "ProfitAmount": "0",
              "compare": ">",
              "OncePerTrade": "false",
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": ""
            },
            "id": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "id_by_user": 15,
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_last_closed",
            "blockName": "Check profit (last closed)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "profit_mode": "PROFIT_MODE_PIPS_SUM",
              "compare": ">",
              "profit_amount": "0.0",
              "profit_mode_each": "PROFIT_MODE_NO_MATTER"
            },
            "id": "13860f4c-e4e0-4f00-97ec-a22cdf1b30bf",
            "id_by_user": 16,
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_unrealized",
            "blockName": "Check Profit (unrealized)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "7e84ef0d-3502-4627-8f62-941cea34ce6b",
            "id_by_user": 18,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade",
            "blockName": "For each Trade"
          },
          {
            "params": {
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "type_pending": "{2,3,4,5}",
              "type": "{2,3,4,5}",
              "second_output": "always",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first"
            },
            "id": "49f07b50-a2cd-49e0-9a24-fbff3d56e494",
            "id_by_user": 19,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_pending_order",
            "blockName": "For each Pending Order"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "10",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "02707afa-f68a-40df-9b59-9a143c0c8f25",
            "id_by_user": 20,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_closed_trade",
            "blockName": "For each Closed Trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
              "pips_on_profit": "15",
              "bep_offset_mode": "BEP_OFFSET_MODE_NONE"
            },
            "id": "13a4fe1d-c771-423a-a677-b0bf62523f8a",
            "id_by_user": 21,
            "category": "trailing_stop_break_even",
            "block_name_mql": "break_even_point_each_trade",
            "blockName": "Break even point (each trade)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "TrailWhat": "1",
              "TrailingReferencePrice": "0",
              "TrailingStopMode": "TRAILING_STOP_MODE_PIP",
              "TrailingStepMode": "TRAILING_STEP_MODE_PIPS",
              "TrailingStartMode": "TRAILING_START_MODE_OFF",
              "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE",
              "LevelColor": "clrDeepPink",
              "symbols_str": "",
              "tStopPips": "40",
              "tStepPips": "1"
            },
            "id": "3970482d-36e3-44da-a398-6e64833b83b5",
            "id_by_user": 22,
            "blockName": "Trailing stop (each trade)",
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_stop_each_trade"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "t_step_pips": "1",
              "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
              "t_distance_pips": "30"
            },
            "id": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "id_by_user": 23,
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_pending_orders",
            "blockName": "Trailing pending orders"
          },
          {
            "params": {
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "order_age_mins": "0",
              "level_color": "clrDeepPink",
              "relative_to": "PRICE_RELATIVE_TO_OPEN_PRICE",
              "new_tpsl_mode": "NEW_STOPS_FIXED",
              "new_stoploss": "50",
              "new_takeprofit": "50"
            },
            "id": "736fee60-19aa-4701-8e8c-eb3d5554fdbf",
            "id_by_user": 24,
            "category": "trading_actions",
            "block_name_mql": "modify_stops_of_trades",
            "blockName": "Modify stops of trades"
          },
          {
            "params": {
              "slippage": "4",
              "arrow_color": "clrDarkGoldenrod",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "older_than": "0",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "aeac1d1b-9b8a-4488-89ef-71fc42269620",
            "id_by_user": 25,
            "category": "trading_actions",
            "block_name_mql": "close_trades",
            "blockName": "Close trades"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "arrow_color": "clrOlive",
              "symbols_str": ""
            },
            "id": "11b41302-2f48-4c36-806d-e0c0f990a792",
            "id_by_user": 26,
            "blockName": "Delete Pending Orders",
            "category": "trading_actions",
            "block_name_mql": "delete_pending_orders"
          },
          {
            "params": {
              "symbols_str": "eurusd,gbpusd,audusd"
            },
            "id": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "id_by_user": 27,
            "category": "controlling_blocks",
            "block_name_mql": "set_current_market_for_next_blocks",
            "blockName": "Set \"Current Market\" for next blocks"
          }
        ],
        "edges": [
          {
            "source": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "sourceHandle": "blue",
            "target": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "5bc87cab-4f9b-4d58-8d88-09e8d93b9194"
          },
          {
            "source": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "sourceHandle": "blue",
            "target": "7e84ef0d-3502-4627-8f62-941cea34ce6b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ecc5ff10-c9a2-4f68-8794-7223b1834ce5"
          },
          {
            "source": "3f25db3e-681c-4535-8c2f-e7bb7fb99570",
            "sourceHandle": "blue",
            "target": "13a4fe1d-c771-423a-a677-b0bf62523f8a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "696bf2c8-2fd8-484a-bf41-d46eff59b669"
          },
          {
            "source": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "sourceHandle": "blue",
            "target": "e77bc162-ec9b-4255-9801-16514456f3a3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "dbc7490c-714e-4774-b2a3-54f31f61c291"
          },
          {
            "source": "7f389702-a286-4b3c-816c-a9e2aae67768",
            "sourceHandle": "blue",
            "target": "9576db6e-3510-4867-8ff3-96e5f894930c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "506015ba-ecaa-4a4e-9261-272f4b4b74e8"
          },
          {
            "source": "e77bc162-ec9b-4255-9801-16514456f3a3",
            "sourceHandle": "blue",
            "target": "a0537cf5-5374-409c-bb36-1642dccd27a3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f65d871c-29e6-4070-9083-d18e1c0959ac"
          },
          {
            "source": "a0537cf5-5374-409c-bb36-1642dccd27a3",
            "sourceHandle": "blue",
            "target": "13860f4c-e4e0-4f00-97ec-a22cdf1b30bf",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "decf0fd3-5c2e-4b93-800b-664213e03f00"
          },
          {
            "source": "9576db6e-3510-4867-8ff3-96e5f894930c",
            "sourceHandle": "blue",
            "target": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "34d24a4f-40fe-448c-920e-a3af272b1c04"
          },
          {
            "source": "13860f4c-e4e0-4f00-97ec-a22cdf1b30bf",
            "sourceHandle": "blue",
            "target": "736fee60-19aa-4701-8e8c-eb3d5554fdbf",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "15da8037-f968-4c61-a3f8-8c82a5abaf96"
          },
          {
            "source": "7e84ef0d-3502-4627-8f62-941cea34ce6b",
            "sourceHandle": "blue",
            "target": "49f07b50-a2cd-49e0-9a24-fbff3d56e494",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "08542aa0-2e4b-4a39-88e1-860cb6f1736b"
          },
          {
            "source": "49f07b50-a2cd-49e0-9a24-fbff3d56e494",
            "sourceHandle": "blue",
            "target": "02707afa-f68a-40df-9b59-9a143c0c8f25",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "c6986f0b-03f8-4cfa-8044-410137f1c75b"
          },
          {
            "source": "13a4fe1d-c771-423a-a677-b0bf62523f8a",
            "sourceHandle": "blue",
            "target": "3970482d-36e3-44da-a398-6e64833b83b5",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "2181c1b4-552a-4c56-abe4-2f419e8f0552"
          },
          {
            "source": "3970482d-36e3-44da-a398-6e64833b83b5",
            "sourceHandle": "blue",
            "target": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "65f1cae8-a358-4d33-b019-140dd99bae3b"
          },
          {
            "source": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "sourceHandle": "blue",
            "target": "919ea4ec-b50a-4e7e-b86f-e0582c4e75a6",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "040ced91-0a1f-4d15-b1f6-96d5d6b69380"
          },
          {
            "source": "919ea4ec-b50a-4e7e-b86f-e0582c4e75a6",
            "sourceHandle": "blue",
            "target": "4c4f3997-30c8-4880-a480-6844ce747ac7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "3fb32ad5-cc8d-46a3-995f-739ffd16b6b3"
          },
          {
            "source": "4c4f3997-30c8-4880-a480-6844ce747ac7",
            "sourceHandle": "blue",
            "target": "be5c334f-e7e2-435c-b437-7cc87c3e1d06",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "74ce54db-fac3-45dc-9f07-0abe6980f655"
          },
          {
            "source": "be5c334f-e7e2-435c-b437-7cc87c3e1d06",
            "sourceHandle": "blue",
            "target": "0aef72c0-43bb-4fe9-9fc7-ecb214f521e0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "78ef36d3-ef34-40c3-b01b-93a7f370b7ff"
          },
          {
            "source": "0aef72c0-43bb-4fe9-9fc7-ecb214f521e0",
            "sourceHandle": "blue",
            "target": "4ddde398-17a4-4a38-ad35-85e39cbda225",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "61c9ddcf-0b38-4d2a-8fd8-15b48d5988ae"
          },
          {
            "source": "a66e5b54-8ab8-4e95-bf70-913d6bd4f57a",
            "sourceHandle": "blue",
            "target": "7bb0915d-88eb-4157-9678-cde67bb527de",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "b16ef988-eea4-4065-8ea5-aaa19b87b3d7"
          },
          {
            "source": "7bb0915d-88eb-4157-9678-cde67bb527de",
            "sourceHandle": "blue",
            "target": "4e2e2295-ae27-4aaf-a690-5893555b49c7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "1441071f-c6bb-490a-9414-cac6addcea9c"
          },
          {
            "source": "4e2e2295-ae27-4aaf-a690-5893555b49c7",
            "sourceHandle": "blue",
            "target": "0f2fc8bf-f57b-4829-97d9-4b809ec562b3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "39ca8490-d47a-4eba-a2c4-141d2dec64fb"
          },
          {
            "source": "0f2fc8bf-f57b-4829-97d9-4b809ec562b3",
            "sourceHandle": "blue",
            "target": "b556553a-8e17-4fdf-a352-8cb50e6b7807",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f6efaa9c-6d00-4168-9881-f8ef352ab1ec"
          },
          {
            "source": "b556553a-8e17-4fdf-a352-8cb50e6b7807",
            "sourceHandle": "blue",
            "target": "5eb60b8a-a148-4b74-9f91-2d74a92037d1",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "893ee9f9-1b74-4c38-8928-476890e478e8"
          },
          {
            "source": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "sourceHandle": "blue",
            "target": "aeac1d1b-9b8a-4488-89ef-71fc42269620",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "c1e91134-2093-4eb1-9246-c0d207f54ab4"
          },
          {
            "source": "a6f15f28-2d99-47b4-b8db-8faef85fd880",
            "sourceHandle": "blue",
            "target": "11b41302-2f48-4c36-806d-e0c0f990a792",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "bed7f7ce-ce96-4758-aace-d3a7c94efce9"
          }
        ]
      },
      "on_trade": {
        "nodes": [
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "symbols_str": ""
            },
            "id": "2562f477-c298-47a9-97ef-cb3446f0bdc1",
            "id_by_user": 28,
            "blockName": "Trade created",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_created"
          },
          {
            "params": {
              "stops_mode": "some",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "group_number": "11",
              "symbols_str": ""
            },
            "id": "780ebaec-893e-4985-b6aa-690480a51c46",
            "id_by_user": 29,
            "blockName": "Trade stops modified",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_stops_modified"
          },
          {
            "params": {
              "sl_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "88864476-a665-4c7f-8a31-ae1326c25533",
            "id_by_user": 30,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_sl_modified",
            "blockName": "Trade SL modified"
          },
          {
            "params": {
              "tp_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}"
            },
            "id": "e76b5f30-ba42-4c75-b9c8-a2a8f9fbf97a",
            "id_by_user": 31,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_tp_modified",
            "blockName": "Trade TP modified"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "close_mode": "",
              "close_partial_mode": "0"
            },
            "id": "f9d3b7ee-2ae9-4bf4-8871-d9f9e14f747a",
            "id_by_user": 32,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "trade_closed",
            "blockName": "Trade closed"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "ca6ab966-bad0-40d4-b274-46e77635b66b",
            "id_by_user": 33,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_created",
            "blockName": "Order created"
          },
          {
            "params": {
              "stops_mode": "some",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}"
            },
            "id": "535b4360-df9b-48cf-bc97-37d76ca59dee",
            "id_by_user": 34,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_stops_modified",
            "blockName": "Order stops modified"
          },
          {
            "params": {
              "sl_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "group_number": "11",
              "symbols_str": ""
            },
            "id": "b92fed55-87ab-4864-a5c0-127fc9a79d8b",
            "id_by_user": 35,
            "blockName": "Order SL modified",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_sl_modified"
          },
          {
            "params": {
              "tp_only": "no",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "group_number": "11",
              "symbols_str": ""
            },
            "id": "1cc2480b-6e51-4de3-a134-02bfe81a3cce",
            "id_by_user": 36,
            "blockName": "Order TP modified",
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_tp_modified"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "close_mode": ""
            },
            "id": "373b4e5a-79f2-496d-b4ab-77d177080b6f",
            "id_by_user": 37,
            "category": "on_trade_filter_specific_event",
            "block_name_mql": "order_deleted",
            "blockName": "Order deleted"
          },
          {
            "params": {},
            "id": "20f6877c-a355-4dfe-a493-d69ba876432d",
            "id_by_user": 38,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          }
        ],
        "edges": [
          {
            "source": "20f6877c-a355-4dfe-a493-d69ba876432d",
            "sourceHandle": "blue",
            "target": "2562f477-c298-47a9-97ef-cb3446f0bdc1",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "2e0c5973-6334-4dc5-84f4-1ef4cc20092e"
          },
          {
            "source": "2562f477-c298-47a9-97ef-cb3446f0bdc1",
            "sourceHandle": "blue",
            "target": "88864476-a665-4c7f-8a31-ae1326c25533",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "de405bc6-bcf1-4f4e-bc2d-c7161da94191"
          },
          {
            "source": "88864476-a665-4c7f-8a31-ae1326c25533",
            "sourceHandle": "blue",
            "target": "f9d3b7ee-2ae9-4bf4-8871-d9f9e14f747a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "cac4ba09-2db3-4281-b0ec-2cb69228078b"
          },
          {
            "source": "f9d3b7ee-2ae9-4bf4-8871-d9f9e14f747a",
            "sourceHandle": "blue",
            "target": "535b4360-df9b-48cf-bc97-37d76ca59dee",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ff31ff28-11d3-4f58-a7fc-79b250d62841"
          },
          {
            "source": "535b4360-df9b-48cf-bc97-37d76ca59dee",
            "sourceHandle": "blue",
            "target": "1cc2480b-6e51-4de3-a134-02bfe81a3cce",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "f954d405-2782-48a7-9ed3-c066348947c8"
          },
          {
            "source": "20f6877c-a355-4dfe-a493-d69ba876432d",
            "sourceHandle": "blue",
            "target": "780ebaec-893e-4985-b6aa-690480a51c46",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "16905f89-f818-428d-8149-1a0ac5c7439e"
          },
          {
            "source": "780ebaec-893e-4985-b6aa-690480a51c46",
            "sourceHandle": "blue",
            "target": "e76b5f30-ba42-4c75-b9c8-a2a8f9fbf97a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "b6379a62-7da8-4d97-a6af-f6c15e605552"
          },
          {
            "source": "e76b5f30-ba42-4c75-b9c8-a2a8f9fbf97a",
            "sourceHandle": "blue",
            "target": "ca6ab966-bad0-40d4-b274-46e77635b66b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "16e19c15-b86a-47de-b6ae-e6253e8ecb7d"
          },
          {
            "source": "ca6ab966-bad0-40d4-b274-46e77635b66b",
            "sourceHandle": "blue",
            "target": "b92fed55-87ab-4864-a5c0-127fc9a79d8b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "fcc68752-3195-4d8c-8095-99577ed2b0c8"
          },
          {
            "source": "b92fed55-87ab-4864-a5c0-127fc9a79d8b",
            "sourceHandle": "blue",
            "target": "373b4e5a-79f2-496d-b4ab-77d177080b6f",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "a2aff953-5bed-47cb-9afc-eb4d82d8c01c"
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
  "selected_name": "486c0457-63a2-4ed1-8ea0-0a8baacf12d8",
  "name_by_user": "",
  "highestIndex": "39"
}

# test order select addition to OrderModify blocks
input_data_11 = {
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
            "params": {},
            "id": "bfaed0f1-abbc-4aee-ba6a-59f82b68f3e8",
            "id_by_user": 1,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "loop_direction": "newest_first",
              "second_output": "always"
            },
            "id": "e5eb8b78-f03a-4982-b9d9-580256522ac1",
            "id_by_user": 2,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade",
            "blockName": "For each Trade"
          },
          {
            "params": {
              "RelativeTo": "openprice",
              "LevelColor": "clrDeepPink",
              "NewSLmode": "fixed",
              "NewStopLoss": "50",
              "NewTPmode": "fixed",
              "NewTakeProfit": "50"
            },
            "id": "6d6cbcdd-96cc-4d19-a4ea-35a2bdd6c772",
            "id_by_user": 3,
            "category": "loop_for_trades_orders",
            "block_name_mql": "modify_stops",
            "blockName": "modify stops"
          },
          {
            "params": {
              "type": "{0,1}",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "order_age_mins": "0",
              "level_color": "clrDeepPink",
              "relative_to": "PRICE_RELATIVE_TO_OPEN_PRICE",
              "new_tpsl_mode": "NEW_STOPS_FIXED",
              "new_stoploss": "50",
              "new_takeprofit": "50"
            },
            "id": "c1cdfd0a-9392-4cc3-8ff3-c8c8eb823ec7",
            "id_by_user": 4,
            "category": "trading_actions",
            "block_name_mql": "modify_stops_of_trades",
            "blockName": "Modify stops of trades"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
              "pips_on_profit": "15",
              "bep_offset_mode": "BEP_OFFSET_MODE_NONE"
            },
            "id": "85f8e9c7-dbd1-4561-af46-6bd8b4e465b7",
            "id_by_user": 5,
            "category": "trailing_stop_break_even",
            "block_name_mql": "break_even_point_each_trade",
            "blockName": "Break even point (each trade)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "TrailingStopMode": "TRAILING_STOP_MODE_PIP",
              "tStopPips": "40",
              "TrailingStepMode": "TRAILING_STEP_MODE_PIPS",
              "tStepPips": "1",
              "TrailWhat": "1",
              "TrailingReferencePrice": "0",
              "TrailingStartMode": "TRAILING_START_MODE_OFF",
              "LevelColor": "clrDeepPink",
              "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_NO_CHANGE"
            },
            "id": "4ae94ca9-9e61-4166-a9d1-2fa4699c2427",
            "id_by_user": 6,
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_stop_each_trade",
            "blockName": "Trailing stop (each trade)"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "type": "{2,3,4,5}",
              "type_pending": "{2,3,4,5}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "t_step_pips": "1",
              "trailing_distance_mode": "TRAILING_DISTANCE_MODE_FIXED",
              "t_distance_pips": "30"
            },
            "id": "df473330-bf25-4af7-be7b-67c6645b69ce",
            "id_by_user": 7,
            "category": "trailing_stop_break_even",
            "block_name_mql": "trailing_pending_orders",
            "blockName": "Trailing pending orders"
          }
        ],
        "edges": [
          {
            "source": "bfaed0f1-abbc-4aee-ba6a-59f82b68f3e8",
            "sourceHandle": "blue",
            "target": "e5eb8b78-f03a-4982-b9d9-580256522ac1",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "85f3c94b-e1df-4982-b1cf-860c4a382781"
          },
          {
            "source": "e5eb8b78-f03a-4982-b9d9-580256522ac1",
            "sourceHandle": "blue",
            "target": "6d6cbcdd-96cc-4d19-a4ea-35a2bdd6c772",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "9c8ae73a-60d2-48ac-ab91-89e7070300ba"
          },
          {
            "source": "bfaed0f1-abbc-4aee-ba6a-59f82b68f3e8",
            "sourceHandle": "blue",
            "target": "c1cdfd0a-9392-4cc3-8ff3-c8c8eb823ec7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "5893573f-67a2-42e2-bbd5-c5b9d948261f"
          },
          {
            "source": "bfaed0f1-abbc-4aee-ba6a-59f82b68f3e8",
            "sourceHandle": "blue",
            "target": "85f8e9c7-dbd1-4561-af46-6bd8b4e465b7",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "84dbcb93-1b08-4f23-bc90-445e8e9788ed"
          },
          {
            "source": "85f8e9c7-dbd1-4561-af46-6bd8b4e465b7",
            "sourceHandle": "blue",
            "target": "4ae94ca9-9e61-4166-a9d1-2fa4699c2427",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "44ed6f33-6113-42eb-b8f7-19ed18353f85"
          },
          {
            "source": "4ae94ca9-9e61-4166-a9d1-2fa4699c2427",
            "sourceHandle": "blue",
            "target": "df473330-bf25-4af7-be7b-67c6645b69ce",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "0ffc6faa-db4b-4512-b81b-7b719cfc8892"
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
    "constants": []
  },
  "selected_name": "e7319aea-d1da-464b-842b-21155467123d",
  "name_by_user": "order select test",
  "highestIndex": "8"
}
