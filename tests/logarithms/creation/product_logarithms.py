import unittest
from math import log
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.logarithms import logarithm
from math_blocks.products import product

class product_logarithm_test(unittest.TestCase):
    def test_product_latex(self):
        loga = logarithm(2,product([1,2]))
        self.assertEqual(loga.latex(), "log_{1 \\cdot 2}2")

    def test_product_eval(self):
        loga = logarithm(2,product([1,2]))
        self.assertEqual(loga.evaluate(), 1)


if __name__ == '__main__':
    unittest.main()
