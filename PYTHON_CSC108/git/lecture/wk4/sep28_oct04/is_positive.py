def is_positive(x):
    '''(num) -> bool
    Return True iff x >= 0
    '''
    
    # The following two blocks are equivalent, but the second is preferred.
    
    # Block 1: redundant test
    # return (x >= 0) == True
    
    # Block 2: preferred -- simpler
    return x >= 0