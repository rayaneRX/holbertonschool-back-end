#!/usr/bin/python3
"""API"""

import requests
from sys import argv


api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_info = requests.get(f"{api_url}/users/{argv[1]}")
    todo_list = requests.get(f"{api_url}/todos?userId={argv[1]}")

    user_data = user_info.json()
    todoDATA = todo_list.json()

    completed = [task for task in todoDATA if task["completed"]]
    EMPLOYEE_NAME = user_data["name"]
    NUMBER_OF_DONE_TASKS = len(completed)
    TOTAL_NUMBER_OF_TASKS = len(todoDATA)

    print("Employee {} is done with task ({}/{})".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed:
        print(f"\t {task['title']}")
