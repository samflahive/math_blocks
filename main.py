from polynomials import polynomial as poly
from exponentials import exponential as exp
from logarithms import logarithm as log
from variables import variable as var
from products import product

x = var("x")

two_x = exp(2, x)
logger = log(two_x, 2)

x.value = 3

print("{}={}".format(two_x.latex(), two_x.evaluate()))

print("{}={}".format(logger.latex(), logger.evaluate()))

y = var("y")

prodA = product(4, x, y)
prodB = product(logger, 3, x)
prodC = prodA*prodB

prodC.arrange()

prodD = product(2, exp(2,7), 3, 4, exp(3,5), logger, 7, exp(x, 4), exp(2,3), exp(x, 2))

y.value = 4

print(prodC.latex())
print(prodA.evaluate(), prodB.evaluate(), prodC.evaluate())

print(prodD.latex())

prodD.reduce()
print(prodD.latex())

polyA = poly(coeffs=[2,3,4], terms=[[exp(x, 2)], [exp(x,2),exp(y,2)], [exp(x, 2)]])
print(polyA.coeffs)
print(polyA.terms[0].latex())
print(polyA.terms[1].latex())
print(polyA.terms[2].latex())
polyA.reduce()
print(polyA.coeffs)
print(polyA.terms[0].latex())
print(polyA.terms[1].latex())
