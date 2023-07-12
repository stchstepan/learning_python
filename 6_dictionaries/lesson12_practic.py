print("#1")
human = {'first_name': 'stepan', 
         'second_name': 'cherkashin', 
         'age': 21, 
         'city': 'moscow'}
print(f'''My name is {human['first_name']. title()}, my second name is 
{human['second_name'].title()}. 
I am {human['age']} years old.
I am living in {human['city'].title()}.''')

print("\n#2")
numbers = {'stepan': 7, 'arseniy': 12, 'petya': 10, 'artem': 3, 'danila': 6}

stepan = f"Stepan's fav number is {numbers['stepan']}"
arseniy = f"Arseniy's fav number is {numbers['arseniy']}"
petya = f"Petya's fav number is {numbers['petya']}"
artem = f"Artem's fav number is {numbers['artem']}"
danila = f"Danila's fav number is {numbers['danila']}"

numbers_in_names = (stepan, arseniy, petya, artem, danila)

for number in numbers_in_names:
  print(number)

print("\n#3")
gloss = {'словарь': 'абоба', 'список': 'абобус', 'переменная': 'кака'}
print(f"Словарь это {gloss['словарь']}")
print(f"Список это {gloss['список']}")
print(f"Переменная это {gloss['переменная']}")