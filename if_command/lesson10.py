print("#1")
age = 19
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote.")
  print("Please register to vote as soon as you turn 18!")

print("\n#2")
age = 12
if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $25.")
else: 
  print("Your admission cost is $40.")

print("\n#2.1")
age = 12
if age < 4:
  price = 0
elif age < 18:
  price = 25
else: 
  price = 45
print(f"Your admission cost is ${price}.")

print("\n#2.2")
age = 65
if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
else: 
  price = 20
print(f"Your admission cost is ${price}.")

print("\n2.3")
age = 65
if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
elif age >= 65:
  price = 20
print(f"Your admission cost is $ {price}.")

print("\n#3")
requsted_toppings = ['mushrooms', 'extra chees']
if 'mushrooms' in requsted_toppings:
  print("Adding mushrooms")
if 'pepperoni' in requsted_toppings:
  print("Adding pepperoni")
if 'extra chees' in requsted_toppings:
  print("Adding extra chees")
print("\nFinished making your pizza!")