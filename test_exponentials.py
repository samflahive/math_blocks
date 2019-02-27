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
        


if __name__ == "__main__":
    unittest.main()
        
