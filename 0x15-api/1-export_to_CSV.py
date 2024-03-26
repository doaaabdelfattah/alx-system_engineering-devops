#!/usr/bin/python3
'''
return todo list info from fiven id from API
'''
import csv
import requests
import sys

if __name__ == "__main__":

    user_url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])

    # Make a GET request to fetch user information
    response_user = requests.get(f'{user_url}/users/{user_id}')
    # Extracts the JSON content from the HTTP response
    # It return a Python dict that can be accessed
    user_name = response_user.json()['username']

    user_todo = 'https://jsonplaceholder.typicode.com/todos'

    # Make a GET request to fetch user's todo list
    response_Todo = requests.get(f'{user_todo}?userId={user_id}')
    user_tasks = response_Todo.json()

    # Writing result to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            writer.writerow([user_id, user_name, task.get(
                'completed'), task.get('title')])
