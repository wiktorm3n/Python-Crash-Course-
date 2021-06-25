import unittest
from tryit11_3 import Employee

class Test_tryit11_3(unittest.TestCase):
    def test_give_default_raise(self):
        annaul_raise = Employee('Wiktor','Maluha','')
        annaul_raise.give_raise()
    def test_give_custom_raise(self):
        custom_raise = Employee('Wiktor','Mahala',6900)
        custom_raise.give_raise()
if __name__ == '__main__':
    unittest.main()