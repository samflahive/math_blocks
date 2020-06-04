import unittest

from math_blocks.products import product
from math_blocks.logarithms import logarithm

from math import log

class logarithm_product_test(unittest.TestCase):
    def test_logarithm_latex(self):
        f = logarithm(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.latex(), "-log_{2}3 \\cdot 2")
        pr2 = product([-f,2])
        self.assertEqual(pr2.latex(), "log_{2}3 \\cdot 2")

    def test_logarithm_eval(self):
        f = logarithm(3,2,sign=False)
        pr = product([f,2])
        self.assertEqual(pr.evaluate(), -2*log(3,2))
        pr2 = product([-f,2])
        self.assertEqual(pr2.evaluate(), 2*log(3,2))

if __name__ == '__main__':
    unittest.main()
