#!/usr/bin/python3
""" Read the file name.
    No, YOU READ IT!
"""
import json


def load_from_json_file(filename):
    """ Read the func. name. """
    with open(filename, 'r') as f:
        return json.load(f)
