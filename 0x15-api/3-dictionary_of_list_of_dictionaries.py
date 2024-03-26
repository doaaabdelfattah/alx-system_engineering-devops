#!/usr/bin/python3
'''
return todo list info from given id from API
'''
import json
import requests
import sys

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    response_user = requests.get(user_url)
    users_data = response_user.json()

    user_todo = 'https://jsonplaceholder.typicode.com/todos'

    json_dict = {}

    for user in users_data:
        id = user['id']
        response_todo = requests.get(f'{user_todo}?userId={id}')
        user_tasks = response_todo.json()
        todo_list = []
        for task in user_tasks:
            task_dict = {
                'task': task['title'],
                'completed': task['completed'],
                'username': user['username']
            }
            todo_list.append(task_dict)
        json_dict[id] = todo_list

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_dict, json_file)
