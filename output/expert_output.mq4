Traceback (most recent call last):
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\mql_generator.py", line 10, in generate_mql
    expert = expert_builder.process_input()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 79, in process_input
    self.process_blocks_tick(self.data.get("events").get("on_tick"))
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 107, in process_blocks_tick
    self.add_task_elements_specific(nodes)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 731, in add_task_elements_specific
    self.condition_1_normal_elements(node)
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 1054, in condition_1_normal_elements
    row1_left = params.get("left").get("row1")
                ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'get'
