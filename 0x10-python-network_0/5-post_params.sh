#!/bin/bash
# sends a POST request to the passed URL, and displays
# the body of the response with extra headers setted
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
