#!/bin/bash
# This script display the status code of an HTML Response
curl -o /dev/null -s -w "%{http_code}\n" "$1"
