print("#1")

message = input("Tell me something? and i will repeat it back to you: ")
print(message)

print("\n#2")

prompt = "If you tell us who you are, we can personalize the messge you see."
prompt += "\nWhat is your first name?  "

name = input(prompt)
print(f"\nHello, {name}")

print("\n#3")

age = input("How old are you? ")
age = int(age)
print(age >= 18)

print("\n#4")

height = input("How tall are you? ")
height = int(height)

if height >= 180:
  print("You are beautiful!")
else:
  print("You are ugly!")

print("\n#5")

number = input("Input number: ")
number = int(number)

if number % 2 == 0:
  print("Even")
else:
  print("Odd")
