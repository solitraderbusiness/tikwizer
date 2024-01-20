import adapter
import expert_builder
import test_input_2
import test_input_3
import test_input
import path_root


def generate_mql(data_raw):
    data_refactored = adapter.refactor(data_raw)
    expert = expert_builder.process_input(data_refactored)
    return expert





def test():
    data = test_input_3.input_data_25
    final_expert = generate_mql(data)
    path = path_root.get()
    path_sub = "/output/"
    file_name = "expert_mvp" + ".mq4"
    with open(path + path_sub + file_name, "w") as result_file:
        result_file.write(final_expert)
    print(final_expert)

test()

