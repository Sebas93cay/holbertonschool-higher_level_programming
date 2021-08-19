#!/bin/bash
# sends a POST request to the passed URL, and displays
curl -so /dev/null -w "%{http_code}" "$1"
