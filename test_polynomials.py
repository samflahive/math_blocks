import unittest
import polynomials
import variables
import exponentials
import products
import poly_terms
import logarithms
import quadratics
import cubics

class test_poly(unittest.TestCase):

    def test_latex(self):
        # test that polynomials are formatted correctly in latex and evaluation
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
        x.value = 3
        y.value = 5
        self.assertEqual(poly.evaluate(), 14010)

    def test_ops(self):
        # test the + * and == operators between polynomials
        
        x = variables.variable("x")
        g = variables.variable("g")
        
        quad = quadratics.quadratic(coeffs=[1,2,3], variable=x) # 11
        cub = cubics.cubic(coeffs=[1,2,3,4], variable=x) # 26

        # add them
        quad_cub_add = quad+cub # 11+26 = 37
        # multiply them
        quad_cub_mul = quad*cub # 11*26 = 286
        
        quad_2 = quadratics.quadratic(coeffs=[1,1,1], variable=g) # 31

        final_poly = (quad_cub_mul+quad_cub_add)*quad_2 # (286+37)*31 = 10013

        # == not finsihed yet - TO DO
        # reduce not finished -> cant test latex or attributes - TO DO

        # test the operations via evaluation
        x.value = 2
        g.value = 5
        final_poly_value = 10013
        self.assertEqual(final_poly.evaluate(), final_poly_value)


    def test_quad_init(self):
        # test the creation of polynomials through the quadratics shortcut
        # test via latex output
        x = variables.variable("x")

        quad = quadratics.quadratic([3,4,5], x)
        latex_format = quad.latex()
        desired_latex = "3x^2+4x+5"
        self.assertEqual(latex_format, desired_latex)

    def test_quad_roots(self):
        # test that creating a quadratic from roots is accurate
        roots = [5,-8]
        x = variables.variable("x")
        quad = quadratics.quadratic.from_roots(roots, x)
        
        # test latex
        latex_format = quad.latex()
        desired_latex = "x^2+3x-40"  
        self.assertEqual(latex_format, desired_latex)

        # test evaluation
        x.value = 5
        self.assertEqual(quad.evaluate(), 0)
        x.value = -8
        self.assertEqual(quad.evaluate(), 0)
        x.value = 2
        self.assertEqual(quad.evaluate(), -30)
        
    def test_cub_init(self):
        # test the creation of polynomials through the cubic shortcut
        # test via latex output
        x = variables.variable("x")

        cub = cubics.cubic([3,4,5,6], x)
        latex_format = cub.latex()
        desired_latex = "3x^3+4x^2+5x+6"
        self.assertEqual(latex_format, desired_latex)

    def test_cubic_roots(self):
        # test that creating a cubic from roots is accurate
        roots = [5,-8, 12]
        x = variables.variable("x")
        quad = cubics.cubic.from_roots(roots, x)
        
        # test latex
        latex_format = quad.latex()
        desired_latex = "x^3-9x^2-76x+480"        
        self.assertEqual(latex_format, desired_latex)

        # test evaluation
        x.value = 5
        self.assertEqual(quad.evaluate(), 0)
        x.value = -8
        self.assertEqual(quad.evaluate(), 0)
        x.value = 12
        self.assertEqual(quad.evaluate(), 0)
        x.value = 2
        self.assertEqual(quad.evaluate(), 300)


if __name__ == "__main__":
    unittest.main()
