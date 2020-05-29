import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain
from math_blocks.exponentials import exponential


class exponential_chain_test(unittest.TestCase):
    def test_exponential_latex(self):
        ch = chain([(3, True),(exponential(3,2), True)])
        self.assertEqual(ch.latex(), "3+3^{2}")
        
        ch2 = chain([(-2, True),(exponential(3, 2, sign=False), False)])
        self.assertEqual(ch2.latex(), "-2-(-3^{2})")

        ch3 = chain([(exponential(3, 2, sign=False), False),(exponential(3, 2, sign=False), False)])
        self.assertEqual(ch3.latex(), "-(-3^{2})-(-3^{2})")
        
    def test_exponential_eval(self):
        ch = chain([(3, True),(exponential(3,2), True)])
        self.assertEqual(ch.evaluate(), 3+3**2)
        
        ch2 = chain([(-2, True),(exponential(3, 2, sign=False), False)])
        self.assertEqual(ch2.evaluate(), -2-(-3**2))

        ch3 = chain([(exponential(3, 2, sign=False), False),(exponential(3, 2, sign=False), False)])
        self.assertEqual(ch3.evaluate(), -(-3**2)-(-3**2))


if __name__ == '__main__':
    unittest.main()
