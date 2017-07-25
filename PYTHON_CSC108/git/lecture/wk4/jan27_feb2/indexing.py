#Recap on indexing

def find_third_letter(s):
    
    """ (str) -> str
    
    Precondition len(s) >= 4
    
    Return the third letter of s.
    
    >>> find_third_letter("Can you find the secret letter?")
    'n'
    
    >>> find_third_letter("No I can't!")
    ' '
    """
    
    #using indexing - we start counting from zero
    return s[2]
    #Can you do this using a negative index? 
    #return s[-len(s) + 2]
    
    #or you can use slicing
    #return s[2:3]
