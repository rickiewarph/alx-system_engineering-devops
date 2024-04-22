#!/usr/bin/python3

"""
Python script exporting data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for m in data2:
        if m['id'] == int(argv[1]):
            employee = m['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for m in data:

            row = []
            if m['userId'] == int(argv[1]):
                row.append(m['userId'])
                row.append(employee)
                row.append(m['completed'])
                row.append(m['title'])

                writ.writerow(row)
