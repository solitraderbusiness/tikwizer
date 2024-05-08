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

# test condition adjust and shift
input_data_6 = {
    "events": {
        "on_tick": {
            "nodes": [
                {
                    "params": {
                        "max_times_to_pass": "1",
                        "symbol": "",
                        "timeframe": "PERIOD_CURRENT"
                    },
                    "id": "55b2ddd9-459d-4e1f-b624-3ec85bed0074",
                    "id_by_user": 2,
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
                                "fast_ema_period": "12",
                                "slow_ema_period": "9",
                                "signal_period": "9",
                                "mode": "MODE_SIGNAL",
                                "applied_price": "PRICE_CLOSE",
                                "adjust": ""
                            }
                        },
                        "right": {
                            "row1": "Indicator",
                            "row2": "macd",
                            "params": {
                                "fast_ema_period": "12",
                                "slow_ema_period": "9",
                                "signal_period": "9",
                                "mode": "MODE_SIGNAL",
                                "applied_price": "PRICE_CLOSE"
                            }
                        }
                    },
                    "id": "c138b498-77d6-4e06-933b-151d9c4ce471",
                    "id_by_user": 3,
                    "blockName": "Condition"
                }
            ],
            "edges": [
                {
                    "source": "55b2ddd9-459d-4e1f-b624-3ec85bed0074",
                    "sourceHandle": "blue",
                    "target": "c138b498-77d6-4e06-933b-151d9c4ce471",
                    "targetHandle": "c",
                    "type": "customEdge",
                    "id": "reactflow__edge-55b2ddd9-459d-4e1f-b624-3ec85bed0074blue-c138b498-77d6-4e06-933b-151d9c4ce471c"
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

# test masoud blocks
input_data_7 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "sleep_seconds": "5",
            "sleep_tester_normal": "false",
            "sleep_tester_visual": "true"
          },
          "id": "a5cc17d6-f03a-40e3-a73e-d3fa21fd4cff",
          "id_by_user": 4,
          "blockName": "Delay"
        },
        {
          "params": {
            "part_vol_mode": "CLOSE_PARTIALLY_PERCENT_OF_CURRENT_VOLUME",
            "slippage": "4",
            "part_vol_value": "20"
          },
          "id": "e929c5f1-ce70-4395-a2e6-b5861de7468e",
          "id_by_user": 5,
          "blockName": "close (partially)"
        },
        {
          "params": {
            "slippage": "4",
            "arrow_color": "clrOlive"
          },
          "id": "3b3a0150-2f99-49d6-9d8c-45b3b60010e2",
          "id_by_user": 6,
          "blockName": "close"
        },
        {
          "params": {
            "message": "Program Terminated Itself"
          },
          "id": "7e0bc962-1cb1-4aae-abe7-0962c19d68eb",
          "id_by_user": 7,
          "blockName": "Terminate"
        },
        {
          "params": {
            "symbol": "",
            "operator": "<",
            "spread_mode": "SPREAD_BENCHMARK_AVERAGE",
            "average_spread_time_period": "10",
            "average_spread_adjust": "0"
          },
          "id": "a38d9387-1e83-4805-9e81-b48cd3a4a1ea",
          "id_by_user": 10,
          "blockName": "Spread Filter"
        }
      ],
      "edges": [
        {
          "source": "a5cc17d6-f03a-40e3-a73e-d3fa21fd4cff",
          "sourceHandle": "blue",
          "target": "e929c5f1-ce70-4395-a2e6-b5861de7468e",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-a5cc17d6-f03a-40e3-a73e-d3fa21fd4cffblue-e929c5f1-ce70-4395-a2e6-b5861de7468ec"
        },
        {
          "source": "a5cc17d6-f03a-40e3-a73e-d3fa21fd4cff",
          "sourceHandle": "blue",
          "target": "3b3a0150-2f99-49d6-9d8c-45b3b60010e2",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-a5cc17d6-f03a-40e3-a73e-d3fa21fd4cffblue-3b3a0150-2f99-49d6-9d8c-45b3b60010e2c"
        },
        {
          "source": "e929c5f1-ce70-4395-a2e6-b5861de7468e",
          "sourceHandle": "blue",
          "target": "7e0bc962-1cb1-4aae-abe7-0962c19d68eb",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-e929c5f1-ce70-4395-a2e6-b5861de7468eblue-7e0bc962-1cb1-4aae-abe7-0962c19d68ebc"
        },
        {
          "source": "3b3a0150-2f99-49d6-9d8c-45b3b60010e2",
          "sourceHandle": "blue",
          "target": "a38d9387-1e83-4805-9e81-b48cd3a4a1ea",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-3b3a0150-2f99-49d6-9d8c-45b3b60010e2blue-a38d9387-1e83-4805-9e81-b48cd3a4a1eac"
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

# test masoud blocks
input_data_8 = {
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
              "row1": "value",
              "row2": "numeric",
              "params": {
                "numeric": "10"
              }
            },
            "right": {
              "row1": "value",
              "row2": "boolean",
              "params": {
                "numeric": "1",
                "boolean-true": "boolean-true"
              }
            }
          },
          "id": "77138f4c-64ed-4847-97b9-92b1db09bf1f",
          "id_by_user": 13,
          "blockName": "Condition"
        },
        {
          "params": {
            "sleep_seconds": "5",
            "sleep_tester_normal": "false",
            "sleep_tester_visual": "true"
          },
          "id": "77190ca7-249c-4c5f-b094-e47bc7c95de2",
          "id_by_user": 14,
          "blockName": "Delay"
        }
      ],
      "edges": [
        {
          "source": "77190ca7-249c-4c5f-b094-e47bc7c95de2",
          "sourceHandle": "blue",
          "target": "77138f4c-64ed-4847-97b9-92b1db09bf1f",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-77190ca7-249c-4c5f-b094-e47bc7c95de2blue-77138f4c-64ed-4847-97b9-92b1db09bf1fc"
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

# test masoud blocks
input_data_9 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "once per bar": "",
            "timeframe": "PERIOD_M1",
            "max_times_to_pass": "1"
          },
          "id": "b7c417ac-6589-461c-a5e6-fb9fa4924166",
          "id_by_user": 4,
          "blockName": "Once per bar",
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
              "row2": "numeric",
              "params": {
                "numeric": "1"
              }
            },
            "right": {
              "row1": "value",
              "row2": "numeric",
              "params": {
                "numeric": "1"
              }
            }
          },
          "id": "fc5449f5-2d83-4090-9a53-a7b694167f83",
          "id_by_user": 5,
          "blockName": "Condition",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "XAU",
            "group": 13,
            "how_much_volume": "35",
            "volume_upper_limit": "0",
            "risk-percent": "1",
            "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
            "money-managment-initial-volume": "0.1",
            "martingale_init_vol": "0.1",
            "martingale_multiply_on_loss": "2",
            "martingale_multiply_on_profit": "1",
            "martingale_addlots_on_loss": "0",
            "martingale_addlots_on_profit": "0",
            "martingale_reset_on_n_losses": "0",
            "martingale_reset_on_n_profits": "1",
            "stoploss": "0.55",
            "stoploss_mode-of-take-prfit": "100",
            "takeprofit": "20",
            "takeprofit-mode-stop-loss": "100",
            "expiration-mode-no": "expiration",
            "expiration-days": "",
            "expiration-hour": "1",
            "expiration-min": "",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrDarkBlue"
          },
          "id": "f3ef83c9-7263-4f74-bfd8-913c9977ad29",
          "id_by_user": 6,
          "blockName": "Buy now",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "b7c417ac-6589-461c-a5e6-fb9fa4924166",
          "sourceHandle": "blue",
          "target": "fc5449f5-2d83-4090-9a53-a7b694167f83",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-b7c417ac-6589-461c-a5e6-fb9fa4924166blue-fc5449f5-2d83-4090-9a53-a7b694167f83c"
        },
        {
          "source": "fc5449f5-2d83-4090-9a53-a7b694167f83",
          "sourceHandle": "blue",
          "target": "f3ef83c9-7263-4f74-bfd8-913c9977ad29",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-fc5449f5-2d83-4090-9a53-a7b694167f83blue-f3ef83c9-7263-4f74-bfd8-913c9977ad29c"
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

# test masoud blocks
input_data_10 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "once per bar": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "96d8e785-bb42-4c51-9322-245852e2f500",
          "id_by_user": 7,
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
              "row2": "numeric",
              "params": {
                "value": "1"
              }
            },
            "right": {
              "row1": "value",
              "row2": "numeric",
              "params": {
                "value": "1"
              }
            }
          },
          "id": "22ce75dc-0bf3-48f2-a27a-876c03601840",
          "id_by_user": 8,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "XAU",
            "group": 13,
            "how_much_volume": "35",
            "volume_upper_limit": "0",
            "risk-percent": "1",
            "look_up_on": "LOOK_UP_RUNNING_THEN_HISTORY",
            "money-managment-initial-volume": "0.1",
            "martingale_init_vol": "0.1",
            "martingale_multiply_on_loss": "2",
            "martingale_multiply_on_profit": "1",
            "martingale_addlots_on_loss": "0",
            "martingale_addlots_on_profit": "0",
            "martingale_reset_on_n_losses": "0",
            "martingale_reset_on_n_profits": "1",
            "stoploss": "0.55",
            "stoploss_mode-of-take-prfit": "100",
            "takeprofit": "20",
            "takeprofit-mode-stop-loss": "100",
            "expiration-mode-no": "expiration",
            "expiration-days": "",
            "expiration-hour": "1",
            "expiration-min": "",
            "slippage": "4",
            "comment": "",
            "arrow_color": "clrDarkBlue"
          },
          "id": "5ec78619-a05d-4d58-b131-693645331957",
          "id_by_user": 9,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "96d8e785-bb42-4c51-9322-245852e2f500",
          "sourceHandle": "blue",
          "target": "22ce75dc-0bf3-48f2-a27a-876c03601840",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-96d8e785-bb42-4c51-9322-245852e2f500blue-22ce75dc-0bf3-48f2-a27a-876c03601840c"
        },
        {
          "source": "22ce75dc-0bf3-48f2-a27a-876c03601840",
          "sourceHandle": "blue",
          "target": "5ec78619-a05d-4d58-b131-693645331957",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-22ce75dc-0bf3-48f2-a27a-876c03601840blue-5ec78619-a05d-4d58-b131-693645331957c"
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

# test masoud blocks
input_data_11 = {
  "events": {
    "on_tick": {
      "nodes": [
        {
          "params": {
            "once per bar": "",
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1"
          },
          "id": "66dbd119-1a10-4275-91af-65ac4bd2f99e",
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
              "row1": "value",
              "row2": "numeric",
              "params": {
                "value": "1"
              }
            },
            "right": {
              "row1": "value",
              "row2": "numeric",
              "params": {
                "value": "1"
              }
            }
          },
          "id": "bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8e",
          "id_by_user": 2,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "XAU",
            "group": 13,
            "how_much_volume": "35",
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
            "arrow_color": "clrDarkBlue"
          },
          "id": "fb195ce3-f0e3-4394-8d0c-d169c2a887b5",
          "id_by_user": 3,
          "blockName": "Buy now",
          "category": "buy_sell",
          "block_name_mql": "buy_now"
        }
      ],
      "edges": [
        {
          "source": "66dbd119-1a10-4275-91af-65ac4bd2f99e",
          "sourceHandle": "blue",
          "target": "bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8e",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-66dbd119-1a10-4275-91af-65ac4bd2f99eblue-bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8ec"
        },
        {
          "source": "bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8e",
          "sourceHandle": "blue",
          "target": "fb195ce3-f0e3-4394-8d0c-d169c2a887b5",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8eblue-fb195ce3-f0e3-4394-8d0c-d169c2a887b5c"
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

# test masoud blocks
input_data_12 = {
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
              "row1": "value",
              "row2": "numeric",
              "params": {
                "value": "1"
              }
            },
            "right": {
              "row1": "value",
              "row2": "numeric",
              "params": {
                "value": "1"
              }
            }
          },
          "id": "bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8e",
          "id_by_user": 2,
          "blockName": "Condition",
          "category": "condition_formula",
          "block_name_mql": "condition"
        },
        {
          "params": {
            "timeframe": "PERIOD_CURRENT",
            "max_times_to_pass": "1",
            "symbol": ""
          },
          "id": "8d53a0e7-6e69-4d83-b830-2da440a3e7fd",
          "id_by_user": 4,
          "blockName": "Once per bar",
          "category": "time_filters",
          "block_name_mql": "once_per_bar"
        },
        {
          "params": {
            "open_at_price": "OPEN_AT_ASK",
            "money_management": "MONEY_MANAGEMENT_FIXED_VOLUME",
            "stop_loss_mode": "TPSL_MODE_FIXED_PIPS",
            "take_profit_mode": "TPSL_MODE_FIXED_PIPS",
            "symbol": "",
            "group": "11",
            "price_offset": "20",
            "how_much_volume": "35",
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
          "id": "07fa121f-69fb-4c34-8ad1-1b26c2b96a44",
          "id_by_user": 5,
          "blockName": "Sell pending order",
          "category": "buy_sell",
          "block_name_mql": "sell_pending_order"
        }
      ],
      "edges": [
        {
          "source": "8d53a0e7-6e69-4d83-b830-2da440a3e7fd",
          "sourceHandle": "blue",
          "target": "bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8e",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-8d53a0e7-6e69-4d83-b830-2da440a3e7fdblue-bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8ec"
        },
        {
          "source": "bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8e",
          "sourceHandle": "blue",
          "target": "07fa121f-69fb-4c34-8ad1-1b26c2b96a44",
          "targetHandle": "c",
          "type": "customEdge",
          "id": "reactflow__edge-bd6c1ecb-96bf-49fb-9cbc-10a2827f6d8eblue-07fa121f-69fb-4c34-8ad1-1b26c2b96a44c"
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
