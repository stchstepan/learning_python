print("#1")

def make_shirt(number, text):
  print(f"\nHere is number of your shirt: {number}")
  print(f"And here is text on your shirt: {text}")

make_shirt(1, 'Stepan')
make_shirt(number = 1,text = 'Stepan')

print("\n#2")

def make_shirt(number, text = 'I love Python', size = 'L'):
  print(f"\nHere is number of your shirt: {number}")
  print(f"And here is text on your shirt: {text}")
  print(f"Size: {size}")

make_shirt(1)

make_shirt(1, 'Stepan', 'M')
make_shirt(number = 1, text = 'Stepan', size = 'M' )

print("\n#3")

def describe_city(city, country):
  print(f"{city.title()} is in {country.title()}")

describe_city('msc', 'russia')

print("\n#3.1")

def describe_city(city, country = 'russia'):
  print(f"{city.title()} is in {country.title()}")

describe_city('msc', 'russia')
describe_city('krsk', 'russia')
describe_city('boston', 'america')