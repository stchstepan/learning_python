print("#1")

def sandwich(*toppings):
  print("Here is toppings for your sandwich:")
  for topping in toppings:
    print(f"- {topping}")

sandwich('mushrooms', 'pepperoni', 'cornishons')

print("\n#2")

def build_profile(first, last, **user_info):
  user_info['first name'] = first
  user_info['last name'] = last
  return user_info

stch_stepa = build_profile('stepan', 'cherkashin', hometown = 'krasnoyarsk',
                           live = 'msc', age = 21)
print(stch_stepa)

print("\n#3")

def auto(brand, model, **car_info):
  car_info['brand'] = brand
  car_info['model'] = model
  return car_info

car = auto('mazda', 'axela', color = 'gray',
                           location = 'krsk', age = 2017)
print(car)

for key, value in car.items():
  print(f"{key.title()}: {value}")