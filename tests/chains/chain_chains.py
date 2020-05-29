import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain

class chain_chain_test(unittest.TestCase):
    def test_chain_latex(self):
        ch = chain([(3, True),(chain([(3,False), (2, True)]), True)])
        self.assertEqual(ch.latex(), "3+(-3+2)")
        
        ch2 = chain([(-2, True),(chain([(3,False), (2, True)]), False)])
        self.assertEqual(ch2.latex(), "-2-(-3+2)")

        ch3 = chain([(-2, False),(-chain([(3,False), (2, True)]), False)])
        self.assertEqual(ch3.latex(), "-(-2)-(-(-3+2))")
        
    def test_chain_eval(self):
        ch = chain([(3, True),(chain([(3,False), (2, True)]), True)])
        self.assertEqual(ch.evaluate(), 2)
        
        ch2 = chain([(-2, True),(chain([(3,False), (2, True)]), False)])
        self.assertEqual(ch2.evaluate(), -1)

        ch3 = chain([(-2, False),(-chain([(3,False), (2, True)]), False)])
        self.assertEqual(ch3.evaluate(), 1)


if __name__ == '__main__':
    unittest.main()
