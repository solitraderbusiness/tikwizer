from . import path_root
from . import mql_generator
from . import test_input_6
from . import test_input_7
from . import test_input_8
from . import test_input_9
from . import test_input_10
from . import test_input_11


def test():
    data = test_input_11.input_data_4
    result = mql_generator.generate_mql(data)
    path = path_root.get()
    path_sub = "/output/"
    file_name = "expert_output" + ".mq4"
    with open(path + path_sub + file_name, "w") as result_file:
        result_file.write(result)
    # print(result)


test()
