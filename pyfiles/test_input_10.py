# test volume profile
input_data_1 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "Order TP modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 15,
                        "type": "{3,5}",
                        "type_pending": "{4,5}",
                        "tp_only": "no"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "Volume profile",
                    "params": {
                        "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                        "RangeMinutes": 1440,
                        "ModeStep": 100,
                        "HgPointScale": "POINT_SCALE_20",
                        "VolumeType": "VOLUME_TICK",
                        "DataSource": "VP_SOURCE_M1",

                        "HgBarStyle": "VP_BAR_STYLE_LINE",
                        "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                        "HgColor": "clrYellow",
                        "HgColor2": "clrOrange",
                        "HgLineWidth": 2,

                        "ModeColor": "clrBlue",
                        "MaxColor": "clrNONE",
                        "MedianColor": "clrNONE",
                        "VwapColor": "clrNONE",
                        "ModeLineWidth": 1,
                        "StatLineStyle": "STYLE_DOT",

                        "ModeLevelColor": "clrNONE",
                        "ModeLevelStyle": "STYLE_SOLID",

                        "Id": "+vpr"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "sourceHandle": "blue",
                    "target": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]

        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [

            ],
            "edges": [

            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test volume profile 2
input_data_2 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "Order TP modified",
                    "params": {
                        "symbol_mode": "SYMBOL_MODE_SPECIFIED",
                        "symbols_str": ",EURUSD,GBPUSD",
                        "group_mode": "ORDER_GROUP_MODE_ALL",
                        "group_number": 11,
                        "type": "{2,4}",
                        "type_pending": "{2,3}",
                        "tp_only": "no"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "Volume profile",
                    "params": {
                        "RangeMode": "VP_RANGE_MODE_MINUTES_TO_LINE",
                        "RangeMinutes": 1440,
                        "ModeStep": 100,
                        "HgPointScale": "POINT_SCALE_20",
                        "VolumeType": "VOLUME_REAL",
                        "DataSource": "VP_SOURCE_M1",

                        "HgBarStyle": "VP_BAR_STYLE_OUTLINE",
                        "HgPosition": "VP_HG_POSITION_WINDOW_RIGHT",
                        "HgColor": "clrYellow",
                        "HgColor2": "clrOrange",
                        "HgLineWidth": 1,

                        "ModeColor": "clrBlue",
                        "MaxColor": "clrNONE",
                        "MedianColor": "clrNONE",
                        "VwapColor": "clrNONE",
                        "ModeLineWidth": 2,
                        "StatLineStyle": "STYLE_DOT",

                        "ModeLevelColor": "clrNONE",
                        "ModeLevelStyle": "STYLE_SOLID",

                        "Id": "+vpr"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "sourceHandle": "blue",
                    "target": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]

        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [

            ],
            "edges": [

            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}

# test condition new apis
input_data_3 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "max_times_to_pass": "1",
                        "symbol": "",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "42cfc35a-969a-4a4d-9eb1-502f55d534f4",
                    "id_by_user": 3,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "operator": {
                            "label": "×>",
                            "cross_width": 1
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": "24",
                                "slow_ema_period": "9",
                                "signal_period": "9",
                                "mode": "MANI_LINE",
                                "applied_price": "PRICE_CLOSE"
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": "24",
                                "slow_ema_period": "9",
                                "signal_period": "9",
                                "mode": "SIGNAL_LINE",
                                "applied_price": "PRICE_CLOSE"
                            }
                        }
                    },
                    "id": "74264b27-d473-45ee-9e68-5a3ed08d6a73",
                    "id_by_user": 4,
                    "blockName": "Condition"
                },
                {
                    "0": "1",
                    "params": {
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "group": "11",
                        "symbol": "",
                        "how_much_volume": "0.2",
                        "volume": "Value,Numeric",
                        "test": "TEST",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "0",
                        "martingale_reset_on_n_profits": "1",
                        "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
                        "stoploss": "20",
                        "takeprofit": "40",
                        "slippage": "4",
                        "comment": "",
                        "arrow_color": "clrBlue"
                    },
                    "id": "a4af4523-bfe3-44d2-9180-283a5f197a61",
                    "id_by_user": 5,
                    "blockName": "Buy now"
                }
            ],
            "edges": [
                {
                    "source": "42cfc35a-969a-4a4d-9eb1-502f55d534f4",
                    "sourceHandle": "blue",
                    "target": "74264b27-d473-45ee-9e68-5a3ed08d6a73",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-42cfc35a-969a-4a4d-9eb1-502f55d534f4blue-74264b27-d473-45ee-9e68-5a3ed08d6a73c"
                },
                {
                    "source": "74264b27-d473-45ee-9e68-5a3ed08d6a73",
                    "sourceHandle": "blue",
                    "target": "a4af4523-bfe3-44d2-9180-283a5f197a61",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-74264b27-d473-45ee-9e68-5a3ed08d6a73blue-a4af4523-bfe3-44d2-9180-283a5f197a61c"
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

# test condition new apis
input_data_4 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "max_times_to_pass": "1",
                        "symbol": "",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "9163ab84-7fdb-484e-87a6-7d7f738127b7",
                    "id_by_user": 1,
                    "blockName": "Once per bar"
                },
                {
                    "params": {
                        "operator": {
                            "label": ">",
                            "cross_width": 1
                        },
                        "left": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": "24",
                                "slow_ema_period": "9",
                                "signal_period": "9",
                                "mode": "MODE_SIGNAL",
                                "applied_price": "PRICE_CLOSE"
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": "20",
                                "slow_ema_period": "9",
                                "signal_period": "9",
                                "mode": "MODE_SIGNAL",
                                "applied_price": "PRICE_CLOSE"
                            }
                        }
                    },
                    "id": "4da69cf8-b84b-4c80-9cb5-8e46e9dc08db",
                    "id_by_user": 2,
                    "blockName": "Condition"
                },
                {
                    "0": "1",
                    "params": {
                        "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
                        "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
                        "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
                        "group": "11",
                        "symbol": "",
                        "how_much_volume": "1",
                        "volume": "Value,Numeric",
                        "test": "TEST",
                        "martingale_init_vol": "0.1",
                        "martingale_multiply_on_loss": "2",
                        "martingale_multiply_on_profit": "1",
                        "martingale_addlots_on_loss": "0",
                        "martingale_addlots_on_profit": "0",
                        "martingale_reset_on_n_losses": "0",
                        "martingale_reset_on_n_profits": "1",
                        "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
                        "stoploss": "20",
                        "takeprofit": "50",
                        "slippage": "4",
                        "comment": "",
                        "arrow_color": "clrBlue"
                    },
                    "id": "6319981d-7cb7-4599-a0f4-74636dccfd11",
                    "id_by_user": 3,
                    "blockName": "Buy now"
                }
            ],
            "edges": [
                {
                    "source": "9163ab84-7fdb-484e-87a6-7d7f738127b7",
                    "sourceHandle": "blue",
                    "target": "4da69cf8-b84b-4c80-9cb5-8e46e9dc08db",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-9163ab84-7fdb-484e-87a6-7d7f738127b7blue-4da69cf8-b84b-4c80-9cb5-8e46e9dc08dbc"
                },
                {
                    "source": "4da69cf8-b84b-4c80-9cb5-8e46e9dc08db",
                    "sourceHandle": "blue",
                    "target": "6319981d-7cb7-4599-a0f4-74636dccfd11",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-4da69cf8-b84b-4c80-9cb5-8e46e9dc08dbblue-6319981d-7cb7-4599-a0f4-74636dccfd11c"
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

# test volume profile multi instance test
input_data_5 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "id": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "id_by_user": 0,
                    "blockName": "Volume profile",
                    "params": {
                        "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                        "RangeMinutes": 1440,
                        "ModeStep": 100,
                        "HgPointScale": "POINT_SCALE_20",
                        "VolumeType": "VOLUME_TICK",
                        "DataSource": "VP_SOURCE_M1",

                        "HgBarStyle": "VP_BAR_STYLE_LINE",
                        "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                        "HgColor": "clrYellow",
                        "HgColor2": "clrOrange",
                        "HgLineWidth": 2,

                        "ModeColor": "clrBlue",
                        "MaxColor": "clrNONE",
                        "MedianColor": "clrNONE",
                        "VwapColor": "clrNONE",
                        "ModeLineWidth": 1,
                        "StatLineStyle": "STYLE_DOT",

                        "ModeLevelColor": "clrNONE",
                        "ModeLevelStyle": "STYLE_SOLID",

                        "Id": "+vpr"
                    }
                },
                {
                    "id": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "id_by_user": 1,
                    "blockName": "Volume profile",
                    "params": {
                        "RangeMode": "VP_RANGE_MODE_BETWEEN_LINES",
                        "RangeMinutes": 1440,
                        "ModeStep": 100,
                        "HgPointScale": "POINT_SCALE_20",
                        "VolumeType": "VOLUME_TICK",
                        "DataSource": "VP_SOURCE_M1",

                        "HgBarStyle": "VP_BAR_STYLE_LINE",
                        "HgPosition": "VP_HG_POSITION_LEFT_INSIDE",
                        "HgColor": "clrYellow",
                        "HgColor2": "clrOrange",
                        "HgLineWidth": 2,

                        "ModeColor": "clrBlue",
                        "MaxColor": "clrNONE",
                        "MedianColor": "clrNONE",
                        "VwapColor": "clrNONE",
                        "ModeLineWidth": 1,
                        "StatLineStyle": "STYLE_DOT",

                        "ModeLevelColor": "clrNONE",
                        "ModeLevelStyle": "STYLE_SOLID",

                        "Id": "+vpr"
                    }
                }
            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5dt",
                    "sourceHandle": "blue",
                    "target": "361e37db-e957-40fd-b072-3122dfc3e04t",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                }
            ]

        },
        "on_chart": {
            "nodes": [

            ],
            "edges": [
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-31a6b06c-eb77-474e-8ab0-e49b1be123baa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "red",
                    "target": "976f8167-8ed7-43da-b339-b3025599dba6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0red-976f8167-8ed7-43da-b339-b3025599dba6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "31a6b06c-eb77-474e-8ab0-e49b1be123ba",
                    "sourceHandle": "blue",
                    "target": "f2ad1905-cdf8-4498-a2c0-bab4aafecb1f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-31a6b06c-eb77-474e-8ab0-e49b1be123bablue-f2ad1905-cdf8-4498-a2c0-bab4aafecb1fa"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5196a96e-8e8d-4405-a5f2-ced6d7a748d0",
                    "sourceHandle": "blue",
                    "target": "d4df2d49-399f-4e47-b65a-262b1b5975dc",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5196a96e-8e8d-4405-a5f2-ced6d7a748d0blue-d4df2d49-399f-4e47-b65a-262b1b5975dca"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "blue",
                    "target": "ed37d0ca-5431-46d4-99b8-17f6d4e64e64",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbblue-ed37d0ca-5431-46d4-99b8-17f6d4e64e64a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "527db3b2-a921-4451-87e3-a8e559bb84bb",
                    "sourceHandle": "red",
                    "target": "671a757d-f060-449d-a12f-4dd66eac8901",
                    "targetHandle": "a",
                    "id": "reactflow__edge-527db3b2-a921-4451-87e3-a8e559bb84bbred-671a757d-f060-449d-a12f-4dd66eac8901a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "50fe37fb-4728-492d-9ae2-d41215ef12c8",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-50fe37fb-4728-492d-9ae2-d41215ef12c8a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "blue",
                    "target": "02443f26-1c88-427b-8876-b367e9a0e204",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172blue-02443f26-1c88-427b-8876-b367e9a0e204a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "28bc69af-2bfd-4459-a941-336d45b34172",
                    "sourceHandle": "red",
                    "target": "391a1ba2-bead-4da8-8949-53591705f44f",
                    "targetHandle": "a",
                    "id": "reactflow__edge-28bc69af-2bfd-4459-a941-336d45b34172red-391a1ba2-bead-4da8-8949-53591705f44fa",
                    "selected": False
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "5d3a9bbc-fb09-454e-bede-d2dc897a3406",
                    "sourceHandle": "blue",
                    "target": "4720d019-aa53-49a4-a8a8-9f94d45bebc6",
                    "targetHandle": "a",
                    "id": "reactflow__edge-5d3a9bbc-fb09-454e-bede-d2dc897a3406blue-4720d019-aa53-49a4-a8a8-9f94d45bebc6a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "907e1754-7cd6-4c2e-9836-e2b58ae74978",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-907e1754-7cd6-4c2e-9836-e2b58ae74978a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "blue",
                    "target": "9058a665-2cc5-4bcc-ae3c-b8b86d1b8650",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4blue-9058a665-2cc5-4bcc-ae3c-b8b86d1b8650a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "a06ea8eb-7b44-4be6-bce4-a0df16fa61f4",
                    "sourceHandle": "red",
                    "target": "3a0a92ab-8e6c-47e7-b30a-176ede61954e",
                    "targetHandle": "a",
                    "id": "reactflow__edge-a06ea8eb-7b44-4be6-bce4-a0df16fa61f4red-3a0a92ab-8e6c-47e7-b30a-176ede61954ea"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "blue",
                    "target": "edee43ad-08e7-429b-a656-c7cf7e74bae0",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000blue-edee43ad-08e7-429b-a656-c7cf7e74bae0a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "d0e8fa53-dc6b-4560-8464-b21378335000",
                    "sourceHandle": "red",
                    "target": "1fcba91a-40c0-4c8b-b482-884e4d982882",
                    "targetHandle": "a",
                    "id": "reactflow__edge-d0e8fa53-dc6b-4560-8464-b21378335000red-1fcba91a-40c0-4c8b-b482-884e4d982882a"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3c61eca7-54f1-40c3-9af2-2888f042d5d2black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "361e37db-e957-40fd-b072-3122dfc3e04c",
                    "sourceHandle": "blue",
                    "target": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "targetHandle": "black",
                    "id": "reactflow__edge-361e37db-e957-40fd-b072-3122dfc3e04cblue-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1",
                    "sourceHandle": "blue",
                    "target": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3e3dd2ce-0aa8-44f4-92ed-7466a1722ae1blue-12a55fe9-a550-446c-bb39-e7f9f8bb0001black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "3c61eca7-54f1-40c3-9af2-2888f042d5d2",
                    "sourceHandle": "blue",
                    "target": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "targetHandle": "black",
                    "id": "reactflow__edge-3c61eca7-54f1-40c3-9af2-2888f042d5d2blue-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13black"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "12a55fe9-a550-446c-bb39-e7f9f8bb0001",
                    "sourceHandle": "blue",
                    "target": "ddeb3db1-4333-4b54-b3d9-e3e4c27baaec",
                    "targetHandle": "black",
                    "id": "reactflow__edge-12a55fe9-a550-446c-bb39-e7f9f8bb0001blue-ddeb3db1-4333-4b54-b3d9-e3e4c27baaecblack"
                },
                {
                    "type": "deleteEdgeBTN",
                    "source": "60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13",
                    "sourceHandle": "blue",
                    "target": "cee1dff9-6c44-4b35-94a2-57d9d8f48a09",
                    "targetHandle": "black",
                    "id": "reactflow__edge-60960b74-5cf5-4dfd-9cbf-c4c9c4f64d13blue-cee1dff9-6c44-4b35-94a2-57d9d8f48a09black"
                }
            ]
        },
        "on_trade": {
            "nodes": [

            ],
            "edges": [

            ]
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
    "constants": [
        {
            "id": 5,
            "type": "double",
            "name": "my_var",
            "value": 20.0,
            "description": "this is my var"
        }
    ],
    "variables": [
        {
            "id": 0,
            "type": "string",
            "name": "mvariable",
            "value": "test value",
            "description": ""
        }
    ]
}
