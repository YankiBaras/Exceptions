class FactorialArgumentError(Exception) :
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "Provided argument %s is not a positive integer." % self._arg

    def get_arg(self):
        return self._arg


def factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
             raise FactorialArgumentError (n)
    except FactorialArgumentError as e:
        print("Function Expected positive integer, and instead got %s." % type(e.get_arg()))
    else:
        fact = 1
        for i in range(n, 0, -1):
            fact = fact * i
        return fact