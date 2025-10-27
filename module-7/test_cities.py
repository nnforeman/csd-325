# test_cities.py
# CSD-325 Module 7
# Author: Natasha Foreman

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        """Does city_country('santiago', 'chile') return 'Santiago, Chile'?"""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
