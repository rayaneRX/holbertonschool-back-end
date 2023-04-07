#!/usr/bin/python3
"""Script that, using this REST API, for a given employee"""
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

    # Create and write to CSV file
    filename = f"{argv[1]}.csv"
    with open(filename, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                'USER_ID': user_data['id'],
                'USERNAME': user_data['username'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })

    # Display progress
    completed_tasks = [task for task in todo_data if task['completed']]
    employee_name = user_data["name"]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")
