#!/usr/bin/python3
# This script that fetches

import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    for header in response.getheaders():
        if header[0] == 'X-Request-Id':
            print(header[1])
            break
