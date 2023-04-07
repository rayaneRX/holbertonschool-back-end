#!/usr/bin/python3
"""API"""

import json
import requests
from sys import argv


api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_info = requests.get(f"{api_url}/users/{argv[1]}").json()
    todo_list = requests.get(f"{api_url}/todos?userId={argv[1]}").json()

    done_tasks = []
    for task in todo_list:
        if task['completed'] is True:
            done_tasks.append(task)
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todo_list)
    employee_name = user_info["name"]

    print(f"Employee {employee_name} is done with tasks\
({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

    user_tasks = []
    for task in todo_list:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = user_info["username"]
        user_tasks.append(task_dict)

    user_dict = {}
    user_dict[argv[1]] = user_tasks

    with open(f"{argv[1]}.json", 'w') as file:
        json.dump(user_dict, file)
