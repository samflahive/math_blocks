import unittest

from math_blocks.algebra.core import Chain

class basic_chain_test(unittest.TestCase):
    def test_basic_latex(self):
        ch = Chain([3,2])
        self.assertEqual(ch.latex(), "3+2")
        
        ch2 = Chain([-2,2])
        self.assertEqual(ch2.latex(), "-2+2")

        ch3 = Chain([-2,-2])
        self.assertEqual(ch3.latex(), "-2-2")
        
    def test_basic_eval(self):
        ch = Chain([3,2])
        self.assertEqual(ch.evaluate(), 5)
        
        ch2 = Chain([-2,2])
        self.assertEqual(ch2.evaluate(), 0)

        ch3 = Chain([-2,-2])
        self.assertEqual(ch3.evaluate(), -4)


if __name__ == '__main__':
    unittest.main()
