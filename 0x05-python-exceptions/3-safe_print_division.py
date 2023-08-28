#!/usr/bin/python3
def safe_print_division(a, b):
    quotion = 0
    try:
        quotion = a / b
    except ZeroDivisionError:
        quotion = None
    finally:
        print("Inside result: {}".format(quotion))
        return (quotion)
