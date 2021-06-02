#!/usr/bin/python3

import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file_name = 'add_item.json'

list = list()

try:
    list = load_from_json_file(file_name)
    for item in sys.argv[1:]:
        list.append(item)
except Exception as e:
    pass

save_to_json_file(list, file_name)
