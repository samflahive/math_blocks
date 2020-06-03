import unittest
from math import log
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.logarithms import logarithm
from math_blocks.fractions import fraction


class logarithm_logarithm_test(unittest.TestCase):
    def test_logarithm_latex(self):
        f1 = logarithm(3,2)
        f2 = logarithm(100,10)
        loga = logarithm(f1,f2)
        self.assertEqual(loga.latex(), "log_{log_{10}100}log_{2}3")

    def test_logarithm_eval(self):
        f1 = logarithm(4,2)
        f2 = logarithm(100,10)
        loga = logarithm(f1,f2)
        self.assertEqual(loga.evaluate(), 1)


if __name__ == '__main__':
    unittest.main()
