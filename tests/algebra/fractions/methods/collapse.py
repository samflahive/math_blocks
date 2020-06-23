import unittest

from math_blocks.algebra.core import Fraction

class collapse_fraction_test(unittest.TestCase):
    def test_fraction_collapse(self):
        ch = Fraction(3,2,  sign=False)
        
        col = ch.to_number()
        
        self.assertEqual(col.latex(), "-1.5")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


