#!/bin/bash
# This script takes in a URL, sends a POST request with parameters, and displays the body of the response
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
