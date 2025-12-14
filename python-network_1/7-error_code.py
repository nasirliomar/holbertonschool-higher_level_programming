#!/usr/bin/python3
"""Displays response body or error code using requests"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
