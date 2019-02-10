from polynomials import polynomial
from exponentials import exponential
from variables import variable

x = variable("x")

exp = exponential(2, x)

x.value = 3

print(exp.evaluate())

print(exp.latex())
