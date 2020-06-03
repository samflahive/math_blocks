import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.complex_numbers import complex_number


class complex_complex_test(unittest.TestCase):
    def test_complex_latex(self):
        c1 = complex_number(3,2)
        c2 = complex_number(c1, c1)
        self.assertEqual(c2.latex(), "(3+2i)+(3+2i)i")

        c2 = complex_number(-3,2, sign=False)
        c1 = complex_number(c2, c2)
        self.assertEqual(c1.latex(), "(-(-3+2i))+(-(-3+2i))i")

    def test_complex_eval(self):
        c1 = complex_number(3,2)
        c2 = complex_number(c1, c1)
        self.assertEqual(c2.evaluate(), complex((3+2j),(3+2j)))

        c2 = complex_number(-3,2, sign=False)
        c1 = complex_number(c2, c2)
        self.assertEqual(c1.evaluate(), complex(-(-3+2j),-(-3+2j)))


if __name__ == '__main__':
    unittest.main()
