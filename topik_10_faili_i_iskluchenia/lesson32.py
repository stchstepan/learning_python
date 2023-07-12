print("\n#1")

import json

numbers = [1, 2, 3, 5, 7, 11, 13]

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/numbers.json'
with open(file_name, 'w') as f:
    json.dump(numbers, f)

print("\n#2")

import json

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/numbers.json'

with open(file_name) as f:
    numbers = json.load(f)

print(numbers)

print("\n#3")

import json

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'

username = input("What is your name? ")

with open(file_name, 'w') as f:
    json.dump(username, f)
    print(f"Hello, {username}!")

print("\n#4")

import json

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/json_files/username.json'

with open(file_name) as f:
    username = json.load(f)

print(f"Welcome back, {username}!")

print("\n#5")

import json

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