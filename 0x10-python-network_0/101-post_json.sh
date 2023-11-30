#!/bin/bash
# Send a POST request with the contents of the JSON file
curl -s -X POST -H "Content-Type: application/json" --data "@$2" "$1"
