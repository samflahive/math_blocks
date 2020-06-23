import unittest


from math_blocks.algebra.core import Fraction, Product, Chain

class block_fraction_test(unittest.TestCase):
    def test_block_latex(self):
        # test the latex expression for fractions with numbers only
        fr = Fraction(Chain([2,2]),Product([2,2], sign=False))
        self.assertEqual(fr.latex(), "\\frac{2+2}{-(2 \\cdot 2)}")

    def test_block_eval(self):
        fr = Fraction(Chain([2,2]),Product([2,2], sign=False))
        self.assertEqual(fr.evaluate(), -1)

    



if __name__ == '__main__':
    unittest.main()

