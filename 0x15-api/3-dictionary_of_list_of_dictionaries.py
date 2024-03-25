#!/usr/bin/python3
""" 0. Gather data from an API """
import json
import requests

url = "https://jsonplaceholder.typicode.com/"


def request_data(endpoint, method, params):
    """Requesting method"""
    return requests.request(method, url+endpoint, params=params)


if __name__ == "__main__":
    """ Work on import only """
    users = request_data(f"users", "GET", None).json()
    data = dict()
    for user in users:
        todos = request_data("todos", "GET", {'userId': user['id']}).json()
        data[f"{user['id']}"] = list(map(lambda x: {
            'username': user['username'],
            'task': x['title'],
            'completed': x['completed'],
        }, todos))
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
