import os


def get():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DIR.rstrip("\py")
