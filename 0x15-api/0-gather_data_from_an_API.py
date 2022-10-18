#!/usr/bin/python3
''' get employee and tasks'''
import sys
import requests

if __name__ == "__main__" and len(sys.argv) >= 2:
    id = sys.argv[1]
    req = f'https://jsonplaceholder.typicode.com/users/{id}'
    r = requests.get(req)
    name = r.json()['name']
    req = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    r = requests.get(req)
    todos = r.json()
    no_t = len(todos)
    no_c = 0
    complete = ''
    for v in todos:
        if v['completed']:
            if no_c != 0:
                complete += f"\n\t {v['title']}"
            else:
                complete += f"\t {v['title']}"
            no_c += 1
    print(f'Employee {name} is done with tasks ({no_c}/{no_t}):')
    print(complete)
