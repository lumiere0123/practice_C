def can_vote(age):
    """ (int) -> bool

    Return True iff age is legal voting age of at least 18 years.

    >>> can_vote(16)
    False
    >>> can_vote(21)
    True
    """

    # The following three blocks of code are equivalent, but the last is
    # the best.

    # Block 1: needless if statement
    # if age < 18:
    #     return False
    # else:
    #     return True

    # Block 2: okay, but why not change the condition?
    # return not (age < 18)

    # Block 3: simplest condition
    return age >= 18