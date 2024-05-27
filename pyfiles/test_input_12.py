# This test file takes place in the period of 50 blocks phase

# If pending order
input_data_1 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "39dd378f-9963-48b9-a181-dded55308916",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
          },
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "df193530-239a-42aa-94e2-ae27014a4afe",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "39dd378f-9963-48b9-a181-dded55308916",
            "sourceHandle": "blue",
            "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
          }
        ],
        "nodes": [
          {
            "params": {
              "operator": {
                "label": "+"
              },
              "left": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "right": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "adjust": "",
              "variable": "sss"
            },
            "id": "39dd378f-9963-48b9-a181-dded55308916",
            "id_by_user": 2,
            "blockName": "Formula",
            "category": "condition_formula",
            "block_name_mql": "formula"
          },
          {
            "params": {
              "symbol": "",
              "timeframe": "PERIOD_CURRENT",
              "max_times_to_pass": "1"
            },
            "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "id_by_user": 3,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
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
                  "ma_period": "5",
                  "ma_shift": "0",
                  "ma_method": "MODE_SMMA",
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
                  "ma_method": "MODE_SMMA",
                  "applied_price": "PRICE_CLOSE",
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              }
            },
            "id": "4be75049-a2ac-4603-b424-9896de7986ea",
            "id_by_user": 4,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{2,4}",
              "type_pending": "{2,3}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "If pending order",
            "category": "check_trades_orders_count",
            "block_name_mql": "if_pending_order"
          },
          {
            "params": {
              "symbol": "",
              "group": "11",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrDarkBlue",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "67000",
                  "adjust": ""
                }
              }
            },
            "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "id_by_user": 6,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
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
    "constants": [
      {
        "type": "double",
        "name": "sss",
        "value": "0",
        "description": ""
      }
    ]
  },
  "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# If trade/order
input_data_2 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "39dd378f-9963-48b9-a181-dded55308916",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
          },
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "df193530-239a-42aa-94e2-ae27014a4afe",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "39dd378f-9963-48b9-a181-dded55308916",
            "sourceHandle": "blue",
            "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
          }
        ],
        "nodes": [
          {
            "params": {
              "operator": {
                "label": "+"
              },
              "left": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "right": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "adjust": "",
              "variable": "sss"
            },
            "id": "39dd378f-9963-48b9-a181-dded55308916",
            "id_by_user": 2,
            "blockName": "Formula",
            "category": "condition_formula",
            "block_name_mql": "formula"
          },
          {
            "params": {
              "symbol": "",
              "timeframe": "PERIOD_CURRENT",
              "max_times_to_pass": "1"
            },
            "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "id_by_user": 3,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
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
                  "ma_period": "5",
                  "ma_shift": "0",
                  "ma_method": "MODE_SMMA",
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
                  "ma_method": "MODE_SMMA",
                  "applied_price": "PRICE_CLOSE",
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              }
            },
            "id": "4be75049-a2ac-4603-b424-9896de7986ea",
            "id_by_user": 4,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0, 2, 4}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "If trade/order",
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade_order"
          },
          {
            "params": {
              "symbol": "",
              "group": "11",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrDarkBlue",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "67000",
                  "adjust": ""
                }
              }
            },
            "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "id_by_user": 6,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
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
    "constants": [
      {
        "type": "double",
        "name": "sss",
        "value": "0",
        "description": ""
      }
    ]
  },
  "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No trade/order
input_data_3 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "39dd378f-9963-48b9-a181-dded55308916",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
          },
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "df193530-239a-42aa-94e2-ae27014a4afe",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "39dd378f-9963-48b9-a181-dded55308916",
            "sourceHandle": "blue",
            "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
          }
        ],
        "nodes": [
          {
            "params": {
              "operator": {
                "label": "+"
              },
              "left": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "right": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "adjust": "",
              "variable": "sss"
            },
            "id": "39dd378f-9963-48b9-a181-dded55308916",
            "id_by_user": 2,
            "blockName": "Formula",
            "category": "condition_formula",
            "block_name_mql": "formula"
          },
          {
            "params": {
              "symbol": "",
              "timeframe": "PERIOD_CURRENT",
              "max_times_to_pass": "1"
            },
            "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "id_by_user": 3,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
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
                  "ma_period": "5",
                  "ma_shift": "0",
                  "ma_method": "MODE_SMMA",
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
                  "ma_method": "MODE_SMMA",
                  "applied_price": "PRICE_CLOSE",
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              }
            },
            "id": "4be75049-a2ac-4603-b424-9896de7986ea",
            "id_by_user": 4,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0, 2, 4}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "No trade/order",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade_order"
          },
          {
            "params": {
              "symbol": "",
              "group": "11",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrDarkBlue",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "67000",
                  "adjust": ""
                }
              }
            },
            "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "id_by_user": 6,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
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
    "constants": [
      {
        "type": "double",
        "name": "sss",
        "value": "0",
        "description": ""
      }
    ]
  },
  "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No trade
input_data_4 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "39dd378f-9963-48b9-a181-dded55308916",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
          },
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "df193530-239a-42aa-94e2-ae27014a4afe",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "39dd378f-9963-48b9-a181-dded55308916",
            "sourceHandle": "blue",
            "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
          }
        ],
        "nodes": [
          {
            "params": {
              "operator": {
                "label": "+"
              },
              "left": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "right": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "adjust": "",
              "variable": "sss"
            },
            "id": "39dd378f-9963-48b9-a181-dded55308916",
            "id_by_user": 2,
            "blockName": "Formula",
            "category": "condition_formula",
            "block_name_mql": "formula"
          },
          {
            "params": {
              "symbol": "",
              "timeframe": "PERIOD_CURRENT",
              "max_times_to_pass": "1"
            },
            "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "id_by_user": 3,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
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
                  "ma_period": "5",
                  "ma_shift": "0",
                  "ma_method": "MODE_SMMA",
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
                  "ma_method": "MODE_SMMA",
                  "applied_price": "PRICE_CLOSE",
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              }
            },
            "id": "4be75049-a2ac-4603-b424-9896de7986ea",
            "id_by_user": 4,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "No trade",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_trade"
          },
          {
            "params": {
              "symbol": "",
              "group": "11",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrDarkBlue",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "67000",
                  "adjust": ""
                }
              }
            },
            "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "id_by_user": 6,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
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
    "constants": [
      {
        "type": "double",
        "name": "sss",
        "value": "0",
        "description": ""
      }
    ]
  },
  "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

# No pending order
input_data_5 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "39dd378f-9963-48b9-a181-dded55308916",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-39dd378f-9963-48b9-a181-dded55308916c"
          },
          {
            "source": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-5bb869b5-ee0e-4b4f-a623-446ff30baefdblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "df193530-239a-42aa-94e2-ae27014a4afe",
            "sourceHandle": "blue",
            "target": "4be75049-a2ac-4603-b424-9896de7986ea",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-df193530-239a-42aa-94e2-ae27014a4afeblue-4be75049-a2ac-4603-b424-9896de7986eac"
          },
          {
            "source": "39dd378f-9963-48b9-a181-dded55308916",
            "sourceHandle": "blue",
            "target": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-39dd378f-9963-48b9-a181-dded55308916blue-3bb12bc6-0a30-424e-97bd-28b07ca72121c"
          }
        ],
        "nodes": [
          {
            "params": {
              "operator": {
                "label": "+"
              },
              "left": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "right": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              },
              "adjust": "",
              "variable": "sss"
            },
            "id": "39dd378f-9963-48b9-a181-dded55308916",
            "id_by_user": 2,
            "blockName": "Formula",
            "category": "condition_formula",
            "block_name_mql": "formula"
          },
          {
            "params": {
              "symbol": "",
              "timeframe": "PERIOD_CURRENT",
              "max_times_to_pass": "1"
            },
            "id": "5bb869b5-ee0e-4b4f-a623-446ff30baefd",
            "id_by_user": 3,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
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
                  "ma_period": "5",
                  "ma_shift": "0",
                  "ma_method": "MODE_SMMA",
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
                  "ma_method": "MODE_SMMA",
                  "applied_price": "PRICE_CLOSE",
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              }
            },
            "id": "4be75049-a2ac-4603-b424-9896de7986ea",
            "id_by_user": 4,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{3, 5}",
              "type_pending": "{2, 3, 4,5}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "No pending order",
            "category": "check_trades_orders_count",
            "block_name_mql": "no_pending_order"
          },
          {
            "params": {
              "symbol": "",
              "group": "11",
              "open_at_price": "OPEN_AT_CUSTOM_PRICE",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrDarkBlue",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "67000",
                  "adjust": ""
                }
              }
            },
            "id": "3bb12bc6-0a30-424e-97bd-28b07ca72121",
            "id_by_user": 6,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
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
    "constants": [
      {
        "type": "double",
        "name": "sss",
        "value": "0",
        "description": ""
      }
    ]
  },
  "selected_name": "d790e4c0-3977-4975-a442-c477ad3eaa29"
}

