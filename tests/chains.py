import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.chains import chain


class basic_product(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        ch = chain([3,2])
        self.assertEqual(ch.latex(), "3+2")
        ch2 = chain([-2,2])
        self.assertEqual(ch2.latex(), "-2+2")

    def test_basic_eval(self):
        ch = chain([3,2])
        self.assertEqual(ch.evaluate(), 5)
        ch2 = chain([-2,2])
        self.assertEqual(ch2.evaluate(), 0)

    def test_basic_addition(self):
        ch = chain([3,2])
        ch2 = ch + 4
        self.assertEqual(ch2.evaluate(), 9)
        self.assertEqual(ch2.latex(), "3+2+4")

        ch3 = chain([-3,2])
        ch4 = ch+ch3
        self.assertEqual(ch4.evaluate(), 4)
        self.assertEqual(ch4.latex(), "3+2+(-3+2)")

    def test_basic_subtraction(self):
        ch = chain([3,2])
        ch2 = ch - 4
        self.assertEqual(ch2.evaluate(), 1)
        self.assertEqual(ch2.latex(), "3+2-4")

        ch3 = chain([-3,2])
        ch4 = ch-ch3
        self.assertEqual(ch4.evaluate(), 4)
        self.assertEqual(ch4.latex(), "3+2-(-3+2)")
        
if __name__ == '__main__':
    unittest.main()
