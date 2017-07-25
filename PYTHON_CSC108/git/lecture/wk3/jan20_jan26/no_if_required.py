def can_vote(age):
    """ (int) -> bool

    Return True iff age is legal voting age of at least 18 years.

    >>> can_vote(16)
    False
    >>> can_vote(21)
    True
    """
    
    #if age < 18:
    #    return False
    #else:
    #    return True
     
    return age >= 18

    #An alternative solution would be age not less than 18    
    #return not (age < 18)



def is_teenager(age):
    """ (int) -> bool

    Return True iff age is a teenager between 13 and 18 inclusive.

    >>> is_teenager(4)
    False
    >>> is_teenager(16)
    True
    >>> is_teenager(19)
    False
    """
    #[13, 18] Here 13, 18 are inclusive
    #(12, 19) Here 12, 19 are not included in the range.
    
    
    #if age < 13:
    #    return False
    #else:
    #    if age > 18:
     #       return False
     #   else:
      #      return True
    
    #Chaining
    return 13 <= age <= 18

    # You could also use and 
    #return (age >= 13) and (age <= 18)

