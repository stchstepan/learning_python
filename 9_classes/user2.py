from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ['Разрешено добавлять сообщения', 'Разрешено банить пользователей', 
                    'Разрешено удалять пользователей и сообщения']

    def show_privileges(self):
        print("Твои привелегии: ")
        for privilege in self.privileges:
            print(f"-{privilege}")