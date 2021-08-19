#!/bin/bash
#displays size of HTTP response
curl -sI "$1" | grep Content-Length | cut -d" " -f 2
