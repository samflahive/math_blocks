import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.products import product
from math_blocks.exponentials import exponential

class exponential_product_test(unittest.TestCase):
    def test_fraction_latex(self):
        f = exponential(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.latex(), "-3^{2} \\cdot 2")
        pr2 = product([-f,2])
        self.assertEqual(pr2.latex(), "3^{2} \\cdot 2")

    def test_fraction_eval(self):
        f = exponential(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.evaluate(), -18)
        pr2 = product([-f,2])
        self.assertEqual(pr2.evaluate(), 18)

if __name__ == '__main__':
    unittest.main()
