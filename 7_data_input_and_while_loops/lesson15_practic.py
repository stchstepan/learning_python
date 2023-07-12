print("#1")

car = input("What car do you prefer?\n")

print(f"Let me see if i can find you a {car}")

print("\n#2")

table = input("How many persons will be attend?\n")
table = int(table)

if table >= 8:
  print("Sorry, you shold wait for 15 min")
else:
  print("Your table is ready, you are welcome!")

print("\n#3")

number = input("Print a number: ")
number = int(number)

if number % 10 == 0:
  print("Your number is /10!")
else:
  print("Your number is not /10!")