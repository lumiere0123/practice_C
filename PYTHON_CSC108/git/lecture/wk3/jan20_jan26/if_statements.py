def earlier_name(name1, name2):
    """ (str, str) -> str

    Return the name, name1 or name2, that comes first alphabetically.

    >>> earlier_name('Jen', 'Paul')
    'Jen'
    >>> earlier_name('Colin', 'Colin')
    'Colin'
    """
    if name1 < name2:
        return name1
    else:
        return name2
    #return min(name1, name2)
    #You could also have name1 <= name2 in the first if statement


def ticket_price(age):
    """(int) -> float

    Precondition: age > 0

    Return the ticket price for a person with age in years.
    Seniors 65 and over pay 4.75, kids 12 and under pay 4.25 and
    everyone else pays 7.50.
    
    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75
    """

    if age >= 65:
        return 4.75
    elif age <= 12:
        return 4.25
    else:
        return 7.50
    #What if I skipped the else? Then I would violate my type contract.
    #This function would return None for anyone between 12 and 65.
    
    
    #You could choose to express "everyone else" first 
    #if 12 < age < 65:
    #    return 7.50
    #elif age <= 12:
    #    return 4.25
    #else:
    #    return 4.75
    
    #In the commented-out code you could also write the first statement as
    # if age > 12 and age < 65
        

def format_name(first, last):
    """ (str, str) -> str

    Return the given first and last name as a single string, in the form:
    <lastname>, <firstname>
    Mononymous persons (those with no last name) should have their name
    returned without a comma.

    >>> format_name('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn'
    >>> format_name('Cher', '')
    'Cher'
    """
    
    #The empty string is ''
    
    if last == '':
        return first
    else:
        return last + ", " + first

    #Alternatively you could write the condition implied in the "else"
    #first. 
    #if last != '':
    #    return last + ", " + first
    #else:
    #    return first

    #You could also find if a string is empty using len built-in function.
    #if len(last) == 0:
    #    return first
    #etc...