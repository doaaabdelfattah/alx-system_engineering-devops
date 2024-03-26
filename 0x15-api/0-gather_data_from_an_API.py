#!/usr/bin/python3
'''Python script that
returns information about his todo list progress.
'''
if __name__ == "__main__":
    import requests
    from sys import argv

    urlUser = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_name = requests.get(urlUser)
    name = response_name.json()['name']

    urlTodo = urlUser + '/todos'
    response_todos = requests.get(urlTodo)
    tasks = response_todos.json()
    total_task = len(tasks)

    count = 0
    for task in tasks:
        if task['completed'] is True:
            count += 1

    print("Employee {} is done with tasks({}/{}):".format(name, count,
          total_task))

    for task in tasks:
        if task['completed'] is True:
            task_name = task['title']
            print("\t {}".format(task_name))