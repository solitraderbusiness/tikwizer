

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
