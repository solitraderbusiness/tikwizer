Traceback (most recent call last):
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\mql_generator.py", line 12, in generate_mql
    expert = expert_builder.process_input()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 105, in process_input
    self.process_blocks_tick(self.data.get("events").get("on_tick"))
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 136, in process_blocks_tick
    self.add_task_elements_specific(nodes)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 827, in add_task_elements_specific
    self.draw_arrow(node)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 1250, in draw_arrow
    row1_time_1 = value_fetch_time_1.get("row1")
                  ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'get'
