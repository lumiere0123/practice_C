def is_IP_address(address):
    """ (str) -> bool    

    Return True iff address contains only digits and periods.
    
    >>> is_IP_address('255.14.128.1')
    True
    
    >>> is_IP_address('40 St. George St')
    False
  
    """
    #This is our loose definition of what constitutes a valid IP address.
    
    for char in address:
        if not char in "0123456789.":
            return False
        #else:
        #   return True
        #The commented out section is incorrect. You can't decide if it's
        #an IP address only after a valid first character.
        #You can uncomment it and run it through the debugger to see.
    return True

#instead of
#   if not char in "0123456789.":
#you could use
#   if char != '.' and char not in "0123456789": 
#Think about why we use an and instead of an or.
#You can use the debugger as well.

valid_IP = is_IP_address("128.10.10.2")
#valid_IP = is_IP_address("A.12")
#valid_IP = is_IP_address("12.A")