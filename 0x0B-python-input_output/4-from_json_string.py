#!/usr/bin/python3
""" decode JSON. """
import json


def from_json_string(my_str):
    """ json decoder. """
    return json.loads(my_str)
