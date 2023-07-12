print("\n#1, #1.1")

import json

print("Enter your fav number, and i will rember it!")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/fav_number.json'

try:
    with open(file_name) as f:
        number = json.load(f)   

except FileNotFoundError:
    number = input("Enter number: ")
    with open(file_name, 'w') as f:
        json.dump(number, f)

print(number)

print("\n#2")

def get_number():
    '''Пытается найти файл с числом'''
    try:
        with open(file_name) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    '''Запись нового числа'''
    print("Enter your fav number, and i will rember it!")
    number = input("Enter number: ")
    file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/fav_number.json'
    with open(file_name, 'w') as f:
        json.dump(number, f)
    return number

def fav_number():
    '''Выводит любимое число'''
    number = get_number()
    if number:
        print(f"Your fav number is {number}")
    else:
        number = get_new_number()
        print(f"Your fav number is {number}")

fav_number()

print("\n#3")

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

def answer():
    username = get_stored_name()
    question = input(f"You are {username}? (print y/n) ")
    if question == 'y':
        print(f"Welcome back, {username}!")
    elif question == 'n':
        username = get_new_username()
        print(f"Hello, {username}!")

answer()