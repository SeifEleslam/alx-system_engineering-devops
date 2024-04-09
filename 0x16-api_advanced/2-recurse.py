#!/usr/bin/python3
"""
Reddit API hot posts
"""

from requests import get


def recurse(subreddit, hot_list=[], after=''):
    """Get Titles of top 10 hot posts"""

    subreddit_info = get(
        "https://www.reddit.com/r/{:s}/hot.json?limit=100&after={}"
        .format(subreddit, after),
        headers={"User-Agent": "Custom-User-Agent"},
        allow_redirects=False)

    if subreddit_info.status_code >= 300:
        return (None)
    else:
        posts = subreddit_info.json().get('data').get('children')
        li = [post.get('data').get('title')
              for post in posts]
        if len(li) == 0:
            return (hot_list)
        hot_list.extend(li)
        return recurse(subreddit, hot_list,
                       "{}".format(posts[-1].get('data').get('name')))
