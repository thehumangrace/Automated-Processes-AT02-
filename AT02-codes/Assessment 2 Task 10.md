# Assessment 2 Task 10

## Overview
This task evaluates the students ability to debug script. 

### Before Debugging

```python

#!/usr/bin/env python3
# coding: utf-8

# Python program to sort users from a file, and write the sorted users to another file.

import sys


def read_users_from_file(file_path: str) -> list[str]:
    """ Read a list of users from a file """
    with open(file_path, 'r') as file:
        users = file.readlines()
    return users

def write_users_to_file(users: list[str], file_path: str):
    """ Write a list of users to file """
    with open(file_path, 'w') as file:
        for user in users:
            file.write(user)

def sort_users(users: list[str]) -> list[str]:
    """ Sort users by name using bubble sort """
    for i in range(len(users) - 1):
        for j in range(i + 1, len(users)):
            if users[i] > users[j]:
                users[i], users[j] = users[i], users[j]
    return users

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python sort_names.py <input_file> <output_file>")
        sys.exit(1)

    input_file = args[0]
    output_file = args[1]

    users = read_users_from_file(input_file)
    sorted_users = sort_users(users)
    write_users_to_file(sorted_users, output_file)

if __name__ == "__main__":
    sys.exit(main())```


### After Debugging

``` python
#!/usr/bin/env python3
# coding: utf-8

# Python program to sort users from a file, and write the sorted users to another file.

import sys


def read_users_from_file(file_path: str) -> list[str]:
    """ Read a list of users from a file """
    with open(file_path, 'r') as file:
        users = file.readlines()
    return users

def write_users_to_file(users: list[str], file_path: str):
    """ Write a list of users to file """
    with open(file_path, 'w') as file:
        for user in users:
            file.write(user)

def sort_users(users: list[str]) -> list[str]:
    """ Sort users by name using bubble sort """
    for i in range(len(users) - 1):
        for j in range(i + 1, len(users)):
            if users[i] > users[j]:
                #Switched the i and the j for = users[j], users [i]
                users[i], users[j] = users[j], users[i]
    return users

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python sort_names.py <input_file> <output_file>")
        sys.exit(1)

    input_file = args[0]
    output_file = args[1]

    users = read_users_from_file(input_file)
    sorted_users = sort_users(users)
    write_users_to_file(sorted_users, output_file)

if __name__ == "__main__":
    #Removed sys.exit() because it is not needed here
    (main())
```
