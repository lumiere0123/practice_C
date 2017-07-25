def abs1(n):
    '''(number) -> number

    Return absolute value of n.

    >>> abs1(8)
    8
    >>> abs1(-8)
    8
    '''

    # try breaking this code and running doctest
    # to see the example in the docstring fail
    if n < 0:
        n = -n
    return n

