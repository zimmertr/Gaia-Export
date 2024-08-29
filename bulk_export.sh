#!/bin/bash

SESSION_ID=$1

if [ -z "$SESSION_ID" ]; then
    echo "Usage: export_tracks.sh <SESSION_ID>"
    exit 1
fi

gaiagps --sessionid "$SESSION_ID" track list --by-id | \
awk '{print $1, substr($0, index($0,$5))}' | \
while read -r id name; do
    clean_name=$(echo "$name" | sed "s/'//g")

    gaiagps --sessionid "$SESSION_ID" track export "$id" "/tmp/$clean_name.gpx"
done
