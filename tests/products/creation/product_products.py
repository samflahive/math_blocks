import unittest

from math_blocks.products import product

class product_product_test(unittest.TestCase):
    def test_product_latex(self):
        pr = product([product([3,2]),2])
        self.assertEqual(pr.latex(), "3 \\cdot 2 \\cdot 2")
        pr2 = product([-2,-product([3,-2])])
        self.assertEqual(pr2.latex(), "-2 \\cdot -(3 \\cdot -2)")

    def test_product_eval(self):
        pr = product([product([3,2]),2])
        self.assertEqual(pr.evaluate(), 12)
        pr2 = product([-2,-product([3,-2])])
        self.assertEqual(pr2.evaluate(), -12)

if __name__ == '__main__':
    unittest.main()
