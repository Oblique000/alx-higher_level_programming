#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence) if sentence else 0
    return sen_len, sentence[:1] if sentence else None
