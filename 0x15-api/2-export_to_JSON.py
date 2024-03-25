#!/usr/bin/python3
""" 0. Gather data from an API """
import json
import requests
from sys import argv as args

url = "https://jsonplaceholder.typicode.com/"


def request_data(endpoint, method, params):
    """Requesting method"""
    return requests.request(method, url+endpoint, params=params)


if __name__ == "__main__":
    """ Work on import only """
    user = request_data(f"users/{args[1]}", "GET", None).json()
    todos = request_data("todos", "GET", {'userId': args[1]}).json()
    data = {f"{user['id']}": list(map(lambda x: {
        'task': x['title'],
        'completed': x['completed'],
        'username': user['username']
    }, todos))}
    with open(f"{user['id']}.json", "w") as f:
        json.dump(data, f)
