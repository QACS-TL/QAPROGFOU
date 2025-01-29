def add(x, z):
    """   Accepts two numeric parameters, adds them and returns sum. """
    return x + z

def subtract(x, z):
    """   Accepts two numeric parameters, subtracts the second from the first and returns the result. """
    return x - z

def multiply(x, z):
    """  Accepts two numeric parameters and return product.  """
    return x * z

def divide(x, z):
    """ Accepts two numeric parameters, divides first by the second and returns result.    """
    if z == 0:
        raise Exception('Divide by zero!')
    return f"{x/z:.3f}"