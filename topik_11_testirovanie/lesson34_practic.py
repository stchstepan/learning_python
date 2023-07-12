print("\n#1")

import unittest
from lesson34_1_practic import city_country

#formatted_city_country = city_country('msc', 'russia')
#print(formatted_city_country)

#class CityCountryTestCase(unittest.TestCase):
    #def test_city_country(self):
        #formatted_city_country = city_country('msc', 'russia')
        #self.assertEqual(formatted_city_country, 'Msc, Russia')

#if __name__ == '__main__':
    #unittest.main()

print("\n#2")

formatted_city_country = city_country('msc', 'russia')
print(formatted_city_country)

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country('msc', 'russia')
        self.assertEqual(formatted_city_country, 'Msc, Russia')
    
    def test_city_country_population(self):
        formatted_city_country = city_country('msc', 'russia', 10000000)
        self.assertEqual(formatted_city_country, 'Msc, Russia - population 10000000')

if __name__ == '__main__':
    unittest.main()