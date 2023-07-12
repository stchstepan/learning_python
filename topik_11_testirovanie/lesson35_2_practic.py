import unittest
from lesson35_1_practic import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        name = "Stepan"
        second = "Cherkashin"
        grade = 60000
        self.me_employee = Employee(name, second, grade)

    def test_default_give_raise(self):
        default_give_raise = self.me_employee.give_raise()
        self.assertEqual(default_give_raise, 65000)

    def test_custom_give_raise(self):
        custom_give_raise = self.me_employee.give_raise(10000)
        self.assertEqual(custom_give_raise, 70000)
        
if __name__ == '__main__':
    unittest.main()