class factor:
    def __init__(self, variable, root):
        self.variable = variable
        self.root = root

    def latex(self):
        return "({}{})".format(variable.latex(), factor.signed_number_format(-root))



    def signed_number_format(number):
        if isinstance(number, (int, float, complex)):
            if number < 0:
                return str(number)
            elif number > 0:
                return "+{}".format(number)
            else:
                return ""
        else:
            return ""
