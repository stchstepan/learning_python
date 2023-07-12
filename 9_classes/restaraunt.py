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