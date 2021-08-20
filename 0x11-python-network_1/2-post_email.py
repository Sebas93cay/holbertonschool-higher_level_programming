#!/usr/bin/python3
"""
This script fetches a give url and prints its header X-Request-Id
"""


from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = request.Request(url=sys.argv[1], data=data)
    with request.urlopen(req) as response:
        html = response.read()
        print(str(html)[2:-1])
