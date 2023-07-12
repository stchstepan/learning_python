print("#1")

s_o = ['tuna', 'bacon', 'pepperoni', 'pastrami']
f_s = []

while s_o:
  sandw = s_o.pop()

  print(f"\n{sandw.title()} is prepearing now. Please wait.")
  
  f_s.append(sandw) 

for sandwich in f_s:
  print(f"\n{sandwich.title()} is ready")

print("\n#2")

s_o = ['tuna', 'bacon', 'pastrami', 'pastrami', 'pastrami', 
       'pepperoni', 'pastrami']
f_s = []

if 'pastrami' in s_o:
  print("Sorry, today we didn't have pastrami sandwich!")
  
  while 'pastrami' in s_o:
    s_o.remove('pastrami')

while s_o:
  sandw = s_o.pop()
  print(f"\n{sandw.title()} is prepearing now. Please wait.")
  f_s.append(sandw) 

for sandwich in f_s:
  print(f"\n{sandwich.title()} is ready")

print("\n#3")

w_l = {}

print("In this task you shold type place where you want to go someday.")

flag = True

while flag:
  name = input("\nPlease, type your name: ")
  place = input("Please, type place, where you dream to go: ")

  w_l[name] = place

  
  choice = input("Did you want ask someone? (yes/no) ")

  if choice == 'no':
    flag = False

for name, place in w_l.items():
    print(f"\n{name.title()} wants to visit {place.title()}")