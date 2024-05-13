Traceback (most recent call last):
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\mql_generator.py", line 10, in generate_mql
    expert = expert_builder.process_input()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 91, in process_input
    self.process_blocks_tick(self.data.get("events").get("on_tick"))
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 119, in process_blocks_tick
    self.add_task_elements_specific(nodes)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 771, in add_task_elements_specific
    self.buy_sell(node)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 960, in buy_sell
    row1 = value_fetch.get("row1")
           ^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'get'
