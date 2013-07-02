#!/bin/sh
URL="http://$1"
if [ $# = 3 ]; then
    QSTR="$2=$3"
else
    QSTR="q=$2"
fi
curl -s -L -A Mozilla/5.0 -G --data-urlencode "$QSTR" "$URL"
