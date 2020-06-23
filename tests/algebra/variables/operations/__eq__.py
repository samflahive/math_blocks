import unittest

from math_blocks.algebra.core import Number
from math_blocks.algebra.polynomials import Variable


class fraction_eq(unittest.TestCase):

    
    def test_number_eq(self):
        main_v = Variable("z",2)
        n = Number(3)
        self.assertEqual(False, main_v == n)

    def test_variable_eq(self):
        main_v = Variable("z",2)
        v = Variable("v")
        z = Variable("z")
        self.assertEqual(False, main_v == v)
        self.assertEqual(True, main_v == z)
        self.assertEqual(False, main_v == -z)
        
if __name__ == '__main__':
    unittest.main()
