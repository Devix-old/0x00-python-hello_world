#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as html:
    if "X-Request-Id" in html.headers:
    	print(html.headers["X-Request-Id"])
