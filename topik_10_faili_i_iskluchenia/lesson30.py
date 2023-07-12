print("\n#1")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson30.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love coding!")

print("\n#1.1")

file_name = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/lesson30.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love coding!\n")
    file_object.write("I love Python!\n")

print("\n#2")

with open(file_name, 'a') as file_object:
    file_object.write("I love pizza\n")
    file_object.write("I love cola!\n")