#!/usr/bin/python3
""" 0. Gather data from an API """
from csv import writer
import requests
from sys import argv as args

url = "https://jsonplaceholder.typicode.com/"


def request_data(endpoint, method, params):
    """Requesting method"""
    return requests.request(method, url+endpoint, params=params)


if __name__ == "__main__":
    """ Work on import only """
    data = list()
    user = request_data(f"users/{args[1]}", "GET", None).json()
    todos = request_data("todos", "GET", {'userId': args[1]}).json()
    for todo in todos:
        data.append([f'"{todo["userId"]}"',
                     f'"{user["username"]}"',
                     f'"{todo["completed"]}"',
                     f'"{todo["title"]}"'])
    with open(f"{user['id']}.csv", "w", newline="") as f:
        writer = writer(f)
        writer.writerows(data)
