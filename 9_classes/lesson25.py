print("\n#1")

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return(long_name)

my_car = Car('bmw', '320d', 2021)
print(my_car.get_descriptive_name())

print("\n#2")

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

my_car = Car('bmw', '320d', 2021)
print(my_car.get_descriptive_name())
my_car.read_odometr()

print("\n#3")

my_car.odometr_reading = 23
my_car.read_odometr()

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
        self.odometr_reading = mileage

my_car = Car('bmw', '320d', 2021)
my_car.update_odometr(23)
my_car.read_odometr()

print("\n#4.1")

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

my_car = Car('bmw', '320d', 2021)
my_car.update_odometr(22)
my_car.read_odometr()

print("\n#5")

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

my_used_car = Car('mazda', 'axela', 2018)

print(my_used_car.get_descriptive_name())

my_used_car.read_odometr()

my_used_car.update_odometr(1000)
my_used_car.read_odometr()

my_used_car.increment_odometer(200)
my_used_car.read_odometr()