import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.exponentials import exponential
from math_blocks.products import product

class product_exponential_test(unittest.TestCase):
    def test_product_latex(self):
        basic_exp_A = exponential(2,-product([-3,2]))
        self.assertEqual(basic_exp_A.latex(), "2^{-(-3 \\cdot 2)}")
        basic_exp_B = exponential(product([2,2]),2)
        self.assertEqual(basic_exp_B.latex(), "(2 \\cdot 2)^{2}")

    def test_product_eval(self):
        basic_exp_A = exponential(2,-product([-3,2]))
        self.assertEqual(basic_exp_A.evaluate(), 2**(6))
        basic_exp_B = exponential(product([2,2]), 2)
        self.assertEqual(basic_exp_B.evaluate(), 16)   

if __name__ == "__main__":
    unittest.main()
