import unittest
from math import log
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.logarithms import logarithm


class basic_logarithm_test(unittest.TestCase):
    def test_basic_latex(self):
        loga = logarithm(2,3)
        self.assertEqual(loga.latex(), "log_{3}2")

    def test_basic_eval(self):
        loga = logarithm(2,3)
        self.assertEqual(loga.evaluate(), log(2,3))


if __name__ == '__main__':
    unittest.main()
