print("\n#1")

from car import Car

my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.odometr_reading = 23
my_new_car.read_odometr()

print("\n#2")

from car import ElectroCar

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n#3")

from car import Car, ElectroCar

from car import Car

my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.odometr_reading = 23
my_new_car.read_odometr()

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n#4")

import car

my_new_car = car.Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.odometr_reading = 23
my_new_car.read_odometr()

my_tesla = car.ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n#5")

from car import Car
from electro_car import ElectroCar

my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.odometr_reading = 23
my_new_car.read_odometr()

my_tesla = ElectroCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n#6")

from electro_car import ElectroCar as EC

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
