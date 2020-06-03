import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.variables import variable
from math_blocks.chains import chain

class chain_variable_test(unittest.TestCase):


    def test_chain_eval(self):
        n = variable("x")
        n.value = chain([1, -3])
        self.assertEqual(n.evaluate(), -2)

        n2 = variable("y", sign=False)
        n2.value = chain([1, -3])
        self.assertEqual(n2.evaluate(), 2)


if __name__ == '__main__':
    unittest.main()
