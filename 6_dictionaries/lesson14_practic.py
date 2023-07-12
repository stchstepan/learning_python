print("#1")

human = {'first_name': 'stepan', 
         'second_name': 'cherkashin', 
         'age': 21, 
         'city': 'moscow'}

human_2 = {'first_name': 'sasha', 
         'second_name': 'fominskih', 
         'age': 21, 
         'city': 'krasnoyarsk'}

human_3 = {'first_name': 'arseniy', 
         'second_name': 'malev', 
         'age': 21, 
         'city': 'krasnodar'}

people = [human, human_2, human_3]

for man in people:
  print(man)

print("\n#2")

tema = {'name': 'tema', 
         'vid': 'cat', 
         'owner': 'sveta',}

bobik = {'name': 'bobik', 
         'vid': 'dog', 
         'owner': 'steets',}

kesha = {'name': 'kesha', 
         'vid': 'parrot', 
         'owner': 'leha',}

pets = [bobik, kesha, tema]

for pet in pets:
  print(pet)

print("\n#3.1")

f_p = {'moscow': ['stepa', 'ars', 'leha'],
       'spb': ['foma'],
       'krasnoyarsk': ['stepa', 'vlad', 'anton']}

for place, names in f_p.items():
  for name in names:
      print(f"{place.title()} is favorite place of {name.title()}")

print("\n#3.2")

f_p = {'moscow': ['stepa', 'ars', 'leha'],
       'spb': ['foma'],
       'krasnoyarsk': ['stepa', 'vlad', 'anton']}

for places, names in f_p.items():
  for name in names:
    if places == f_p['moscow']:
      print(f"{places.title()} is fav place of: {name.title()}")
    elif places == f_p['spb']:
      print(f"{places.title()} is fav place of: {name.title()}")
    else:
      print(f"{places.title()} is fav place of: {name.title()}")

print("\n#4")

numbers = {'stepan': [7, 8], 
           'arseniy': [1, 12], 
           'petya': [10, 7,], 
           'artem': [3, 0], 
           'danila': [6]}

for numbers in numbers['stepan']:
  print(f"Stepan's fav numbers is: {numbers}")

print("\n#4")

cities = {'moscow': {'country': 'russia',
                     'population': '15.000.000'},
          'krasnoyarsk': {'country': 'russia',
                     'population': '1.000.000'},
          'krasnodar': {'country': 'russia',
                     'population': '2.000.000'}}

for city, city_info in cities.items():
  print(f"\nHere some information about {city.title()}:")
  
  c_p = f'''Country: {city_info['country'].title()}, 
  population: {city_info['population'].title()}'''

  print(f"\t{c_p}")

