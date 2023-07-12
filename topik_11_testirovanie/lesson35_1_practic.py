class Employee():
    def __init__(self, name, second, grade):
        self.name = name
        self.second = second
        self.grade = grade

    def give_raise(self, f_raise=5000):
        self.grade += f_raise
        return self.grade