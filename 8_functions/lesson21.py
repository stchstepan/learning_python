print("#1")

def greet_users(names):
  for name in names:
    message = f"Hello, {name.title()}!"
    print(message)

usernames = ['stch_stepa', 'afominskih', 'malevarrr']
greet_users(usernames)

print("\n#2")

def print_models(unprinted_models, completed_models):
  while unprinted_models:
    current_design = unprinted_models.pop()
    print(f"Printing model {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  print("\nThe following models have been printed: ")
  for completed_model in completed_models:
    print(completed_model)

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprintrd_models, completed_models)
show_completed_models(completed_models)

print("\n#2.1")

def print_models(unprinted_models, completed_models):
  while unprinted_models:
    current_design = unprinted_models.pop()
    print(f"Printing model {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  print("\nThe following models have been printed: ")
  for completed_model in completed_models:
    print(completed_model)

unprintrd_models = ['phoe case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprintrd_models[:], completed_models)
show_completed_models(completed_models)