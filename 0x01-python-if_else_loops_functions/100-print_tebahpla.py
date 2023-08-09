#!/usr/bin/python3
alpha = 122
i = 0
start = 1
while(i <= 25):
    if start % 2 == 0:
        print("{}".format(chr(alpha - 32)),end="")
    else:
        print("{}".format(chr(alpha)),end="")
    alpha = alpha - 1
    i = i + 1
    start += 1
