#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        print("{}".format(message))
    except TypeError:
        raise raise_exception_msg
    
