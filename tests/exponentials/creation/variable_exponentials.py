import unittest

from math_blocks.exponentials import exponential
from math_blocks.variables import variable

class variable_exponential_test(unittest.TestCase):
    def test_variable_latex(self):
        x = variable("x")
        basic_exp_A = exponential(2,x, sign=False)
        self.assertEqual(basic_exp_A.latex(), "-2^{x}")

        y = variable("y", sign=False)
        basic_exp_B = exponential(y,2)
        self.assertEqual(basic_exp_B.latex(), "(-y)^{2}")

    def test_variable_evaluation(self):
        x = variable("x")
        x.value = 3
        basic_exp_A = exponential(2,x, sign=False)
        self.assertEqual(basic_exp_A.evaluate(), -(2**3))

        y = variable("y", sign=False)
        y.value = 2
        basic_exp_B = exponential(y,3)
        self.assertEqual(basic_exp_B.evaluate(), (-2)**3)

if __name__ == "__main__":
    unittest.main()
