#!/bin/bash
# script that makes a request to 0.0.0.0:5000/cartch+me
curl -sl 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
