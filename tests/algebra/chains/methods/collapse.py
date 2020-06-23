import unittest

from math_blocks.algebra.core import Number, Chain, Fraction

class collapse_chain_test(unittest.TestCase):
    def test_chain_collapse(self):
        ch = Chain([3,2],  sign=False)
        
        col = ch.to_number()
        
        self.assertEqual(col.latex(), "-5")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

    def test_advanced_chain_collapse(self):
        f = Fraction(Fraction(4,2), 2) # 1
        ch = Chain([Chain([3,2]),f],  sign=False) # -(5+1) = -6
        
        col = ch.to_number()
        
        self.assertEqual(col.latex(), "-6.0")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()

