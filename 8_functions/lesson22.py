print("#1")

def make_pizza(*toppings):
  print("Making a pizza with the fokkowing toppings: ")
  for topping in toppings:
    print(f"- {topping}")

make_pizza('pepperoni', 'chees', 'pineapple')

print("\n#2")

def make_pizza(size, *toppings):
  print(f"\nMaking a {size}-cm pizza with following toppings: ")
  for topping in toppings:
    print(f"- {topping}")

make_pizza(22, 'pepperoni', 'chees', 'pinapple')

print("\n#3")

def build_person(first, last, **user_info):
  user_info['first name'] = first
  user_info['last name'] = last
  return user_info

user_profile = build_person('stepan', 'cherkashin', location = 'msc', uni = 'fu')
print(user_profile)