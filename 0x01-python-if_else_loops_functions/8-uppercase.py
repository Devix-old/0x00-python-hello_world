#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if ord(word) >= ord('a') and ord(word) <= ord('z'):
            upper = chr(ord(word) - 32)
        else:
            upper = word
        print("{:s}".format(upper), end="")
    print('')
