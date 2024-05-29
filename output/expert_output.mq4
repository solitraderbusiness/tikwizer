Traceback (most recent call last):
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\mql_generator.py", line 8, in generate_mql
    data_refactored = adapter.refactor(data_raw)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\adapter.py", line 20, in refactor
    params_fill(event.get("nodes"))
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\adapter.py", line 136, in params_fill
    with open(path_task_id + "input.json") as input_file:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\asus\\PycharmProjects\\mql-generator/contents/tasks/loop_for_trades_orders/loop_break/input.json'
