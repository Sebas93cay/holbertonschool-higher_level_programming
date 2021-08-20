#!/usr/bin/python3
"""
This script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""

import requests
import sys


if __name__ == '__main__':
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data={"q": "" if len(sys.argv) == 1 else sys.argv[1]})
    if r.headers.get('content-type') == 'application/json':
        d = r.json()
        if d == {}:
            print("No result")
        else:
            print("[{}] {}".format(d['id'], d['name']))
    else:
        print("Not a valid JSON")
