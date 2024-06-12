
# test for each trade new
input_data_1 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "4eb302a9-43d7-4c6a-9e4a-34a2b7a67cde",
            "sourceHandle": "blue",
            "target": "b62ec518-9b85-4ae0-ad7a-0b5054a64b88",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-4eb302a9-43d7-4c6a-9e4a-34a2b7a67cdeblue-b62ec518-9b85-4ae0-ad7a-0b5054a64b88c"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "4eb302a9-43d7-4c6a-9e4a-34a2b7a67cde",
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
              "type": "{0,1}",
              "loop_direction": "newest_last",
              "skip_n": "0",
              "every_n": "1",
              "not_more_than_n": "0",
              "symbols_str": "",
              "second_output": "if_not_empty"
            },
            "id": "b62ec518-9b85-4ae0-ad7a-0b5054a64b88",
            "id_by_user": 2,
            "blockName": "For each Trade",
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade"
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
  "selected_name": "409f8aa1-318e-41a2-b529-607c8f727a2d",
  "name_by_user": "test 6524",
  "highestIndex": "3"
}

# test for each trade
input_data_2 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "c86ae960-00e5-48ca-8fef-065d9aac72cc",
            "sourceHandle": "blue",
            "target": "6ed57532-5a0a-4eda-a91b-073fde51bb24",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-c86ae960-00e5-48ca-8fef-065d9aac72ccblue-6ed57532-5a0a-4eda-a91b-073fde51bb24c"
          }
        ],
        "nodes": [
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
              "loop_direction": "LOOP_DIRECTION_NEWEST_TO_OLDEST"
            },
            "id": "c86ae960-00e5-48ca-8fef-065d9aac72cc",
            "id_by_user": 3,
            "category": "loop_for_trades_orders",
            "block_name_mql": "for_each_trade",
            "blockName": "For each Trade"
          },
          {
            "params": {
              "operator": ">",
              "check_mode": "CHECK_PROFIT_LOSS_MODE_DEPOSIT_CURRENCY",
              "check_value": "10"
            },
            "id": "6ed57532-5a0a-4eda-a91b-073fde51bb24",
            "id_by_user": 4,
            "category": "loop_for_trades_orders",
            "block_name_mql": "check_loss",
            "blockName": "check loss"
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
  "selected_name": "409f8aa1-318e-41a2-b529-607c8f727a2d",
  "name_by_user": "test 6524",
  "highestIndex": "5"
}
