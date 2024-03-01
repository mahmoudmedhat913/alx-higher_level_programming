#!/usr/bin/python3
"""python script that takes github credentials"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    token = HTTPBasicAuth(username, password)
    request = requests.get('https://api.github.com/user', auth=token)
    print(request.json().get('id'))
