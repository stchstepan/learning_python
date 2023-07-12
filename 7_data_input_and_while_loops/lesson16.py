print("#1")

current_number = 1

while current_number <= 5:
  print(current_number)
  current_number += 1

print("\n#2")

prompt = "\nTell me something? and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programm "

message = ""

while message != 'quit':
  message = input(prompt)
  print(message)

print("\n#2.1")

prompt = "\nTell me something? and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programm "

message = ""

while message != 'quit':
  message = input(prompt)

  if message != 'quit':
    print(message)

print("\n#3")

prompt = "\nTell me something? and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the programm "

active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message) 


print("\n#4")

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the programm "

while True: 
  city = input(prompt)

  if city == 'quit':
    break
  else: 
    print(f"I'd like to go to {city.title()}!")

print("\n#5")

current_number = 0

while current_number < 10: 
  current_number += 1
  if current_number % 2 == 0:
    continue
  
  print(current_number)