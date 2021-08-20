#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import requests

r = requests.get("https://intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
