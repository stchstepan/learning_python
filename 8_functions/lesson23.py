print("\n#1")

import pizza

pizza.make_pizza(22, 'pepperoni', 'pineapple', 'mushrooms', 'chees')

print("\n#2")

from pizza import make_pizza

make_pizza(22, 'pepperoni', 'pineapple', 'mushrooms', 'chees')

print("\n#3")

from pizza import make_pizza as mp

mp(22, 'pepperoni', 'pineapple', 'mushrooms', 'chees')

print("\n#4")

import pizza as p

p.make_pizza(22, 'pepperoni', 'pineapple', 'mushrooms', 'chees')

print("\n#5")

from pizza import *

pizza.make_pizza(22, 'pepperoni', 'pineapple', 'mushrooms', 'chees')