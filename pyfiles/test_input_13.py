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

# test object on the chart numeric
input_data_3 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "sourceHandle": "blue",
                        "target": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4afd77dc-82a4-4656-9f0a-6f2b0bb17b9bblue-e44bb335-3d39-4c87-a8f4-7be791aabef5c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0}",
                            "TrailWhat": "0",
                            "TrailingReferencePrice": "2",
                            "TrailingStopMode": "TRAILING_STOP_MODE_CUSTOM_LEVEL",
                            "TrailingStepMode": "TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingStartMode": "TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP",
                            "LevelColor": "clrSlateGray",
                            "symbols_str": "",
                            "value_fetch_trailingstopmode_custom_level": {
                                "row1": "object_on_the_chart",
                                "row2": "attribute_set_1_numeric",
                                "params": {
                                    "ObjSource": "name",
                                    "Name": "my_object_name",
                                    "Property": "OBJPROP_PRICE1",
                                    "FiboLevelID": 0,
                                    "TLpriceLevel": 1.2,
                                    "Shift": 0
                                }
                            },
                            "tStepPercentTS": "15",
                            "tStartPercentTS": "97",
                            "tTPpercentTS": "23"
                        },
                        "id": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "id_by_user": 1,
                        "blockName": "Trailing stop (each trade)",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_stop_each_trade"
                    },
                    {
                        "params": {},
                        "id": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
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
    "selected_name": "12302dfb-ac61-45c1-a388-f93acc8c56cd",
    "name_by_user": "test 9541",
    "highestIndex": "3"
}

# test object on the chart string
input_data_4 = {
    "data": {
        "events": {
            "on_tick": {
                "edges": [
                    {
                        "source": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "sourceHandle": "blue",
                        "target": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "targetHandle": "c",
                        "type": "customEdge",
                        "id": "reactflow__edge-4afd77dc-82a4-4656-9f0a-6f2b0bb17b9bblue-e44bb335-3d39-4c87-a8f4-7be791aabef5c"
                    }
                ],
                "nodes": [
                    {
                        "params": {
                            "group_mode": "ORDER_GROUP_MODE_NUMBER",
                            "group_number": "11",
                            "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                            "type": "{0}",
                            "TrailWhat": "0",
                            "TrailingReferencePrice": "2",
                            "TrailingStopMode": "TRAILING_STOP_MODE_CUSTOM_LEVEL",
                            "TrailingStepMode": "TRAILING_STEP_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingStartMode": "TRAILING_START_MODE_PERCENT_OF_TRAILING_STOP",
                            "TrailingTPmode": "TRAILING_OPPOSITE_STOP_MODE_PERCENT_OF_TRAILING_STOP",
                            "LevelColor": "clrSlateGray",
                            "symbols_str": "",
                            "value_fetch_trailingstopmode_custom_level": {
                                "row1": "object_on_the_chart",
                                "row2": "attribute_set_2_text",
                                "params": {
                                    "ObjSource": "name",
                                    "Name": "my_object_name",
                                    "Property": "OBJPROP_TEXT",
                                    "adjust": "+\"hello\""
                                }
                            },
                            "tStepPercentTS": "15",
                            "tStartPercentTS": "97",
                            "tTPpercentTS": "23"
                        },
                        "id": "e44bb335-3d39-4c87-a8f4-7be791aabef5",
                        "id_by_user": 1,
                        "blockName": "Trailing stop (each trade)",
                        "category": "trailing_stop_break_even",
                        "block_name_mql": "trailing_stop_each_trade"
                    },
                    {
                        "params": {},
                        "id": "4afd77dc-82a4-4656-9f0a-6f2b0bb17b9b",
                        "id_by_user": 2,
                        "category": "more",
                        "block_name_mql": "pass",
                        "blockName": "Pass"
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
    "selected_name": "12302dfb-ac61-45c1-a388-f93acc8c56cd",
    "name_by_user": "test 9541",
    "highestIndex": "3"
}

# test value > text
input_data_5 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "f86625a3-931f-436f-a8d9-7f84b09891f1",
            "sourceHandle": "blue",
            "target": "4402e815-fe75-4f58-8b85-331902cc366a",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-f86625a3-931f-436f-a8d9-7f84b09891f1blue-4402e815-fe75-4f58-8b85-331902cc366ac"
          }
        ],
        "nodes": [
          {
            "params": {
              "operator": {
                "label": ">",
                "cross_width": 1
              },
              "left": {
                "row1": "value",
                "row2": "Text_code_input",
                "params": {
                  "value": "test",
                  "adjust": ""
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
            "id": "4402e815-fe75-4f58-8b85-331902cc366a",
            "id_by_user": 1,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
          },
          {
            "params": {},
            "id": "f86625a3-931f-436f-a8d9-7f84b09891f1",
            "id_by_user": 2,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
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
  "selected_name": "4b8a6158-eaae-4594-8165-07266c19b782",
  "name_by_user": "test 563",
  "highestIndex": "3"
}
