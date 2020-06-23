import unittest

from math_blocks.algebra.exponentials import Logarithm
from math_blocks.algebra.core import Number


class logarithm_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_lg = Logarithm(1,2)
        n = Number(3)
        self.assertEqual(False, main_lg == n)


    def test_exp_eq(self):
        main_lg = Logarithm(1,2)
        alt_fr = Logarithm(1,2, sign=False)

        self.assertEqual(False, main_lg == alt_fr)
        self.assertEqual(True, main_lg == -alt_fr)
        
if __name__ == '__main__':
    unittest.main()
