import unittest

import math_blocks

class inv_fraction_test(unittest.TestCase):
    def test_frac_inv(self):
        
        f = math_blocks.fraction(4, 2, False)
        
        inv = f.inverse()
        
        self.assertEqual(inv.latex(), "-\\frac{2}{4}")
        
        f = math_blocks.fraction(4, 2, True)
        
        inv = f.inverse()
        
        self.assertEqual(inv.latex(), "\\frac{2}{4}")



if __name__ == '__main__':
    unittest.main()
