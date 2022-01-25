import unittest
"""使用测试样例,方法必须要test打头"""
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    """测试name_funciton.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('janis','joplin','victor')
        self.assertEqual(formatted_name,'Janis Victor Joplin')
if __name__ == '__main__':
    unittest.main()


