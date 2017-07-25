def is_valid_password(password):
    '''(str) -> bool
    Return True iff password is at least length 5, contains a 
    non-letter character, and contains 
    both upper and lowercase letters.

    >>> is_valid_password('aA3')
    False
    >>> is_valid_password('aA3bc')
    True
    >>> is_valid_password('aa3bc')
    False
    >>> is_valid_password('AA3BC')
    False
    >>> is_valid_password('AAbBC')
    False
    '''

    return len(password) >= 5 and not password.isalpha() and \
           password.lower() != password and password.upper() != password


def remove_invalid(password_list):
    '''(list of str) -> None
    Remove invalid passwords from password_list.
    
    >>> L = ['aA3', 'aA3', 'aA3bc', 'aa3bc', 'AA3BC', 'AAbBC']
    >>> remove_invalid(L)
    >>> L
    ['aA3bc']
    '''
    
    # "Homework" for Wednesday
    # Don't forget to use is_valid_password

    # Here are two options:
    # 1. for loop over items and track which indices to remove
    # 2. while loop and manage the index carefully and appropriately