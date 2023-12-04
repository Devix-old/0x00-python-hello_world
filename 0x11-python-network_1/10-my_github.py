#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/devix-old"
    auth = (username, token)

    try:
        response = requests.get(url, auth=auth)
        user_info = response.json()

        if 'id' in user_info:
            print(user_info['id'])
        else:
            print("None")

    except ValueError:
        print("None")
