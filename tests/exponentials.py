import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.exponentials import exponential


class basic_exponential(unittest.TestCase):
    def test_basic_latex(self):
        basic_exp_A = exponential(2,-3)
        self.assertEqual(basic_exp_A.latex(), "2^{-3}")
        basic_exp_B = exponential(4,2)
        self.assertEqual(basic_exp_B.latex(), "4^{2}")

    def test_basic_evaluation(self):
        basic_exp_A = exponential(2,-3)
        self.assertEqual(basic_exp_A.evaluate(), 2**-3)
        basic_exp_B = exponential(4,2)
        self.assertEqual(basic_exp_B.evaluate(), 4**2)

    def test_basic_operations(self):
        # multiplying exponentials (same base)
        basic_exp_A = exponential(2,-3)
        basic_exp_B = exponential(2,2)
        basic_exp_C = basic_exp_A*basic_exp_B
        self.assertEqual(basic_exp_C.evaluate(), 2**-1)
        self.assertEqual(basic_exp_C.latex(), "2^{-1}")

        # dividing exponentials (same base)
        basic_exp_D = basic_exp_B / basic_exp_A
        self.assertEqual(basic_exp_D.evaluate(), 2**5)
        self.assertEqual(basic_exp_D.latex(), "2^{5}")

        # adding and subtracting exponentials
        exp_sum = basic_exp_A + basic_exp_B - basic_exp_C
        self.assertEqual(exp_sum.latex(), "2^{-3}+4^{8}-2^{-1}")
        self.assertEqual(exp_sum.evaluate(), 2**-3 + 4**2 - 2**-1)

        # multiplying exponential and number
        exp_prod = basic_exp_D * 2
        self.assertEqual(exp_prod.evaluate(), 2**6)
        self.assertEqual(exp_prod.latex(), "2^{5} \cdot 2")

        # dividing exponential and number
        exp_frac = basic_exp_D / 3
        self.assertEqual(exp_frac.latex(), "\frac{2^{5}}{3}")
        self.assertEqual(exp_frac.evaluate(), 2**5 / 3)

        
if __name__ == '__main__':
    unittest.main()
