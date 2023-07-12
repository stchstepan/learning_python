print("#1")

gloss = {'словарь': 'абоба', 'список': 'абобус', 'переменная': 'кака'}

gloss['set()'] = 'множество'
gloss['.get()'] = 'умное ображение'
gloss['.keys()'] = 'только ключи'
gloss['.items()'] = 'пара ключ-значение'
gloss['.values()'] = 'только значения'

for word, deff in gloss.items():
  print(f"{word.title()} - это {deff}")

print("\n#2")

riv_cou = {'enisey': 'russia', 'nile': 'egypt', 'arizona': 'america'}

for riv, cou in riv_cou.items():
  print(f"The {riv.title()} runs through {cou.title()}")

for riv in riv_cou:
  print(riv.title())

for cou in riv_cou.values():
  print(cou.title())

print("\n#3")

f_l = {'artem': 'r',
       'stepa': 'python',
       'danila': 'sql',
       'misha': ' c++'}

for name, lang in f_l.items():
  print(f"{name.title()}, your favorite lang is {lang}")

if 'lena'.lower() not in f_l:
  print("Lena, please vote")

if 'Stepa'.lower() not in f_l:
  print("Stepa, please vote")