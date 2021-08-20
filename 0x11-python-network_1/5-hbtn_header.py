#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
