#!/bin/bash
#catch a message
curl -sLX PUT -d "user_id=98" -H"Origin: HolbertonSchool" "$1"
