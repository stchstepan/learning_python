def make_pizza(size, *toppings):
  print(f"\nMaking a {size}-cm pizza with following toppings: ")
  for topping in toppings:
    print(f"- {topping}")