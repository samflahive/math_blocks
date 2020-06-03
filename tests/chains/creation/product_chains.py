import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain
from math_blocks.products import product

class product_chain_test(unittest.TestCase):
    def test_product_latex(self):
        ch = chain([3, product([-3,2])])
        self.assertEqual(ch.latex(), "3+(-3 \\cdot 2)")
        
        ch2 = chain([-2, product([-3,2])])
        self.assertEqual(ch2.latex(), "-2+(-3 \\cdot 2)")

        ch3 = chain([-2, -product([3,2])])
        self.assertEqual(ch3.latex(), "-2-(3 \\cdot 2)")
        
    def test_product_eval(self):
        ch = chain([3, product([-3,2])])
        self.assertEqual(ch.evaluate(), -3)
        
        ch2 = chain([-2, product([-3,2])])
        self.assertEqual(ch2.evaluate(), -8)

        ch3 = chain([-2, -product([3,2])])
        self.assertEqual(ch3.evaluate(), -8)


if __name__ == '__main__':
    unittest.main()
