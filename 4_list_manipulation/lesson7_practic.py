print('#1')
cars = ['bmw', 'audi', 'toyota', 'lada', 'ferrari', 'tesla']
print(f"The first three cars in the list are: {cars[:3]}")
print("\n")

print("The first three cars in the list are:")
for car in cars[:3]:
  print(car.title())
print("\n")

print("The car from the middle of the list is:")
for car in cars[2:3]:
  print(car.title())
print("\n")

print("The last two cars in the list are:")
for car in cars[4:]:
  print(car.title())
print("\n")

print('#2')
my_pizza = ['margarita', 'pepperoni', 'hawaii']
friends_pizza = my_pizza[:]
my_pizza.append('four cheeses')
friends_pizza.append('with ham')
print('My favorite pizzas are:')
for pizza in my_pizza: 
  print(pizza.title())
print("\n")
print("My friend favorite pizzas are:")
for pizza2 in friends_pizza: 
  print(pizza2.title())
print("\n")

print("#3")
for pizza in my_pizza: 
  print(pizza.upper())
print("\n")
for pizza2 in friends_pizza:
  print(pizza2.upper())