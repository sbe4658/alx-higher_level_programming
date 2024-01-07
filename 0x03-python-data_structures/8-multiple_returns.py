#!/usr/bin/python3

def multiple_returns(sentence):
    infos = len(sentence), sentence[0] if sentence != "" else None
    return infos
