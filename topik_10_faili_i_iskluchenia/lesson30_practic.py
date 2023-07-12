print("\n#1")

guest = input("Say your name: ")
path = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/guest.txt'

with open(path, 'a') as file_object:
    file_object.write(guest)

print("\n#2")

path = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/guest_book.txt'

while True:
    message = "\nif you want stop print 'stop'"
    message += "\nPrint your name: "
    ask = input(message)

    if ask != 'stop':
        print(f"Hello {ask}!")
        with open(path, 'a') as file_object:
            file_object.write(f"{ask}\n")

    else:
        break

print("\n#3")

path = 'learning_python_erik_matiz/part_1/topik_10_faili_i_iskluchenia/text_files/answers.txt'

while True:
    message = "\nif you want stop print 'stop'"
    message += "\nPrint why you love coding? "
    ask = input(message)

    if ask != 'stop':
        with open(path, 'a') as file_object:
            file_object.write(f"{ask}\n")

    else:
        break