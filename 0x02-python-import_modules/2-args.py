#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    if len == 0:
        print("0 argument.")
    elif len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len))
    for i in range(1, len+1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
