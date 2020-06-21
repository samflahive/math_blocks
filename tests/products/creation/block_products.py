import unittest

from math_blocks.algebra.core import Product, Chain

class block_product_test(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        pr = Product([Chain([2,2],sign=False),2])
        self.assertEqual(pr.latex(), "(-(2+2)) \\cdot 2")
        pr2 = Product([Chain([2,2]),2])
        self.assertEqual(pr2.latex(), "(2+2) \\cdot 2")

    def test_basic_eval(self):
        pr = Product([Chain([2,2],sign=False),2])
        self.assertEqual(pr.evaluate(), -8)
        pr2 = Product([Chain([2,2]),2])
        self.assertEqual(pr2.evaluate(), 8)

if __name__ == '__main__':
    unittest.main()

