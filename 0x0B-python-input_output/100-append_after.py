#!/usr/bin/python3
"""Module 100 : append after"""


def append_after(filename="", search_string="", new_string=""):
    """This function append to a text a new_string after a search_string"""
    with open(filename, 'r+') as f:
        data = f.readlines()

    for i in range(len(data)):
        if search_string in data[i]:
            data.insert(i + 1, new_string)

    data = "".join(data)
    with open(filename, 'w') as f:
        f.write("")
        f.write(data)
