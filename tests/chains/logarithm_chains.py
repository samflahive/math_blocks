import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain
from math_blocks.logarithms import logarithm
from math import log


class logarithm_chain_test(unittest.TestCase):
    def test_logarithm_latex(self):
        ch = chain([(3, True),(logarithm(3,2), True)])
        self.assertEqual(ch.latex(), "3+log_{2}3")
        
        ch2 = chain([(-logarithm(3,2), True),(2, True)])
        self.assertEqual(ch2.latex(), "-log_{2}3+2")

        ch3 = chain([(-logarithm(3,2), False),(-logarithm(3,2), False)])
        self.assertEqual(ch3.latex(), "-(-log_{2}3)-(-log_{2}3)")
        
    def test_logarithm_eval(self):
        ch = chain([(3, True),(logarithm(3,2), True)])
        self.assertEqual(ch.evaluate(), 3+log(3,2))
        
        ch2 = chain([(-logarithm(3,2), True),(2, True)])
        self.assertEqual(ch2.evaluate(), -log(3,2)+2)

        ch3 = chain([(-logarithm(3,2), False),(-logarithm(3,2), False)])
        self.assertEqual(ch3.evaluate(), 2*log(3,2))


if __name__ == '__main__':
    unittest.main()
