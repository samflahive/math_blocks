import unittest

from math_blocks.products import product
from math_blocks.fractions import fraction

class fraction_product_test(unittest.TestCase):
    def test_fraction_latex(self):
        f = fraction(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.latex(), "-\\frac{3}{2} \\cdot 2")
        pr2 = product([-f,2])
        self.assertEqual(pr2.latex(), "\\frac{3}{2} \\cdot 2")

    def test_fraction_eval(self):
        f = fraction(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.evaluate(), -3)
        pr2 = product([-f,2])
        self.assertEqual(pr2.evaluate(), 3)

if __name__ == '__main__':
    unittest.main()
