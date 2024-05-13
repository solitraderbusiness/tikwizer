

# 20 blocks final: once per bar, buy now
input_data_1 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{0,1}",
            "group_number": "15",
            "symbols_str": "EURUSD"
          },
          "id": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "id_by_user": 1,
          "blockName": "If trade",
          "category": "check_trades_orders_count",
          "block_name_mql": "if_trade"
        },
        {
          "params": {
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "",
            "group": "11",
            "how_much_volume": "2.5",
            "volume_upper_limit": "0",
            "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
            "martingale_init_vol": "0.1",
            "martingale_multiply_on_loss": "2",
            "martingale_multiply_on_profit": "1",
            "martingale_addlots_on_loss": "0",
            "martingale_addlots_on_profit": "0",
            "martingale_reset_on_n_losses": "0",
            "martingale_reset_on_n_profits": "1",
            "stoploss": "20",
            "takeprofit": "20",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon"
          },
          "id": "3777456e-5c77-493b-a8e2-4130fc21c653",
          "id_by_user": 2,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "sourceHandle": "blue",
          "target": "3777456e-5c77-493b-a8e2-4130fc21c653",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-93740514-b4fe-4399-aa59-3af4f37ab542blue-3777456e-5c77-493b-a8e2-4130fc21c653c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: close trades
input_data_2 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{0,1}",
            "group_number": "15",
            "symbols_str": "EURUSD"
          },
          "id": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "id_by_user": 1,
          "blockName": "If trade",
          "category": "check_trades_orders_count",
          "block_name_mql": "if_trade"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "symbols_str": "",
            "type": "{0,1}",
            "older_than": "",
            "slippage": "4",
            "arrow_color": "clrDarkGoldenrod"
          },
          "id": "08e03ebd-cbca-4abb-bb66-740be5ab32e7",
          "id_by_user": 2,
          "blockName": "Close trades",
          "category": "trading_actions",
          "block_name_mql": "close_trades"
        }
      ],
      "edges": [
        {
          "source": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "sourceHandle": "blue",
          "target": "08e03ebd-cbca-4abb-bb66-740be5ab32e7",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-93740514-b4fe-4399-aa59-3af4f37ab542blue-08e03ebd-cbca-4abb-bb66-740be5ab32e7c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: and or
input_data_3 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{0,1}",
            "group_number": "15",
            "symbols_str": "EURUSD"
          },
          "id": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "id_by_user": 1,
          "blockName": "If trade",
          "category": "check_trades_orders_count",
          "block_name_mql": "if_trade"
        },
        {
          "params": {},
          "id": "c9325419-3f4a-4bef-88e4-2720116e4a2c",
          "id_by_user": 2,
          "blockName": "AND",
          "category": "controlling_blocks",
          "block_name_mql": "and"
        },
        {
          "params": {},
          "id": "ed98c346-320c-47db-ae39-4fd4905d754b",
          "id_by_user": 3,
          "blockName": "OR",
          "category": "controlling_blocks",
          "block_name_mql": "or"
        }
      ],
      "edges": [
        {
          "source": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "sourceHandle": "blue",
          "target": "ed98c346-320c-47db-ae39-4fd4905d754b",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-93740514-b4fe-4399-aa59-3af4f37ab542blue-ed98c346-320c-47db-ae39-4fd4905d754bc"
        },
        {
          "source": "93740514-b4fe-4399-aa59-3af4f37ab542",
          "sourceHandle": "blue",
          "target": "c9325419-3f4a-4bef-88e4-2720116e4a2c",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-93740514-b4fe-4399-aa59-3af4f37ab542blue-c9325419-3f4a-4bef-88e4-2720116e4a2cc"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: one per bar
input_data_4 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "",
            "group": "11",
            "how_much_volume": "2.5",
            "volume_upper_limit": "0",
            "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
            "martingale_init_vol": "0.1",
            "martingale_multiply_on_loss": "2",
            "martingale_multiply_on_profit": "1",
            "martingale_addlots_on_loss": "0",
            "martingale_addlots_on_profit": "0",
            "martingale_reset_on_n_losses": "0",
            "martingale_reset_on_n_profits": "1",
            "stoploss": "20",
            "takeprofit": "20",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon"
          },
          "id": "352aad27-4782-44d5-921c-a7ab159f1eb6",
          "id_by_user": 2,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        },
        {
          "params": {
            "symbol": "XAUUSD",
            "timeframe": "PERIOD_H8",
            "max_times_to_pass": "13"
          },
          "id": "aae3bd1f-bda1-4694-b218-6e2abf7ce5ea",
          "id_by_user": 3,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        }
      ],
      "edges": [
        {
          "source": "aae3bd1f-bda1-4694-b218-6e2abf7ce5ea",
          "sourceHandle": "blue",
          "target": "352aad27-4782-44d5-921c-a7ab159f1eb6",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-aae3bd1f-bda1-4694-b218-6e2abf7ce5eablue-352aad27-4782-44d5-921c-a7ab159f1eb6c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: if trade > sell pending order
input_data_5 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "open_at_price": "OPEN_AT_ASK",
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "",
            "group": "11",
            "price_offset": "20",
            "how_much_volume": "2.5",
            "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
            "martingale_init_vol": "0.1",
            "martingale_multiply_on_loss": "2",
            "martingale_multiply_on_profit": "1",
            "martingale_addlots_on_loss": "0",
            "martingale_addlots_on_profit": "0",
            "martingale_reset_on_n_losses": "0",
            "martingale_reset_on_n_profits": "1",
            "stoploss": "20",
            "takeprofit": "20",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon"
          },
          "id": "b150bf2b-b3b8-42e7-8997-4d98716e112d",
          "id_by_user": 4,
          "blockName": "Sell pending order",
          "category": "buy_sell",
          "block_name_mql": "sell_pending_order"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_ALL",
            "symbol_mode": "SYMBOL_MODE_ANY",
            "type": "{0,1}"
          },
          "id": "1c0e396d-3c2c-405a-b002-6dd93b7c5c5c",
          "id_by_user": 5,
          "blockName": "If trade",
          "category": "check_trades_orders_count",
          "block_name_mql": "if_trade"
        }
      ],
      "edges": [
        {
          "source": "1c0e396d-3c2c-405a-b002-6dd93b7c5c5c",
          "sourceHandle": "blue",
          "target": "b150bf2b-b3b8-42e7-8997-4d98716e112d",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-1c0e396d-3c2c-405a-b002-6dd93b7c5c5cblue-b150bf2b-b3b8-42e7-8997-4d98716e112dc"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: close trades
input_data_6 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_ALL",
            "symbol_mode": "SYMBOL_MODE_ANY",
            "type": "{0,1}"
          },
          "id": "1c0e396d-3c2c-405a-b002-6dd93b7c5c5c",
          "id_by_user": 5,
          "blockName": "If trade",
          "category": "check_trades_orders_count",
          "block_name_mql": "if_trade"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "11",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "symbols_str": "",
            "type": "{0,1}",
            "older_than": "0",
            "slippage": "4",
            "arrow_color": "clrDarkGoldenrod"
          },
          "id": "8d1bd745-e0ca-44aa-90db-edcf6f6702a1",
          "id_by_user": 6,
          "blockName": "Close trades",
          "category": "trading_actions",
          "block_name_mql": "close_trades"
        }
      ],
      "edges": [
        {
          "source": "1c0e396d-3c2c-405a-b002-6dd93b7c5c5c",
          "sourceHandle": "blue",
          "target": "8d1bd745-e0ca-44aa-90db-edcf6f6702a1",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-1c0e396d-3c2c-405a-b002-6dd93b7c5c5cblue-8d1bd745-e0ca-44aa-90db-edcf6f6702a1c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: delay
input_data_7 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_ALL",
            "symbol_mode": "SYMBOL_MODE_ANY",
            "type": "{0,1}"
          },
          "id": "1c0e396d-3c2c-405a-b002-6dd93b7c5c5c",
          "id_by_user": 5,
          "blockName": "If trade",
          "category": "check_trades_orders_count",
          "block_name_mql": "if_trade"
        },
        {
          "params": {
            "sleep_seconds": "9",
            "sleep_tester_normal": "false",
            "sleep_tester_visual": "false"
          },
          "id": "194e2554-c858-4abb-baf8-a9e22d25ae84",
          "id_by_user": 6,
          "blockName": "Delay",
          "category": "more",
          "block_name_mql": "delay"
        }
      ],
      "edges": [
        {
          "source": "1c0e396d-3c2c-405a-b002-6dd93b7c5c5c",
          "sourceHandle": "blue",
          "target": "194e2554-c858-4abb-baf8-a9e22d25ae84",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-1c0e396d-3c2c-405a-b002-6dd93b7c5c5cblue-194e2554-c858-4abb-baf8-a9e22d25ae84c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: buy now
input_data_8 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "439cee96-5cd8-4263-adaa-c0bb1c80c1a5",
          "id_by_user": 10,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "XAUUSD",
            "group": "66",
            "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
            "volume_upper_limit": "0.1",
            "stop_loss_mode": "TPSL_MODE_NO_SL",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "40",
            "comment": "fsdfdsafs",
            "arrow_color": "clrDarkBlue",
            "how_much_volume": "2.5",
            "takeprofit": "57"
          },
          "id": "ccf2fc2b-4403-49e5-add3-78a54aef8fb0",
          "id_by_user": 11,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "439cee96-5cd8-4263-adaa-c0bb1c80c1a5",
          "sourceHandle": "blue",
          "target": "ccf2fc2b-4403-49e5-add3-78a54aef8fb0",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-439cee96-5cd8-4263-adaa-c0bb1c80c1a5blue-ccf2fc2b-4403-49e5-add3-78a54aef8fb0c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: buy now test 2
input_data_9 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "439cee96-5cd8-4263-adaa-c0bb1c80c1a5",
          "id_by_user": 10,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "XAUUSD",
            "group": "66",
            "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
            "volume_upper_limit": "0.18",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_NO_TP",
            "slippage": "23",
            "comment": "comment yes",
            "arrow_color": "clrOlive",
            "look_up_on": "LOOK_UP_RUNNING_ONLY",
            "martingale_init_vol": "0.15",
            "martingale_multiply_on_loss": "3",
            "martingale_multiply_on_profit": "2",
            "martingale_addlots_on_loss": "4",
            "martingale_addlots_on_profit": "5",
            "martingale_reset_on_n_losses": "8",
            "martingale_reset_on_n_profits": "8",
            "stoploss": "99"
          },
          "id": "ccf2fc2b-4403-49e5-add3-78a54aef8fb0",
          "id_by_user": 11,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "439cee96-5cd8-4263-adaa-c0bb1c80c1a5",
          "sourceHandle": "blue",
          "target": "ccf2fc2b-4403-49e5-add3-78a54aef8fb0",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-439cee96-5cd8-4263-adaa-c0bb1c80c1a5blue-ccf2fc2b-4403-49e5-add3-78a54aef8fb0c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: buy now test 3
input_data_10 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "439cee96-5cd8-4263-adaa-c0bb1c80c1a5",
          "id_by_user": 10,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "",
            "group": "66",
            "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
            "volume_upper_limit": "60",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_NO_TP",
            "slippage": "23",
            "comment": "comment yes",
            "arrow_color": "clrOlive",
            "stoploss": "99",
            "how_much_volume": "55"
          },
          "id": "ccf2fc2b-4403-49e5-add3-78a54aef8fb0",
          "id_by_user": 11,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "439cee96-5cd8-4263-adaa-c0bb1c80c1a5",
          "sourceHandle": "blue",
          "target": "ccf2fc2b-4403-49e5-add3-78a54aef8fb0",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-439cee96-5cd8-4263-adaa-c0bb1c80c1a5blue-ccf2fc2b-4403-49e5-add3-78a54aef8fb0c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: sell now test
input_data_11 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "id_by_user": 13,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "BTCUSD",
            "group": "87",
            "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
            "volume_upper_limit": "1",
            "stop_loss_mode": "TPSL_MODE_NO_SL",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "14",
            "comment": "my test comment",
            "arrow_color": "clrTeal",
            "how_much_volume": "2.5",
            "takeprofit": "99"
          },
          "id": "a21c0064-aeb7-46ac-bf48-ec1e7386a71c",
          "id_by_user": 14,
          "blockName": "Sell now",
          "category": "buy_sell",
          "block_name_mql": "sell_now"
        }
      ],
      "edges": [
        {
          "source": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "sourceHandle": "blue",
          "target": "a21c0064-aeb7-46ac-bf48-ec1e7386a71c",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-db0b13be-d398-4355-a8c8-d7103a1f7853blue-a21c0064-aeb7-46ac-bf48-ec1e7386a71cc"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: condition 1
input_data_12 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "id_by_user": 13,
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
                "symbol": "GBPUSD",
                "timeframe": "PERIOD_M15",
                "shift": "10"
              }
            },
            "right": {
              "row1": "candle",
              "row2": "candle",
              "params": {
                "price_mode": "CANDLE_GAP_TO_PREV",
                "find_method": "FIND_BY_ID",
                "shift": "12",
                "symbol": "",
                "timeframe": "PERIOD_M2"
              }
            }
          },
          "id": "96607589-9f83-4499-b80d-1b64f173fc04",
          "id_by_user": 14,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        }
      ],
      "edges": [
        {
          "source": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "sourceHandle": "blue",
          "target": "96607589-9f83-4499-b80d-1b64f173fc04",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-db0b13be-d398-4355-a8c8-d7103a1f7853blue-96607589-9f83-4499-b80d-1b64f173fc04c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}

# 20 blocks final: buy pending
input_data_13 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "id_by_user": 13,
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
                "symbol": "GBPUSD",
                "timeframe": "PERIOD_M15",
                "shift": "10"
              }
            },
            "right": {
              "row1": "candle",
              "row2": "candle",
              "params": {
                "price_mode": "CANDLE_GAP_TO_PREV",
                "find_method": "FIND_BY_ID",
                "shift": "12",
                "symbol": "",
                "timeframe": "PERIOD_M2"
              }
            }
          },
          "id": "96607589-9f83-4499-b80d-1b64f173fc04",
          "id_by_user": 14,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "NULL",
            "group": "45",
            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
            "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrDarkBlue",
            "stoploss": "20",
            "takeprofit": "20",
            "OPEN_AT_CUSTOM_PRICE": {
              "row1": "value",
              "row2": "Numeric",
              "params": {
                "value": "200"
              }
            },
            "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
            "martingale_init_vol": "0.1",
            "martingale_multiply_on_loss": "2",
            "martingale_multiply_on_profit": "1",
            "martingale_addlots_on_loss": "0",
            "martingale_addlots_on_profit": "0",
            "martingale_reset_on_n_losses": "0",
            "martingale_reset_on_n_profits": "1"
          },
          "id": "623d0ed6-a5ea-43c0-a418-1803a3960ca5",
          "id_by_user": 15,
          "blockName": "Buy pending order",
          "category": "buy_sell",
          "block_name_mql": "buy_pending_order"
        }
      ],
      "edges": [
        {
          "source": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "sourceHandle": "blue",
          "target": "96607589-9f83-4499-b80d-1b64f173fc04",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-db0b13be-d398-4355-a8c8-d7103a1f7853blue-96607589-9f83-4499-b80d-1b64f173fc04c"
        },
        {
          "source": "db0b13be-d398-4355-a8c8-d7103a1f7853",
          "sourceHandle": "blue",
          "target": "623d0ed6-a5ea-43c0-a418-1803a3960ca5",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-db0b13be-d398-4355-a8c8-d7103a1f7853blue-623d0ed6-a5ea-43c0-a418-1803a3960ca5c"
        }
      ]
    },
    "on_trade": {
      "nodes": [],
      "edges": []
    },
    "on_chart": {
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
  "variables": [],
  "constants": []
}
