import unittest
import polynomials
import variables
import exponentials
import products
import poly_terms
import logarithms
import quadratics
import cubics

class test_exp(unittest.TestCase):
    def test_eval(self):
        # test the eval method of exponential objects
        # should evaluate the exponential at current values
        
        # number ^ number
        exp = exponentials.exponential(3,7)
        self.assertEqual(exp.evaluate(), 3**7)
        
        x = variables.variable("x")
        x.value = 2

        exp.base = x
        # variable ^ number
        self.assertEqual(exp.evaluate(), 2**7)

        y = variables.variable("y")
        y.value = 3
        x.value = 5

        exp.power = y
        # variable ^ variable
        self.assertEqual(exp.evaluate(), 5**3)

    def test_latex(self):
        # test the latex formatting of exponentials

        # number ^ number
        exp = exponentials.exponential(3,7)
        self.assertEqual(exp.latex(), "3^7")
        
        x = variables.variable("x")

        exp.base = x
        # variable ^ number
        self.assertEqual(exp.latex(), "x^7")

        y = variables.variable("y")

        exp.power = y
        # variable ^ variable
        self.assertEqual(exp.latex(), "x^y")

    def test_mult(self):
        # test the multiplication operator

        expA = exponentials.exponential(2,3)
        expB = exponentials.exponential(2,6)

        # multiply two exp objects
        expC = expA*expB

        # test result via:
        # 1) evaluation
        self.assertEqual(expC.evaluate(), expA.evaluate()*expB.evaluate())
        #2) latex format
        self.assertEqual(expC.latex(), "2^9")

        # test mult for differing bases via evaluate
        expA.base = 3
        expC = expA*expB
        self.assertAlmostEqual(expC.evaluate(), expA.evaluate()*expB.evaluate())

    def test_eq(self):
        # test the == operator
        
        expA = exponentials.exponential(3,7)
        expB = exponentials.exponential(3,6)
        self.assertEqual(expA==expB, False)
        
        x = variables.variable("x")

        expA.power = x
        self.assertEqual(expA==expB, False)

        expB.power = x
        self.assertEqual(expA==expB, True)

        y = variables.variable("y")

        expB.power = y
        self.assertEqual(expA==expB, False)
        
        
        


if __name__ == "__main__":
    unittest.main()
        
