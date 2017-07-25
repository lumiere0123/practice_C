def is_even(num):
    '''(number) -> bool
    Return True iff num is an even number
    
    >>> is_even(2)
    True
    >>> is_even(-14)
    True
    >>> is_even(1)
    False
    '''

    return num % 2 == 0

    # The following three return statements would also "work".
    # However, they aren't good choices for other reasons -- 
    # they are functional code but not good code. Why not?
    #     return not (num % 2)
    #     return num / 2 == num // 2
    #     return (num // 2) * 2 == num