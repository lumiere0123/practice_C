# Given a student's term mark and their mark on the final exam, return their final 
# mark in the course.

# Remember: The final exam is worth 45%. The term mark is worth 55%.
# Remember: If you score less than 40% on the final exam, your final mark is no higher than 47.

def calculate_mark(term, exam):
    '''(number, number) -> number
    Return a student's final mark given their term mark and final exam mark.
    
    >>> calculate_mark(100, 100)
    100.0
    >>> calculate_mark(100, 35)
    47.0
    >>> calculate_mark(40, 40)
    40.0
    '''
    
    # Don't just CODE. Come up with a plan, in English (or your favored language).
    # Then, translate into Python.
    
    # check exam mark. If too low
    #     return fail
    # otherwise
    #     calculate actual mark
    #     return actual mark

    actual_mark = .45 * exam + .55 * term   
    if exam < 40:
        return min(47.0, actual_mark)
    else:
        return actual_mark
