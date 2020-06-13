import unittest

from math_blocks.chains import chain

class collapse_chain_test(unittest.TestCase):
    def test_chain_ripple(self):
        ch = chain([3,2],  sign=False)
        
        col = ch.collapse_numbers()
        
        self.assertEqual(col.latex(), "-5")
        
        
        self.assertEqual(ch.evaluate(), col.evaluate())

        


if __name__ == '__main__':
    unittest.main()

