#!/usr/bin/python3
''' get employee and tasks'''
import json
import requests
import sys


if __name__ == "__main__":
    req = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(req)
    obj = {}
    for u in r.json():
        id = u.get('id')
        name = u.get('username')
        req = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
        r = requests.get(req)
        todos = r.json()
        tasks = []
        for t in todos:
            task = {}
            task['username'] = name
            task['task'] = t.get('title')
            task['completed'] = t.get('completed')
            tasks.append(task)
        obj[id] = tasks
    with open('todo_all_employees.json', 'w', newline='') as f:
        json.dump(obj, f)
