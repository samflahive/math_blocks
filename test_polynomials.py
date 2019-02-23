import unittest
import polynomials
import variables
import exponentials
import products
import poly_terms
import logarithms
import quadratics

class test_poly(unittest.TestCase):

    def test_latex(self):
        x = variables.variable("x")
        y = variables.variable("y")

        x1 = exponentials.exponential(x,1)
        x2 = exponentials.exponential(x,2)
        x3 = exponentials.exponential(x,3)

        y1 = exponentials.exponential(y,1)
        y2 = exponentials.exponential(y,2)
        y3 = exponentials.exponential(y,3)

        coeffs = [1,1,4,-3,-1]
        terms = [[x1,y2],
                 poly_terms.poly_term(y3,x2),
                 poly_terms.poly_term(x3,y3),
                 [x2,y2],
                 poly_terms.poly_term(x1,y1)]
        
        poly = polynomials.polynomial(coeffs, terms)
        latex_format = poly.latex()
        desired_latex = "xy^2+y^3x^2+4x^3y^3-3x^2y^2-xy"
        self.assertEqual(latex_format, desired_latex)


if __name__ == "__main__":
    unittest.main()
