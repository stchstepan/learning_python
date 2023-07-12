from car import Car

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