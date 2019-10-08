import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.products import product


class basic_product(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        pr = product([3,2])
        self.assertEqual(pr.latex(), "3 \\cdot 2")
        pr2 = product([-2,2])
        self.assertEqual(pr2.latex(), "-2 \\cdot 2")

    def test_basic_eval(self):
        pr = product([3,2])
        self.assertEqual(pr.evaluate(), 6)
        pr2 = product([-2,2])
        self.assertEqual(pr2.evaluate(), -4)




if __name__ == '__main__':
    unittest.main()
