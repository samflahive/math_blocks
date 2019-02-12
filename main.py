from polynomials import polynomial as poly
from exponentials import exponential as exp
from logarithms import logarithm as log
from variables import variable as var

x = var("x")

two_x = exp(2, x)
logger = log(two_x, 2)

x.value = 3

print("{}={}".format(two_x.latex(), two_x.evaluate()))

print("{}={}".format(logger.latex(), logger.evaluate()))
