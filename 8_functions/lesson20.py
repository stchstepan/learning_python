print("#1")

def get_formated_name (first_name, last_name):
  full_name = f"{first_name} {last_name}"
  return full_name.title()

person = get_formated_name('stepan', 'cherkashin')
print(person)

print("\n#2")

def get_formated_name (first_name, second_name, last_name = ''):
  if last_name: 
    full_name = f"{second_name} {first_name} {last_name}"
  else:
    full_name = f"{second_name} {first_name}"
  return full_name.title()

person = get_formated_name('stepan', 'cherkashin')
print(person)

person = get_formated_name('stepan', 'cherkashin', 'nikitich')
print(person)

print("\n#3")

def build_person(first_name, last_name):
  person = {'first': first_name, 'last': last_name}
  return person

musician = build_person('stepan', 'cherkashin')
print(musician)

print("\n#4")

def build_person(first_name, second_name, age = None):
  person = {'first': first_name, 'last': second_name}

  if age: 
    person['age'] = age

  return person

musician = build_person('stepan', 'cherkashin', age = 21)
print(musician)

print("\n#5")

def get_formatted_name(first_name, last_name):
  full_name = f"{first_name.title()} {last_name.title()}"
  return full_name

while True:
  print("\nPlease tell me your name: ")
  print("(enter 'q' at any time to quit)")

  f_name = input("First name: ")
  
  if f_name == 'q': 
    break

  l_name = input("Last name: ")

  if l_name == 'q':
    break

  formated_name = get_formated_name(f_name, l_name)
  print(f"\nHello, {formated_name}!")