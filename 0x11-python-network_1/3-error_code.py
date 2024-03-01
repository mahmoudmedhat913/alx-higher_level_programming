#!/usr/bin/python3
"""script that takes in a URL"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UtF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
