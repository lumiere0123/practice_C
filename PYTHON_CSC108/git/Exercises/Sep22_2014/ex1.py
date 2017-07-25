def cookies_needed(adults, teens, children):    
    ''' (int, int, int) -> int
    Return the number of cookies needed to
    feed this number of adults, teens and children.
    Each adult eats three, each teen five, and each child two.
    >>> cookies_needed(2, 3, 1)
    23
    '''
    adults = adults * 3
    teens = teens * 5
    children = children * 2
    return adults + teens + children


def percentage(raw_mark, max_mark):
    ''' (number, number) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark is max_mark.
    >>> percentage(15, 20)
    75.0
    '''
    return 100 * raw_mark / max_mark


def is_multiple_of_3(x):
    ''' (int) -> bool
    Return True iff x is a multiple of 3.
    >>> is_multiple_of_3(15)
    True
    >>> is_multiple_of_3(7)
    False
    '''

    return x % 3 == 0

def is_multiple(x, y):
    ''' (int, int) -> bool
    Return True iff x is an even multiple of y.
    >>> is_multiple(15, 3)
    True
    >>> is_multiple(7, 2)
    False
    '''
    
    return x % y == 0


def same_abs(num1, num2):
    """ (number, number) -> bool
    Return True iff (if and only if) num1 and num2 have the same absolute value.
    >>> same_abs(-3, 3)
    True
    >>> same_abs(3, 3.5)
    False
    """

    num1 = abs(num1)
    num2 = abs(num2)
    return num1 == num2

def different_types(obj1, obj2):
    """ (object, object) -> bool
    Return True iff obj1 and obj2 are of different types.
    >>> different_types(3, '3')
    True
    >>> different_types(108.0, 3.14)
    False
    """
    obj1_py = type(obj1)
    obj2_py = type(obj2)

    #return not (obj1_py == obj2_py)

    return obj1_py != obj2_py

def is_right_triangle(side1, side2, hypotenuse):
    """ (int, int, int) -> bool
    Return whether a triangle with sides of length side1, side2 and hypotenuse
    is a right triangle.
    >>> is_right_triangle(3, 4, 5)
    True
    >>> is_right_triangle(2, 2, 4)
    False
    """
    return side1 ** 2 + side2 ** 2 == hypotenuse ** 2


import doctest
doctest.testmod()
