print("#1")
users = ['admin', 'stepan', 'anton', 'slava', 'sasha']
for user in users:
  if user == 'admin':
    print(f"Hello, {user.title()}! Would you like to see a ststus report?")
  else:
    print(f"Hello, {user.title()}! Thank you for logging again!")

print("\n#2")
users = []
if users:
  for user in users:
    if user == 'admin':
      print(f"Hello, {user.title()}! Would you like to see a ststus report?")
    else:
      print(f"Hello, {user.title()}! Thank you for logging again!")
else:
  print("We need to in some users!")

print("\n#3")
current_users = ['stch_stepa', 'ma.agni', 'bk00d', 'malevarrr', 'afomonskih']
new_users = ['denis_kurpas', 'sssanchez', 'k_podpaskova', 
             'STCH_STEPA', 'ma.agni']
for user in new_users:
  if user.lower() in current_users:
    print("К сожалению, данное имя пользователя уже занято. Подберите другое.")
  else:
    print("Данное имя пользователя свободно!")

print("\n#4")
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
  if number == '1':
    print(f"{number}st")
  elif number == '2':
    print(f"{number}nd")
  elif number == '3':
    print(f"{number}rd")
  else:
    print(f"{number}th")