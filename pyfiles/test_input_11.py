

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
              "row2": "Text_code_input",
              "params": {
                "value": "test price"
              }
            }
          },
          "id": "0b334277-407c-45e1-8a28-e9ebbe977867",
          "id_by_user": 16,
          "blockName": "Buy pending order",
          "category": "buy_sell",
          "block_name_mql": "buy_pending_order"
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
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "id_by_user": 17,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        }
      ],
      "edges": [
        {
          "source": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "sourceHandle": "blue",
          "target": "0b334277-407c-45e1-8a28-e9ebbe977867",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-24ede79e-617d-4242-8326-96c39f8d4b8bblue-0b334277-407c-45e1-8a28-e9ebbe977867c"
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

# 20 blocks final: buy pending 2
input_data_14 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "group": "11",
            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
            "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
            "volume_upper_limit": "01",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrDarkBlue",
            "stoploss": "20",
            "takeprofit": "20",
            "price_to_open_dynamic_level": {
              "row1": "value",
              "row2": "Text_code_input",
              "params": {
                "value": "test price"
              }
            },
            "martingale_init_vol": "0.11",
            "martingale_multiply_on_loss": "22",
            "martingale_multiply_on_profit": "11",
            "martingale_addlots_on_loss": "01",
            "martingale_addlots_on_profit": "01",
            "martingale_reset_on_n_losses": "01",
            "martingale_reset_on_n_profits": "11"
          },
          "id": "0b334277-407c-45e1-8a28-e9ebbe977867",
          "id_by_user": 16,
          "blockName": "Buy pending order",
          "category": "buy_sell",
          "block_name_mql": "buy_pending_order"
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
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "id_by_user": 17,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        }
      ],
      "edges": [
        {
          "source": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "sourceHandle": "blue",
          "target": "0b334277-407c-45e1-8a28-e9ebbe977867",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-24ede79e-617d-4242-8326-96c39f8d4b8bblue-0b334277-407c-45e1-8a28-e9ebbe977867c"
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

# 20 blocks final: sell pending
input_data_15 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "id_by_user": 17,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "BTCUSD",
            "group": "55",
            "open_at_price": "OPEN_AT_MID",
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "volume_upper_limit": "10",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_NO_TP",
            "slippage": "3",
            "comment": "test comment yes",
            "arrow_color": "clrRed",
            "how_much_volume": "0.15",
            "stoploss": "31",
            "price_offset": "50"
          },
          "id": "28d703cf-d6ba-4bfe-a8e3-d455493bea59",
          "id_by_user": 18,
          "blockName": "Sell pending order",
          "category": "buy_sell",
          "block_name_mql": "sell_pending_order"
        }
      ],
      "edges": [
        {
          "source": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "sourceHandle": "blue",
          "target": "28d703cf-d6ba-4bfe-a8e3-d455493bea59",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-24ede79e-617d-4242-8326-96c39f8d4b8bblue-28d703cf-d6ba-4bfe-a8e3-d455493bea59c"
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

# 20 blocks final: sell pending 2
input_data_16 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "id_by_user": 17,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "BTCUSD",
            "group": "55",
            "open_at_price": "OPEN_AT_MID",
            "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
            "volume_upper_limit": "15",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_NO_TP",
            "slippage": "3",
            "comment": "test comment yes",
            "arrow_color": "clrRed",
            "price_offset": "50",
            "stoploss": "31",
            "martingale_init_vol": "0.12",
            "martingale_multiply_on_loss": "23",
            "martingale_multiply_on_profit": "12",
            "martingale_addlots_on_loss": "12",
            "martingale_addlots_on_profit": "12",
            "martingale_reset_on_n_losses": "01",
            "martingale_reset_on_n_profits": "12"
          },
          "id": "28d703cf-d6ba-4bfe-a8e3-d455493bea59",
          "id_by_user": 18,
          "blockName": "Sell pending order",
          "category": "buy_sell",
          "block_name_mql": "sell_pending_order"
        }
      ],
      "edges": [
        {
          "source": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "sourceHandle": "blue",
          "target": "28d703cf-d6ba-4bfe-a8e3-d455493bea59",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-24ede79e-617d-4242-8326-96c39f8d4b8bblue-28d703cf-d6ba-4bfe-a8e3-d455493bea59c"
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

# 20 blocks final: sell pending 3
input_data_17 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "id_by_user": 17,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "BTCUSD",
            "group": "55",
            "open_at_price": "OPEN_AT_CUSTOM_PRICE",
            "money_management": "MONEY_MANAGEMENT_BETTING_MARTINGALE_PAROLI",
            "volume_upper_limit": "15",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_NO_TP",
            "slippage": "3",
            "comment": "test comment yes",
            "arrow_color": "clrRed",
            "martingale_init_vol": "0.12",
            "martingale_multiply_on_loss": "23",
            "martingale_multiply_on_profit": "12",
            "martingale_addlots_on_loss": "12",
            "martingale_addlots_on_profit": "12",
            "martingale_reset_on_n_losses": "01",
            "martingale_reset_on_n_profits": "12",
            "stoploss": "31",
            "price_to_open_dynamic_level": {
              "row1": "candle",
              "row2": "candle",
              "params": {
                "price_mode": "BULL_CANDLE_BODY_SIZE",
                "find_method": "FIND_BY_DATE",
                "timestr": "00:45",
                "adjust": "*10",
                "symbol": "USDJPY",
                "timeframe": "PERIOD_M15",
                "shift": "20"
              }
            }
          },
          "id": "28d703cf-d6ba-4bfe-a8e3-d455493bea59",
          "id_by_user": 18,
          "blockName": "Sell pending order",
          "category": "buy_sell",
          "block_name_mql": "sell_pending_order"
        }
      ],
      "edges": [
        {
          "source": "24ede79e-617d-4242-8326-96c39f8d4b8b",
          "sourceHandle": "blue",
          "target": "28d703cf-d6ba-4bfe-a8e3-d455493bea59",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-24ede79e-617d-4242-8326-96c39f8d4b8bblue-28d703cf-d6ba-4bfe-a8e3-d455493bea59c"
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
input_data_18 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "id_by_user": 18,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_MANUAL",
            "symbol_mode": "SYMBOL_MODE_ANY",
            "type": "{1}",
            "older_than": "10",
            "slippage": "40",
            "arrow_color": "clrNavy"
          },
          "id": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "id_by_user": 19,
          "blockName": "Close trades",
          "category": "trading_actions",
          "block_name_mql": "close_trades"
        }
      ],
      "edges": [
        {
          "source": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "sourceHandle": "blue",
          "target": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-c0ec4e92-bb9f-40ea-99b6-874d5ab3a42ablue-6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49c"
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

# 20 blocks final: close trades 2
input_data_19 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "id_by_user": 18,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "18",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{0,1}",
            "older_than": "1",
            "slippage": "4",
            "arrow_color": "clrDarkSlateGray",
            "symbols_str": "XAUUSD"
          },
          "id": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "id_by_user": 19,
          "blockName": "Close trades",
          "category": "trading_actions",
          "block_name_mql": "close_trades"
        }
      ],
      "edges": [
        {
          "source": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "sourceHandle": "blue",
          "target": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-c0ec4e92-bb9f-40ea-99b6-874d5ab3a42ablue-6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49c"
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

# 20 blocks final: no trade nearby
input_data_20 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "id_by_user": 18,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "18",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{0,1}",
            "older_than": "1",
            "slippage": "4",
            "arrow_color": "clrDarkSlateGray",
            "symbols_str": "XAUUSD"
          },
          "id": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "id_by_user": 19,
          "blockName": "Close trades",
          "category": "trading_actions",
          "block_name_mql": "close_trades"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_ALL",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "symbols_str": "EURUSD",
            "type": "{0}",
            "mode_base_price": "custom_price",
            "mode_range": "pips",
            "range_position": "0",
            "time_1": {
              "row1": "value",
              "row2": "Time",
              "params": {
                "mode_time": "MODE_TIME_NOW",
                "mode_time_shift": "0",
                "time_source": "TIME_SERVER"
              }
            },
            "time_2": {
              "row1": "value",
              "row2": "Time",
              "params": {
                "mode_time": "MODE_TIME_NOW",
                "mode_time_shift": "0",
                "time_source": "TIME_SERVER"
              }
            },
            "range_pips": "10",
            "price": {
              "row1": "market-properties",
              "row2": "HIGHEST_PRICE_CANDLE_PERIOD",
              "params": {
                "range_start": "0",
                "range_end": "10",
                "what_to_get": "GET_PRICE"
              }
            }
          },
          "id": "9e1a663a-b2fd-42dc-95ec-0c946496364d",
          "id_by_user": 20,
          "blockName": "No trade nearby",
          "category": "check_trades_orders_count",
          "block_name_mql": "no_trade_nearby"
        }
      ],
      "edges": [
        {
          "source": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "sourceHandle": "blue",
          "target": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-c0ec4e92-bb9f-40ea-99b6-874d5ab3a42ablue-6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49c"
        },
        {
          "source": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "sourceHandle": "blue",
          "target": "9e1a663a-b2fd-42dc-95ec-0c946496364d",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49blue-9e1a663a-b2fd-42dc-95ec-0c946496364dc"
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

# 20 blocks final: no trade nearby 2
input_data_21 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE"
              }
            }
          },
          "id": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "id_by_user": 18,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "18",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{0,1}",
            "older_than": "1",
            "slippage": "4",
            "arrow_color": "clrDarkSlateGray",
            "symbols_str": "XAUUSD"
          },
          "id": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "id_by_user": 19,
          "blockName": "Close trades",
          "category": "trading_actions",
          "block_name_mql": "close_trades"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_ALL",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "symbols_str": "EURUSD",
            "type": "{0}",
            "mode_base_price": "custom_price",
            "mode_range": "fraction",
            "range_position": "1",
            "Time 1": {
              "row1": "value",
              "row2": "Time",
              "params": {
                "mode_time": "MODE_TIME_COMPONENTS",
                "mode_time_shift": "0",
                "time_source": "TIME_LOCAL",
                "time_component_year": "",
                "time_component_month": "",
                "time_component_day": "",
                "time_component_hour": "12",
                "time_component_minute": "0",
                "time_component_second": "0"
              }
            },
            "Time 2": {
              "row1": "value",
              "row2": "Time",
              "params": {
                "mode_time": "MODE_TIME_CANDLE_TIME",
                "mode_time_shift": "1",
                "time_candle_id": "1",
                "time_market": "",
                "time_candle_timeframe": "PERIOD_M15",
                "time_shift_years": "1",
                "time_shift_months": "2",
                "time_shift_weeks": "3",
                "time_shift_days": "4",
                "time_shift_hours": "5",
                "time_shift_minutes": "6",
                "time_shift_seconds": "7",
                "time_skip_weekdays": "true"
              }
            },
            "price": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "ma_period": "5",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE",
                "adjust": "*5%",
                "symbol": "EURUSD",
                "timeframe": "PERIOD_M30",
                "shift": "11"
              }
            },
            "range_fraction": "0.005"
          },
          "id": "9e1a663a-b2fd-42dc-95ec-0c946496364d",
          "id_by_user": 20,
          "blockName": "No trade neary",
          "category": "check_trades_orders_count",
          "block_name_mql": "no_trade_neary"
        }
      ],
      "edges": [
        {
          "source": "c0ec4e92-bb9f-40ea-99b6-874d5ab3a42a",
          "sourceHandle": "blue",
          "target": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-c0ec4e92-bb9f-40ea-99b6-874d5ab3a42ablue-6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49c"
        },
        {
          "source": "6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49",
          "sourceHandle": "blue",
          "target": "9e1a663a-b2fd-42dc-95ec-0c946496364d",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-6ecc85ad-abd1-4f9e-9ca8-bb67b6331c49blue-9e1a663a-b2fd-42dc-95ec-0c946496364dc"
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

# 20 blocks final: loop pass n times
input_data_22 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "cycles": "20"
          },
          "id": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "id_by_user": 3,
          "blockName": "Loop (pass \"n\" times)",
          "category": "counters",
          "block_name_mql": "loop_pass_n_times"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-0dee5145-f3da-4ed9-9637-e64e0851d794c"
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

# 20 blocks final: check profit unrealized
input_data_23 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "cycles": "20"
          },
          "id": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "id_by_user": 3,
          "blockName": "Loop (pass \"n\" times)",
          "category": "counters",
          "block_name_mql": "loop_pass_n_times"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "17",
            "symbol_mode": "SYMBOL_MODE_ANY",
            "type": "{1}",
            "profit_mode_each": "PROFIT_MODE_MONEY",
            "profit_mode": "PROFIT_MODE_MONEY",
            "profit-mode-money": "!=",
            "profit_amount": "200",
            "compare_each": "==",
            "profit_amount_each": "10.5"
          },
          "id": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "id_by_user": 4,
          "blockName": "Check Profit (unrealized)",
          "category": "check_trading_conditions",
          "block_name_mql": "check_profit_unrealized"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-0dee5145-f3da-4ed9-9637-e64e0851d794c"
        },
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-829dc7ae-1668-4a8a-a1c3-b9e678f3ef68c"
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

# 20 blocks final: check profit unrealized 2
input_data_24 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "cycles": "20"
          },
          "id": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "id_by_user": 3,
          "blockName": "Loop (pass \"n\" times)",
          "category": "counters",
          "block_name_mql": "loop_pass_n_times"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "17",
            "symbol_mode": "SYMBOL_MODE_ANY",
            "type": "{1}",
            "profit_mode_each": "PROFIT_MODE_NO_MATTER",
            "profit_mode": "PROFIT_MODE_MONEY",
            "profit-mode-money": "!=",
            "profit_amount": "200"
          },
          "id": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "id_by_user": 4,
          "blockName": "Check Profit (unrealized)",
          "category": "check_trading_conditions",
          "block_name_mql": "check_profit_unrealized"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-0dee5145-f3da-4ed9-9637-e64e0851d794c"
        },
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-829dc7ae-1668-4a8a-a1c3-b9e678f3ef68c"
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

# 20 blocks final: check profit unrealized 3
input_data_25 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "cycles": "20"
          },
          "id": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "id_by_user": 3,
          "blockName": "Loop (pass \"n\" times)",
          "category": "counters",
          "block_name_mql": "loop_pass_n_times"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "17",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{1}",
            "profit_mode_each": "PROFIT_MODE_MONEY",
            "profit_mode": "PROFIT_MODE_PIPS_SUM",
            "symbols_str": "",
            "profit-mode-money": ">",
            "profit_amount": "0.0",
            "compare_each": ">",
            "profit_amount_each": "0.0"
          },
          "id": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "id_by_user": 4,
          "blockName": "Check Profit (unrealized)",
          "category": "check_trading_conditions",
          "block_name_mql": "check_profit_unrealized"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "0dee5145-f3da-4ed9-9637-e64e0851d794",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-0dee5145-f3da-4ed9-9637-e64e0851d794c"
        },
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-829dc7ae-1668-4a8a-a1c3-b9e678f3ef68c"
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

# 20 blocks final: check loop pass n times
input_data_26 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "group_mode": "ORDER_GROUP_MODE_NUMBER",
            "group_number": "17",
            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
            "type": "{1}",
            "profit_mode_each": "PROFIT_MODE_MONEY",
            "profit_mode": "PROFIT_MODE_PIPS_SUM",
            "symbols_str": "",
            "profit-mode-money": ">",
            "profit_amount": "0.0",
            "compare_each": ">",
            "profit_amount_each": "0.0"
          },
          "id": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "id_by_user": 4,
          "blockName": "Check Profit (unrealized)",
          "category": "check_trading_conditions",
          "block_name_mql": "check_profit_unrealized"
        },
        {
          "params": {
            "n": "30"
          },
          "id": "1788e890-a61d-486c-9112-bfcc3824e5e8",
          "id_by_user": 5,
          "blockName": "Loop (pass \"n\" times)",
          "category": "counters",
          "block_name_mql": "loop_pass_n_times"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "829dc7ae-1668-4a8a-a1c3-b9e678f3ef68",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-829dc7ae-1668-4a8a-a1c3-b9e678f3ef68c"
        },
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "1788e890-a61d-486c-9112-bfcc3824e5e8",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-1788e890-a61d-486c-9112-bfcc3824e5e8c"
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

# 20 blocks final: modify variables
input_data_27 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "variable1": {
              "variable_name": "test",
              "value_fetch": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": "-5"
                }
              }
            },
            "variable2": {
              "variable_name": "test",
              "value_fetch": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              }
            },
            "variable3": {
              "variable_name": "my_var",
              "value_fetch": {
                "row1": "indicator",
                "row2": "accelerator_oscillator",
                "params": {
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "0"
                }
              }
            },
            "variable4": {
              "variable_name": "",
              "value_fetch": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              }
            },
            "variable5": {
              "variable_name": "",
              "value_fetch": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              }
            }
          },
          "variable1": {},
          "variable2": {},
          "variable3": {},
          "variable4": {},
          "variable5": {},
          "id": "be084649-dbe5-4017-9883-ae1d10cc8455",
          "id_by_user": 2,
          "blockName": "Modify Variables",
          "category": "variables",
          "block_name_mql": "modify_variables"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "be084649-dbe5-4017-9883-ae1d10cc8455",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-be084649-dbe5-4017-9883-ae1d10cc8455c"
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
  "variables": [
    {
      "type": "double",
      "name": "my_var",
      "value": "5",
      "description": ""
    }
  ],
  "constants": [
    {
      "type": "double",
      "name": "test",
      "value": "10",
      "description": ""
    }
  ]
}

# 20 blocks final: test value > adjust
input_data_28 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "id_by_user": 1,
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
              "row1": "value",
              "row2": "Numeric",
              "params": {
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE",
                "adjust": "-5",
                "symbol": "",
                "time_candle_timeframe": "PERIOD_CURRENT",
                "mode_time_shift": "0",
                "value": "1"
              }
            }
          },
          "id": "88e36ffa-8d94-4ed7-b738-fdcd49d1ea05",
          "id_by_user": 2,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        }
      ],
      "edges": [
        {
          "source": "67efb53c-790d-4c06-9f11-aa4f9eb60756",
          "sourceHandle": "blue",
          "target": "88e36ffa-8d94-4ed7-b738-fdcd49d1ea05",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-67efb53c-790d-4c06-9f11-aa4f9eb60756blue-88e36ffa-8d94-4ed7-b738-fdcd49d1ea05c"
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
  "variables": [
    {
      "type": "double",
      "name": "my_var",
      "value": "5",
      "description": ""
    }
  ],
  "constants": [
    {
      "type": "double",
      "name": "test",
      "value": "10",
      "description": ""
    }
  ]
}

# 20 blocks final: one per bar
input_data_29 = {
  "events": {
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
          "id": "37d1178c-a412-45e2-9e90-a4c61c813225",
          "id_by_user": 2,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "cacf5206-73c8-4eb8-b4bc-134ad3bdb202",
          "id_by_user": 3,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        }
      ],
      "edges": [
        {
          "source": "cacf5206-73c8-4eb8-b4bc-134ad3bdb202",
          "sourceHandle": "blue",
          "target": "37d1178c-a412-45e2-9e90-a4c61c813225",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-cacf5206-73c8-4eb8-b4bc-134ad3bdb202blue-37d1178c-a412-45e2-9e90-a4c61c813225c"
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
  "variables": [
    {
      "type": "double",
      "name": "my_var",
      "value": "5",
      "description": ""
    }
  ],
  "constants": [
    {
      "type": "double",
      "name": "test",
      "value": "10",
      "description": ""
    }
  ]
}

# 20 blocks final: buy now, fixed volume
input_data_30 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "cacf5206-73c8-4eb8-b4bc-134ad3bdb202",
          "id_by_user": 3,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "",
            "group": "11",
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon",
            "how_much_volume": "0.1",
            "stoploss": "20",
            "takeprofit": "20"
          },
          "id": "9c03b701-51b1-4808-940b-bd21591b3156",
          "id_by_user": 4,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "cacf5206-73c8-4eb8-b4bc-134ad3bdb202",
          "sourceHandle": "blue",
          "target": "9c03b701-51b1-4808-940b-bd21591b3156",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-cacf5206-73c8-4eb8-b4bc-134ad3bdb202blue-9c03b701-51b1-4808-940b-bd21591b3156c"
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
  "variables": [
    {
      "type": "double",
      "name": "my_var",
      "value": "5",
      "description": ""
    }
  ],
  "constants": [
    {
      "type": "double",
      "name": "test",
      "value": "10",
      "description": ""
    }
  ]
}

# 20 blocks final: buy now, percent of equity
input_data_31 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "cacf5206-73c8-4eb8-b4bc-134ad3bdb202",
          "id_by_user": 3,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "",
            "group": "11",
            "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon",
            "stoploss": "20",
            "takeprofit": "20",
            "how_much_volume": "1"
          },
          "id": "9c03b701-51b1-4808-940b-bd21591b3156",
          "id_by_user": 4,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "cacf5206-73c8-4eb8-b4bc-134ad3bdb202",
          "sourceHandle": "blue",
          "target": "9c03b701-51b1-4808-940b-bd21591b3156",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-cacf5206-73c8-4eb8-b4bc-134ad3bdb202blue-9c03b701-51b1-4808-940b-bd21591b3156c"
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
  "variables": [
    {
      "type": "double",
      "name": "my_var",
      "value": "5",
      "description": ""
    }
  ],
  "constants": [
    {
      "type": "double",
      "name": "test",
      "value": "10",
      "description": ""
    }
  ]
}

# 20 blocks final: buy now, switch erraction removed, slippage value calc corrected
input_data_32 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "55b1db93-ea73-4505-8583-488e582db4c1",
          "id_by_user": 5,
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
          "id": "66b43634-ad92-4b79-a496-bdc1e9edefec",
          "id_by_user": 6,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "",
            "group": "11",
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon",
            "how_much_volume": "0.1",
            "stoploss": "20",
            "takeprofit": "20"
          },
          "id": "9d9bf64f-7764-4184-ab05-7466f66fdf27",
          "id_by_user": 7,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "55b1db93-ea73-4505-8583-488e582db4c1",
          "sourceHandle": "blue",
          "target": "66b43634-ad92-4b79-a496-bdc1e9edefec",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-55b1db93-ea73-4505-8583-488e582db4c1blue-66b43634-ad92-4b79-a496-bdc1e9edefecc"
        },
        {
          "source": "66b43634-ad92-4b79-a496-bdc1e9edefec",
          "sourceHandle": "blue",
          "target": "9d9bf64f-7764-4184-ab05-7466f66fdf27",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-66b43634-ad92-4b79-a496-bdc1e9edefecblue-9d9bf64f-7764-4184-ab05-7466f66fdf27c"
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

# events added by behrouz
input_data_33 = {
  "events": {
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
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE",
                "adjust": "",
                "symbol": "",
                "timeframe": "PERIOD_CURRENT",
                "shift": ""
              }
            },
            "right": {
              "row1": "indicator",
              "row2": "ma",
              "params": {
                "value": "1",
                "ma_period": "20",
                "ma_shift": "0",
                "ma_method": "MODE_SMMA",
                "applied_price": "PRICE_CLOSE",
                "adjust": "",
                "symbol": "",
                "timeframe": "PERIOD_CURRENT",
                "shift": ""
              }
            }
          },
          "id": "74c4c2aa-2ad3-401d-87bd-5a570e444509",
          "id_by_user": 1,
          "category": "condition_formula",
          "block_name_mql": "condition",
          "blockName": "Condition"
        },
        {
          "params": {
            "time_start_mode": "TIME_MODE_TEXT",
            "time_start": "00:00",
            "time_end_mode": "TIME_MODE_TEXT",
            "time_end": "00:01",
            "time_mode": "TIME_SERVER"
          },
          "id": "4afbd2b8-43ee-4a77-8360-28f73ccce4c6",
          "id_by_user": 2,
          "category": "time_filters",
          "block_name_mql": "time_filter",
          "blockName": "Time filter"
        }
      ],
      "edges": [
        {
          "source": "4afbd2b8-43ee-4a77-8360-28f73ccce4c6",
          "sourceHandle": "blue",
          "target": "74c4c2aa-2ad3-401d-87bd-5a570e444509",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-4afbd2b8-43ee-4a77-8360-28f73ccce4c6blue-74c4c2aa-2ad3-401d-87bd-5a570e444509c"
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

# 20 blocks final: buy now, lots calc for percent of equity corrected
input_data_34 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "55b1db93-ea73-4505-8583-488e582db4c1",
          "id_by_user": 5,
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
          "id": "66b43634-ad92-4b79-a496-bdc1e9edefec",
          "id_by_user": 6,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "symbol": "",
            "group": "11",
            "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon",
            "stoploss": "20",
            "takeprofit": "20",
            "how_much_volume": "2.5"
          },
          "id": "9d9bf64f-7764-4184-ab05-7466f66fdf27",
          "id_by_user": 7,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "55b1db93-ea73-4505-8583-488e582db4c1",
          "sourceHandle": "blue",
          "target": "66b43634-ad92-4b79-a496-bdc1e9edefec",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-55b1db93-ea73-4505-8583-488e582db4c1blue-66b43634-ad92-4b79-a496-bdc1e9edefecc"
        },
        {
          "source": "66b43634-ad92-4b79-a496-bdc1e9edefec",
          "sourceHandle": "blue",
          "target": "9d9bf64f-7764-4184-ab05-7466f66fdf27",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-66b43634-ad92-4b79-a496-bdc1e9edefecblue-9d9bf64f-7764-4184-ab05-7466f66fdf27c"
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

# 20 blocks final: buy pending issue solved?
input_data_35 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "55b1db93-ea73-4505-8583-488e582db4c1",
          "id_by_user": 5,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "",
            "group": "11",
            "open_at_price": "OPEN_AT_ASK",
            "money_management": "MONEY_MANAGEMENT_PERCENT_OF_EQUITY",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrDarkBlue",
            "price_offset": "20",
            "stoploss": "20",
            "takeprofit": "20",
            "how_much_volume": "2.5"
          },
          "id": "550d5451-e687-4548-b209-f76578320962",
          "id_by_user": 6,
          "blockName": "Buy pending order",
          "category": "buy_sell",
          "block_name_mql": "buy_pending_order"
        }
      ],
      "edges": [
        {
          "source": "55b1db93-ea73-4505-8583-488e582db4c1",
          "sourceHandle": "blue",
          "target": "550d5451-e687-4548-b209-f76578320962",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-55b1db93-ea73-4505-8583-488e582db4c1blue-550d5451-e687-4548-b209-f76578320962c"
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

input_data_36 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "55b1db93-ea73-4505-8583-488e582db4c1",
          "id_by_user": 5,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "symbol": "",
            "group": "11",
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "volume_upper_limit": "0",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrMaroon",
            "how_much_volume": "0.1",
            "stoploss": "20",
            "takeprofit": "20"
          },
          "id": "9274f652-9c59-421f-b754-84fea251770b",
          "id_by_user": 6,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "55b1db93-ea73-4505-8583-488e582db4c1",
          "sourceHandle": "blue",
          "target": "9274f652-9c59-421f-b754-84fea251770b",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-55b1db93-ea73-4505-8583-488e582db4c1blue-9274f652-9c59-421f-b754-84fea251770bc"
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

input_data_37 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {},
          "id": "a114335f-8f24-4938-a439-1c4ad155162f",
          "id_by_user": 1,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
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
              "row1": "market-properties",
              "row2": "highset_price_candle_period"
            },
            "time_2": {
              "row1": "value",
              "row2": "Time",
              "params": {
                "mode_time": "MODE_TIME_NOW",
                "mode_time_shift": "0",
                "time_source": "TIME_SERVER"
              }
            },
            "range_pips": "10"
          },
          "id": "48d377a4-a859-441f-917e-d92cc1d807f7",
          "id_by_user": 2,
          "blockName": "No trade nearby",
          "category": "check_trades_orders_count",
          "block_name_mql": "no_trade_nearby"
        }
      ],
      "edges": [
        {
          "source": "a114335f-8f24-4938-a439-1c4ad155162f",
          "sourceHandle": "blue",
          "target": "48d377a4-a859-441f-917e-d92cc1d807f7",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-a114335f-8f24-4938-a439-1c4ad155162fblue-48d377a4-a859-441f-917e-d92cc1d807f7c"
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

input_data_38 = {
  "events": {
    "on_tick": {
      "edges": [
        {
          "source": "38f822a8-e6a3-45aa-8244-9470dd234db5",
          "sourceHandle": "blue",
          "target": "e1a6c752-60f4-497f-a3df-2ef65480f8d4",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-38f822a8-e6a3-45aa-8244-9470dd234db5blue-e1a6c752-60f4-497f-a3df-2ef65480f8d4c"
        }
      ],
      "nodes": [
        {
          "params": {
            "symbol": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "38f822a8-e6a3-45aa-8244-9470dd234db5",
          "id_by_user": 2,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "value_fetch_1": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "value_fetch_2": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "value_fetch_3": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "value_fetch_4": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "Value": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "value_fetch_6": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "value_fetch_7": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "value_fetch_8": {
              "row1": "value",
              "row2": "Text",
              "params": {
                "value": "sample text",
                "adjust": ""
              }
            },
            "title": "This is comment",
            "obj_chart_subwindow": "",
            "obj_corner": "CORNER_RIGHT_UPPER",
            "obj_x": "80",
            "obj_y": "80",
            "obj_title_font": "Georgia",
            "obj_title_font_color": "clrOlive",
            "obj_title_font_size": "13",
            "obj_label_font": "Vardena",
            "obj_label_font_color": "clrOlive",
            "obj_label_font_size": "10",
            "obj_font": "Vardena",
            "obj_font_color": "clrOlive",
            "obj_font_size": "10",
            "label_1": "triger_1 : ",
            "format_number_1": "4",
            "format_time_1": "TIME_DATE",
            "label_2": "",
            "format_number_2": "EMPTY_VALUE",
            "format_time_2": "EMPTY_VALUE",
            "label_3": "",
            "format_number_3": "EMPTY_VALUE",
            "format_time_3": "EMPTY_VALUE",
            "label_4": "",
            "format_number_4": "EMPTY_VALUE",
            "format_time_4": "EMPTY_VALUE",
            "label_5": "",
            "format_number_5": "EMPTY_VALUE",
            "format_time_5": "EMPTY_VALUE",
            "label_6": "",
            "format_number_6": "EMPTY_VALUE",
            "format_time_6": "EMPTY_VALUE",
            "label_7": "",
            "format_number_7": "EMPTY_VALUE",
            "format_time_7": "EMPTY_VALUE",
            "label_8": "",
            "format_time_8": "EMPTY_VALUE"
          },
          "id": "e1a6c752-60f4-497f-a3df-2ef65480f8d4",
          "id_by_user": 3,
          "blockName": "Comment",
          "category": "output_communication",
          "block_name_mql": "comment"
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
      "name": "xxx",
      "value": "50",
      "description": ""
    }
  ]
}

# 20 blocks final: candle > total size pips > runtime error > divide by zero : Bug solved
input_data_39 = {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "c1e6f259-e56d-4973-84cb-aca42ed22594",
            "sourceHandle": "blue",
            "target": "9b2ba02e-5d1a-4260-b6e4-9f5ea6fbb82c",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-c1e6f259-e56d-4973-84cb-aca42ed22594blue-9b2ba02e-5d1a-4260-b6e4-9f5ea6fbb82cc"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "c1e6f259-e56d-4973-84cb-aca42ed22594",
            "id_by_user": 2,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
          },
          {
            "params": {
              "operator": {
                "label": "+"
              },
              "left": {
                "row1": "candle",
                "row2": "Candle",
                "params": {
                  "price_mode": "BEAR_CANDLE_TOTAL_SIZE",
                  "find_method": "FIND_BY_ID",
                  "adjust": "",
                  "symbol": "",
                  "timeframe": "PERIOD_CURRENT",
                  "shift": "10"
                }
              },
              "right": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": "*20"
                }
              },
              "adjust": "",
              "variable": ""
            },
            "id": "9b2ba02e-5d1a-4260-b6e4-9f5ea6fbb82c",
            "id_by_user": 3,
            "blockName": "Formula",
            "category": "condition_formula",
            "block_name_mql": "formula"
          }
        ]
      },
      "on_init": {
        "nodes": [],
        "edges": []
      },
      "on_timer": {
        "nodes": [],
        "edges": []
      },
      "on_trade": {
        "nodes": [],
        "edges": []
      },
      "on_chart": {
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

input_data_40 = {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "c1e6f259-e56d-4973-84cb-aca42ed22594",
            "sourceHandle": "blue",
            "target": "37a14f9e-94ca-4f6a-b8ad-1b91bd52b6ef",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-c1e6f259-e56d-4973-84cb-aca42ed22594blue-37a14f9e-94ca-4f6a-b8ad-1b91bd52b6efc"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "c1e6f259-e56d-4973-84cb-aca42ed22594",
            "id_by_user": 2,
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
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "20",
                  "adjust": "-15%"
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
            "id": "37a14f9e-94ca-4f6a-b8ad-1b91bd52b6ef",
            "id_by_user": 3,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          }
        ]
      },
      "on_init": {
        "nodes": [],
        "edges": []
      },
      "on_timer": {
        "nodes": [],
        "edges": []
      },
      "on_trade": {
        "nodes": [],
        "edges": []
      },
      "on_chart": {
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

input_data_41 = {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "c1e6f259-e56d-4973-84cb-aca42ed22594",
            "sourceHandle": "blue",
            "target": "37a14f9e-94ca-4f6a-b8ad-1b91bd52b6ef",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-c1e6f259-e56d-4973-84cb-aca42ed22594blue-37a14f9e-94ca-4f6a-b8ad-1b91bd52b6efc"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "c1e6f259-e56d-4973-84cb-aca42ed22594",
            "id_by_user": 2,
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
                "row1": "value",
                "row2": "Text",
                "params": {
                  "value": "hello",
                  "adjust": "+ How r u?"
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
            "id": "37a14f9e-94ca-4f6a-b8ad-1b91bd52b6ef",
            "id_by_user": 3,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          }
        ]
      },
      "on_init": {
        "nodes": [],
        "edges": []
      },
      "on_timer": {
        "nodes": [],
        "edges": []
      },
      "on_trade": {
        "nodes": [],
        "edges": []
      },
      "on_chart": {
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

# 20 blocks final: buy/sell pending > open at custom price > price offset won't apply in this situation
input_data_42 = {
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
              "type": "{0,1}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "If trade",
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade"
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
}

# 20 blocks final: data structure changed at backend side. So I updated the structure: whole data is set in an object with the key: "data"
input_data_43 = {
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
              "type": "{0,1}",
              "symbols_str": ""
            },
            "id": "df193530-239a-42aa-94e2-ae27014a4afe",
            "id_by_user": 5,
            "blockName": "If trade",
            "category": "check_trades_orders_count",
            "block_name_mql": "if_trade"
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

input_data_44 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "da1e5c89-8787-43d9-a3e0-2d23ba0e4a42",
            "sourceHandle": "blue",
            "target": "c7c13326-a0ea-4768-af90-dd0d236de389",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-da1e5c89-8787-43d9-a3e0-2d23ba0e4a42blue-c7c13326-a0ea-4768-af90-dd0d236de389c"
          }
        ],
        "nodes": [
          {
            "params": {
              "symbol": "",
              "group": "11",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrMaroon",
              "how_much_volume": "0.1",
              "stoploss": "20",
              "takeprofit": "20"
            },
            "id": "c7c13326-a0ea-4768-af90-dd0d236de389",
            "id_by_user": 1,
            "blockName": "Buy now",
            "category": "buy_sell",
            "block_name_mql": "buy_now"
          },
          {
            "params": {
              "symbol": "",
              "timeframe": "PERIOD_CURRENT",
              "max_times_to_pass": "1"
            },
            "id": "da1e5c89-8787-43d9-a3e0-2d23ba0e4a42",
            "id_by_user": 2,
            "blockName": "Once per bar",
            "category": "time_filters",
            "block_name_mql": "once_per_bar"
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
  "selected_name": "17f204c7-74b5-4f9d-af54-5dbdb83ad576"
}

input_data_45 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "957c8089-1f72-4362-aad8-65e6e65113a4",
            "sourceHandle": "blue",
            "target": "48680d23-0da5-4e01-8233-e640080b8ac9",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-957c8089-1f72-4362-aad8-65e6e65113a4blue-48680d23-0da5-4e01-8233-e640080b8ac9c"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "957c8089-1f72-4362-aad8-65e6e65113a4",
            "id_by_user": 3,
            "blockName": "Pass",
            "category": "more",
            "block_name_mql": "pass"
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
              "price_offset": "20",
              "price_to_open_dynamic_level": {
                "row1": "value",
                "row2": "Numeric",
                "params": {
                  "value": "1",
                  "adjust": ""
                }
              }
            },
            "id": "48680d23-0da5-4e01-8233-e640080b8ac9",
            "id_by_user": 4,
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
    "constants": []
  },
  "selected_name": "8129b83c-a940-4930-a7fe-a410b1df760f"
}












