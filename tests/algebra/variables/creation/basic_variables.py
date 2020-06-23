import unittest

from math_blocks.algebra.polynomials import Variable

class basic_variable_test(unittest.TestCase):
    def test_basic_latex(self):
        n = Variable("x")
        self.assertEqual(n.latex(), "x")

        n2 = Variable("y", sign=False)
        self.assertEqual(n2.latex(), "-y")


    def test_basic_eval(self):
        n = Variable("x")
        n.value = 5
        self.assertEqual(n.evaluate(), 5)

        n2 = Variable("y", sign=False)
        n2.value = 3
        self.assertEqual(n2.evaluate(), -3)

        n3 = Variable("z", sign=False)
        # no value set -> error
        self.assertRaises(ValueError, n3.evaluate)

if __name__ == '__main__':
    unittest.main()
