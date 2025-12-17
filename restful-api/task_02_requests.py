#!/usr/bin/python3
"""
task_02_requests.py

Fetch posts from JSONPlaceholder using requests.
- fetch_and_print_posts(): prints status code and all post titles
- fetch_and_save_posts(): writes id,title,body to posts.csv
"""

import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print status code + titles."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        # Response wasn't valid JSON
        return

    for post in posts:
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts():
    """Fetch all posts and save id,title,body to posts.csv."""
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        return

    # Structure data: list of dicts with keys id, title, body
    data = [
        {
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        }
        for post in posts
    ]

    fieldnames = ["id", "title", "body"]

    with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
