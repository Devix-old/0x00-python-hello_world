#!/usr/bin/python3
import urllib.request, sys

with urllib.request.urlopen(sys.argv[1]) as html:
    print(html.headers["X-Request-Id"])
