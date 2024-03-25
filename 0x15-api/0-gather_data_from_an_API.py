#!/usr/bin/python3
""" 0. Gather data from an API """

from sys import argv as args
import requests

url = "https://jsonplaceholder.typicode.com/"


def request_data(endpoint, method, params):
    """Requesting method"""
    return requests.request(method, url+endpoint, params=params)


if __name__ == "__main__":
    """ Work on import only """
    user = request_data(f"users/{args[1]}", "GET", None).json()
    todos = request_data("todos", "GET", {'userId': args[1]}).json()
    todos_done = list(filter(lambda todo: todo["completed"], todos))
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"],
        len(todos_done),
        len(todos)
    ))
    for todo in todos_done:
        print(f"\t {todo['title']}")
