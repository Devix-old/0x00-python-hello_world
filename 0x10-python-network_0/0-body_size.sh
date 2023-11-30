#!/bin/bash
# This script takes in a URL, sends a request, and displays the size of the response body
curl -s "$1" | wc -c
