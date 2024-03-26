#!/usr/bin/python3
'''
return todo list info from fiven id from API
'''
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])

    # Make a GET request to fetch user information
    response_user = requests.get(f'{user_url}/users/{user_id}')
    # Extracts the JSON content from the HTTP response
    # It return a Python dict that can be accessed
    user_name = response_user.json()['name']

    user_todo = 'https://jsonplaceholder.typicode.com/todos'

    # Make a GET request to fetch user's todo list
    response_Todo = requests.get(f'{user_todo}?userId={user_id}')
    user_tasks = response_Todo.json()

    count = 0
    for data in user_tasks:
        if data.get('completed') is True:
            count += 1

    print("Employee {} is done with tasks({}/{}):".format(user_name,
          count, len(user_tasks)))

    for task in user_tasks:
        if task.get('completed') is True:
            print("\t {}".format(task['title']))
