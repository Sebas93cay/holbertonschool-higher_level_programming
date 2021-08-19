#!/bin/bash
#displays size of HTTP response
if [[ $(curl -sIL "$1" | grep -c "200 OK") -eq 1 ]]
then
	curl -sL "$1"
fi
