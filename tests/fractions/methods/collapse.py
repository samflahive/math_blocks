import unittest

from math_blocks.fractions import fraction

class collapse_fraction_test(unittest.TestCase):
    def test_fraction_collapse(self):
        ch = fraction(3,2,  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-1.5")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()


