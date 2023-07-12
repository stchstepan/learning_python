print("\n#1")

import json

def greet_user():
    file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'

    try:
        with open(file_name) as f:
            username = json.load(f)

    except FileNotFoundError:
        username = input("What is your name? ")
        with open(file_name, 'w') as f:
            json.dump(username, f)
            print(f"Hello, {username}!")

    else:
        print(f"Welcome back, {username}!")

greet_user()

print("\n#1.1")

def get_stored_name():
    file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'

    try:
        with open(file_name) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username

def greet_user():
    username = get_stored_name()

    if username:
        print(f"Welcome back, {username}!")

    else:
        username = input("What is your name? ")
        file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'
        with open(file_name, 'w') as f:
            json.dump(username, f)
            print(f"Hello, {username}!")

greet_user()

print("\n#1.2")

def get_stored_name():
    file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'

    try:
        with open(file_name) as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username

def get_new_username():
        username = input("What is your name? ")
        file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'
        with open(file_name, 'w') as f:
            json.dump(username, f)
        return username

def greet_user():
    username = get_stored_name()

    if username:
        print(f"Welcome back, {username}!")

    else:
        username = get_new_username()
        print(f"Hello, {username}!")

greet_user()