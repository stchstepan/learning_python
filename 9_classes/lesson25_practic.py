print("\n#1")

class Restareunt():
    def __init__(self, restareunt_name, cuisine_type):
        self.restareunt_name = restareunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is {self.cuisine_type}")

    def open_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is open now!")

    def number_served_clients(self):
        print(f"Now served {self.number_served} clients")

pino = Restareunt('pino', 'italian')

pino.describe_restaraunt()
pino.open_restaraunt()

pino.number_served = 38
pino.number_served_clients()

print("\n#1.1")

class Restareunt():
    def __init__(self, restareunt_name, cuisine_type):
        self.restareunt_name = restareunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is {self.cuisine_type}")

    def open_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is open now!")

    def number_served_clients(self):
        print(f"Now served {self.number_served} clients")

    def set_number_served_clients(self, clients):
        self.number_served = clients

pino = Restareunt('pino', 'italian')

pino.describe_restaraunt()
pino.open_restaraunt()

pino.set_number_served_clients(42)
pino.number_served_clients()

print("\n#1.2")

class Restareunt():
    def __init__(self, restareunt_name, cuisine_type):
        self.restareunt_name = restareunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is {self.cuisine_type}")

    def open_restaraunt(self):
        print(f"The {self.restareunt_name.title()} is open now!")

    def number_served_clients(self):
        print(f"Now served {self.number_served} clients")

    def set_number_served_clients(self, clients):
        self.number_served = clients

    def increment_number_served_clients(self, new_clients):
        self.number_served += new_clients

pino = Restareunt('pino', 'italian')

pino.describe_restaraunt()
pino.open_restaraunt()

pino.set_number_served_clients(42)
pino.number_served_clients()

pino.increment_number_served_clients(20)
pino.number_served_clients()

print("\n#2")

class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is {self.age} year old. {self.city.title()}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

stch_stepa = User('stepan', 'cherkashin', 21, 'moscow')

stch_stepa.describe_user()
stch_stepa.greet_user()

stch_stepa.increment_login_attempts()
stch_stepa.increment_login_attempts()
stch_stepa.increment_login_attempts()
stch_stepa.increment_login_attempts()

stch_stepa.reset_login_attempts()