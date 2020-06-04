import unittest

from math_blocks.complex_numbers import complex_number
from math_blocks.variables import variable


class variable_complex_test(unittest.TestCase):
    def test_variable_latex(self):
        x = variable("x")
        c1 = complex_number(3,x)
        self.assertEqual(c1.latex(), "3+xi")


        y = variable("y", sign=False)
        c2 = complex_number(-2, y, sign=False)
        self.assertEqual(c2.latex(), "-(-2-yi)")

    def test_variable_eval(self):
        x = variable("x", value=3)
        c1 = complex_number(3,x)
        self.assertEqual(c1.evaluate(), 3+3j)


        y = variable("y", value=2, sign=False)
        c2 = complex_number(-2, y, sign=False)
        self.assertEqual(c2.evaluate(), -(-2-2j))


if __name__ == '__main__':
    unittest.main()
