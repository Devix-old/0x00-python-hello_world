#!/usr/bin/python3
"""define my_list module"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        print(sorted(self))
