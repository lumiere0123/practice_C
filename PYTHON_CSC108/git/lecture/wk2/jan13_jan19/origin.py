import math

def distance(x, y):
    """ (number, number) -> float
    
    Return the distance from point (x, y) to the origin.

    >>> distance(1, 1)
    1.414213562730951
    >>> distance(0, 0)
    0.0
    """
    
    return math.sqrt(x ** 2 + y ** 2)
    
    # An equivalent solution:
    #return (x ** 2 + y ** 2) ** 0.5