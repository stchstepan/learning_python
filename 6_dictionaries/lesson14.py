print("#1")

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
  print(alien)

print("\n#2")

aliens = []

for alien_number in range(30):
  new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens[:5]:
  print(alien)

print(f"Total number of aliens: {len(aliens)}")

print("\n#3")

aliens = []

for alien_number in range(30):
  new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens [:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

for alien in aliens[:5]:
  print(alien)

print(f"Total number of aliens: {len(aliens)}")

print("\n#4")

aliens = []

for alien_number in range(30):
  new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens [:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

  elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['points'] = 15
    alien['speed'] = 'fast'

for alien in aliens[:5]:
  print(alien)

print(f"Total number of aliens: {len(aliens)}")

print("\n#5")

pizza = {'crust': 'thick', 
         'toppings': ['mushrooms', 'extra cheese']}

print(f"You ordered a {pizza['crust']}-crust pizza.")

print("And here your toppings:")

for topping in pizza['toppings']: 
  print(topping.title())

print("\n#5.1")

pizza = {'crust': ['thick'], 
         'toppings': ['mushrooms', 'extra cheese']}

for crust in pizza['crust']: 
  print(f"You ordered a {crust}-crust pizza.")

print("And here your toppings:")

for topping in pizza['toppings']: 
  print(topping.title())

print("\n#6")

f_l = {'danila': ['python', 'r', 'c#'],
       'stepa': ['python', 'java script', 'sql'],
       'artemik': ['c++', 'c'],
       'ars': ['exel']}

for names, languages in f_l.items():
  if len(languages) == 1:
    print(f"\n{names.title()}'s favorite languages is:")
  else:
    print(f"\n{names.title()}'s favorite languages are:")
  for language in languages:
    print(language.title())

print("\n#7")

users = {'afominskih': {'first': 'sasha',
                        'second': 'fominskih',
                        'city': 'krasnoyarsk'},
         'stch_stepa': {'first': 'stepa', 
                        'second': 'cherkashin',
                        'city': 'moscow'},
         'malevarrr': {'first': 'arseniy',
                       'second': 'malev',
                       'city': 'krasnodar'}}

for username, user_info in users.items():
  print(f"\nUsername: {username}")
  
  full_name = f"{user_info['first']} {user_info['second']}"
  city = user_info['city']

  print(f"\tFull name: {full_name.title()}")
  print(f"\tCity: {city.title()}")

