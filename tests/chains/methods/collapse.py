import unittest

import math_blocks

class collapse_chain_test(unittest.TestCase):
    def test_chain_collapse(self):
        ch = math_blocks.chain([3,2],  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-5")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

    def test_advanced_chain_collapse(self):
        f = math_blocks.fraction(3,2)
        cx = math_blocks.complex_number(2,0, sign=False)
        p = math_blocks.product([f,cx])
        ch = math_blocks.chain([3,2,p],  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-2.0")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()

