print("#1")

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

class IceCreamStand(Restareunt):
    def __init__(self, restareunt_name, cuisine_type):
        super().__init__(restareunt_name, cuisine_type)

    def assortiment_flavors(self, flavors):
        print("We have following flavors:")
        for flavor in flavors:
            print(f"-{flavor}")
            

pino = Restareunt('pino', 'italian')

pino.describe_restaraunt()
pino.open_restaraunt()
pino.number_served = 38
pino.number_served_clients()

flavors = ['vanil', 'chokolate', 'eskimo']

baskin_robins = IceCreamStand('Baskin robins', 'american')
baskin_robins.describe_restaraunt()
baskin_robins.open_restaraunt()
baskin_robins.assortiment_flavors(flavors)

print("#2")

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

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ['Разрешено добавлять сообщения', 'Разрешено банить пользователей', 
                    'Разрешено удалять пользователей и сообщения']

    def show_privileges(self):
        print("Твои привелегии: ")
        for privilege in self.privileges:
            print(f"-{privilege}")

            

stch_stepa = User('stepan', 'cherkashin', 21, 'moscow')

stch_stepa.describe_user()
stch_stepa.greet_user()

stch_stepa.increment_login_attempts()
stch_stepa.increment_login_attempts()
stch_stepa.increment_login_attempts()
stch_stepa.increment_login_attempts()

stch_stepa.reset_login_attempts()


stch_stepa = Admin('stepan', 'cherkashin', 21, 'msc')

stch_stepa.describe_user()
stch_stepa.greet_user()

stch_stepa.show_privileges()

print("\n#3")

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

class Privileges():
    def __init__(self):
        self.privileges = ['Разрешено добавлять сообщения', 'Разрешено банить пользователей', 
                    'Разрешено удалять пользователей и сообщения']

    def show_privileges(self):
        print("Твои привелегии: ")
        for privilege in self.privileges:
            print(f"-{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

stch_stepa = Admin('stepan', 'cherkashin', 21, 'msc')

stch_stepa.describe_user()
stch_stepa.greet_user()

stch_stepa.privileges.show_privileges()

print("\n#4")

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return(long_name)

    def read_odometr(self):
        print(f"This car {self.odometr_reading} miles on it")

    def update_odometr(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometr!")

    def increment_odometer(self, miles):
        self.odometr_reading += miles
    
    def fill_gas_tank(self):
        print("Please fill gas tank")

class Baterry():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def change_battery_size(self, kwh):
        self.battery_size = kwh

    def get_range(self):
        if self.battery_size == 75:
            self.battery_size = 75
            range = 260
        elif self.battery_size == 100:
            self.battery_size = 100
            range = 315
        elif self.battery_size > 100:
            self.battery_size = 100
            range = 315
        elif self.battery_size > 75:
            self.battery_size = 75
            range = 260
        elif self.battery_size < 75:
            self.battery_size = 75
            range = 260
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectroCar(Car):
    """Представляет аспекты машины, специфические для электрмобилей"""
    def __init__(self, make, model, year):
        """Ининциализирует аспекты машины, специфические для электрмобилей"""
        super().__init__(make, model, year)
        self.battery = Baterry()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

tesla = ElectroCar('tesla', 'roadster', 2008)

print(tesla.get_descriptive_name())
tesla.battery.change_battery_size(200)
tesla.battery.get_range()