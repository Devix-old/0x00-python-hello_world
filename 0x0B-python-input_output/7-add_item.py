#!/usr/bin/python3
"""7-add_item"""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


data = []
filename = "add_item.json"

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    data = load_from_json_file(filename)
else:
    data = []
if len(sys.argv) > 1:
    data.extend(sys.argv[1:])

save_to_json_file(data, filename)
