#!/bin/bash
# script that takes in a URL
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
