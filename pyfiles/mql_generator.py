from . import adapter
from . import expert_builder_class
import traceback


def generate_mql(data_raw):
    try:
        data_refactored = adapter.refactor(data_raw)
        expert_builder = expert_builder_class.ExpertBuilder(data_refactored)
        expert = expert_builder.process_input()
        return expert
    except Exception:
        exception_traceback = traceback.format_exc()
        print("Traceback: ", exception_traceback)
        return exception_traceback
