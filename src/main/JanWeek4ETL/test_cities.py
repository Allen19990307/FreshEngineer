import unittest
"""书写自动化测试的脚本"""
from city_functions import name
class test_cities(unittest.TestCase):
    def test_city_country(self):
        name1 = name('San Francisco', 'USA','')
        self.assertEqual(name1,'San Francisco,USA')
    def test_city_country_population(self):
        name1 = name('San Francisco', 'USA','397w')
        self.assertEqual(name1,'San Francisco,USA-population 397w')
if __name__ == '__main__':
    unittest.main