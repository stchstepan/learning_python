print("\n#1")

class Dog():
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('tema', 6)

print(f"My dog's name {my_dog.name.title()}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 6)

print(f"\nYour dog's name {your_dog.name.title()}")
print(f"My dog is {your_dog.age} years old")

your_dog.sit()
your_dog.roll_over()
