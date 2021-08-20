#!/usr/bin/python3
# This script fetches a give url and prints its header X-Request-Id

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(dict(response.getheaders()).get('X-Request-Id'))
