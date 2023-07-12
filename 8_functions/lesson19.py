print("#1")

def describe_pet(animal_type, pet_name):
  print(f"I have a {animal_type}")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('cat', 'tema')

print("\n#1.1")

describe_pet('cat', 'tema')
describe_pet('dog', 'sasha')

print("\n#2")

describe_pet(animal_type = 'cat', pet_name = 'tema')
describe_pet(pet_name = 'tema', animal_type = 'cat')

print("\n#3")

def describe_pet(pet_name, animal_type = 'cat'):
  print(f"I have a {animal_type}")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name = 'tema')
describe_pet('tema')

print("\n#4")

def describe_pet(pet_name, animal_type = 'cat'):
  """Выводит информацию о животных"""
  print(f"I have a {animal_type}")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name = 'tema')
describe_pet('tema')

describe_pet(pet_name = 'tema', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'tema')
describe_pet('tema', 'hamster')