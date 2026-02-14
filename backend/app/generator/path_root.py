import os

_base_path = None


def set_base_path(path):
    global _base_path
    _base_path = path


def get():
    if _base_path:
        return _base_path
    # Default: go up from app/generator/ to backend/
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
