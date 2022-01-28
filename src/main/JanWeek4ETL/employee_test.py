from employee import Employee
import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Allen', 'Qian', 8800)
    def test_give_default_raise(self):
        self.employee.give_raise()
    def test_give_custom_raise(self):
        self.employee.give_raise(3000)
if __name__ == '__main__':
    unittest.main()