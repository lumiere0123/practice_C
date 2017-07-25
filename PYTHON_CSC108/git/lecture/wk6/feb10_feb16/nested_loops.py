def digital_sum(nums_list):
    """ (list of str) -> int
    
    Precondition: s.isdigit() holds for each string s in nums_list.
    
    Return the sum of all the digits in all strings in nums_list.
    
    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    """

    sum = 0 
    for item in nums_list:
        for char in item:
            sum = sum + int(char)
            #sum += int(char)
    return sum
        
    #It's OK to call int(char) because the precondition guarantees us
    #that all characters in item will be digits.
    
    #Question: What would happen if we moved sum = 0 to the line
    #immediately after line 15? Why would this be a bad idea?
    
    #Could you use range() in the innermost loop?
    #Yes, that could work too, although the previous way is a bit cleaner.
    #You could use range() in the outermost loop too, but this code would
    #be unecessarily complicated.
    #sum = 0
    #for item in nums_list:
    #    for i in range(len(item)):
    #        sum = sum + int(item[i])
    #return sum



def can_pay_with_two_coins(denoms, amount):
    """ (list of int, int) -> bool
    
    Return True if and only if it is possible to form amount, a number
    of cents, using two coins of any of the denominatins in denoms.
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    """

    
    for coin1 in denoms:
        for coin2 in denoms:
            if coin1 + coin2 == amount:
                return True
    return False

    #What will the values of coin1 and coin2 be for the first two complete
    #iterations of the outer loop?
    #coin1, coin2
    #1, 1
    #1, 5
    #1, 10
    #1, 25
    #5, 1
    #5, 5
    #5, 10
    #5, 25
    #Notice that 2 iterations of the outer loop imply we do 8 iterations
    #of the innermost loop. You can use the debugger to see this more clearly.
    
    #Why did we choose not to use range() here? 
    #Because we really care about the actual
    #value of each list item and not for its position/index.
    #But you can modify this code to use range() too, if you want.