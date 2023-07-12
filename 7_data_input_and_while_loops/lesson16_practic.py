print("#1")
message = "\nIf you want add some toppings for pizza, print here: "
message += "\nFor end adding print 'quit' "

toppings = " "

while toppings != 'quit':
  toppings = input(message)

  if toppings == 'quit':
    break

  print(f"\nNice! Your topping is here: {toppings}")

print("\n#2")

message = "\nEnter your age: "

age = " "
flag = True

while flag: 
  age = input(message)
  age = int(age)

  if age <= 3:
    print("free")
    flag = False
  elif age <= 12:
    print("10")
    flag = False
  else: 
    print("15")
    flag = False
 
print("\n#3")

message = "\nIf you want add some toppings for pizza, print here: "
message += "\nFor end adding print 'quit' "

toppings = " "

while toppings != 'quit':
  toppings = input(message)

  if toppings != 'quit':
    print(f"\nNice! Your topping is here: {toppings}")

print("\n#4")