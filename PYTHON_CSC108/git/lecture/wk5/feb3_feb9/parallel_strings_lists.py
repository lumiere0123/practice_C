def stretch_string(s, stretch_factors):
    """ (str, list of int) -> str

    Precondition: len(s) == len(stretch_factors) and the items of
                  stretch_factors are non-negative
     
    Return a string consisting of the characters in s in the same order as in
    s, repeated the number of times indicated by the item at the 
    corresponding position of stretch_factors.
    
    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    
    new_string = ''
    for i in range(len(s)):
        new_string = new_string + s[i] * stretch_factors[i]
    return new_string

    #Can you do this without using the range function?
    #Yes, but you need to keep track of the current index in a local variable
    
    #new_string = ''
    #i = 0 
    #for char in s:
    #    new_string = new_string + char * stretch_factors[i]
    #    i = i + 1
    #return new_string

    #Could you write the same code with a while loop?
    #new_string = ''
    #i = 0
    #while i < len(s):
    #    new_string = new_string + s[i] * stretch_factors[i]
    #    i = i + 1
    #return new_string
