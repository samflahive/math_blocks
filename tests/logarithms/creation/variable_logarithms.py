import unittest
from math import log

from math_blocks.logarithms import logarithm
from math_blocks.variables import variable


class variable_logarithm_test(unittest.TestCase):
    def test_variable_latex(self):
        x = variable("x", value=-3, sign=False)
        y = variable("y", value=2, sign=True)
        loga = logarithm(y,x)
        self.assertEqual(loga.latex(), "log_{-x}y")

    def test_variable_eval(self):
        x = variable("x", value=-3, sign=False)
        y = variable("y", value=2, sign=True)
        loga = logarithm(y,x)
        self.assertEqual(loga.evaluate(), log(2,3))


if __name__ == '__main__':
    unittest.main()
