#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    previous = 0
    my_list = []

    for i in roman_string:
        my_list.append(r[i])

    for element in reversed(my_list):
        if element >= previous:
            result += element
        else:
            result -= element
        previous = element

    return result
