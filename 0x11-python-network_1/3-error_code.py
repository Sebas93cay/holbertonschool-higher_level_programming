#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


from urllib import request, parse, error
import sys

if __name__ == "__main__":
    req = request.Request(url=sys.argv[1])
    try:
        with request.urlopen(req) as response:
            html = response.read()
            print(str(html)[2:-1])
    except error.URLError as e:
        print("Error code: {}".format(e.code))
