Traceback (most recent call last):
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\mql_generator.py", line 12, in generate_mql
    expert = expert_builder.process_input()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 102, in process_input
    self.add_consts_system()
  File "C:\Users\asus\PycharmProjects\mql-generator\pyfiles\expert_builder_class.py", line 424, in add_consts_system
    rule = self.data.get("project_options").get("pip_size").get("rules")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'get'
