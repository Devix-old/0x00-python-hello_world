#!/usr/bin/python3
"""This Python script sends a URL request, displays the body of the
response (decoded in utf-8), and handles urllib HTTP errors by printing
the corresponding error code."""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
