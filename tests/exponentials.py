import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.exponentials import exponential
from math_blocks.variables import variable


class basic_exponential(unittest.TestCase):
    def test_basic_latex(self):
        basic_exp_A = exponential(2,-3)
        self.assertEqual(basic_exp_A.latex(), "2^{-3}")
        basic_exp_B = exponential(4,2)
        self.assertEqual(basic_exp_B.latex(), "4^{2}")

    def test_variable_latex(self):
        x = variable("x")
        basic_exp_A = exponential(2,x, sign=False)
        self.assertEqual(basic_exp_A.latex(), "-2^{x}")

        y = variable("y", sign=False)
        basic_exp_B = exponential(y,2)
        self.assertEqual(basic_exp_B.latex(), "(-y)^{2}")

    def test_exponential_latex(self):
        exp1 = exponential(2,3)
        exp2 = exponential(exp1, 2)
        exp3 = exponential(exp1, exp2)

        self.assertEqual(exp3.latex(), "(2^{3})^{(2^{3})^{2}}")

    def test_basic_evaluation(self):
        basic_exp_A = exponential(2,-3)
        self.assertEqual(basic_exp_A.evaluate(), 2**-3)
        basic_exp_B = exponential(4,2)
        self.assertEqual(basic_exp_B.evaluate(), 4**2)

    def test_variable_evaluation(self):
        x = variable("x")
        x.value = 3
        basic_exp_A = exponential(2,x, sign=False)
        self.assertEqual(basic_exp_A.evaluate(), -(2**3))

        y = variable("y", sign=False)
        y.value = 2
        basic_exp_B = exponential(y,3)
        self.assertEqual(basic_exp_B.evaluate(), (-2)**3)


        
if __name__ == '__main__':
    unittest.main()
