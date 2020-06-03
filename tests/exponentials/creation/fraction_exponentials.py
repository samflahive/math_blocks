import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.exponentials import exponential
from math_blocks.fractions import fraction

class fraction_exponential_test(unittest.TestCase):
    def test_fraction_latex(self):
        exp1 = exponential(fraction(3,2),3)
        exp2 = exponential(2, -fraction(3,2))

        self.assertEqual(exp1.latex(), "(\\frac{3}{2})^{3}")
        self.assertEqual(exp2.latex(), "2^{-\\frac{3}{2}}")

    def test_fraction_evaluation(self):
        exp1 = exponential(fraction(3,2),3)
        exp2 = exponential(2, -fraction(3,2))

        self.assertEqual(exp1.evaluate(), (3/2)**3)
        self.assertEqual(exp2.evaluate(), 2**(-3/2))

if __name__ == "__main__":
    unittest.main()
