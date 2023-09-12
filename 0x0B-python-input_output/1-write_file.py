#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):

    with open(filename, 'w', encoding="utf-8") as f:
        nb = f.write(text)

    return nb
