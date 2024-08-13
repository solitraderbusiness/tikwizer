Traceback (most recent call last):
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\mql_generator.py", line 10, in generate_mql
    data_refactored = adapter.refactor(data_raw)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\adapter.py", line 21, in refactor
    set_blocks_input_dic(key, event["nodes"], event["edges"])
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\adapter.py", line 262, in set_blocks_input_dic
    input_dic["nexts_true"] = get_nexts_true(node, edges)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\adapter.py", line 315, in get_nexts_true
    return sorted(result)
TypeError: '<' not supported between instances of 'int' and 'str'
