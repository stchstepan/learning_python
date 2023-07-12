print("#1")
print("\n#1.1")
alien_color = ('green', 'yellow', 'red')
color = 'green'
if color == 'green':
  print("+5 points")

print("\n#1.2")
if color == 'green':
  print()

print("\n#2")
print("\n#2.1")
alien_color = ('green', 'yellow', 'red')
color = 'green'
if color == 'green':
  print("+5 points")
else:
  print("+10 points")

print("\n#2.2")
alien_color = ('green', 'yellow', 'red')
color = 'yellow'
if color == 'green':
  print("+5 points")
else:
  print("+10 points")

print("\n#3")
print("\n#3.1")
alien_color = ('green', 'yellow', 'red')
color = 'green'
if color == 'green':
  print("+5 points")
elif color == 'yellow':
  print("+10 points")
else:
  print("+15 points")

print("\n#3.2")
alien_color = ('green', 'yellow', 'red')
color = 'yellow'
if color == 'green':
  print("+5 points")
elif color == 'yellow':
  print("+10 points")
else:
  print("+15 points")

print("\n#3.3")
alien_color = ('green', 'yellow', 'red')
color = 'red'
if color == 'green':
  print("+5 points")
elif color == 'yellow':
  print("+10 points")
else:
  print("+15 points")

print("\n#4")
age = 65
if age < 2:
  status = 'младенец'
elif age < 4:
  status = 'малыш'
elif age < 13:
  status = 'ребенок'
elif age < 20:
  status = 'подросток'
elif age < 65:
  status = 'взрослый'
else:
  status = 'пожилой человек'
print(f"Вы {status}!")

print("\n#5")
favorite_fruits = ['pineaple', 'banana', 'peach']
if 'pineaple' in favorite_fruits:
  print("You really like pineaples")
if 'banana' in favorite_fruits:
  print("You really like banana")
if 'peach' in favorite_fruits:
  print("You really like peach")
if 'apple' in favorite_fruits:
  print("You really like apple")
if 'berries' in favorite_fruits:
  print("You really like berries")