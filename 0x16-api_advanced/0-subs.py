#!/usr/bin/python3
"""
Reddit API subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Get Number of subscribers"""
    subreddit_info = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        allow_redirects=False)
    return 0 if subreddit_info.status_code >= 300 else \
        subreddit_info.json().get('data').get('subscribers')
