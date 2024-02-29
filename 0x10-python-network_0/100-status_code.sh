#!/bin/bash
# script that sends a request to a URL
curl -s -L -X HEAD -w "%[http_code}" "$1"
