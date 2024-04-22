#!/usr/bin/python3

"""
Python script exporting data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    new_dict1 = {}

    for j in data2:

        row = []
        for m in data:

            new_dict2 = {}

            if j['id'] == m['userId']:

                new_dict2['username'] = j['username']
                new_dict2['task'] = m['title']
                new_dict2['completed'] = m['completed']
                row.append(new_dict2)

        new_dict1[j['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
