#!/usr/bin/python3
"""Uses GitHub API to display the authenticated user's id"""

import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(user, token)
    )

    print(response.json().get("id"))
