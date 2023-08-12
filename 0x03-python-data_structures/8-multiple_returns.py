#!/usr/bin/python3
"""
    Function that returns a tuple with the length
    of a string and its first character.
    ...

    Parameters
    ----------
    sentence : str
        The string to check

    Return:
        tuple
    """
def multiple_returns(sentence):
    if sentence == None:
        return 0, None
    else:
        return len(sentence), sentence[0]
