#!/usr/bin/python3
''' get employee and tasks'''
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    r = requests.get(req)
    name = r.json().get('username')
    req = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    r = requests.get(req)
    todos = r.json()
    tasks = []
    for t in todos:
        task = {'task': t.get('title')}
        task['completed'] = t.get('completed')
        task['username'] = name
        tasks.append(task)
    obj = {id: tasks}
    with open('{}.json'.format(id), 'w', newline='') as f:
        json.dump(obj, f)
