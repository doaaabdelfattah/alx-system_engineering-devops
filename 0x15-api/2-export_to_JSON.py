#!/usr/bin/python3
'''
return todo list info from fiven id from API
'''
import json
import requests
import sys

if __name__ == "__main__":

    user_url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])

    # Make a GET request to fetch user information
    response_user = requests.get(f'{user_url}/users/{user_id}')
    # Extracts the JSON content from the HTTP response
    # It return a Python dict that can be accessed
    users_data = response_user.json()

    user_todo = 'https://jsonplaceholder.typicode.com/todos'

    # Make a GET request to fetch user's todo list
    response_Todo = requests.get(f'{user_todo}?userId={user_id}')
    user_tasks = response_Todo.json()

    todo_list = []
    json_dict = {}
    for task in user_tasks:
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        task_dict['username'] = users_data['username']
        todo_list.append(task_dict)

    json_dict[user_id] = todo_list
    # Write data to JSON file
    json_file_name = f"{user_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(json_dict, json_file)
