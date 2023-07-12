print("\n#1")

class Restareunt():
    def __init__(self, restareunt_name, cuisine_type):
        self.restareunt_name = restareunt_name
        self.cuisine_type = cuisine_type

    def describe_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is {self.cuisine_type}")

    def open_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is open now!")

pino = Restareunt('pino', 'italian')

pino.describe_restaraunt()
pino.open_restaraunt()

print("\n#2")

tehnikum = Restareunt('tehnikum', 'other')

tehnikum.describe_restaraunt()
tehnikum.open_restaraunt()

mushrooms = Restareunt('mushrooms', 'italian')

mushrooms.describe_restaraunt()
mushrooms.open_restaraunt()

print("\n#3")

class User():
    def __init__(self, f_n, l_n, age, city):
        self.f_n = f_n
        self.l_n = l_n
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"\n{self.f_n.title()} {self.l_n.title()} is {self.age} year old. {self.city.title()}.")

    def greet_user(self):
        print(f"Hello, {self.f_n.title()} {self.l_n.title()}")

stch_stepa = User('stepan', 'cherkashin', 21, 'moscow')

stch_stepa.describe_user()
stch_stepa.greet_user()

malevarr = User('ars', 'malev', 21, 'moscow')

malevarr.describe_user()
malevarr.greet_user()

afominskih = User('aleksandr', 'foma', 21, 'krasnoyarsk')

afominskih.describe_user()
afominskih.greet_user()