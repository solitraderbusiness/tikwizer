Traceback (most recent call last):
  File "D:\Python\Projects\mql_generator\pyfiles\mql_generator.py", line 12, in generate_mql
    expert = expert_builder.process_input()
  File "D:\Python\Projects\mql_generator\pyfiles\expert_builder_class.py", line 103, in process_input
    self.process_blocks_tick(self.data.get("events").get("on_tick"))
  File "D:\Python\Projects\mql_generator\pyfiles\expert_builder_class.py", line 134, in process_blocks_tick
    self.add_task_elements_specific(nodes)
  File "D:\Python\Projects\mql_generator\pyfiles\expert_builder_class.py", line 820, in add_task_elements_specific
    self.buy_sell(node)
  File "D:\Python\Projects\mql_generator\pyfiles\expert_builder_class.py", line 1336, in buy_sell
    row1 = value_fetch.get("row1")
AttributeError: 'NoneType' object has no attribute 'get'
