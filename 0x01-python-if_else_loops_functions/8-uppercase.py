#!/usr/bin/python3
def uppercase(str):
    l = list(str)
    for i in range(len(l)):
        if ord(l[i]) >= ord('a') and ord(l[i]) <= ord('z'):
            l[i] = chr(ord(l[i]) - 32)
    str = "".join(l)
    print("{}".format(str))
