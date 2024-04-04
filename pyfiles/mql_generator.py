from . import adapter
from . import expert_builder_class
from . import test_input_6
from . import test_input_7
from . import test_input_8
from . import path_root


def generate_mql(data_raw):
    data_refactored = adapter.refactor(data_raw)
    expert_builder = expert_builder_class.ExpertBuilder(data_refactored)
    expert = expert_builder.process_input()
    return expert


def test():
    data = test_input_8.input_data_17
    result = generate_mql(data)
    if isinstance(result, Exception):
        print("Error occurred")
    else:
        path = path_root.get()
        path_sub = "/output/"
        file_name = "expert_output" + ".mq4"
        with open(path + path_sub + file_name, "w") as result_file:
            result_file.write(result)
        # print(result)


test()
