#!/bin/bash
# send a GET request with an extra header variable
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
