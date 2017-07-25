def same_abs(num1, num2):
    """ (number, number) -> bool
    
    Return True iff num1 and num2 have the same absolute value.
    
    >>> same_abs(-3, 3)
    True
    >>> same_abs(3, 3.5)
    False
    """
    return abs(num1) == abs(num2)

def different_types(obj1, obj2):
    """ (object, object) -> bool
    
    Return True iff obj1 and obj2 are of different types.
    
    >>> different_types(3, '3')
    True
    >>> different_types(108.0, 3.14)
    False
    """

    return type(obj1) != type(obj2)

def is_right_triangle(side1, side2, hypotenuse):
    """ (int, int, int) -> bool
    
    Return whether a triangle with sides of length side1, side2 and 
    hypotenuse is a right triangle.
    
    >>> is_right_triangle(3, 4, 5)
    True
    >>> is_right_triangle(2, 2, 4)
    False
    """
    return (side1 ** 2) + (side2 ** 2) == (hypotenuse ** 2)

