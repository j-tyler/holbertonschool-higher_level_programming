#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        l = l, None
    else:
        l = l, list(sentence)[0]
    return l
