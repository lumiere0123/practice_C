#Recap on slicing
    
def find_hidden_letters(s):
    
    """ (str) -> str
    
    Precondition len(s) >= 4
    
    Return a string containing the third and fourth letters of s.
    
    >>> find_hidden_letters("Can you find the secret letters?")
    'n '
    >>> find_hidden_letters("No I can't!")
    ' I'
    """
    return s[2:4]
