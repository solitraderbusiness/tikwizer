
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
