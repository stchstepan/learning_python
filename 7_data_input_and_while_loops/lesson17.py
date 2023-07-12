print("#1")

unconfirmed_users = ['stch_stepa', 'afominskih', 'seeemsgoog', 'malevarrr']
confirmed_users = []

while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print(f"Verifying user: {current_user}")
  confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
  print(confirmed_user)

print("\n#2")

pets = ['cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
  pets.remove('cat')

print(pets)

print("\n#3")

responses = {}

flag = True

while flag:
  name = input("\nWhats your name? ")
  respons = input("Which mountin wold you like to climb someday? ")

  responses[name] = respons

  repeat = input("\nWould you like to let another person respond? (yes/no) ")

  if repeat == 'no':
    flag = False

for name, respons in responses.items():
  print(f"\n{name.title()} would like to climb {respons.title()}")