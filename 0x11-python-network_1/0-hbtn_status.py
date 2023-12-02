#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    data = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- uft8 content".format(data.decode()))
