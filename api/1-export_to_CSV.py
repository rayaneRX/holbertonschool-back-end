#!/usr/bin/python3
"""Gather data from an API"""

import csv
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

    with open(f"{argv[1]}.csv", 'w', newline='') as file:
        csv_content = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            csv_content.writerows([[task['userId'], user_info['username'],
                                    task['completed'], task['title']]])

"""#!/usr/bin/python3
Script that, using this REST API, for a given employee
import requests
import csv
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    # User information
    user_response = requests.get(f"{API_URL}/users/{argv[1]}")
    user_data = user_response.json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={argv[1]}")
    todo_data = todo_response.json()
    # Display progress
    completed_tasks = [task for task in todo_data if task['completed']]
    employee_name = user_data["name"]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)
        print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")
    # Create and write to CSV file
    filename = f"{argv[1]}.csv"
    with open(filename, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME',
        'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow([[task['userId'], todo_data['username'],
                                    task['completed'], task['title']]])
"""
