def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        return l, None
    return l, list(sentence)[0]
