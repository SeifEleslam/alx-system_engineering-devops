#!/usr/bin/python3
"""
Reddit API hot posts
"""

from requests import get


def count_words(subreddit, word_list, after='', word_dict=None):
    """Get Titles of top 10 hot posts"""
    if not word_list:
        return
    subreddit_info = get(
        "https://www.reddit.com/r/{:s}/hot.json?limit=100&after={}"
        .format(subreddit, after),
        headers={"User-Agent": "Custom-User-Agent"},
        allow_redirects=False)

    if subreddit_info.status_code >= 300:
        return (None)
    if not word_dict:
        word_dict = {}
        for word in word_list.split(' '):
            word_dict[word] = 0
    posts = subreddit_info.json().get('data').get('children')
    li = [post.get('data').get('title')
          for post in posts]
    for post in posts:
        for word in post.get('data').get('title').split():
            if word_dict.get(word) is not None:
                word_dict[word] += 1
    if len(li) == 0:
        word_dict = dict(
            sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
        for word, count in word_dict.items():
            if count > 0:
                print("{}: {}".format(word, count))
        return
    return count_words(subreddit, word_list,
                       "{}".format(posts[-1].get('data').get('name')),
                       word_dict)
