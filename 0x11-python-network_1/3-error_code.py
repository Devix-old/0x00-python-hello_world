#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":
    
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    with urllib.request.urlopen(url, data=encoded_data) as response:
        print(response.read().decode("utf-8"))
    
