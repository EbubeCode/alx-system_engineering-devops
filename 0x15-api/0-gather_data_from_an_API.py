#!/usr/bin/python3
''' get employee and tasks'''
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    req = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    r = requests.get(req)
    name = r.json().get('name')
    req = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    r = requests.get(req)
    todos = r.json()
    no_t = len(todos)
    no_c = 0
    complete = ''
    for v in todos:
        if v.get('completed'):
            if no_c != 0:
                complete += "\n\t {}".format(v.get('title'))
            else:
                complete += "\t {}".format(v.get('title'))
            no_c += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, no_c, no_t))
    print(complete)
