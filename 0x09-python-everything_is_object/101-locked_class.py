#!/usr/bin/python3
"""Define locked_class module"""
class LockedClass:
    """Representation of the class LockedClass"""
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
