#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):

    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
