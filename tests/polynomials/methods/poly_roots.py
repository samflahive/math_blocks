import unittest


from math_blocks.algebra.polynomials import Variable, Polynomial

class from_roots(unittest.TestCase):
    def test_root_to_factor(self):
        #y^2 + 2yz - x^2
        y = Variable("y")
        x = Variable("x")
        p = Polynomial.root_to_factor(x, 3)
        p2 = Polynomial.root_to_factor(y, -3)
        
        self.assertEqual(p.latex(), "1x-3")
        self.assertEqual(p2.latex(), "1y+3")

    def test_from_roots(self):
        y = Variable("y")
        x = Variable("x")

        p = Polynomial.from_roots([(x, -2),(x, 3),(y, -1),(y, 0)])

        
        y.value = -1
        x.value = 1
        self.assertEqual(p.evaluate(), 0)
        
        y.value = 1
        x.value = 3
        self.assertEqual((-p).evaluate(), 0)

        y.value = 1
        x.value = 1
        # (3)(-2)(2)(1)
        self.assertEqual(p.evaluate(), -12)

if __name__ == '__main__':
    unittest.main()
