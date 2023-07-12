#25 practic, num 2

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
        if self.login_attempts < 3:
            self.login_attempts += 1
            print(self.login_attempts)
        else:
            print("Prove your person!")

    
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