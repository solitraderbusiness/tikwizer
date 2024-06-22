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
                                "row1": "object-on-the-chart",
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
                                "row1": "object-on-the-chart",
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

# test field referenced to global var
input_data_6 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "7538d537-ca45-4ede-b401-40c35c7c1774",
            "sourceHandle": "blue",
            "target": "99a78f55-6255-4687-b23c-b6afa221f6ba",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-7538d537-ca45-4ede-b401-40c35c7c1774blue-99a78f55-6255-4687-b23c-b6afa221f6bac"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "7538d537-ca45-4ede-b401-40c35c7c1774",
            "id_by_user": 1,
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
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrMaroon",
              "how_much_volume": "test",
              "stoploss": "20",
              "takeprofit": "20"
            },
            "id": "99a78f55-6255-4687-b23c-b6afa221f6ba",
            "id_by_user": 2,
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
    "variables": [
      {
        "type": "double",
        "name": "test",
        "value": "",
        "description": ""
      }
    ],
    "constants": []
  },
  "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
  "name_by_user": "test 8624",
  "highestIndex": "3"
}

# test field referenced to global var
input_data_7 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
            "sourceHandle": "blue",
            "target": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-ad6608c5-5627-4517-ad41-2be6d7ed938bblue-9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4c"
          },
          {
            "source": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
            "sourceHandle": "blue",
            "target": "b5f6e916-91bc-410e-bff0-94640b249cd8",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-ad6608c5-5627-4517-ad41-2be6d7ed938bblue-b5f6e916-91bc-410e-bff0-94640b249cd8c"
          },
          {
            "source": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
            "sourceHandle": "red",
            "target": "730acf16-7e2d-4c9f-9c99-d692ecc637b0",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-ad6608c5-5627-4517-ad41-2be6d7ed938bred-730acf16-7e2d-4c9f-9c99-d692ecc637b0c"
          },
          {
            "source": "b5f6e916-91bc-410e-bff0-94640b249cd8",
            "sourceHandle": "blue",
            "target": "23f4a20a-3966-4cda-a926-a028218c2ba3",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-b5f6e916-91bc-410e-bff0-94640b249cd8blue-23f4a20a-3966-4cda-a926-a028218c2ba3c"
          },
          {
            "source": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
            "sourceHandle": "blue",
            "target": "5d36e995-fccd-4f36-b7c6-19f0e78fff9b",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4blue-5d36e995-fccd-4f36-b7c6-19f0e78fff9bc"
          },
          {
            "source": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
            "sourceHandle": "red",
            "target": "3455f650-9d7a-4212-982c-3050085fe535",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4red-3455f650-9d7a-4212-982c-3050085fe535c"
          }
        ],
        "nodes": [
          {
            "params": {
              "symbol": "",
              "group": "11",
              "open_at_price": "OPEN_AT_ASK",
              "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
              "volume_upper_limit": "0",
              "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
              "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
              "slippage": "4",
              "comment": "",
              "arrow_color": "clrDarkBlue",
              "price_offset": "20",
              "how_much_volume": "0.1",
              "stoploss": "test",
              "takeprofit": "20"
            },
            "id": "ad6608c5-5627-4517-ad41-2be6d7ed938b",
            "id_by_user": 2,
            "blockName": "Buy pending order",
            "category": "buy_sell",
            "block_name_mql": "buy_pending_order"
          },
          {
            "params": {
              "server_or_local_time": "TIME_SERVER",
              "FirstStartMinute": "5",
              "FirstEndMinute": "test",
              "SecondMinutesBlock": "false",
              "ThirdMinutesBlock": "false",
              "FourthMinutesBlock": "false"
            },
            "id": "730acf16-7e2d-4c9f-9c99-d692ecc637b0",
            "id_by_user": 3,
            "blockName": "Minutes filter",
            "category": "time_filters",
            "block_name_mql": "minutes_filter"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "symbols_str": "",
              "type": "{0,1}",
              "profit_mode_each": "PROFIT_MODE_NO_MATTER",
              "profit_mode": "PROFIT_MODE_PIPS_SUM",
              "compare": ">",
              "profit_amount": "my_int"
            },
            "id": "9b280a8f-e0a6-4c44-8d2d-84a2fbf7e7f4",
            "id_by_user": 4,
            "blockName": "Check Profit (unrealized)",
            "category": "check_trading_conditions",
            "block_name_mql": "check_profit_unrealized"
          },
          {
            "params": {
              "title": "Comment Message",
              "obj_chart_subwindow": "",
              "obj_corner": "CORNER_LEFT_UPPER",
              "obj_x": "5",
              "obj_y": "24",
              "obj_title_font": "Georgia",
              "obj_title_font_color": "clrGold",
              "obj_title_font_size": "13",
              "obj_label_font": "Vardena",
              "obj_label_font_color": "clrDarkGray",
              "obj_label_font_size": "10",
              "obj_font": "Vardena",
              "obj_font_color": "clrWhite",
              "obj_font_size": "10",
              "label_1": "greetings",
              "format_number_1": "EMPTY_VALUE",
              "format_time_1": "EMPTY_VALUE",
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
              "format_number_8": "EMPTY_VALUE",
              "format_time_8": "EMPTY_VALUE",
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
              "value_fetch_5": {
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
              }
            },
            "id": "23f4a20a-3966-4cda-a926-a028218c2ba3",
            "id_by_user": 5,
            "blockName": "Comment",
            "category": "output_communication",
            "block_name_mql": "comment"
          },
          {
            "params": {
              "TimesToPass": "3",
              "CounterID": "test"
            },
            "id": "3455f650-9d7a-4212-982c-3050085fe535",
            "id_by_user": 6,
            "blockName": "Counter: Pass \"n\" times",
            "category": "counters",
            "block_name_mql": "counter_pass_n_times"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "order_age_mins": "0",
              "slippage": "4",
              "arrow_color": "clrDarkGoldenrod",
              "symbols_str": "greetings"
            },
            "id": "b5f6e916-91bc-410e-bff0-94640b249cd8",
            "id_by_user": 7,
            "blockName": "Close trades",
            "category": "trading_actions",
            "block_name_mql": "close_trades"
          },
          {
            "params": {
              "group_mode": "ORDER_GROUP_MODE_NUMBER",
              "group_number": "11",
              "symbol_mode": "SYMBOL_MODE_SPECIFIED",
              "type": "{0,1}",
              "on_profit_mode": "ON_PROFIT_MODE_FIXED_VALUE",
              "bep_offset_mode": "BEP_OFFSET_MODE_NONE",
              "symbols_str": "",
              "pips_on_profit": "my_int"
            },
            "id": "5d36e995-fccd-4f36-b7c6-19f0e78fff9b",
            "id_by_user": 8,
            "blockName": "Break even point (each trade)",
            "category": "trailing_stop_break_even",
            "block_name_mql": "break_even_point_each_trade"
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
    "variables": [
      {
        "type": "double",
        "name": "test",
        "value": "",
        "description": ""
      },
      {
        "type": "string",
        "name": "greetings",
        "value": "hellow how are your",
        "description": ""
      },
      {
        "type": "int",
        "name": "my_int",
        "value": "20",
        "description": ""
      }
    ],
    "constants": []
  },
  "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
  "name_by_user": "test 8624",
  "highestIndex": "9"
}

# test object on the chart numeric
input_data_8 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "00f7330c-2fbe-47e1-a302-bec9470ab009",
            "sourceHandle": "blue",
            "target": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-00f7330c-2fbe-47e1-a302-bec9470ab009blue-02ec7d05-12f9-4bb3-a61c-013e13eaa98fc"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "00f7330c-2fbe-47e1-a302-bec9470ab009",
            "id_by_user": 7,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "operator": {
                "label": ">",
                "cross_width": 1
              },
              "left": {
                "row1": "object-on-the-chart",
                "row2": "attribute_set_1_numeric",
                "params": {
                  "ObjSource": "name",
                  "Property": "OBJPROP_RAY_LEFT",
                  "Name": "my_object_name"
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
            "id": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
            "id_by_user": 8,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
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
    "variables": [
      {
        "type": "double",
        "name": "test",
        "value": "",
        "description": ""
      },
      {
        "type": "string",
        "name": "greetings",
        "value": "hellow how are your",
        "description": ""
      },
      {
        "type": "int",
        "name": "my_int",
        "value": "20",
        "description": ""
      }
    ],
    "constants": []
  },
  "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
  "name_by_user": "test 8624",
  "highestIndex": "9"
}

# test object on the chart numeric 2
input_data_9 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "00f7330c-2fbe-47e1-a302-bec9470ab009",
            "sourceHandle": "blue",
            "target": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-00f7330c-2fbe-47e1-a302-bec9470ab009blue-02ec7d05-12f9-4bb3-a61c-013e13eaa98fc"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "00f7330c-2fbe-47e1-a302-bec9470ab009",
            "id_by_user": 7,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "operator": {
                "label": ">",
                "cross_width": 1
              },
              "left": {
                "row1": "object-on-the-chart",
                "row2": "attribute_set_1_numeric",
                "params": {
                  "ObjSource": "objloop",
                  "Property": "OBJPROP_PERIOD"
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
            "id": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
            "id_by_user": 8,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
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
    "variables": [
      {
        "type": "double",
        "name": "test",
        "value": "",
        "description": ""
      },
      {
        "type": "string",
        "name": "greetings",
        "value": "hellow how are your",
        "description": ""
      },
      {
        "type": "int",
        "name": "my_int",
        "value": "20",
        "description": ""
      }
    ],
    "constants": []
  },
  "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
  "name_by_user": "test 8624",
  "highestIndex": "9"
}

# test object on the chart string
input_data_10 = {
  "data": {
    "events": {
      "on_tick": {
        "edges": [
          {
            "source": "00f7330c-2fbe-47e1-a302-bec9470ab009",
            "sourceHandle": "blue",
            "target": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
            "targetHandle": "c",
            "type": "customEdge",
            "id": "reactflow__edge-00f7330c-2fbe-47e1-a302-bec9470ab009blue-02ec7d05-12f9-4bb3-a61c-013e13eaa98fc"
          }
        ],
        "nodes": [
          {
            "params": {},
            "id": "00f7330c-2fbe-47e1-a302-bec9470ab009",
            "id_by_user": 7,
            "category": "more",
            "block_name_mql": "pass",
            "blockName": "Pass"
          },
          {
            "params": {
              "operator": {
                "label": ">",
                "cross_width": 1
              },
              "left": {
                "row1": "object-on-the-chart",
                "row2": "attribute_set_2_text",
                "params": {
                  "ObjSource": "name",
                  "Property": "OBJPROP_TOOLTIP",
                  "Name": "my_test_name"
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
            "id": "02ec7d05-12f9-4bb3-a61c-013e13eaa98f",
            "id_by_user": 8,
            "blockName": "Condition",
            "category": "condition_formula",
            "block_name_mql": "condition"
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
    "variables": [
      {
        "type": "double",
        "name": "test",
        "value": "",
        "description": ""
      },
      {
        "type": "string",
        "name": "greetings",
        "value": "hellow how are your",
        "description": ""
      },
      {
        "type": "int",
        "name": "my_int",
        "value": "20",
        "description": ""
      }
    ],
    "constants": []
  },
  "selected_name": "e4cb9870-8f3f-4abf-b156-55f656b06c07",
  "name_by_user": "test 8624",
  "highestIndex": "9"
}
