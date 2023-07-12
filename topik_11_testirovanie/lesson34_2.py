print("\n#1")

from lesson34_1 import get_formated_name

print("If you want to stop - enter 'q' anytime")
while True:
    first = input("First: ")
    if first == 'q':
        break
    last = input("Second: ")
    if last == 'q':
        break

    formated_name = get_formated_name(first, last)
    print(f"Formated name is: {formated_name}")

print("\n#2")

#import unittest
#from lesson34_1 import get_formated_name

#class NamesTestsCase(unittest.TestCase):

    #def test_first_last_name(self):
        #formated_name = get_formated_name('stepan', 'cherkshin')
        #self.assertEqual(formated_name, 'Stepan Cherkshin')

#if __name__ == '__main__':
    #unittest.main()

print("\n#3")

import unittest
from lesson34_1 import get_formated_name

class NamesTestsCase(unittest.TestCase):

    def test_first_last_name(self):
        formated_name = get_formated_name('stepan', 'cherkshin')
        self.assertEqual(formated_name, 'Stepan Cherkshin')

    def test_first_last_second_name(self):
        formated_name = get_formated_name('stepan', 'cherkshin', 'nikitich')
        self.assertEqual(formated_name, 'Cherkshin Stepan Nikitich')

if __name__ == '__main__':
    unittest.main()