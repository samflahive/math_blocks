import unittest

from math_blocks.algebra.core import Chain, Product, Number, Fraction

class block_chain_test(unittest.TestCase):
    def test_block_latex(self):
        ch = Chain([Number(3), -Fraction(3,2), Product([2,2])])
        self.assertEqual(ch.latex(), "3-\\frac{3}{2}+(2 \\cdot 2)")
        
        ch2 = -ch
        self.assertEqual(ch2.latex(), "-(3-\\frac{3}{2}+(2 \\cdot 2))")
        
    def test_block_eval(self):
        ch = Chain([Number(3), -Fraction(3,2), Product([2,2])])
        self.assertEqual(ch.evaluate(), 5.5)
        
        ch2 = -ch
        self.assertEqual(ch2.evaluate(), -5.5)


if __name__ == '__main__':
    unittest.main()

