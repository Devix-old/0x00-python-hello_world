#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(response.text), response.text))
