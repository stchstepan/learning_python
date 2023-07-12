print("#1")
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

print("\n#2")
alien_0 = {'color': 'green', 'points': '5'}
new_points = alien_0['points']
print(f"You just earned {new_points} points.")

print("\n#3")
alien_0 = {'color': 'green', 'points': '5'}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n#4")
alien_0 ={}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("\n#5")
alien_0 = {'color': 'green'}
print(f"The alien is now {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

print("\n#6")
alien_0 = {'color': 'green', 'x_position': 0, 'y_position': 25, 
           'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}, {alien_0['y_position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
  x_increment = 1
  y_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
  y_increment = 2
else:
  x_increment = 3
  y_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment

print(f"New position: {alien_0['x_position']}, {alien_0['y_position']}")

print("\n#7")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print("\n#8")
point_value = alien_0.get('points', 'No points value')
print(point_value)
