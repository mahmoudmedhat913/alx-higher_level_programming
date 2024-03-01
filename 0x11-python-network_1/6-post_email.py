#!/usr/bin/python3
"""script that takes in a URL and email address"""
import requests
from sys import argv

if __name__ == "__main__":
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
