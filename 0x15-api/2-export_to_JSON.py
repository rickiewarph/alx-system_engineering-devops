#!/usr/bin/python3

"""
Python script exporting data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for m in data2:
        if m['id'] == int(argv[1]):
            u_name = m['username']
            id_no = m['id']

    row = []

    for m in data:

        new_dict = {}

        if m['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = m['title']
            new_dict['completed'] = m['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
