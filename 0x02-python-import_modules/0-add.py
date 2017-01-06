#!/usr/bin/python3
def main():
    from add_0 import add
    a, b = 1, 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
if __name__ == "__main__":
    main()
