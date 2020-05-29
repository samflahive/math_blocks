import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.variables import variable
from math_blocks.products import product

class product_variable_test(unittest.TestCase):

    def test_product_eval(self):
        n = variable("x")
        n.value = product([2,2])
        self.assertEqual(n.evaluate(), 4)

        n2 = variable("y", sign=False)
        n2.value = product([2,1])
        self.assertEqual(n2.evaluate(), -2)


if __name__ == '__main__':
    unittest.main()
