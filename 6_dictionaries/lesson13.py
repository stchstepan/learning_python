f_l = {'artem': 'r',
       'stepa': 'python',
       'danila': 'sql'}

print(f"Danila's favorite language is {f_l['danila'].upper()}")

for names, languages in f_l.items():
  if f_l['danila'] == 'sql':
    f_l['danila'] = 'sql'.upper()
  print(f"\n{names.title()}'s favorite language is {languages}")


print("#1.1")

users_0 = {'name': 'stch', '2_name': '_', '3_name': 'stepa'}
for key, value in users_0.items():
   print(f"\nKey: {key}")
   print(f"Value: {value}")

print("\n#2")

for name in f_l.keys():
  print(f"{name.title()}")
  
print("\n#3")

f_l = {'artem': 'r',
       'stepa': 'python',
       'danila': 'sql'}

friends = ['danila', 'stepa']

for name in f_l:
  print(f"Hello, {name.title()}")

  if name in friends:
    language = f_l[name].title()
    print(f"\t{name.title()}, i see you love {language}")

print("\n#4")

if 'erin' not in f_l:
  print("Erin, please take our poll!")

print("\n#5")

f_l = {'artem': 'r',
       'stepa': 'python',
       'danila': 'sql'}

for name in sorted(f_l.keys()):
  print(f"{name.title()}, thank you for taking poll!")

print("#6")

print("The following languages have been mentioned:")

for languages in f_l.values():
  print(languages)

print("#7")

f_l = {'artem': 'r',
       'stepa': 'python',
       'danila': 'sql',
       'anton': 'python'}

print("The following languages have been mentioned:")

for languages in set(f_l.values()):
  print(languages)