print("\n#1")

from restaraunt import Restareunt

pino = Restareunt('pino', 'italian')

pino.describe_restaraunt()
pino.open_restaraunt()
pino.number_served = 38
pino.number_served_clients()

print("\n#2")

#from user import User, Admin 

#stch_stepa = User('stepan', 'cherkashin', 21, 'moscow')

#stch_stepa.describe_user()
#stch_stepa.greet_user()

#stch_stepa.increment_login_attempts()
#stch_stepa.increment_login_attempts()
#stch_stepa.increment_login_attempts()
#stch_stepa.increment_login_attempts()

#stch_stepa.reset_login_attempts()

#stch_stepa = Admin('stepan', 'cherkashin', 21, 'msc')

#stch_stepa.describe_user()
#stch_stepa.greet_user()

#stch_stepa.show_privileges()

print("\n#3")

from user2 import Admin 

stch_stepa = Admin('stepan', 'cherkashin', 21, 'msc')

stch_stepa.describe_user()
stch_stepa.greet_user()

stch_stepa.show_privileges()