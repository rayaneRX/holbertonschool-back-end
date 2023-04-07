#!/usr/bin/python3
"""API"""

import requests
from sys import argv


api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_info = requests.get(f"{api_url}/users/{argv[1]}").json()
    todo_list = requests.get(f"{api_url}/todos/{argv[1]}").json()

    completed = [task for task in todo_list if task["completed"]]
    EMPLOYEE_NAME = todo_list["name"]
    NUMBER_OF_DONE_TASKS = len(completed)
    TOTAL_NUMBER_OF_TASKS = len(todo_list)

    print("Employee {} is done with task ({}/{})".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed:
        print(f"\t {task['title']}")
    