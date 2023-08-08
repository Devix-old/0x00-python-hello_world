#!/usr/bin/python3
for i in range(1, 89):
    if i < 10:
        print('0', end="")
    if i / 10 < i % 10:
        print("{} ,".format(i), end="")
print("89")
