import unittest

import math_blocks

class split_fraction_test(unittest.TestCase):
    def test_chain_split(self):
        ch = math_blocks.chain([3,2], sign=False)
        f = math_blocks.fraction(ch, 2, False)
        
        split = f.split()
        
        self.assertEqual(split.latex(), "-(-\\frac{3}{2}-\\frac{2}{2})")
        
        split2 = (-f).split()
        self.assertEqual(split2.latex(), "-\\frac{3}{2}-\\frac{2}{2}")

        self.assertEqual(split.ripple_sign().latex(), "\\frac{3}{2}+\\frac{2}{2}")

    def test_product_split(self):
        ch = math_blocks.product([3,2], sign=False)
        f = math_blocks.fraction(ch, 2, False)
        
        split = f.split()
        
        self.assertEqual(split.latex(), "-(-\\frac{3}{2} \\cdot -\\frac{2}{2})")
        
        split = (-f).split()
        self.assertEqual(split.latex(), "-\\frac{3}{2} \\cdot -\\frac{2}{2}")

    def test_product_split(self):
        ch = math_blocks.simple_poly([3,2,1], math_blocks.variable("x"), sign=False)
        f = math_blocks.fraction(ch, 2, False)
        
        split = f.split()
        
        self.assertEqual(split.latex(), "-(-\\frac{3x^{2}}{2}-\\frac{2x}{2}-\\frac{1}{2})")
        
        split = (-f).split()
        self.assertEqual(split.latex(), "-\\frac{3x^{2}}{2}-\\frac{2x}{2}-\\frac{1}{2}")

    def test_complex_split(self):
        ch = math_blocks.complex_number(3,2, sign=False)
        f = math_blocks.fraction(ch, 2, False)
        
        split = f.split()
        
        self.assertEqual(split.latex(), "(\\frac{3}{2})+(\\frac{2}{2})i")
        
        split = (-f).split()
        self.assertEqual(split.latex(), "-((\\frac{3}{2})+(\\frac{2}{2})i)")        


if __name__ == '__main__':
    unittest.main()
