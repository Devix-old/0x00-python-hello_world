#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest) of a repository.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get(
                'commit', {}).get('author', {}).get('name')
            print(f"{sha}: {author_name}")

    except ValueError:
        print("Error: Not a valid JSON")

    except requests.RequestException as e:
        print(f"Error: {e}")
