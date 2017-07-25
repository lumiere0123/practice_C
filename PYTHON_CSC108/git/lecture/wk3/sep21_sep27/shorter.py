def is_shorter(s1, s2):
    '''(str, str) -> bool
    Return True if the first string is shorter than the second; false otherwise.
    
    >>> is_shorter("", "cat")
    True
    >>> is_shorter("kitten", "cat")
    False
    >>> is_shorter("cat", "dog")
    False
    '''
    
    return len(s1) < len(s2)
    # Homework: modify this so that it returns the shorter *string*