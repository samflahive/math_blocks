import unittest
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from math_blocks.chains import chain
from math_blocks.variables import variable

class variable_chain_test(unittest.TestCase):

    def test_variable_latex(self):
        x = variable("x", value=3)
        ch = chain([(x, True),(2, True)])
        self.assertEqual(ch.latex(), "x+2")
        
        ch2 = chain([(-2, True),(x, True)])
        self.assertEqual(ch2.latex(), "-2+x")

        y = variable("y", -1)
        ch3 = chain([(x, False),(y, False)])
        self.assertEqual(ch3.latex(), "-x-y")


        z = variable("z", value=-1, sign=False)
        ch4 = chain([(x, False),(y, False),(z,True)])
        self.assertEqual(ch4.latex(), "-x-y+(-z)")

        ch5 = chain([(x, False),(y, False),(z,False)])
        self.assertEqual(ch5.latex(), "-x-y-(-z)")

    def test_variable_eval(self):
        x = variable("x", value=3)
        ch = chain([(x, True),(2, True)])
        self.assertEqual(ch.evaluate(), 5)
        
        ch2 = chain([(-2, True),(x, True)])
        self.assertEqual(ch2.evaluate(), 1)

        y = variable("y", value=-1)
        ch3 = chain([(x, False),(y, False)])
        self.assertEqual(ch3.evaluate(), -2)


        z = variable("z", value=-1, sign=False)
        ch4 = chain([(x, False),(y, False),(z,True)])
        self.assertEqual(ch4.evaluate(), -1)

        ch5 = chain([(x, False),(y, False),(z,False)])
        self.assertEqual(ch5.evaluate(), -3)

    
if __name__ == '__main__':
    unittest.main()
