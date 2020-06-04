import unittest
from math import log

from math_blocks.logarithms import logarithm
from math_blocks.chains import chain

class chain_logarithm_test(unittest.TestCase):
    def test_chain_latex(self):
        loga = logarithm(2,chain([1,2]))
        self.assertEqual(loga.latex(), "log_{1+2}2")

    def test_chain_eval(self):
        loga = logarithm(2,chain([1,2]))
        self.assertEqual(loga.evaluate(), log(2,3))


if __name__ == '__main__':
    unittest.main()
