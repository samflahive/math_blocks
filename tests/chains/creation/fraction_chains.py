import unittest

from math_blocks.chains import chain
from math_blocks.fractions import fraction


class fraction_chain_test(unittest.TestCase):
    def test_fraction_latex(self):
        ch = chain([3,fraction(3,2)])
        self.assertEqual(ch.latex(), "3+\\frac{3}{2}")
        
        ch2 = chain([-2, fraction(3, 2, sign=False)])
        self.assertEqual(ch2.latex(), "-2-\\frac{3}{2}")

        ch3 = chain([fraction(3, 2, sign=False),fraction(3, 2, sign=False)])
        self.assertEqual(ch3.latex(), "-\\frac{3}{2}-\\frac{3}{2}")
        
    def test_fraction_eval(self):
        ch = chain([3,fraction(3,2)])
        self.assertEqual(ch.evaluate(), 4.5)
        
        ch2 = chain([-2, fraction(3, 2, sign=False)])
        self.assertEqual(ch2.evaluate(), -3.5)

        ch3 = chain([fraction(3, 2, sign=False),fraction(3, 2, sign=False)])
        self.assertEqual(ch3.evaluate(), -3)


if __name__ == '__main__':
    unittest.main()
