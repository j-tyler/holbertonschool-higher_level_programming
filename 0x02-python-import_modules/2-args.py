#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 0:
        print("0 argument.")
    elif len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len))
    for s in sys.argv:
        print("{:d}: {:s}".format(sys.argv.index(s), s))
