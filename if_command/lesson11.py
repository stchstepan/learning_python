print("#1")
requsted_toppings = ['mushrooms', 'green peppes', 'extra chees']
for toppings in requsted_toppings: 
  if toppings == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
  else:
    print(f"Adding {toppings}.")
print("\nFinished making yorur pizza!")

print("\n#2")
requsted_toppings = []
if requsted_toppings:
  for topping in requsted_toppings:
    print(f"Adding {topping}.")
  print("\nFinished making yor pizza!")
else:
  print("Are you sure you want a plain pizza?")

print("\n#3")
available_toppings = ['mushrooms', 'pepperoni', 'olives', 
                      'green peppers', 'pineapple', 'extra chees']
requsted_toppings = ['mushrooms', 'french fries', 'extra chees']
for topping in requsted_toppings:
  if topping in available_toppings:
    print(f"Adding {topping}")
  else:
    print(f"Sorry, we don't have {topping} now!")
print("\nFinished making yorur pizza!")