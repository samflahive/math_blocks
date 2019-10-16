import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from math_blocks.fractions import fraction


class basic_fraction(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        fr = fraction(3,2)
        self.assertEqual(fr.latex(), "\\frac{3}{2}")
        fr2 = fraction(-2,2)
        self.assertEqual(fr2.latex(), "\\frac{-2}{2}")

    def test_basic_eval(self):
        fr = fraction(3,2)
        self.assertEqual(fr.evaluate(), 1.5)
        fr2 = fraction(-2,2)
        self.assertEqual(fr2.evaluate(), -1)

    def test_basic_addition(self):
        fr = fraction(3,2)
        fr2 = fr + 4
        self.assertEqual(fr2.evaluate(), 5.5)
        self.assertEqual(fr2.latex(), "\\frac{3}{2}+4")

        fr3 = fraction(-3,2)
        fr4 = fr+fr3
        self.assertEqual(fr4.evaluate(), 0)
        self.assertEqual(fr4.latex(), "\\frac{0}{2}")

    def test_basic_subtraction(self):
        fr = fraction(3,2)
        fr2 = fr - 4
        self.assertEqual(fr2.evaluate(), -2.5)
        self.assertEqual(fr2.latex(), "\\frac{3}{2}-4")

        fr3 = fraction(-3,2)
        fr4 = fr-fr3
        self.assertEqual(fr4.evaluate(), 3)
        self.assertEqual(fr4.latex(), "\\frac{6}{2}")

    def test_basic_multiplication(self):
        fr = fraction(3,2)
        fr2 = fr * 4
        self.assertEqual(fr2.evaluate(), 6)
        self.assertEqual(fr2.latex(), "\\frac{12}{2}")

        fr3 = fraction(-3,2)
        fr4 = fr*fr3
        self.assertEqual(fr4.evaluate(), -9/4)
        self.assertEqual(fr4.latex(), "\\frac{-9}{4}")

    def test_basic_division(self):
        fr = fraction(3,2)
        fr2 = fr / 4
        self.assertEqual(fr2.evaluate(), 3/8)
        self.assertEqual(fr2.latex(), "\\frac{3}{8}")

        fr3 = fraction(-3,2)
        fr4 = fr/fr3
        self.assertEqual(fr4.evaluate(), -1)
        self.assertEqual(fr4.latex(), "\\frac{3}{\\frac{-6}{2}}")



if __name__ == '__main__':
    unittest.main()
