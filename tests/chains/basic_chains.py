import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain

class basic_chain_test(unittest.TestCase):
    def test_basic_latex(self):
        ch = chain([(3, True),(2, True)])
        self.assertEqual(ch.latex(), "3+2")
        
        ch2 = chain([(-2, True),(2, True)])
        self.assertEqual(ch2.latex(), "-2+2")

        ch3 = chain([(-2, False),(2, False)])
        self.assertEqual(ch3.latex(), "-(-2)-2")
        
    def test_basic_eval(self):
        ch = chain([(3, True),(2, True)])
        self.assertEqual(ch.evaluate(), 3+2)
        
        ch2 = chain([(-2, True),(2, True)])
        self.assertEqual(ch2.evaluate(), -2+2)

        ch3 = chain([(-2, False),(2, False)])
        self.assertEqual(ch3.evaluate(), -(-2)-2)


if __name__ == '__main__':
    unittest.main()
