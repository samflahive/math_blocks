import unittest

from math_blocks.algebra.core import Number
from math_blocks.algebra.exponentials import Exponential


class exponential_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_ex = Exponential(1,2)
        n = Number(3)
        self.assertEqual(False, main_ex == n)


    def test_exp_eq(self):
        main_ex = Exponential(1,2)
        alt_fr = Exponential(1,2, sign=False)

        self.assertEqual(False, main_ex == alt_fr)
        self.assertEqual(True, main_ex == -alt_fr)
        
if __name__ == '__main__':
    unittest.main()
