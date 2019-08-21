# math_blocks
Secondary level math curriculum concepts represented in python.

The purpose of this library is to enable the creation of educational tools (or be one in and of itself).
This library is not intended to be used for serious mathematical computation or manipulation.

For example, if you wanted to develop a online math test with the details of the questions randomly generated. One approach would be to randomly generate these details. For example "What are the roots of this polynomial" might involve randomly generating the coefficients of a polynomial and then use some software to find the roots, so that you can check whether the student is correct.

The math_blocks approach would be to randomly generate the roots themselves, then use the math_blocks package to generate a polynomial from those roots, achieving the same result from the students perspective, but with "nicer" looking numbers and often efficiency gains.

The general approach is not "generate the question and use software to solve it" but rather "generate the answer and use software to build the question".
