import unittest

from math_blocks.chains import chain

class chain_chain_test(unittest.TestCase):
    def test_chain_latex(self):
        ch = chain([3, chain([-3, 2])])
        self.assertEqual(ch.latex(), "3+(-3+2)")
        
        ch2 = chain([-2, -chain([-3, 2])])
        self.assertEqual(ch2.latex(), "-2-(-3+2)")

        ch3 = chain([chain([3, 2]), -chain([3, 2])])
        self.assertEqual(ch3.latex(), "3+2-(3+2)")
        
    def test_chain_eval(self):
        ch = chain([3, chain([-3, 2])])
        self.assertEqual(ch.evaluate(), 2)
        
        ch2 = chain([-2, -chain([-3, 2])])
        self.assertEqual(ch2.evaluate(), -1)

        ch3 = chain([chain([3, 2]), -chain([3, 2])])
        self.assertEqual(ch3.evaluate(), 0)


if __name__ == '__main__':
    unittest.main()
