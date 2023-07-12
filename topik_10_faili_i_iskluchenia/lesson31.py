print("\n#1")

#print(5/0)

print("\n#1.1")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("\n#2")

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' ti quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

print("\n#2.1")

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' ti quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

print("\n#3")

file_name = 'alice.txt'

try: 
    with open (file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist.")

print("\n#4")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/alice.txt'

try: 
    with open (file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist.")
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")

print("\n#5")

def count_words(file_name):
    try: 
        with open (file_name, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/alice.txt'
count_words(file_name)

print("\n#5.1")

def count_words(file_name):
    try: 
        with open (file_name, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_names = ['learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/alice.txt', 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/idiot.txt']
for file_name in file_names:
    count_words(file_name)

print("\n#6")

def count_words(file_name):
    try: 
        with open (file_name, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")

file_names = ['learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/alice.txt', 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/idiot.txt']
for file_name in file_names:
    count_words(file_name)