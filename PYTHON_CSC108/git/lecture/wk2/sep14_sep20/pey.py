# Original problem description:
# A student is eligible for PEY if their CGPA is at least 2, they are in 
# year 2 or year 3, and they are registered full-time.
# Write a function that evaluates whether they are eligible.

def pey_eligible(cgpa, year, is_fulltime):
    '''(number, int, bool) -> bool
    Return whether a student is eligible for PEY given their CGPA, year of 
    study, and whether they are a full-time student.

    >>> pey_eligible(3.7, 3, True)
    True
    >>> pey_eligible(1.7, 2, True)
    False
    >>> pey_eligible(4, 2, True)
    True
    '''
    return (cgpa >= 2) and (year == 2 or year == 3) and is_fulltime
