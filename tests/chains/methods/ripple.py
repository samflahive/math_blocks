import unittest

from math_blocks.algebra.core import Chain, Fraction

class ripple_chain_test(unittest.TestCase):
    def test_chain_ripple(self):
        ch = Chain([3, Fraction(4,2)], sign=False)
        
        ripped = ch.ripple_sign()
        
        self.assertEqual(ripped.latex(), "-3-\\frac{4}{2}")
        
        
        self.assertEqual(ch.evaluate(), ripped.evaluate())

        


if __name__ == '__main__':
    unittest.main()
