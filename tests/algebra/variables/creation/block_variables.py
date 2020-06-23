import unittest

from math_blocks.algebra.core import Fraction
from math_blocks.algebra.polynomials import Variable

class block_variable_test(unittest.TestCase):

    def test_basic_eval(self):
        n = Variable("x")
        n.value = Fraction(25,5)
        self.assertEqual(n.evaluate(), 5)

        n2 = Variable("y", sign=False)
        n2.value = Variable("a", 3)
        self.assertEqual(n2.evaluate(), -3)


if __name__ == '__main__':
    unittest.main()

