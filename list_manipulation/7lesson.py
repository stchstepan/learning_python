print("#1")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print("\n")

print("#2")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())
print("\n")

print("#3")
my_foods = ['pizza', 'pasta', 'burgers', 'pie']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")

print("#4")
my_foods.append('sushi')
print(my_foods)

friend_foods.append('bread')
print(friend_foods)
print("\n")