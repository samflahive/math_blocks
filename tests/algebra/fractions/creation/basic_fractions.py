import unittest


from math_blocks.algebra.core import Fraction

class basic_fraction_test(unittest.TestCase):
    def test_basic_latex(self):
        # test the latex expression for fractions with numbers only
        fr = Fraction(3,2)
        self.assertEqual(fr.latex(), "\\frac{3}{2}")
        fr2 = Fraction(-2,2, sign=False)
        self.assertEqual(fr2.latex(), "-\\frac{-2}{2}")

    def test_basic_eval(self):
        fr = Fraction(3,2)
        self.assertEqual(fr.evaluate(), 1.5)
        fr2 = Fraction(-2,2, sign=False)
        self.assertEqual(fr2.evaluate(), 1)

    



if __name__ == '__main__':
    unittest.main()
