#!/usr/bin/python3
"""API"""


import requests
import sys

employee_id = sys.argv[1]

employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
employee_data = employee_response.json()

todo_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
todo_data = todo_response.json()

completed_tasks = [task for task in todo_data if task['completed']]
num_completed_tasks = len(completed_tasks)
total_tasks = len(todo_data)

print(f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t {task['title']}")
