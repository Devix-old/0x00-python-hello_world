#!/usr/bin/python3
from urllib import request
url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    data = response.read()
    print("Body response:")
    print("	- type: {}".format(type(data)))
    print("	- content: {}".format(data))
    print("	- uft8 content".format(data.decode()))
