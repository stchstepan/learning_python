print("#1")

def city_country(city, country):
  formatted = print(f"{city.title()}, {country.title()}")
  return formatted

msc = city_country('msc', 'russia')
krsk = city_country('krsk', 'russia')
krd = city_country('krd', 'russia')

print("\n#2")

def make_album(artist, album):
  formatted = {'artist': artist, 'album': album}
  return formatted

new_album = make_album('stepan', 'cherkashin')
print(new_album)

print("\n#2.1")

def make_album(artist, album, number=None):
  if number:
    formatted = {'artist': artist, 'album': album, 'number': number}
  else:
    formatted = {'artist': artist, 'album': album}
  return formatted

new_album = make_album('stepan', 'cherkashin')
print(new_album)

new_album = make_album('stepan', 'cherkashin', 24)
print(new_album)

print("\n#3")

def make_album(artist, album):
  formatted = {'artist': artist, 'album': album}
  return formatted

while True:
  print("\nIf you want to quit print 'q' any time")

  singer = input("Artist: ")

  if singer == 'q':
    break

  alb = input("Album: ")

  if alb == 'q':
    break

  information = make_album(singer, alb)
  print(information)

print("\n#3 (EXPEREMENT)")

def make_album(artist, album, number=None):
  if number:
    formatted = {'information': {'artist': artist, 
                               'album': album, 
                               'number': number}
                }
  else:
    formatted = {'information': {'artist': artist, 
                               'album': album}
                }
  return formatted

while True:
  print("\nIf you want to quit print 'q' any time")

  singer = input("\nArtist: ")
  if singer == 'q':
    break

  alb = input("Album: ")
  if alb == 'q':
    break

  while True:
    print("\nDo you want print number of songs in album? (yes/no)")
    answer = input()
    
    if answer == 'q':
      break
    if answer == 'yes':
      number = input("Number: ")
      if number == 'q':
       break
    elif answer == 'no':
      number = None
      break
    else: 
      break
    
    break

  information_album = make_album(singer, alb, number)
  
  for inf, inf2 in information_album.items():
    if answer == 'yes':
      message = (f"\n\t{inf2['artist'].title()} is autor of ") 
      message += (f"{inf2['album'].title()}. Here is {inf2['number']} songs.")
      print(message)
    else:
      print(f"\n\t{inf2['artist'].title()} is autor of {inf2['album'].title()}")

print(f"\n{information_album}")