#!/usr/bin/python3
def multiple_returns(sentence=None):
    if (sentence is None):
        return 0, None
    length = len(sentence)
    if (length == 0):
        return 0, None
    return len(sentence), sentence[0]
