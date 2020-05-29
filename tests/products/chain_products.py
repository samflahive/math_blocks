import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.products import product
from math_blocks.chains import chain

class chain_product_test(unittest.TestCase):
    def test_chain_latex(self):
        pr = product([chain([3,2]),2])
        self.assertEqual(pr.latex(), "(3+2) \\cdot 2")
        pr2 = product([-2,-chain([3,-2])])
        self.assertEqual(pr2.latex(), "-2 \\cdot (-(3+(-2)))")

    def test_chain_eval(self):
        pr = product([chain([3,2]),2])
        self.assertEqual(pr.evaluate(), 10)
        pr2 = product([-2,-chain([3,-2])])
        self.assertEqual(pr2.evaluate(), 2)

if __name__ == '__main__':
    unittest.main()
