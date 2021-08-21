#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the given repository
"""

import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    user = sys.argv[2]
    r = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(user, repo))
    commits = r.json()[:10]
    for commit in commits:
        print("{}: {}".format(commit.get('sha'), commit.get(
            'commit').get('author').get('name')))
