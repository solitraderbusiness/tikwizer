from . import adapter
from . import expert_builder
from . import test_input_2
from . import test_input_3
from . import test_input_4
from . import test_input_5
from . import test_input
from . import path_root


def generate_mql(data_raw):
    data_refactored = adapter.refactor(data_raw)
    expert = expert_builder.process_input(data_refactored)
    return expert


def test():
    data = test_input_5.input_data_5
    result = generate_mql(data)
    if isinstance(result, Exception):
        print("Error occured")
    else:
        path = path_root.get()
        path_sub = "/output/"
        file_name = "expert_output" + ".mq4"
        with open(path + path_sub + file_name, "w") as result_file:
            result_file.write(result)
        print(result)


test()
