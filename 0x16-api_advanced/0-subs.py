#!/usr/bin/python3
"""
Reddit API subscribers
"""
import requests


def number_of_subscribers(subreddit):
    subreddit_info = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json").json()
    subreddit_data = subreddit_info.get('data')
    return (subreddit_data.get('subscribers')
            if subreddit_data and subreddit_data.get('subscribers') else 0)


# if __name__ == "__main__":
#     number_of_subscribers("learnpython")
