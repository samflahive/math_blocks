import unittest

from math_blocks.algebra.core import Fraction, Chain, Product
from math_blocks.algebra.exponentials import ComplexNumber

class split_fraction_test(unittest.TestCase):
    def test_chain_split(self):
        ch = Chain([3,2], sign=False)
        f = Fraction(ch, 2, False)
        
        split = f.split()
        
        self.assertEqual(split.latex(), "-(-\\frac{3}{2}-\\frac{2}{2})")
        
        split2 = (-f).split()
        self.assertEqual(split2.latex(), "-\\frac{3}{2}-\\frac{2}{2}")

        self.assertEqual(split.ripple_sign().latex(), "\\frac{3}{2}+\\frac{2}{2}")

    def test_product_split(self):
        ch = Product([3,2], sign=False)
        f = Fraction(ch, 2, False)
        
        split = f.split()
        
        self.assertEqual(split.latex(), "-(-\\frac{3}{2} \\cdot -\\frac{2}{2})")
        
        split = (-f).split()
        self.assertEqual(split.latex(), "-\\frac{3}{2} \\cdot -\\frac{2}{2}")

    def test_complex_split(self):
        ch = ComplexNumber(3,2, sign=False) # -(3+2i)
        f = Fraction(ch, 2, False) # -(-(3+2i)/2)
        
        split = f.split() # -((-3/2)-(2/2)i)
        
        self.assertEqual(split.latex(), "-((-\\frac{3}{2})+(-\\frac{2}{2})i)")
        
       


if __name__ == '__main__':
    unittest.main()
