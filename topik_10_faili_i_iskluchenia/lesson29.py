print("\n#1")

with open ('learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt') as file_object:
    content = file_object.read()
print(content)

print("\n#2")

with open('learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson29.txt') as file_object:
        content = file_object.read()
print(content)


print("\n#3")

with open("learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt") as file_object:
    for line in file_object:
        print(line)

print("\n#3.1")
 
with open("learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt") as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n#4")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("\n#5")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print("\n#5.1")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print("\n#!")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/lesson29.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

pi_string = float(pi_string)

res = pi_string + 5

print(res)

print("\n#6")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson29_million.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(pi_string[:52])

print("\n#7")

ile_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson29_million.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Yes")
else:
    print("No")