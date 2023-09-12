#!/usr/bin/python3
"""6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """Load from json file function"""
    with open(filename, 'r') as f:
        return json.load(f)
