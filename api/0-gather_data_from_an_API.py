#!/usr/bin/python3

import requests
import sys

employee_id = sys.argv[1]  # Get the employee ID from command line argument

# Make API request to get the employee info
employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
employee_data = employee_response.json()

# Make API request to get the employee's TODO list
todo_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
todo_data = todo_response.json()

# Calculate the number of completed tasks and total number of tasks
completed_tasks = [task for task in todo_data if task['completed']]
num_completed_tasks = len(completed_tasks)
total_tasks = len(todo_data)

# Print the output in the required format
print(f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t {task['title']}")

