import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.products import product
from math_blocks.complex_numbers import complex_number


class complex_product_test(unittest.TestCase):
    def test_complex_latex(self):
        f = complex_number(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.latex(), "(-(3+2i)) \\cdot 2")
        pr2 = product([-f,2])
        self.assertEqual(pr2.latex(), "(3+2i) \\cdot 2")

    def test_complex_eval(self):
        f = complex_number(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.evaluate(), -6-4j)
        pr2 = product([-f,2])
        self.assertEqual(pr2.evaluate(), 6+4j)

if __name__ == '__main__':
    unittest.main()
