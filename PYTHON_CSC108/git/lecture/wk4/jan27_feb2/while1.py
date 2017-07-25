def every_nth_character(s, n):
    
    """(str, int) -> str
    
    Return every nth character in s starting at index 0.
    
    >>>every_nth_character('Computer Science', 3)
    'CpeSee'
    """
    
    result = ''
    i = 0
    while i < len(s):
        result = result + s[i]
        i = i + n
    return result

    #What would happen if n was zero? 
    #We can add a precondition n > 0 to avoid this scenario.
