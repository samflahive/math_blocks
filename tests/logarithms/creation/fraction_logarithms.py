import unittest
from math import log

from math_blocks.logarithms import logarithm
from math_blocks.fractions import fraction


class fraction_logarithm_test(unittest.TestCase):
    def test_fraction_latex(self):
        f1 = fraction(3,2)
        f2 = fraction(-3,2, sign=False)
        loga = logarithm(f1,f2)
        self.assertEqual(loga.latex(), "log_{-\\frac{-3}{2}}\\frac{3}{2}")

    def test_fraction_eval(self):
        f1 = fraction(3,2)
        f2 = fraction(-3,2, sign=False)
        loga = logarithm(f1,f2)
        self.assertEqual(loga.evaluate(), 1)


if __name__ == '__main__':
    unittest.main()
