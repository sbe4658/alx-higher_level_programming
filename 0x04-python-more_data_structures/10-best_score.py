#!/usr/bin/python3
def best_score(a_dict):
    tmp = 0
    if a_dict is None or a_dict == {}:
        return None
    for key in a_dict:
        if a_dict.get(key) > tmp:
            tmp = a_dict.get(key)
            best_score = key
    return best_score
