#!/usr/bin/python3
""" Write stuff to json file, named add_item.json"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    """ Write stuff to json file, named add_item.json"""
    myFile = 'add_item.json'
    try:
        data = load_from_json_file(myFile)
    except Exception:
        data = []
    data += sys.argv[1:]
    save_to_json_file(data, myFile)
