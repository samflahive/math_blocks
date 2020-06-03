import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.complex_numbers import complex_number
from math_blocks.fractions import fraction


class fraction_complex_test(unittest.TestCase):
    def test_fraction_latex(self):
        f1 = fraction(3,2)
        c1 = complex_number(f1,f1)
        self.assertEqual(c1.latex(), "(\\frac{3}{2})+(\\frac{3}{2})i")

        f2 = fraction(-3,2, sign=False)
        c1 = complex_number(f2, f2)
        self.assertEqual(c1.latex(), "(-\\frac{-3}{2})+(-\\frac{-3}{2})i")

    def test_fraction_eval(self):
        f1 = fraction(3,2)
        c1 = complex_number(f1,f1)
        self.assertEqual(c1.evaluate(), 3/2+(3j)/2)

        f2 = fraction(-3,2, sign=False)
        c1 = complex_number(f2, f2)
        self.assertEqual(c1.evaluate(), 3/2+(3j)/2)


if __name__ == '__main__':
    unittest.main()
