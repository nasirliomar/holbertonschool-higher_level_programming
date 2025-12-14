#!/usr/bin/python3
"""Displays the X-Request-Id header from a URL response"""

import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
