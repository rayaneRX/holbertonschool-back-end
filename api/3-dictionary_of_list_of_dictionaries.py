#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv


api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    all_users = requests.get(f"{api_url}/users").json()
    todo_dict = {}
    for user in all_users:
        user_id = user["id"]
        user_name = user["username"]
        todo_list = requests.get(f"{api_url}/todos?userId={user_id}").json()
        new_todo_list = []
        for task in todo_list:
            task_dict = {"username": user_name, "task": task["title"],
                         "completed": task["completed"]}
            new_todo_list.append(task_dict)
        todo_dict[user_id] = new_todo_list
    with open("todo_all_employees.json", "w") as file:
        json.dump(todo_dict, file)