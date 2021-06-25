import unittest
from unittest.main import main
from city_functions import city_country

class Test_city_country(unittest.TestCase):
    def test_city_country(self):
        test = city_country('santiago','chile',)
        self.assertEqual(test, 'Santiago, Chile')
if __name__ == '__main__':
    unittest.main()

Test_city_country()
