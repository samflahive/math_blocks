import unittest

from math_blocks.chains import chain

class ripple_chain_test(unittest.TestCase):
    def test_chain_ripple(self):
        ch = chain([3,2],  sign=False)
        
        ripped = ch.ripple_sign()
        
        self.assertEqual(ripped.latex(), "-3-2")
        
        
        self.assertEqual(ch.evaluate(), ripped.evaluate())

        


if __name__ == '__main__':
    unittest.main()
