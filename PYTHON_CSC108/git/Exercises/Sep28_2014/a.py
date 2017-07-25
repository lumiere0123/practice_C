# Original problem description:
# Adults order two slices, boys order three slices, and girls order one slice. 
# Each pizza has eight slices. Write a function that takes three parameters 
# representing the number of adults, boys, and girls, and returns the required 
# number of pizzas. 

def num_pizzas(adults, boys, girls):
    '''(int, int, int) -> int
    Return the number of pizzas required to feed the specified number of adults 
    (2 slices), boys (3 slices), and girls (1 slice), assuming that each pizza
    has 8 slices.
    >>> num_pizzas(1, 1, 1)
    1
    >>> num_pizzas(0, 0, 16)
    2
    >>> num_pizzas(0, 3, 0)
    3
    '''
    a_pizzas = adults * 2
    b_pizzas = boys * 3
    g_pizzas = girls * 1
    msum = a_pizzas + b_pizzas + g_pizzas  

    # check if msum is divisible by 8 
    #  yes -- return the qutient of msum divide by 8
    #   no -- return the qutient of msum divide by 8 + 1

    if msum % 8 == 0:
        return msum // 8
    else:
        return msum // 8 +1

    #return (adults * 2 + boys * 3 + girls + 7) // 8

import doctest
doctest.testmod()
