print("\n#1")

print("'q' for stop")

while True:
    f_n = input("Enter first number: ")
    if f_n == 'q':
        break
    s_n = input("Enter second number: ")
    if s_n == 'q':
        break
    try:
        sum = int(f_n) + int(s_n)
    except ValueError:
        print("You can't enter text!")

print("\n#2")

print("'q' for stop")

while True:
    f_n = input("Enter first number: ")
    if f_n == 'q':
        break
    s_n = input("Enter second number: ")
    if s_n == 'q':
        break
    try:
        sum = int(f_n) + int(s_n)
    except ValueError:
        print("You can't enter text!")
    else:
        print(sum)

print("\n#3")

file_path_cats = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/cats.txt'
file_path_dogs = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/dogs.txt'

def reading_files(path):
    try:
        with open(path, encoding='utf-8') as f:
            file = f.read()
    except FileNotFoundError:
        print(f"File {path} not found!")
    else:
        print(file)

files_for_reading = [file_path_cats, file_path_dogs]

for file_for_reading in files_for_reading:
    reading_files(file_for_reading)

print("\n#4")

file_path_cats = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/cats.txt'
file_path_dogs = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/dogs.txt'

def reading_files(path):
    try:
        with open(path, encoding='utf-8') as f:
            file = f.read()
    except FileNotFoundError:
        pass
    else:
        print(file)

files_for_reading = [file_path_cats, file_path_dogs]

for file_for_reading in files_for_reading:
    reading_files(file_for_reading)

print("\n#5")

files_path = ['learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/idiot.txt', 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/alice.txt']

for file_path in files_path:
    with open(file_path, encoding='utf-8') as f:
        file = f.read()
    if 'the ' in file:
        sum_the = file.lower().count('the ')
    print(f"\n{sum_the}")