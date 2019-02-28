import unittest
import polynomials
import variables
import exponentials
import products
import poly_terms
import logarithms
import quadratics
import cubics

class test_log(unittest.TestCase):
    def test_eval(self):
        # test the evaluation method

        
        # number, number
        log = logarithms.logarithm(100,10)
        self.assertAlmostEqual(log.evaluate(), 2)
        
        # number, variable
        x = variables.variable("x")
        x.value = 1000
        log.exponent = x
        self.assertAlmostEqual(log.evaluate(), 3)
        
        # variable, number
        log.exponent = 25
        log.base = x
        x.value = 5
        self.assertAlmostEqual(log.evaluate(), 2)

    def test_latex(self):
        # test the latex method

        # number, number
        log = logarithms.logarithm(100,10)
        self.assertEqual(log.latex(), "log_10(100)")
        
        # number, variable
        x = variables.variable("x")
        x.value = 1000
        log.exponent = x
        self.assertEqual(log.latex(), "log_10(x)")
        
        # variable, number
        log.exponent = 25
        log.base = x
        x.value = 5
        self.assertEqual(log.latex(), "log_x(25)")

    def test_add(self):
        # test the + operator
        
        # number, number
        logA = logarithms.logarithm(100,10)
        logB = logarithms.logarithm(1000,10)
        logC = logA + logB

        self.assertAlmostEqual(logC.evaluate(), 5)
        self.assertEqual(logC.latex(), "log_10(100000)")

        # number, variable
        x = variables.variable("x")
        x.value = 100
        
        logA.base = x
        logB.base = x
        logC = logA + logB

        self.assertAlmostEqual(logC.evaluate(), 2.5)
        self.assertEqual(logC.latex(), "log_x(100000)")

    def test_sub(self):
        # test the - operator
        
        # number, number
        logA = logarithms.logarithm(100,10)
        logB = logarithms.logarithm(1000,10)
        logC = logB - logA

        self.assertAlmostEqual(logC.evaluate(), 1)
        self.assertEqual(logC.latex(), "log_10(10)")

        # number, variable
        x = variables.variable("x")
        x.value = 100
        
        logA.base = x
        logB.base = x
        logC = logB - logA

        self.assertAlmostEqual(logC.evaluate(), 0.5)
        self.assertEqual(logC.latex(), "log_x(10)")
        


if __name__ == "__main__":
    unittest.main()
        
