import unittest

from math_blocks.exponentials import exponential
from math_blocks.logarithms import logarithm
from math import log

class logarithm_exponential_test(unittest.TestCase):
    def test_logarithm_latex(self):
        basic_exp_A = exponential(3,logarithm(9,3))
        self.assertEqual(basic_exp_A.latex(), "3^{log_{3}9}")
        basic_exp_B = exponential(-logarithm(9,3),2)
        self.assertEqual(basic_exp_B.latex(), "(-log_{3}9)^{2}")

    def test_logarithm_eval(self):
        basic_exp_A = exponential(3,logarithm(9,3))
        self.assertEqual(basic_exp_A.evaluate(), 9)
        
        basic_exp_B = exponential(-logarithm(9,3),2)
        self.assertEqual(basic_exp_B.evaluate(), 4)    


if __name__ == "__main__":
    unittest.main()
