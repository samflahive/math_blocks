import unittest

from math_blocks.exponentials import exponential
from math_blocks.variables import variable

class exponential_exponential_test(unittest.TestCase):
    def test_exponential_latex(self):
        exp1 = exponential(2,3)
        exp2 = exponential(exp1, 2)
        exp3 = exponential(exp1, exp2)

        self.assertEqual(exp3.latex(), "(2^{3})^{(2^{3})^{2}}")

    def test_exponential_evaluation(self):
        basic_exp_A = exponential(2,-3)
        self.assertEqual(basic_exp_A.evaluate(), 2**-3)
        basic_exp_B = exponential(4,2)
        self.assertEqual(basic_exp_B.evaluate(), 4**2)

if __name__ == "__main__":
    unittest.main()
