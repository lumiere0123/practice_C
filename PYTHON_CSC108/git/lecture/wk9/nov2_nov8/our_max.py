def our_max(num1, num2):
    '''(number, number) -> number
    Return the larger of num1 and num2.
    
    >>> our_max(6, 8)
    8
    >>> our_max(6, 6)
    6
    >>> our_max(8, 6)
    8
    >>> our_max(-1, -7)
    -1
    >>> our_max(4.5, 5.0)
    5.0
    >>> our_max(4.5, 4)
    4.5
    '''

    return num1 if num1 > num2 else num2