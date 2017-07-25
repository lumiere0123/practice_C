def format_name(first, last):
    """ (str, str) -> str
    
    Return a string containing last then first separated by a comma and
    a space.
    
    >>> format_name('Billy', 'Bob')
    'Bob, Billy'
    """
    
    return last + ', ' + first
    

def to_listing(first, last, phone_number):
    """ (str, str, str) -> str

    Return a string containing last then first separated by a comma
    and a space, followed by a colon and phone_number.
    
    >>> to_listing('Billy', 'Bob', '416-123-4567')
    'Bob, Billy: 416-123-4567'
    """
    
    return format_name(first, last) + ': ' + phone_number