#!/usr/bin/python3
def no_c(my_string):
    tmp_string = list(my_string)
    for c in range(0, len(tmp_string)):
        if ord(tmp_string[c]) == ord('c') or ord(tmp_string[c]) == ord('C'):
            tmp_string[c] = ''
    return ''.join(tmp_string)
