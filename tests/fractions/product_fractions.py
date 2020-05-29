import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))

from math_blocks.fractions import fraction
from math_blocks.products import product

class product_fraction_test(unittest.TestCase):
    def test_product_latex(self):
        fr = fraction(product([3,1]),2)
        self.assertEqual(fr.latex(), "\\frac{3 \\cdot 1}{2}")
        fr2 = fraction(1,-product([-2,2]), sign=False)
        self.assertEqual(fr2.latex(), "-\\frac{1}{-(-2 \\cdot 2)}")

    def test_product_eval(self):
        fr = fraction(product([3,1]),2)
        self.assertEqual(fr.evaluate(), 1.5)
        fr2 = fraction(1,-product([-2,3]), sign=False)
        self.assertEqual(fr2.evaluate(), 1/6)

    



if __name__ == '__main__':
    unittest.main()
