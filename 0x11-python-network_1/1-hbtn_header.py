#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as html:
    print(html.headers["X-Request-Id"])
