#!/usr/bin/python3
''' get employee and tasks'''
import csv
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
    with open('{}.csv'.format(id), 'w', newline='') as csvfile:
        writ = csv.writer(csvfile, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_ALL)
        for t in todos:
            writ.writerow([id, name, t.get('completed'), t.get('title')])
