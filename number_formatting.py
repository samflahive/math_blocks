def number_coeff(number, index, explicit=False):
    # return a string representation of the number as if it were a coefficient
    # index respresents which coefficient it is in the equation

    if number < 0:
        if explicit or number != -1:
            return str(number)
        else:
            return "-"
    else:
        if index == 0:
            if explicit:
                return "+{}".format(number)
            else:
                return "" if number == 1 else str(number)
        else:
            if explicit or number != 1:
                return "+{}".format(number)
            else:
                return "+"
