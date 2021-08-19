#!/bin/bash
#send a delete request to the specified network
curl -sI "$1" | grep Allow: | cut -d" " -f 2-
