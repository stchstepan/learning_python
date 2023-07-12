print("\n#1")

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

class ElectroCar(Car):
    """Представляет аспекты машины, специфические для электрмобилей"""
    def __init__(self, make, model, year):
        """Ининциализирует аспекты машины, специфические для электрмобилей"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

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

    def update_odometr(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometr!")

    def increment_odometer(self, miles):
        self.odometr_reading += miles
    
    def fill_gas_tank(self):
        print("Please fill gas tank")

class ElectroCar(Car):
    """Представляет аспекты машины, специфические для электрмобилей"""
    def __init__(self, make, model, year):
        """Ининциализирует аспекты машины, специфические для электрмобилей"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_tesla.fill_gas_tank()

print("\n#3")

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

class ElectroCar(Car):
    """Представляет аспекты машины, специфические для электрмобилей"""
    def __init__(self, make, model, year):
        """Ининциализирует аспекты машины, специфические для электрмобилей"""
        super().__init__(make, model, year)
        self.battery = Baterry()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()

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

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectroCar(Car):
    """Представляет аспекты машины, специфические для электрмобилей"""
    def __init__(self, make, model, year):
        """Ининциализирует аспекты машины, специфические для электрмобилей"""
        super().__init__(make, model, year)
        self.battery = Baterry()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()