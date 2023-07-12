print("\n#1")

from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def change (self, new_sides):
        self.sides = new_sides

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)

one = Die()
one.roll_die()

two = Die()
two.roll_die()

three = Die()
three.roll_die()

four = Die()
four.roll_die()

five= Die()
five.roll_die()

six= Die()
six.roll_die()

seven = Die()
seven.roll_die()

eight= Die()
eight.roll_die()

nine = Die()
nine.roll_die()

ten = Die()
ten.roll_die()

print("#1.1")

one = Die()
one.change(10)
one.roll_die()

two = Die()
two.change(10)
two.roll_die()

three = Die()
three.change(10)
three.roll_die()

four = Die()
four.change(10)
four.roll_die()

five = Die()
five.change(10)
five.roll_die()

six = Die()
six.change(10)
six.roll_die()

one = Die()
one.change(10)
one.roll_die()

seven = Die()
seven.change(10)
seven.roll_die()

eight = Die()
eight.change(10)
eight.roll_die()

nine = Die()
nine.change(10)
nine.roll_die()

ten = Die()
ten.change(10)
ten.roll_die()

print("\n#2")

from random import choice

def win_lotery(ticket):
    win = []
    while len(win) < 4:
        symbol = choice(ticket)
        win.append(symbol)
    print(f"Winers ticket is {win}")
    return win

lotery = ['1', '2', '3', '4', '5', '6' , '7', '8', '9', '10,', 'q', 'w' , 'e', 'r', 't']

win_lotery(lotery)

print("\n#3")

from random import choice

def win_lotery(ticket):
    win = []
    while len(win) < 4:
        symbol = choice(ticket)
        win.append(symbol)
    print(f"Winers ticket is {win}")
    return win

lotery = ['1', '2', '3', '4', '5', '6' , '7', '8', '9', '10,', 'q', 'w' , 'e', 'r', 't']

my_ticket = ['q', '5', 'w', '4']

sum = 0

while True:
    if my_ticket == win_lotery(lotery):
        print(f"\n{sum}")
        print("you win!")
        break
    sum += 1
    print(f"\n{sum}") 