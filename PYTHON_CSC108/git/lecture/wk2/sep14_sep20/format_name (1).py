# The original format_name was much simpler, but as we discussed in class,
# the point of going through the design process is to *understand* the 
# human problem we are trying to solve. In this case, we found we had to 
# rewrite the proposed function because it was moer difficult than we 
# originally expected!

def format_name(first_name, last_name):
    ''' (str, str) -> str
    Return a string that formats a person's name. If they have both names,
    the formatted name is last_name then first_name separated by a comma 
    and a space. Otherwise, we want only the non-empty component of the name.

    >>> format_name("Mary", "Smith")
    Smith, Mary
    >>> format_name("Mausam", "")
    Mausam
    >>> format_name("", "Anja")
    Anja
    '''
    
    # To solve this more difficult problem, we're going to need a new structure
    # -- if statements! We'll revisit this problem soon.