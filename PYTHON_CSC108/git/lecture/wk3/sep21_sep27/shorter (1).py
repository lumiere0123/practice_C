def is_shorter(s1, s2):
    '''(str, str) -> str
    Return the shorter of the two provided strings.
    
    >>> is_shorter("", "cat")
    ''
    >>> is_shorter("kitten", "cat")
    'cat'
    >>> is_shorter("cat", "dog")
    'dog'
    '''
    
    if len(s1) < len(s2):
        return s1
    else:
        return s2