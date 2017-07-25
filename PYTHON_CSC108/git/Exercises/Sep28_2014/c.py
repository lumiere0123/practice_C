def taxes_due(income, credits, is_resident):
    '''(int, int, bool) -> float
    Return the taxes due on the specified income. The calculated tax is10% of the first $100,000 and 20% of any income 
    above $100,000. Taxes due is the calculates tax less (minus) credits. No taxes are due if the taxpayer is not a resident or if 
    credits exceeds the calculated tax.

    >>> taxes_due(500000, 0, False)
    0.0
    >>> taxes_due(10000, 1500, True)
    0.0
    >>> taxes_due(10000, 500, True)
    500.0
    >>> taxes_due(500000, 0, True)
    90000.0
    >>> taxes_due(120000, 10000, True)
    4000.0
    '''

    
    #tax1 = income * 0.1 - credits
    #tax2 = (100000 * 0.1) + (income - 100000) * 0.2 - credits

    #if not is_resident:
    #    return float(0)
    #elif credits >= income *0.1 or credits >= income * 0.2:
    #    return float(0)
    #elif income <= 100000:
    #    return tax1
    #elif income > 100000:
    #    return tax2 

    # calculate tax

    if True:
        a=123
    
    print(a)



    #if is_resident:
    #    if ( income >= 100000):
    #        tax = 100000 * 0.1 +  ( income - 100000 ) * 0.2
    #    else:
    #        tax = income * 0.1 

    #    if tax > credits:
    #        return float(tax - credits)
    #    else:
    #        return 0.0
    #else:
    #    return 0.0


def format_name(first, last):
    """ (str, str) -> str
    
    Return the given first and last name as a single string, in the form:
    LAST_NAME, FIRST_NAME
    where LAST_NAME and FIRST_NAME are replaced by last and first.
    Mononymous persons (those with either a first or a last name but not
    both) should have their name returned without a comma.

    >>> format_name('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn'
    >>> format_name('Cher', '')
    'Cher'
    """

    #if !(first == "" or  last == ""): 

    if first != "" and last != "": 
        return last + ", " + first
    else:
        if first == "":
            return last
        else:
            return first

taxes_due(10,10,True)
#import doctest
#doctest.testmod()
