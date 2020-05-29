import unittest
from math import log
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

from math_blocks.logarithms import logarithm
from math_blocks.exponentials import exponential


class exponential_logarithm_test(unittest.TestCase):
    def test_exponential_latex(self):
        f1 = exponential(3, 2)
        loga = logarithm(f1, 3)
        self.assertEqual(loga.latex(), "log_{3}3^{2}")
        logb = logarithm(f1,f1)
        self.assertEqual(logb.latex(), "log_{3^{2}}3^{2}")

    def test_exponential_eval(self):
        f1 = exponential(3, 2)
        loga = logarithm(f1, 3)
        self.assertEqual(loga.evaluate(), 2)
        logb = logarithm(f1,f1)
        self.assertEqual(logb.evaluate(), 1.0)


if __name__ == '__main__':
    unittest.main()
