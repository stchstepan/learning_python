print("\n#1")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson29_practic.txt'

with open(file_name) as file_object:
    vivod = file_object.read()
print(vivod)

print("\n#1.1")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson29_practic.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())

print("\n#1.2")

with open(file_name) as file_object:
    vivod = file_object.readlines()

for line in vivod:
    print(line.strip())

print("\n#2")

with open(file_name) as file_object:
    vivod = file_object.read()

vivod = vivod.replace('aaaa', 'qqqq')
print(vivod)