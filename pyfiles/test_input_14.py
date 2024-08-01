
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

# test enum in constants fix
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
            "id": "7fbbd085-22c7-4296-977a-e216ad8af62e",
            "id_by_user": 1,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {},
            "id": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
            "id_by_user": 2,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {},
            "id": "3f394871-ee41-4bda-aeef-1af9890e8458",
            "id_by_user": 3,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrMaroon",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "stoploss": "20",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "takeprofit": "20",
              "symbol": "",
              "group": "11",
              "volume_upper_limit": "0",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "how_much_volume": "0.1"
            },
            "id": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
            "id_by_user": 4,
            "category": "buy_sell",
            "block_name_mql": "buy_now",
            "blockName": "Buy now"
          },
          {
            "params": {
              "type": "{0,1}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "815fcf92-7d67-4df8-8965-8f1e506db863",
            "id_by_user": 5,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade",
            "blockName": "If trade"
          }
        ],
        "edges": [
          {
            "source": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
            "sourceHandle": "blue",
            "target": "7fbbd085-22c7-4296-977a-e216ad8af62e",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "60d7f212-fb62-4536-9f1c-dd1074134c92"
          },
          {
            "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
            "sourceHandle": "blue",
            "target": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "e8c7cb9f-86f4-4c3d-91ba-ec477c72be99"
          },
          {
            "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
            "sourceHandle": "blue",
            "target": "815fcf92-7d67-4df8-8965-8f1e506db863",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ee667621-0fb5-45ca-b2d2-d6436f7405a9"
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
    "constants": [
      {
        "type": "enum ",
        "name": "my_enum",
        "value": "{hello}",
        "description": ""
      }
    ]
  },
  "selected_name": "a79a3586-967f-4e69-89d7-dfd97031fd21",
  "name_by_user": "",
  "highestIndex": "6"
}

# test enum in constants fix 2
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
            "params": {
              "operator": {
                "label": ">",
                "cross_width": 1
              },
              "left": {
                "row1": "indicator",
                "row2": "ma",
                "params": {
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
            "id": "7fbbd085-22c7-4296-977a-e216ad8af62e",
            "id_by_user": 1,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {},
            "id": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
            "id_by_user": 2,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {},
            "id": "3f394871-ee41-4bda-aeef-1af9890e8458",
            "id_by_user": 3,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrMaroon",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "stoploss": "20",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "takeprofit": "20",
              "symbol": "",
              "group": "11",
              "volume_upper_limit": "0",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "how_much_volume": "0.1"
            },
            "id": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
            "id_by_user": 4,
            "category": "buy_sell",
            "block_name_mql": "buy_now",
            "blockName": "Buy now"
          },
          {
            "params": {
              "type": "{0,1}",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11"
            },
            "id": "815fcf92-7d67-4df8-8965-8f1e506db863",
            "id_by_user": 5,
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade",
            "blockName": "If trade"
          }
        ],
        "edges": [
          {
            "source": "a5c060ff-0fbe-48bc-9a28-55c0bb6090ea",
            "sourceHandle": "blue",
            "target": "7fbbd085-22c7-4296-977a-e216ad8af62e",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "60d7f212-fb62-4536-9f1c-dd1074134c92"
          },
          {
            "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
            "sourceHandle": "blue",
            "target": "311a5d51-5857-4397-b0d3-3886d2f5d97b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "e8c7cb9f-86f4-4c3d-91ba-ec477c72be99"
          },
          {
            "source": "3f394871-ee41-4bda-aeef-1af9890e8458",
            "sourceHandle": "blue",
            "target": "815fcf92-7d67-4df8-8965-8f1e506db863",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "ee667621-0fb5-45ca-b2d2-d6436f7405a9"
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
        "type": "double",
        "name": "z",
        "value": "",
        "description": ""
      }
    ],
    "constants": [
      {
        "type": "enum",
        "name": "my_enum",
        "value": "{hello}",
        "description": ""
      },
      {
        "type": "my_enum",
        "name": "chetori",
        "value": "hello",
        "description": ""
      }
    ]
  },
  "selected_name": "a79a3586-967f-4e69-89d7-dfd97031fd21",
  "name_by_user": "",
  "highestIndex": "6"
}
