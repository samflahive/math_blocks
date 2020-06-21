import unittest

from math_blocks.algebra.exponentials import Exponential


class basic_exponential_test(unittest.TestCase):
    def test_basic_latex(self):
        basic_exp_A = Exponential(2,-3)
        self.assertEqual(basic_exp_A.latex(), "2^{-3}")
        basic_exp_B = Exponential(4,2)
        self.assertEqual(basic_exp_B.latex(), "4^{2}")

    def test_basic_eval(self):
        basic_exp_A = Exponential(2,-3)
        self.assertEqual(basic_exp_A.evaluate(), 2**(-3))
        basic_exp_B = Exponential(4,2)
        self.assertEqual(basic_exp_B.evaluate(), 4**(2))    

if __name__ == "__main__":
    unittest.main()
